from __future__ import annotations

import json, math, os, re, sys, time, warnings
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import requests
import statsmodels.formula.api as smf
from scipy import stats
import nflreadpy as nfl

warnings.filterwarnings('ignore')

SEASONS = list(range(2016, 2026))
OUT = Path('weather_audit_output')
OUT.mkdir(parents=True, exist_ok=True)
CACHE = OUT / 'weather_cache.csv'

PATCH_COORDS = {
    'Acrisure Stadium': (40.446667, -80.015833), 'Heinz Field': (40.446667, -80.015833),
    'Highmark Stadium': (42.7738, -78.7868), 'New Era Field': (42.7738, -78.7868), 'Ralph Wilson Stadium': (42.7738, -78.7868),
    'FirstEnergy Stadium': (41.506111, -81.699444), 'Cleveland Browns Stadium': (41.506111, -81.699444), 'Huntington Bank Field': (41.506111, -81.699444),
    'Paycor Stadium': (39.095, -84.516), 'Paul Brown Stadium': (39.095, -84.516),
    'FedExField': (38.907778, -76.864444), 'FedEx Field': (38.907778, -76.864444), 'Commanders Field': (38.907778, -76.864444), 'Northwest Stadium': (38.907778, -76.864444),
    'TIAA Bank Field': (30.323889, -81.6375), 'TIAA Bank Field - Jacksonville': (30.323889, -81.6375), 'EverBank Field': (30.323889, -81.6375), 'EverBank Stadium': (30.3239, -81.6373),
    'CenturyLink Field': (47.5952, -122.3316), 'CenturyLink Field - Seattle': (47.5952, -122.3316), 'Lumen Field': (47.5952, -122.3316),
    'Sports Authority Field at Mile High': (39.743889, -105.02), 'Broncos Stadium at Mile High': (39.743889, -105.02), 'Empower Field at Mile High': (39.743889, -105.02),
    'Oakland Coliseum': (37.751667, -122.200556), 'Oakland-Alameda County Coliseum': (37.751667, -122.200556), 'O.co Coliseum': (37.751667, -122.200556),
    'Los Angeles Memorial Coliseum': (34.014167, -118.287778), 'Dignity Health Sports Park': (33.864, -118.261), 'StubHub Center': (33.864, -118.261),
    'SoFi Stadium': (33.95345, -118.3392), 'Arrowhead Stadium': (39.048889, -94.483889), 'GEHA Field at Arrowhead Stadium': (39.048889, -94.483889),
    'Bank of America Stadium': (35.225833, -80.852778), 'Gillette Stadium': (42.091, -71.264), 'Hard Rock Stadium': (25.958056, -80.238889),
    "Levi's Stadium": (37.403, -121.97), 'Lambeau Field': (44.501389, -88.062222), 'Lincoln Financial Field': (39.900833, -75.1675),
    'M&T Bank Stadium': (39.278056, -76.622778), 'MetLife Stadium': (40.813528, -74.074361), 'Nissan Stadium': (36.166389, -86.771389),
    'Raymond James Stadium': (27.975833, -82.503333), 'Soldier Field': (41.8623, -87.6167),
    'Wembley Stadium': (51.555833, -0.279722), 'Twickenham Stadium': (51.456111, -0.341667), 'Tottenham Hotspur Stadium': (51.604444, -0.066389),
    'Estadio Azteca': (19.302911, -99.150442), 'Allianz Arena': (48.2188, 11.6247), 'Deutsche Bank Park': (50.0686, 8.6455), 'Frankfurt Stadium': (50.0686, 8.6455),
    'Neo Quimica Arena': (-23.5453, -46.4742), 'Neo Química Arena': (-23.5453, -46.4742), 'Arena Corinthians': (-23.5453, -46.4742),
    'Santiago Bernabeu': (40.4531, -3.6883), 'Santiago Bernabéu': (40.4531, -3.6883), 'Estadio Santiago Bernabeu': (40.4531, -3.6883), 'Estadio Santiago Bernabéu': (40.4531, -3.6883),
    'Lucas Oil Stadium': (39.760056, -86.162806), 'NRG Stadium': (29.684722, -95.410833), 'State Farm Stadium': (33.528, -112.263),
    'University of Phoenix Stadium': (33.528, -112.263), 'Mercedes-Benz Stadium': (33.755556, -84.4), 'AT&T Stadium': (32.747778, -97.092778), 'Rogers Centre': (43.641389, -79.389167),
}

def norm_stadium(x: str) -> str:
    x = str(x or '').lower().replace('é','e').replace('í','i').replace('ã','a').replace('ç','c')
    return re.sub(r'[^a-z0-9]+', ' ', x).strip()
PATCH_NORM = {norm_stadium(k): v for k, v in PATCH_COORDS.items()}

def load_coord_table() -> dict[str, tuple[float,float]]:
    url = 'https://raw.githubusercontent.com/ThompsonJamesBliss/WeatherData/master/data/stadium_coordinates.csv'
    coords = dict(PATCH_NORM)
    try:
        old = pd.read_csv(url)
        for _, r in old.iterrows(): coords[norm_stadium(r['StadiumName'])] = (float(r['Latitude']), float(r['Longitude']))
    except Exception as e: print('WARN old coordinate table unavailable:', e)
    return coords

def geocode_stadium(name: str, session: requests.Session) -> tuple[float,float] | None:
    try:
        rr = session.get('https://nominatim.openstreetmap.org/search', params={'q':f'{name} stadium','format':'jsonv2','limit':1}, headers={'User-Agent':'DeadEyeFantasy-weather-audit/1.0'}, timeout=30)
        rr.raise_for_status(); arr=rr.json()
        if arr:
            time.sleep(1.05); return (float(arr[0]['lat']), float(arr[0]['lon']))
    except Exception as e: print('WARN geocode failed', name, e)
    return None

def load_schedules() -> pd.DataFrame:
    s=nfl.load_schedules(SEASONS).to_pandas()
    s=s[(s['season'].isin(SEASONS)) & s['game_type'].eq('REG') & s['roof'].isin(['outdoors','open'])].copy()
    if 'result' in s.columns: s=s[s['result'].notna()]
    elif 'home_score' in s.columns: s=s[s['home_score'].notna()]
    cols=[c for c in ['game_id','season','week','gameday','gametime','away_team','home_team','away_score','home_score','stadium_id','stadium','roof','temp','wind','location'] if c in s.columns]
    s[cols].sort_values(['season','week','game_id']).to_csv(OUT/'outdoor_open_games.csv',index=False)
    return s

def attach_coords(games: pd.DataFrame) -> pd.DataFrame:
    coords=load_coord_table(); session=requests.Session(); resolved={}; unresolved=[]
    for st in sorted(games['stadium'].dropna().unique()):
        n=norm_stadium(st)
        if n in coords: resolved[st]=coords[n]
        else:
            geo=geocode_stadium(st,session)
            if geo: resolved[st]=geo
            else: unresolved.append(st)
    if unresolved:
        print('UNRESOLVED STADIUMS:',unresolved); pd.DataFrame({'stadium':unresolved}).to_csv(OUT/'unresolved_stadiums.csv',index=False); raise RuntimeError(f'Unresolved stadium coordinates: {unresolved}')
    g=games.copy(); g['latitude']=g['stadium'].map(lambda x:resolved[x][0]); g['longitude']=g['stadium'].map(lambda x:resolved[x][1])
    pd.DataFrame([{'stadium':k,'latitude':v[0],'longitude':v[1]} for k,v in resolved.items()]).sort_values('stadium').to_csv(OUT/'stadium_coordinates_used.csv',index=False)
    return g

def kickoff_utc(row) -> pd.Timestamp:
    dt=pd.Timestamp(f"{row['gameday']} {row['gametime']}")
    if dt.tzinfo is None: dt=dt.tz_localize('America/New_York',ambiguous='infer',nonexistent='shift_forward')
    return dt.tz_convert('UTC')

def fetch_weather_for_group(stadium,season,lat,lon,dates,session):
    start=(pd.Timestamp(min(dates))-pd.Timedelta(days=1)).date().isoformat(); end=(pd.Timestamp(max(dates))+pd.Timedelta(days=1)).date().isoformat()
    params={'latitude':lat,'longitude':lon,'start_date':start,'end_date':end,'hourly':'temperature_2m,precipitation,rain,snowfall,wind_speed_10m,wind_gusts_10m','temperature_unit':'fahrenheit','wind_speed_unit':'mph','precipitation_unit':'mm','timezone':'UTC'}
    for attempt in range(6):
        try:
            r=session.get('https://archive-api.open-meteo.com/v1/archive',params=params,timeout=90)
            if r.status_code in (429,502,503,504): time.sleep(2**attempt); continue
            r.raise_for_status(); h=pd.DataFrame(r.json()['hourly']); h['time']=pd.to_datetime(h['time'],utc=True); h['stadium']=stadium; h['season']=season; return h
        except Exception as e:
            if attempt==5: raise
            print('weather retry',stadium,season,attempt,e); time.sleep(2**attempt)

def attach_weather(games: pd.DataFrame) -> pd.DataFrame:
    g=games.copy(); g['kickoff_utc']=g.apply(kickoff_utc,axis=1); session=requests.Session(); all_hourly=[]; groups=list(g.groupby(['stadium','season']))
    for i,((stadium,season),grp) in enumerate(groups,1):
        print(f'WEATHER {i}/{len(groups)} {season} {stadium}')
        all_hourly.append(fetch_weather_for_group(stadium,int(season),float(grp['latitude'].iloc[0]),float(grp['longitude'].iloc[0]),grp['gameday'].tolist(),session)); time.sleep(.12)
    hourly=pd.concat(all_hourly,ignore_index=True); hourly.to_parquet(OUT/'open_meteo_hourly.parquet',index=False)
    out=[]
    for _,r in g.iterrows():
        start=r['kickoff_utc'].floor('h'); end=start+pd.Timedelta(hours=3); h=hourly[(hourly['stadium'].eq(r['stadium'])) & hourly['season'].eq(r['season']) & hourly['time'].between(start,end)]
        if h.empty: print('WARN no weather window',r['game_id'],r['stadium'],start); continue
        rr=r.to_dict(); rr.update({'temperature_f_avg':h['temperature_2m'].mean(),'temperature_f_kickoff':h.iloc[0]['temperature_2m'],'wind_speed_mph_avg':h['wind_speed_10m'].mean(),'wind_speed_mph_max':h['wind_speed_10m'].max(),'wind_gust_mph_avg':h['wind_gusts_10m'].mean(),'wind_gust_mph_max':h['wind_gusts_10m'].max(),'rain_mm_h_avg':h['rain'].mean(),'rain_mm_h_max':h['rain'].max(),'rain_total_mm_4h':h['rain'].sum(),'snow_cm_h_avg':h['snowfall'].mean(),'snow_cm_h_max':h['snowfall'].max(),'snow_total_cm_4h':h['snowfall'].sum(),'precip_mm_h_avg':h['precipitation'].mean(),'weather_hours':len(h)}); out.append(rr)
    gw=pd.DataFrame(out); gw.to_csv(OUT/'game_weather_join.csv',index=False); return gw

def kicker_points(df: pd.DataFrame) -> pd.Series:
    c=set(df.columns); pts=pd.Series(np.zeros(len(df)),index=df.index,dtype=float)
    for x in ['pat_made','extra_points_made','xp_made']:
        if x in c: pts+=pd.to_numeric(df[x],errors='coerce').fillna(0); break
    used=False
    for names,mult in [(['fg_made_0_19','fg_made_20_29','fg_made_30_39'],3),(['fg_made_40_49'],4),(['fg_made_50_59','fg_made_60_'],5)]:
        for x in names:
            if x in c: pts+=mult*pd.to_numeric(df[x],errors='coerce').fillna(0); used=True
    if not used:
        for x in ['fg_made','field_goals_made']:
            if x in c: pts+=3*pd.to_numeric(df[x],errors='coerce').fillna(0); break
    return pts

def build_position_production(game_weather: pd.DataFrame) -> pd.DataFrame:
    p=nfl.load_player_stats(SEASONS,summary_level='week').to_pandas(); pd.DataFrame({'column':p.columns}).to_csv(OUT/'player_stats_columns.csv',index=False)
    p=p[(p['season'].isin(SEASONS)) & p['season_type'].eq('REG')].copy(); p['fantasy_points_ppr']=pd.to_numeric(p['fantasy_points_ppr'],errors='coerce').fillna(0)
    rows=[]
    for pos in ['QB','RB','WR','TE']:
        z=p[p['position'].eq(pos)].groupby(['game_id','team'],as_index=False)['fantasy_points_ppr'].sum(); z['position']=pos; z=z.rename(columns={'fantasy_points_ppr':'fantasy_points'}); rows.append(z)
    kp=p[p['position'].eq('K')].copy(); kp['k_fp']=kicker_points(kp); k=kp.groupby(['game_id','team'],as_index=False)['k_fp'].sum().rename(columns={'k_fp':'fantasy_points'}); k['position']='K'; rows.append(k)
    prod=pd.concat(rows,ignore_index=True)
    def_num=['def_sacks','def_interceptions','def_fumble_recovery_opp','def_tds','def_safety']
    for c in def_num:
        if c not in p.columns: p[c]=0
        p[c]=pd.to_numeric(p[c],errors='coerce').fillna(0)
    d=p.groupby(['game_id','team'],as_index=False)[def_num].sum(); st_candidates=[c for c in ['special_teams_tds','kickoff_return_tds','punt_return_tds'] if c in p.columns]
    if st_candidates:
        st=p.groupby(['game_id','team'],as_index=False)[st_candidates].sum(); st['st_tds']=st[st_candidates].sum(axis=1); d=d.merge(st[['game_id','team','st_tds']],on=['game_id','team'],how='left')
    else: d['st_tds']=0
    sched_scores=game_weather[['game_id','home_team','away_team','home_score','away_score']].drop_duplicates(); home=sched_scores[['game_id','home_team','away_score']].rename(columns={'home_team':'team','away_score':'points_allowed'}); away=sched_scores[['game_id','away_team','home_score']].rename(columns={'away_team':'team','home_score':'points_allowed'}); pa=pd.concat([home,away],ignore_index=True); d=d.merge(pa,on=['game_id','team'],how='inner')
    def pa_pts(x):
        if pd.isna(x): return np.nan
        if x==0:return 10
        if x<=6:return 7
        if x<=13:return 4
        if x<=20:return 1
        if x<=27:return 0
        if x<=34:return -1
        return -4
    d['fantasy_points']=d['def_sacks']+2*d['def_interceptions']+2*d['def_fumble_recovery_opp']+6*d['def_tds']+2*d['def_safety']+6*d['st_tds']+d['points_allowed'].map(pa_pts); d['position']='DST'; prod=pd.concat([prod,d[['game_id','team','position','fantasy_points']]],ignore_index=True)
    meta=game_weather[['game_id','season','week','home_team','away_team','stadium','roof','temperature_f_avg','temperature_f_kickoff','wind_speed_mph_avg','wind_speed_mph_max','wind_gust_mph_avg','wind_gust_mph_max','rain_mm_h_avg','rain_mm_h_max','rain_total_mm_4h','snow_cm_h_avg','snow_cm_h_max','snow_total_cm_4h']].copy(); prod=prod.merge(meta,on='game_id',how='inner'); prod['home']=(prod['team']==prod['home_team']).astype(int); prod['opponent']=np.where(prod['home'].eq(1),prod['away_team'],prod['home_team']); prod['fantasy_points']=pd.to_numeric(prod['fantasy_points'],errors='coerce'); prod=prod.dropna(subset=['fantasy_points']).copy(); prod.to_csv(OUT/'team_position_game_production.csv',index=False); return prod

def add_expectations(prod: pd.DataFrame) -> pd.DataFrame:
    x=prod.sort_values(['team','position','season','week','game_id']).copy(); x['expected_fp']=x.groupby(['team','position'])['fantasy_points'].transform(lambda s:s.shift(1).ewm(span=6,adjust=False,min_periods=4).mean())
    allowed=x[['game_id','season','week','position','team','opponent','fantasy_points']].rename(columns={'team':'offense','opponent':'defense','fantasy_points':'allowed_fp'}).sort_values(['defense','position','season','week','game_id']); allowed['opp_allowed_expected']=allowed.groupby(['defense','position'])['allowed_fp'].transform(lambda s:s.shift(1).ewm(span=6,adjust=False,min_periods=4).mean()); key=allowed[['game_id','position','offense','opp_allowed_expected']].rename(columns={'offense':'team'}); x=x.merge(key,on=['game_id','position','team'],how='left')
    floors={'QB':8,'RB':8,'WR':8,'TE':4,'K':4,'DST':4}; x['residual_points']=x['fantasy_points']-x['expected_fp']; x['denom']=x.apply(lambda r:max(abs(r['expected_fp']) if pd.notna(r['expected_fp']) else 0,floors.get(r['position'],4)),axis=1); x['residual_pct']=x['residual_points']/x['denom']; x=x.dropna(subset=['expected_fp']).copy(); x['gust_excess_mph']=(x['wind_gust_mph_max']-x['wind_speed_mph_avg']).clip(lower=0); x['wind_over_10']=(x['wind_speed_mph_avg']-10).clip(lower=0); x['gust_over_20']=(x['wind_gust_mph_max']-20).clip(lower=0); x['cold_10f']=(55-x['temperature_f_avg']).clip(lower=0)/10; x['heat_10f']=(x['temperature_f_avg']-85).clip(lower=0)/10; x['rain_any']=(x['rain_mm_h_avg']>.05).astype(int); x['snow_any']=(x['snow_cm_h_avg']>.02).astype(int); x.to_csv(OUT/'modeling_dataset.csv',index=False); return x

def correlation_table(x):
    rows=[]; vars=['temperature_f_avg','wind_speed_mph_avg','wind_gust_mph_max','rain_mm_h_avg','snow_cm_h_avg']; outcomes=['fantasy_points','residual_points','residual_pct']
    for pos,g in x.groupby('position'):
        for v in vars:
            for y in outcomes:
                z=g[[v,y]].dropna()
                if len(z)<20 or z[v].nunique()<2: continue
                pr,pp=stats.pearsonr(z[v],z[y]); sr,sp=stats.spearmanr(z[v],z[y]); rows.append({'position':pos,'weather_variable':v,'outcome':y,'n':len(z),'pearson_r':pr,'pearson_p':pp,'spearman_rho':sr,'spearman_p':sp})
    return pd.DataFrame(rows)

def bucket_tables(x):
    frames=[]; specs={'wind_speed_mph_avg':([-np.inf,10,15,20,25,np.inf],['<10','10-14.9','15-19.9','20-24.9','25+']),'wind_gust_mph_max':([-np.inf,15,25,35,45,np.inf],['<15','15-24.9','25-34.9','35-44.9','45+']),'temperature_f_avg':([-np.inf,20,33,46,56,86,np.inf],['<20','20-32','33-45','46-55','56-85','86+']),'rain_mm_h_avg':([-np.inf,.05,.5,2.5,7.5,np.inf],['none/trace','light','moderate','heavy','extreme']),'snow_cm_h_avg':([-np.inf,.02,.1,.5,1.5,np.inf],['none/trace','light','moderate','heavy','extreme'])}
    for var,(bins,labels) in specs.items():
        tmp=x.copy(); tmp['bucket']=pd.cut(tmp[var],bins=bins,labels=labels,right=False); t=tmp.groupby(['position','bucket'],observed=True).agg(n=('residual_pct','size'),mean_residual_pct=('residual_pct','mean'),median_residual_pct=('residual_pct','median'),mean_residual_points=('residual_points','mean'),mean_actual_fp=('fantasy_points','mean'),mean_expected_fp=('expected_fp','mean'),weather_mean=(var,'mean')).reset_index(); t['weather_variable']=var; frames.append(t)
    return pd.concat(frames,ignore_index=True)

def fit_models(x):
    rows=[]
    for pos,g in x.groupby('position'):
        g=g.replace([np.inf,-np.inf],np.nan).dropna(subset=['residual_pct','temperature_f_avg','wind_speed_mph_avg','wind_gust_mph_max','rain_mm_h_avg','snow_cm_h_avg']).copy()
        if len(g)<100: continue
        g['opp_allowed_expected']=g['opp_allowed_expected'].fillna(g['opp_allowed_expected'].median())
        formulas={'raw':'residual_pct ~ temperature_f_avg + wind_speed_mph_avg + wind_gust_mph_max + rain_mm_h_avg + snow_cm_h_avg + opp_allowed_expected + home + C(season)','piecewise':'residual_pct ~ wind_over_10 + gust_over_20 + rain_any + rain_mm_h_avg + snow_any + snow_cm_h_avg + cold_10f + heat_10f + opp_allowed_expected + home + C(season)','interaction':'residual_pct ~ wind_over_10 + gust_over_20 + rain_any + rain_mm_h_avg + snow_any + snow_cm_h_avg + cold_10f + heat_10f + wind_over_10:rain_any + wind_over_10:snow_any + opp_allowed_expected + home + C(season)'}
        for name,f in formulas.items():
            try:
                m=smf.ols(f,data=g).fit(cov_type='cluster',cov_kwds={'groups':g['game_id']})
                for term in m.params.index:
                    if term.startswith('C(season)') or term in ['Intercept','opp_allowed_expected','home']: continue
                    rows.append({'position':pos,'model':name,'term':term,'coef':m.params[term],'std_err':m.bse[term],'p_value':m.pvalues[term],'ci_low':m.conf_int().loc[term,0],'ci_high':m.conf_int().loc[term,1],'n':int(m.nobs),'r2':m.rsquared})
            except Exception as e: print('MODEL FAIL',pos,name,e)
    return pd.DataFrame(rows)

def holdout_validation(x):
    rows=[]; blocks={'2016-2021':(2016,2021),'2022-2023':(2022,2023),'2024-2025':(2024,2025)}; f='residual_pct ~ wind_over_10 + gust_over_20 + rain_any + rain_mm_h_avg + snow_any + snow_cm_h_avg + cold_10f + heat_10f + opp_allowed_expected + home'
    for pos,gg in x.groupby('position'):
      for block,(a,b) in blocks.items():
        g=gg[gg['season'].between(a,b)].replace([np.inf,-np.inf],np.nan).dropna(subset=['residual_pct','wind_over_10','gust_over_20','rain_mm_h_avg','snow_cm_h_avg','cold_10f','heat_10f']).copy()
        if len(g)<80: continue
        g['opp_allowed_expected']=g['opp_allowed_expected'].fillna(g['opp_allowed_expected'].median())
        try:
          m=smf.ols(f,data=g).fit(cov_type='cluster',cov_kwds={'groups':g['game_id']})
          for term in ['wind_over_10','gust_over_20','rain_any','rain_mm_h_avg','snow_any','snow_cm_h_avg','cold_10f','heat_10f']:
            rows.append({'position':pos,'block':block,'term':term,'coef':m.params.get(term,np.nan),'p_value':m.pvalues.get(term,np.nan),'n':int(m.nobs)})
        except Exception as e: print('HOLDOUT FAIL',pos,block,e)
    return pd.DataFrame(rows)

def summarize(games,model,corr,buckets,coeff,hold):
    lines=['# DeadEye Weather Audit — Empirical Results\n',f'- Seasons: **{min(SEASONS)}–{max(SEASONS)} regular season**',f'- Outdoor/open-roof completed games: **{len(games):,}**',f'- Stadiums represented: **{games.stadium.nunique()}**',f'- Team-position modeling rows after pregame expectation warmup: **{len(model):,}**','- Weather: Open-Meteo Historical API, four-hour game window beginning at kickoff hour (UTC).','- Fantasy outcome: team-position PPR total for QB/RB/WR/TE, standard-ish K and D/ST scoring; residual is actual minus a 6-game EWMA pregame expectation.','\n## Stadiums / game counts\n']
    lines.append(games.groupby(['stadium','roof']).size().reset_index(name='games').sort_values('games',ascending=False).to_markdown(index=False)); lines.append('\n## Correlations with residual fantasy production\n'); cc=corr[corr['outcome'].eq('residual_pct')].copy(); lines.append(cc.sort_values(['position','weather_variable']).to_markdown(index=False,floatfmt='.4f')); lines.append('\n## Piecewise regression coefficients\n'); lines.append(coeff[coeff['model'].eq('piecewise')].to_markdown(index=False,floatfmt='.5f')); lines.append('\n## Interaction test\n'); ic=coeff[(coeff['model'].eq('interaction')) & coeff['term'].str.contains(':',regex=False)].copy(); lines.append(ic.to_markdown(index=False,floatfmt='.5f')); lines.append('\n## Bucket summaries\n'); lines.append(buckets.to_markdown(index=False,floatfmt='.4f')); lines.append('\n## Coefficient stability blocks\n'); lines.append(hold.to_markdown(index=False,floatfmt='.5f')); (OUT/'AUDIT_REPORT.md').write_text('\n'.join(lines),encoding='utf-8')

def main():
    print('Loading nflreadpy schedules...'); games=load_schedules(); print('Outdoor/open games',len(games),'stadiums',games.stadium.nunique()); games=attach_coords(games); games=attach_weather(games); prod=build_position_production(games); model=add_expectations(prod); corr=correlation_table(model); corr.to_csv(OUT/'correlations.csv',index=False); buckets=bucket_tables(model); buckets.to_csv(OUT/'bucket_effects.csv',index=False); coeff=fit_models(model); coeff.to_csv(OUT/'regression_coefficients.csv',index=False); hold=holdout_validation(model); hold.to_csv(OUT/'coefficient_stability.csv',index=False); summarize(games,model,corr,buckets,coeff,hold); print('DONE'); print((OUT/'AUDIT_REPORT.md').read_text()[:12000])
if __name__=='__main__': main()
