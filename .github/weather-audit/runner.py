import importlib.util
from pathlib import Path
import pandas as pd

p = Path(__file__).with_name('audit.py')
spec = importlib.util.spec_from_file_location('deadeye_audit', p)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

# nflverse schedule naming aliases that the fallback geocoder did not resolve.
audit.PATCH_NORM.update({
    audit.norm_stadium('Ring Central Coliseum'): (37.751667, -122.200556),
    audit.norm_stadium('TIAA Bank Stadium'): (30.323889, -81.6375),
})

# nflverse schedule gametime is represented in US Eastern time. NFL kickoffs in
# this sample are not in the repeated 1 a.m. DST hour, so no ambiguous inference
# is needed for scalar Timestamps.
def kickoff_utc(row):
    dt = pd.Timestamp(f"{row['gameday']} {row['gametime']}")
    if dt.tzinfo is None:
        dt = dt.tz_localize('America/New_York', ambiguous=False, nonexistent='shift_forward')
    return dt.tz_convert('UTC')

audit.kickoff_utc = kickoff_utc

audit.main()
