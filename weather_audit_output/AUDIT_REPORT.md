# DeadEye Weather Audit — Empirical Results

- Seasons: **2016–2025 regular season**
- Outdoor/open-roof completed games: **1,878**
- Stadiums represented: **44**
- Team-position modeling rows after pregame expectation warmup: **21,665**
- Weather: Open-Meteo Historical API, four-hour game window beginning at kickoff hour (UTC).
- Fantasy outcome: team-position PPR total for QB/RB/WR/TE, standard-ish K and D/ST scoring; residual is actual minus a 6-game EWMA pregame expectation.

## Stadiums / game counts

| stadium                             | roof     |   games |
|:------------------------------------|:---------|--------:|
| MetLife Stadium                     | outdoors |     165 |
| M&T Bank Stadium                    | outdoors |      83 |
| FedExField                          | outdoors |      82 |
| FirstEnergy Stadium                 | outdoors |      82 |
| Gillette Stadium                    | outdoors |      82 |
| Hard Rock Stadium                   | outdoors |      82 |
| Nissan Stadium                      | outdoors |      82 |
| Lincoln Financial Field             | outdoors |      81 |
| New Era Field                       | outdoors |      81 |
| Bank of America Stadium             | outdoors |      81 |
| Lambeau Field                       | outdoors |      81 |
| Soldier Field                       | outdoors |      81 |
| Raymond James Stadium               | outdoors |      80 |
| Levi's Stadium                      | outdoors |      79 |
| TIAA Bank Stadium                   | outdoors |      62 |
| Empower Field at Mile High          | outdoors |      59 |
| Heinz Field                         | outdoors |      49 |
| Paul Brown Stadium                  | outdoors |      48 |
| Lumen Field                         | outdoors |      46 |
| GEHA Field at Arrowhead Stadium     | outdoors |      42 |
| Arrowhead Stadium                   | outdoors |      40 |
| CenturyLink Field                   | outdoors |      36 |
| Acrisure Stadium                    | outdoors |      34 |
| Paycor Stadium                      | outdoors |      33 |
| Los Angeles Memorial Coliseum       | outdoors |      29 |
| Sports Authority Field at Mile High | outdoors |      24 |
| StubHub Center                      | outdoors |      22 |
| Oakland-Alameda County Coliseum     | outdoors |      21 |
| Mercedes-Benz Stadium               | open     |      18 |
| EverBank Field                      | outdoors |      14 |
| Lucas Oil Stadium                   | open     |      13 |
| Wembley Stadium                     | outdoors |      12 |
| Tottenham Stadium                   | outdoors |      10 |
| State Farm Stadium                  | open     |       8 |
| Qualcomm Stadium                    | outdoors |       8 |
| Ring Central Coliseum               | outdoors |       7 |
| NRG Stadium                         | open     |       5 |
| Azteca Stadium                      | outdoors |       4 |
| Twickenham Stadium                  | outdoors |       3 |
| AT&T Stadium                        | open     |       3 |
| Allianz Arena                       | outdoors |       2 |
| Deutsche Bank Park                  | outdoors |       2 |
| Arena Corinthians                   | outdoors |       1 |
| University of Phoenix Stadium       | open     |       1 |

## Correlations with residual fantasy production

| position   | weather_variable   | outcome      |    n |   pearson_r |   pearson_p |   spearman_rho |   spearman_p |
|:-----------|:-------------------|:-------------|-----:|------------:|------------:|---------------:|-------------:|
| DST        | rain_mm_h_avg      | residual_pct | 3556 |      0.0463 |      0.0057 |         0.0389 |       0.0204 |
| DST        | snow_cm_h_avg      | residual_pct | 3556 |      0.0229 |      0.1723 |         0.0163 |       0.3322 |
| DST        | temperature_f_avg  | residual_pct | 3556 |      0.0062 |      0.7100 |         0.0054 |       0.7495 |
| DST        | wind_gust_mph_max  | residual_pct | 3556 |      0.0192 |      0.2517 |         0.0372 |       0.0266 |
| DST        | wind_speed_mph_avg | residual_pct | 3556 |      0.0322 |      0.0551 |         0.0416 |       0.0132 |
| K          | rain_mm_h_avg      | residual_pct | 3616 |     -0.0132 |      0.4258 |        -0.0121 |       0.4678 |
| K          | snow_cm_h_avg      | residual_pct | 3616 |     -0.0259 |      0.1187 |        -0.0480 |       0.0039 |
| K          | temperature_f_avg  | residual_pct | 3616 |      0.0615 |      0.0002 |         0.0557 |       0.0008 |
| K          | wind_gust_mph_max  | residual_pct | 3616 |     -0.0558 |      0.0008 |        -0.0523 |       0.0017 |
| K          | wind_speed_mph_avg | residual_pct | 3616 |     -0.0660 |      0.0001 |        -0.0675 |       0.0000 |
| QB         | rain_mm_h_avg      | residual_pct | 3623 |     -0.0611 |      0.0002 |        -0.0654 |       0.0001 |
| QB         | snow_cm_h_avg      | residual_pct | 3623 |     -0.0381 |      0.0218 |        -0.0356 |       0.0321 |
| QB         | temperature_f_avg  | residual_pct | 3623 |      0.0882 |      0.0000 |         0.0809 |       0.0000 |
| QB         | wind_gust_mph_max  | residual_pct | 3623 |     -0.0712 |      0.0000 |        -0.0606 |       0.0003 |
| QB         | wind_speed_mph_avg | residual_pct | 3623 |     -0.0836 |      0.0000 |        -0.0688 |       0.0000 |
| RB         | rain_mm_h_avg      | residual_pct | 3628 |     -0.0099 |      0.5502 |        -0.0130 |       0.4340 |
| RB         | snow_cm_h_avg      | residual_pct | 3628 |      0.0004 |      0.9795 |         0.0253 |       0.1270 |
| RB         | temperature_f_avg  | residual_pct | 3628 |      0.0117 |      0.4811 |        -0.0046 |       0.7803 |
| RB         | wind_gust_mph_max  | residual_pct | 3628 |      0.0176 |      0.2889 |         0.0088 |       0.5979 |
| RB         | wind_speed_mph_avg | residual_pct | 3628 |      0.0079 |      0.6364 |         0.0013 |       0.9380 |
| TE         | rain_mm_h_avg      | residual_pct | 3614 |     -0.0336 |      0.0436 |        -0.0569 |       0.0006 |
| TE         | snow_cm_h_avg      | residual_pct | 3614 |     -0.0252 |      0.1293 |        -0.0243 |       0.1443 |
| TE         | temperature_f_avg  | residual_pct | 3614 |      0.0362 |      0.0294 |         0.0339 |       0.0413 |
| TE         | wind_gust_mph_max  | residual_pct | 3614 |     -0.0719 |      0.0000 |        -0.0583 |       0.0005 |
| TE         | wind_speed_mph_avg | residual_pct | 3614 |     -0.0712 |      0.0000 |        -0.0505 |       0.0024 |
| WR         | rain_mm_h_avg      | residual_pct | 3628 |     -0.0572 |      0.0006 |        -0.0279 |       0.0930 |
| WR         | snow_cm_h_avg      | residual_pct | 3628 |     -0.0467 |      0.0049 |        -0.0636 |       0.0001 |
| WR         | temperature_f_avg  | residual_pct | 3628 |      0.0893 |      0.0000 |         0.0820 |       0.0000 |
| WR         | wind_gust_mph_max  | residual_pct | 3628 |     -0.0917 |      0.0000 |        -0.0823 |       0.0000 |
| WR         | wind_speed_mph_avg | residual_pct | 3628 |     -0.1059 |      0.0000 |        -0.0931 |       0.0000 |

## Piecewise regression coefficients

| position   | model     | term          |     coef |   std_err |   p_value |   ci_low |   ci_high |    n |      r2 |
|:-----------|:----------|:--------------|---------:|----------:|----------:|---------:|----------:|-----:|--------:|
| DST        | piecewise | wind_over_10  |  0.03069 |   0.01249 |   0.01401 |  0.00621 |   0.05517 | 3556 | 0.04002 |
| DST        | piecewise | gust_over_20  | -0.01142 |   0.00545 |   0.03595 | -0.02210 |  -0.00075 | 3556 | 0.04002 |
| DST        | piecewise | rain_any      |  0.03011 |   0.04687 |   0.52064 | -0.06175 |   0.12196 | 3556 | 0.04002 |
| DST        | piecewise | rain_mm_h_avg |  0.09310 |   0.04079 |   0.02247 |  0.01315 |   0.17306 | 3556 | 0.04002 |
| DST        | piecewise | snow_any      | -0.07298 |   0.13703 |   0.59433 | -0.34155 |   0.19559 | 3556 | 0.04002 |
| DST        | piecewise | snow_cm_h_avg |  0.28208 |   0.24440 |   0.24842 | -0.19693 |   0.76109 | 3556 | 0.04002 |
| DST        | piecewise | cold_10f      |  0.02930 |   0.01939 |   0.13071 | -0.00870 |   0.06730 | 3556 | 0.04002 |
| DST        | piecewise | heat_10f      |  0.08282 |   0.18808 |   0.65968 | -0.28581 |   0.45145 | 3556 | 0.04002 |
| K          | piecewise | wind_over_10  | -0.00730 |   0.00818 |   0.37238 | -0.02334 |   0.00874 | 3616 | 0.01329 |
| K          | piecewise | gust_over_20  | -0.00324 |   0.00360 |   0.36866 | -0.01030 |   0.00382 | 3616 | 0.01329 |
| K          | piecewise | rain_any      | -0.03307 |   0.03174 |   0.29746 | -0.09528 |   0.02914 | 3616 | 0.01329 |
| K          | piecewise | rain_mm_h_avg | -0.00124 |   0.02389 |   0.95859 | -0.04807 |   0.04559 | 3616 | 0.01329 |
| K          | piecewise | snow_any      | -0.10704 |   0.06622 |   0.10598 | -0.23683 |   0.02274 | 3616 | 0.01329 |
| K          | piecewise | snow_cm_h_avg |  0.04756 |   0.15665 |   0.76144 | -0.25948 |   0.35459 | 3616 | 0.01329 |
| K          | piecewise | cold_10f      | -0.03859 |   0.01170 |   0.00098 | -0.06153 |  -0.01564 | 3616 | 0.01329 |
| K          | piecewise | heat_10f      |  0.02051 |   0.10205 |   0.84068 | -0.17950 |   0.22053 | 3616 | 0.01329 |
| QB         | piecewise | wind_over_10  | -0.01258 |   0.00725 |   0.08287 | -0.02679 |   0.00164 | 3623 | 0.03119 |
| QB         | piecewise | gust_over_20  | -0.00071 |   0.00306 |   0.81640 | -0.00671 |   0.00529 | 3623 | 0.03119 |
| QB         | piecewise | rain_any      | -0.03372 |   0.02864 |   0.23904 | -0.08986 |   0.02241 | 3623 | 0.03119 |
| QB         | piecewise | rain_mm_h_avg | -0.05076 |   0.02031 |   0.01245 | -0.09056 |  -0.01095 | 3623 | 0.03119 |
| QB         | piecewise | snow_any      |  0.08510 |   0.07537 |   0.25885 | -0.06262 |   0.23282 | 3623 | 0.03119 |
| QB         | piecewise | snow_cm_h_avg | -0.25988 |   0.16985 |   0.12600 | -0.59277 |   0.07301 | 3623 | 0.03119 |
| QB         | piecewise | cold_10f      | -0.04435 |   0.01003 |   0.00001 | -0.06402 |  -0.02469 | 3623 | 0.03119 |
| QB         | piecewise | heat_10f      |  0.08190 |   0.10236 |   0.42363 | -0.11871 |   0.28251 | 3623 | 0.03119 |
| RB         | piecewise | wind_over_10  | -0.00411 |   0.00624 |   0.50986 | -0.01634 |   0.00812 | 3628 | 0.01372 |
| RB         | piecewise | gust_over_20  |  0.00325 |   0.00262 |   0.21481 | -0.00189 |   0.00839 | 3628 | 0.01372 |
| RB         | piecewise | rain_any      |  0.00219 |   0.02470 |   0.92945 | -0.04623 |   0.05061 | 3628 | 0.01372 |
| RB         | piecewise | rain_mm_h_avg | -0.01739 |   0.02163 |   0.42125 | -0.05978 |   0.02500 | 3628 | 0.01372 |
| RB         | piecewise | snow_any      |  0.09609 |   0.07653 |   0.20928 | -0.05391 |   0.24608 | 3628 | 0.01372 |
| RB         | piecewise | snow_cm_h_avg | -0.15372 |   0.10783 |   0.15396 | -0.36506 |   0.05761 | 3628 | 0.01372 |
| RB         | piecewise | cold_10f      | -0.01374 |   0.00776 |   0.07650 | -0.02895 |   0.00146 | 3628 | 0.01372 |
| RB         | piecewise | heat_10f      | -0.09789 |   0.08681 |   0.25946 | -0.26804 |   0.07225 | 3628 | 0.01372 |
| TE         | piecewise | wind_over_10  | -0.02420 |   0.00933 |   0.00947 | -0.04248 |  -0.00592 | 3614 | 0.01678 |
| TE         | piecewise | gust_over_20  | -0.00035 |   0.00462 |   0.93965 | -0.00940 |   0.00870 | 3614 | 0.01678 |
| TE         | piecewise | rain_any      | -0.07956 |   0.03767 |   0.03466 | -0.15338 |  -0.00574 | 3614 | 0.01678 |
| TE         | piecewise | rain_mm_h_avg | -0.01200 |   0.02937 |   0.68289 | -0.06957 |   0.04557 | 3614 | 0.01678 |
| TE         | piecewise | snow_any      |  0.24864 |   0.13356 |   0.06265 | -0.01313 |   0.51041 | 3614 | 0.01678 |
| TE         | piecewise | snow_cm_h_avg | -0.47531 |   0.18550 |   0.01040 | -0.83889 |  -0.11173 | 3614 | 0.01678 |
| TE         | piecewise | cold_10f      | -0.04438 |   0.01422 |   0.00180 | -0.07224 |  -0.01651 | 3614 | 0.01678 |
| TE         | piecewise | heat_10f      | -0.05718 |   0.15035 |   0.70373 | -0.35185 |   0.23750 | 3614 | 0.01678 |
| WR         | piecewise | wind_over_10  | -0.00763 |   0.00526 |   0.14672 | -0.01795 |   0.00268 | 3628 | 0.02369 |
| WR         | piecewise | gust_over_20  | -0.00354 |   0.00249 |   0.15530 | -0.00842 |   0.00134 | 3628 | 0.02369 |
| WR         | piecewise | rain_any      |  0.01041 |   0.02379 |   0.66173 | -0.03623 |   0.05705 | 3628 | 0.02369 |
| WR         | piecewise | rain_mm_h_avg | -0.05318 |   0.01632 |   0.00111 | -0.08516 |  -0.02121 | 3628 | 0.02369 |
| WR         | piecewise | snow_any      | -0.06353 |   0.05205 |   0.22225 | -0.16556 |   0.03849 | 3628 | 0.02369 |
| WR         | piecewise | snow_cm_h_avg | -0.08689 |   0.14698 |   0.55442 | -0.37496 |   0.20119 | 3628 | 0.02369 |
| WR         | piecewise | cold_10f      | -0.02785 |   0.00884 |   0.00163 | -0.04517 |  -0.01052 | 3628 | 0.02369 |
| WR         | piecewise | heat_10f      |  0.06808 |   0.09472 |   0.47232 | -0.11758 |   0.25373 | 3628 | 0.02369 |

## Interaction test

| position   | model       | term                  |     coef |   std_err |   p_value |   ci_low |   ci_high |    n |      r2 |
|:-----------|:------------|:----------------------|---------:|----------:|----------:|---------:|----------:|-----:|--------:|
| DST        | interaction | wind_over_10:rain_any |  0.00288 |   0.01342 |   0.83025 | -0.02342 |   0.02917 | 3556 | 0.04021 |
| DST        | interaction | wind_over_10:snow_any | -0.02472 |   0.02182 |   0.25735 | -0.06749 |   0.01805 | 3556 | 0.04021 |
| K          | interaction | wind_over_10:rain_any |  0.00544 |   0.00844 |   0.51900 | -0.01110 |   0.02199 | 3616 | 0.01356 |
| K          | interaction | wind_over_10:snow_any |  0.01291 |   0.01277 |   0.31230 | -0.01213 |   0.03794 | 3616 | 0.01356 |
| QB         | interaction | wind_over_10:rain_any | -0.00409 |   0.00755 |   0.58816 | -0.01889 |   0.01071 | 3623 | 0.03183 |
| QB         | interaction | wind_over_10:snow_any | -0.01840 |   0.01008 |   0.06789 | -0.03815 |   0.00135 | 3623 | 0.03183 |
| RB         | interaction | wind_over_10:rain_any | -0.01065 |   0.00669 |   0.11129 | -0.02376 |   0.00246 | 3628 | 0.01645 |
| RB         | interaction | wind_over_10:snow_any | -0.03193 |   0.00892 |   0.00035 | -0.04941 |  -0.01444 | 3628 | 0.01645 |
| TE         | interaction | wind_over_10:rain_any |  0.00560 |   0.00837 |   0.50368 | -0.01080 |   0.02199 | 3614 | 0.01711 |
| TE         | interaction | wind_over_10:snow_any | -0.02100 |   0.01675 |   0.20979 | -0.05382 |   0.01182 | 3614 | 0.01711 |
| WR         | interaction | wind_over_10:rain_any | -0.00664 |   0.00582 |   0.25427 | -0.01805 |   0.00477 | 3628 | 0.02431 |
| WR         | interaction | wind_over_10:snow_any | -0.01103 |   0.00772 |   0.15323 | -0.02616 |   0.00411 | 3628 | 0.02431 |

## Bucket summaries

| position   | bucket     |    n |   mean_residual_pct |   median_residual_pct |   mean_residual_points |   mean_actual_fp |   mean_expected_fp |   weather_mean | weather_variable   |
|:-----------|:-----------|-----:|--------------------:|----------------------:|-----------------------:|-----------------:|-------------------:|---------------:|:-------------------|
| DST        | <10        | 2519 |              0.0539 |               -0.1502 |                -0.1700 |           5.1008 |             5.2708 |         5.9658 | wind_speed_mph_avg |
| DST        | 10-14.9    |  774 |              0.1865 |               -0.0220 |                 0.4531 |           5.7494 |             5.2963 |        11.9681 | wind_speed_mph_avg |
| DST        | 15-19.9    |  220 |              0.0894 |               -0.0916 |                 0.0153 |           5.3773 |             5.3620 |        16.9995 | wind_speed_mph_avg |
| DST        | 20-24.9    |   36 |              0.3660 |               -0.1169 |                 1.3604 |           6.0000 |             4.6396 |        21.3611 | wind_speed_mph_avg |
| DST        | 25+        |    7 |             -0.0047 |               -0.2445 |                -0.6203 |           5.0000 |             5.6203 |        27.3286 | wind_speed_mph_avg |
| K          | <10        | 2573 |              0.0733 |               -0.0258 |                 0.1634 |           8.0326 |             7.8693 |         5.9710 | wind_speed_mph_avg |
| K          | 10-14.9    |  778 |              0.0214 |               -0.0693 |                -0.3097 |           7.4512 |             7.7608 |        11.9675 | wind_speed_mph_avg |
| K          | 15-19.9    |  222 |             -0.0258 |               -0.1160 |                -0.6512 |           7.3243 |             7.9756 |        16.9899 | wind_speed_mph_avg |
| K          | 20-24.9    |   35 |             -0.1545 |               -0.3523 |                -1.6167 |           6.2000 |             7.8167 |        21.3929 | wind_speed_mph_avg |
| K          | 25+        |    8 |             -0.3415 |               -0.2550 |                -2.3430 |           4.7500 |             7.0930 |        27.5250 | wind_speed_mph_avg |
| QB         | <10        | 2573 |              0.0561 |               -0.0000 |                 0.3253 |          16.7514 |            16.4261 |         5.9763 | wind_speed_mph_avg |
| QB         | 10-14.9    |  784 |             -0.0119 |               -0.0565 |                -0.7194 |          15.4155 |            16.1349 |        11.9694 | wind_speed_mph_avg |
| QB         | 15-19.9    |  222 |             -0.0133 |               -0.0600 |                -0.6886 |          15.5232 |            16.2118 |        16.9899 | wind_speed_mph_avg |
| QB         | 20-24.9    |   36 |             -0.2758 |               -0.2708 |                -4.9777 |          12.6044 |            17.5822 |        21.3611 | wind_speed_mph_avg |
| QB         | 25+        |    8 |             -0.4032 |               -0.3357 |                -6.6582 |          10.6050 |            17.2632 |        27.5250 | wind_speed_mph_avg |
| RB         | <10        | 2577 |              0.0258 |               -0.0523 |                -0.0300 |          22.4573 |            22.4873 |         5.9732 | wind_speed_mph_avg |
| RB         | 10-14.9    |  785 |              0.0257 |               -0.0488 |                -0.1185 |          22.6255 |            22.7440 |        11.9675 | wind_speed_mph_avg |
| RB         | 15-19.9    |  222 |              0.0731 |               -0.0098 |                 0.6178 |          22.9141 |            22.2964 |        16.9899 | wind_speed_mph_avg |
| RB         | 20-24.9    |   36 |             -0.1047 |               -0.2328 |                -2.7691 |          21.6472 |            24.4163 |        21.3611 | wind_speed_mph_avg |
| RB         | 25+        |    8 |              0.0707 |               -0.0808 |                 1.2904 |          22.2875 |            20.9971 |        27.5250 | wind_speed_mph_avg |
| TE         | <10        | 2569 |              0.1000 |               -0.0617 |                 0.3080 |          12.7624 |            12.4544 |         5.9775 | wind_speed_mph_avg |
| TE         | 10-14.9    |  779 |              0.0528 |               -0.1005 |                -0.3437 |          11.6437 |            11.9874 |        11.9668 | wind_speed_mph_avg |
| TE         | 15-19.9    |  222 |             -0.1115 |               -0.1821 |                -1.6071 |          11.1996 |            12.8068 |        16.9899 | wind_speed_mph_avg |
| TE         | 20-24.9    |   36 |             -0.2098 |               -0.2918 |                -3.2868 |           9.5889 |            12.8757 |        21.3611 | wind_speed_mph_avg |
| TE         | 25+        |    8 |             -0.3662 |               -0.2386 |                -5.5362 |           9.1625 |            14.6987 |        27.5250 | wind_speed_mph_avg |
| WR         | <10        | 2577 |              0.0440 |               -0.0090 |                 0.5504 |          33.5575 |            33.0071 |         5.9732 | wind_speed_mph_avg |
| WR         | 10-14.9    |  785 |             -0.0397 |               -0.0854 |                -2.0541 |          30.6417 |            32.6958 |        11.9675 | wind_speed_mph_avg |
| WR         | 15-19.9    |  222 |             -0.0316 |               -0.0931 |                -1.3922 |          31.0650 |            32.4571 |        16.9899 | wind_speed_mph_avg |
| WR         | 20-24.9    |   36 |             -0.1256 |               -0.1842 |                -5.4952 |          26.7944 |            32.2896 |        21.3611 | wind_speed_mph_avg |
| WR         | 25+        |    8 |             -0.4614 |               -0.4054 |               -14.6125 |          17.4375 |            32.0500 |        27.5250 | wind_speed_mph_avg |
| DST        | <15        | 1157 |              0.0554 |               -0.1717 |                -0.1692 |           5.0761 |             5.2452 |        11.1918 | wind_gust_mph_max  |
| DST        | 15-24.9    | 1650 |              0.0762 |               -0.1123 |                -0.0720 |           5.2255 |             5.2974 |        19.4990 | wind_gust_mph_max  |
| DST        | 25-34.9    |  589 |              0.2104 |                0.0056 |                 0.5931 |           5.8998 |             5.3067 |        28.7569 | wind_gust_mph_max  |
| DST        | 35-44.9    |  135 |              0.0139 |               -0.2336 |                -0.2927 |           4.8815 |             5.1741 |        38.6948 | wind_gust_mph_max  |
| DST        | 45+        |   25 |             -0.1049 |               -0.1749 |                -0.9961 |           4.1600 |             5.1561 |        51.0920 | wind_gust_mph_max  |
| K          | <15        | 1172 |              0.0824 |               -0.0104 |                 0.2498 |           8.0947 |             7.8449 |        11.1855 | wind_gust_mph_max  |
| K          | 15-24.9    | 1685 |              0.0574 |               -0.0524 |                 0.0120 |           7.9092 |             7.8972 |        19.4823 | wind_gust_mph_max  |
| K          | 25-34.9    |  597 |              0.0153 |               -0.0567 |                -0.3343 |           7.3853 |             7.7196 |        28.7484 | wind_gust_mph_max  |
| K          | 35-44.9    |  136 |             -0.0303 |               -0.1435 |                -0.7089 |           7.2206 |             7.9295 |        38.7066 | wind_gust_mph_max  |
| K          | 45+        |   26 |             -0.2690 |               -0.3113 |                -2.2062 |           5.4231 |             7.6292 |        51.1385 | wind_gust_mph_max  |
| QB         | <15        | 1171 |              0.0614 |               -0.0068 |                 0.4120 |          16.9714 |            16.5594 |        11.1891 | wind_gust_mph_max  |
| QB         | 15-24.9    | 1689 |              0.0390 |               -0.0045 |                 0.0875 |          16.2874 |            16.1999 |        19.4866 | wind_gust_mph_max  |
| QB         | 25-34.9    |  600 |             -0.0175 |               -0.0763 |                -0.8994 |          15.3796 |            16.2790 |        28.7533 | wind_gust_mph_max  |
| QB         | 35-44.9    |  137 |             -0.0313 |               -0.0952 |                -0.9220 |          15.9943 |            16.9163 |        38.7212 | wind_gust_mph_max  |
| QB         | 45+        |   26 |             -0.1598 |               -0.2540 |                -2.9454 |          14.2331 |            17.1785 |        51.1385 | wind_gust_mph_max  |
| RB         | <15        | 1173 |              0.0208 |               -0.0606 |                -0.1124 |          22.2065 |            22.3189 |        11.1876 | wind_gust_mph_max  |
| RB         | 15-24.9    | 1692 |              0.0267 |               -0.0473 |                -0.0268 |          22.6872 |            22.7140 |        19.4868 | wind_gust_mph_max  |
| RB         | 25-34.9    |  600 |              0.0271 |               -0.0514 |                -0.1618 |          22.4381 |            22.5999 |        28.7533 | wind_gust_mph_max  |
| RB         | 35-44.9    |  137 |              0.0961 |                0.0200 |                 0.9664 |          23.0336 |            22.0672 |        38.7212 | wind_gust_mph_max  |
| RB         | 45+        |   26 |              0.0203 |               -0.0531 |                 0.7389 |          24.0192 |            23.2804 |        51.1385 | wind_gust_mph_max  |
| TE         | <15        | 1168 |              0.1301 |               -0.0590 |                 0.6790 |          13.1989 |            12.5199 |        11.1931 | wind_gust_mph_max  |
| TE         | 15-24.9    | 1684 |              0.0690 |               -0.0612 |                -0.0646 |          12.2559 |            12.3205 |        19.4806 | wind_gust_mph_max  |
| TE         | 25-34.9    |  599 |              0.0349 |               -0.1218 |                -0.4904 |          11.6082 |            12.0987 |        28.7573 | wind_gust_mph_max  |
| TE         | 35-44.9    |  137 |             -0.1485 |               -0.2989 |                -2.3504 |          10.7628 |            13.1132 |        38.7212 | wind_gust_mph_max  |
| TE         | 45+        |   26 |             -0.2281 |               -0.3975 |                -2.4734 |          10.7269 |            13.2004 |        51.1385 | wind_gust_mph_max  |
| WR         | <15        | 1173 |              0.0491 |               -0.0009 |                 0.6652 |          33.8970 |            33.2317 |        11.1876 | wind_gust_mph_max  |
| WR         | 15-24.9    | 1692 |              0.0234 |               -0.0301 |                -0.0068 |          32.6546 |            32.6614 |        19.4868 | wind_gust_mph_max  |
| WR         | 25-34.9    |  600 |             -0.0301 |               -0.0912 |                -1.8420 |          30.9813 |            32.8233 |        28.7533 | wind_gust_mph_max  |
| WR         | 35-44.9    |  137 |             -0.0496 |               -0.1123 |                -2.2487 |          30.9420 |            33.1908 |        38.7212 | wind_gust_mph_max  |
| WR         | 45+        |   26 |             -0.2033 |               -0.2924 |                -6.6725 |          26.5869 |            33.2595 |        51.1385 | wind_gust_mph_max  |
| DST        | <20        |   56 |              0.3972 |                0.0105 |                 1.2625 |           6.4643 |             5.2018 |        13.9214 | temperature_f_avg  |
| DST        | 20-32      |  195 |              0.0929 |               -0.0530 |                 0.0165 |           5.2615 |             5.2450 |        28.4396 | temperature_f_avg  |
| DST        | 33-45      |  682 |              0.0724 |               -0.1069 |                -0.0146 |           5.2713 |             5.2859 |        39.8383 | temperature_f_avg  |
| DST        | 46-55      |  654 |              0.0602 |               -0.1326 |                -0.2270 |           5.1927 |             5.4197 |        51.2700 | temperature_f_avg  |
| DST        | 56-85      | 1865 |              0.0899 |               -0.1244 |                 0.0196 |           5.2386 |             5.2190 |        69.9292 | temperature_f_avg  |
| DST        | 86+        |  104 |              0.1564 |               -0.1634 |                 0.1774 |           5.6154 |             5.4379 |        88.7964 | temperature_f_avg  |
| K          | <20        |   56 |             -0.1035 |               -0.1098 |                -1.3551 |           6.5893 |             7.9444 |        13.9214 | temperature_f_avg  |
| K          | 20-32      |  196 |             -0.0154 |               -0.1148 |                -0.4917 |           7.2194 |             7.7111 |        28.3912 | temperature_f_avg  |
| K          | 33-45      |  690 |              0.0002 |               -0.0877 |                -0.3644 |           7.5188 |             7.8832 |        39.8305 | temperature_f_avg  |
| K          | 46-55      |  665 |              0.0219 |               -0.0626 |                -0.1562 |           7.7624 |             7.9186 |        51.2905 | temperature_f_avg  |
| K          | 56-85      | 1906 |              0.0929 |               -0.0211 |                 0.2311 |           8.0567 |             7.8256 |        69.8911 | temperature_f_avg  |
| K          | 86+        |  103 |              0.0819 |                0.0749 |                 0.4531 |           8.3107 |             7.8575 |        88.8381 | temperature_f_avg  |
| QB         | <20        |   56 |             -0.1641 |               -0.2256 |                -3.8138 |          12.7725 |            16.5863 |        13.9214 | temperature_f_avg  |
| QB         | 20-32      |  198 |             -0.0667 |               -0.0978 |                -1.5335 |          15.6226 |            17.1561 |        28.3866 | temperature_f_avg  |
| QB         | 33-45      |  688 |              0.0022 |               -0.0485 |                -0.5305 |          15.9182 |            16.4487 |        39.8438 | temperature_f_avg  |
| QB         | 46-55      |  663 |              0.0091 |               -0.0520 |                -0.3875 |          16.0871 |            16.4746 |        51.3034 | temperature_f_avg  |
| QB         | 56-85      | 1913 |              0.0640 |                0.0067 |                 0.4714 |          16.7099 |            16.2385 |        69.8992 | temperature_f_avg  |
| QB         | 86+        |  105 |              0.1063 |                0.0284 |                 1.1916 |          16.9512 |            15.7597 |        88.8195 | temperature_f_avg  |
| RB         | <20        |   56 |             -0.0706 |               -0.1076 |                -2.0417 |          21.2911 |            23.3328 |        13.9214 | temperature_f_avg  |
| RB         | 20-32      |  198 |              0.0010 |               -0.0430 |                -0.2190 |          22.6831 |            22.9022 |        28.3866 | temperature_f_avg  |
| RB         | 33-45      |  690 |              0.0490 |               -0.0165 |                 0.4467 |          22.9813 |            22.5347 |        39.8305 | temperature_f_avg  |
| RB         | 46-55      |  665 |              0.0166 |               -0.0620 |                -0.2643 |          22.2849 |            22.5492 |        51.2905 | temperature_f_avg  |
| RB         | 56-85      | 1914 |              0.0283 |               -0.0559 |                -0.0677 |          22.4675 |            22.5352 |        69.8996 | temperature_f_avg  |
| RB         | 86+        |  105 |              0.0415 |               -0.0569 |                 0.3059 |          22.0480 |            21.7421 |        88.8195 | temperature_f_avg  |
| TE         | <20        |   56 |             -0.0035 |               -0.2953 |                -1.3030 |          11.3143 |            12.6172 |        13.9214 | temperature_f_avg  |
| TE         | 20-32      |  196 |             -0.0403 |               -0.1997 |                -1.2760 |          11.4837 |            12.7597 |        28.4328 | temperature_f_avg  |
| TE         | 33-45      |  687 |              0.0609 |               -0.1127 |                -0.1954 |          12.3044 |            12.4998 |        39.8353 | temperature_f_avg  |
| TE         | 46-55      |  664 |              0.0463 |               -0.0813 |                -0.0728 |          12.4704 |            12.5432 |        51.2842 | temperature_f_avg  |
| TE         | 56-85      | 1907 |              0.0994 |               -0.0555 |                 0.2892 |          12.5818 |            12.2926 |        69.9069 | temperature_f_avg  |
| TE         | 86+        |  104 |              0.0854 |               -0.0798 |                -0.4011 |          11.0635 |            11.4645 |        88.8363 | temperature_f_avg  |
| WR         | <20        |   56 |             -0.0486 |               -0.1286 |                -2.6761 |          28.8304 |            31.5065 |        13.9214 | temperature_f_avg  |
| WR         | 20-32      |  198 |             -0.0510 |               -0.0756 |                -1.9210 |          30.6104 |            32.5314 |        28.3866 | temperature_f_avg  |
| WR         | 33-45      |  690 |             -0.0273 |               -0.0696 |                -1.7554 |          30.7541 |            32.5095 |        39.8305 | temperature_f_avg  |
| WR         | 46-55      |  665 |              0.0068 |               -0.0373 |                -0.4696 |          32.3500 |            32.8196 |        51.2905 | temperature_f_avg  |
| WR         | 56-85      | 1914 |              0.0445 |               -0.0142 |                 0.5512 |          33.6404 |            33.0892 |        69.8996 | temperature_f_avg  |
| WR         | 86+        |  105 |              0.0860 |               -0.0142 |                 1.7226 |          35.5785 |            33.8559 |        88.8195 | temperature_f_avg  |
| DST        | none/trace | 2807 |              0.0722 |               -0.1361 |                -0.1121 |           5.1496 |             5.2618 |         0.0010 | rain_mm_h_avg      |
| DST        | light      |  497 |              0.0819 |               -0.1038 |                 0.0750 |           5.4044 |             5.3294 |         0.1804 | rain_mm_h_avg      |
| DST        | moderate   |  222 |              0.2432 |                0.0569 |                 0.8591 |           6.2297 |             5.3706 |         1.0734 | rain_mm_h_avg      |
| DST        | heavy      |   30 |              0.5223 |                0.1501 |                 1.9069 |           6.9667 |             5.0598 |         3.8700 | rain_mm_h_avg      |
| K          | none/trace | 2857 |              0.0605 |               -0.0381 |                 0.0405 |           7.9174 |             7.8769 |         0.0010 | rain_mm_h_avg      |
| K          | light      |  502 |              0.0398 |               -0.0611 |                -0.1018 |           7.6633 |             7.7652 |         0.1800 | rain_mm_h_avg      |
| K          | moderate   |  227 |             -0.0083 |               -0.0626 |                -0.3531 |           7.3921 |             7.7451 |         1.0706 | rain_mm_h_avg      |
| K          | heavy      |   30 |              0.0151 |               -0.1141 |                -0.8249 |           6.7000 |             7.5249 |         3.8700 | rain_mm_h_avg      |
| QB         | none/trace | 2862 |              0.0461 |               -0.0019 |                 0.1857 |          16.5488 |            16.3631 |         0.0010 | rain_mm_h_avg      |
| QB         | light      |  504 |              0.0207 |               -0.0751 |                -0.2204 |          16.1730 |            16.3934 |         0.1806 | rain_mm_h_avg      |
| QB         | moderate   |  227 |             -0.0815 |               -0.1338 |                -1.8623 |          14.4174 |            16.2797 |         1.0706 | rain_mm_h_avg      |
| QB         | heavy      |   30 |             -0.1645 |               -0.2897 |                -3.6609 |          12.8473 |            16.5082 |         3.8700 | rain_mm_h_avg      |
| RB         | none/trace | 2866 |              0.0273 |               -0.0467 |                -0.0137 |          22.6057 |            22.6193 |         0.0010 | rain_mm_h_avg      |
| RB         | light      |  505 |              0.0374 |               -0.0520 |                 0.1093 |          22.3503 |            22.2410 |         0.1803 | rain_mm_h_avg      |
| RB         | moderate   |  227 |              0.0119 |               -0.0667 |                -0.5538 |          21.7293 |            22.2830 |         1.0706 | rain_mm_h_avg      |
| RB         | heavy      |   30 |             -0.0057 |               -0.1095 |                -0.4324 |          22.3567 |            22.7890 |         3.8700 | rain_mm_h_avg      |
| TE         | none/trace | 2855 |              0.0960 |               -0.0619 |                 0.2506 |          12.6471 |            12.3965 |         0.0010 | rain_mm_h_avg      |
| TE         | light      |  504 |             -0.0111 |               -0.1430 |                -0.7982 |          11.3795 |            12.1777 |         0.1802 | rain_mm_h_avg      |
| TE         | moderate   |  226 |             -0.0120 |               -0.1658 |                -1.1793 |          11.4877 |            12.6670 |         1.0690 | rain_mm_h_avg      |
| TE         | heavy      |   29 |             -0.1025 |               -0.2057 |                -1.4687 |          11.1379 |            12.6066 |         3.8241 | rain_mm_h_avg      |
| WR         | none/trace | 2866 |              0.0231 |               -0.0271 |                -0.0250 |          32.8695 |            32.8945 |         0.0010 | rain_mm_h_avg      |
| WR         | light      |  505 |              0.0387 |               -0.0235 |                 0.1105 |          33.1799 |            33.0695 |         0.1803 | rain_mm_h_avg      |
| WR         | moderate   |  227 |             -0.0615 |               -0.1124 |                -2.7896 |          29.8562 |            32.6458 |         1.0706 | rain_mm_h_avg      |
| WR         | heavy      |   30 |             -0.1592 |               -0.1798 |                -5.6264 |          26.4820 |            32.1084 |         3.8700 | rain_mm_h_avg      |
| DST        | none/trace | 3475 |              0.0864 |               -0.1236 |                -0.0211 |           5.2708 |             5.2919 |         0.0001 | snow_cm_h_avg      |
| DST        | light      |   31 |              0.1903 |               -0.1064 |                 0.6344 |           5.2903 |             4.6559 |         0.0514 | snow_cm_h_avg      |
| DST        | moderate   |   38 |              0.0338 |               -0.1124 |                 0.0091 |           4.7632 |             4.7540 |         0.2413 | snow_cm_h_avg      |
| DST        | heavy      |   10 |              0.3651 |                0.2197 |                 1.5742 |           5.2000 |             3.6258 |         0.7350 | snow_cm_h_avg      |
| DST        | extreme    |    2 |              0.8954 |                0.8954 |                 4.0114 |          10.0000 |             5.9886 |         1.6800 | snow_cm_h_avg      |
| K          | none/trace | 3535 |              0.0574 |               -0.0403 |                 0.0219 |           7.8764 |             7.8544 |         0.0001 | snow_cm_h_avg      |
| K          | light      |   31 |             -0.1420 |               -0.2879 |                -1.4891 |           6.5161 |             8.0052 |         0.0519 | snow_cm_h_avg      |
| K          | moderate   |   38 |             -0.2120 |               -0.2466 |                -1.7912 |           5.8684 |             7.6596 |         0.2413 | snow_cm_h_avg      |
| K          | heavy      |   10 |              0.1197 |               -0.1307 |                -0.3039 |           6.5000 |             6.8039 |         0.7350 | snow_cm_h_avg      |
| K          | extreme    |    2 |             -0.1274 |               -0.1274 |                -0.3636 |           6.5000 |             6.8636 |         1.6800 | snow_cm_h_avg      |
| QB         | none/trace | 3541 |              0.0353 |               -0.0204 |                 0.0075 |          16.3593 |            16.3518 |         0.0001 | snow_cm_h_avg      |
| QB         | light      |   32 |             -0.1855 |               -0.1996 |                -3.3806 |          14.6050 |            17.9856 |         0.0514 | snow_cm_h_avg      |
| QB         | moderate   |   38 |              0.0497 |               -0.0476 |                -0.0251 |          16.7258 |            16.7509 |         0.2413 | snow_cm_h_avg      |
| QB         | heavy      |   10 |             -0.0562 |               -0.3393 |                -1.1545 |          13.6900 |            14.8445 |         0.7350 | snow_cm_h_avg      |
| QB         | extreme    |    2 |             -0.8168 |               -0.8168 |                -9.1277 |           1.8600 |            10.9877 |         1.6800 | snow_cm_h_avg      |
| RB         | none/trace | 3546 |              0.0262 |               -0.0538 |                -0.0598 |          22.4766 |            22.5365 |         0.0001 | snow_cm_h_avg      |
| RB         | light      |   32 |             -0.0286 |               -0.0697 |                -1.1054 |          23.2438 |            24.3492 |         0.0514 | snow_cm_h_avg      |
| RB         | moderate   |   38 |              0.2220 |                0.1566 |                 3.8769 |          26.0026 |            22.1257 |         0.2413 | snow_cm_h_avg      |
| RB         | heavy      |   10 |             -0.0419 |                0.0358 |                -1.6277 |          19.9400 |            21.5677 |         0.7350 | snow_cm_h_avg      |
| RB         | extreme    |    2 |             -0.1469 |               -0.1469 |                -3.1077 |          22.2500 |            25.3577 |         1.6800 | snow_cm_h_avg      |
| TE         | none/trace | 3534 |              0.0732 |               -0.0816 |                 0.0149 |          12.4014 |            12.3865 |         0.0001 | snow_cm_h_avg      |
| TE         | light      |   31 |             -0.1210 |               -0.2137 |                -2.3703 |           9.9000 |            12.2703 |         0.0519 | snow_cm_h_avg      |
| TE         | moderate   |   38 |              0.2914 |               -0.0702 |                 1.6819 |          13.8474 |            12.1655 |         0.2413 | snow_cm_h_avg      |
| TE         | heavy      |    9 |             -0.1673 |               -0.1989 |                -2.3681 |          10.7000 |            13.0681 |         0.7544 | snow_cm_h_avg      |
| TE         | extreme    |    2 |             -0.7404 |               -0.7404 |                -8.8022 |           3.0500 |            11.8522 |         1.6800 | snow_cm_h_avg      |
| WR         | none/trace | 3546 |              0.0226 |               -0.0302 |                -0.1003 |          32.8137 |            32.9140 |         0.0001 | snow_cm_h_avg      |
| WR         | light      |   32 |             -0.2280 |               -0.3244 |                -8.9255 |          25.1969 |            34.1224 |         0.0514 | snow_cm_h_avg      |
| WR         | moderate   |   38 |             -0.1236 |               -0.1784 |                -4.3907 |          27.5253 |            31.9160 |         0.2413 | snow_cm_h_avg      |
| WR         | heavy      |   10 |              0.0144 |               -0.0562 |                 1.9065 |          30.3200 |            28.4135 |         0.7350 | snow_cm_h_avg      |
| WR         | extreme    |    2 |             -0.6024 |               -0.6024 |               -14.3927 |           9.5500 |            23.9427 |         1.6800 | snow_cm_h_avg      |

## Coefficient stability blocks

| position   | block     | term          |     coef |   p_value |    n |
|:-----------|:----------|:--------------|---------:|----------:|-----:|
| DST        | 2016-2021 | wind_over_10  |  0.05254 |   0.00113 | 2084 |
| DST        | 2016-2021 | gust_over_20  | -0.02226 |   0.00135 | 2084 |
| DST        | 2016-2021 | rain_any      |  0.02294 |   0.70791 | 2084 |
| DST        | 2016-2021 | rain_mm_h_avg |  0.10180 |   0.04085 | 2084 |
| DST        | 2016-2021 | snow_any      |  0.20757 |   0.25768 | 2084 |
| DST        | 2016-2021 | snow_cm_h_avg |  0.04154 |   0.93307 | 2084 |
| DST        | 2016-2021 | cold_10f      |  0.00279 |   0.91167 | 2084 |
| DST        | 2016-2021 | heat_10f      | -0.11049 |   0.76228 | 2084 |
| DST        | 2022-2023 | wind_over_10  | -0.01838 |   0.40965 |  756 |
| DST        | 2022-2023 | gust_over_20  |  0.00820 |   0.49725 |  756 |
| DST        | 2022-2023 | rain_any      | -0.04816 |   0.54650 |  756 |
| DST        | 2022-2023 | rain_mm_h_avg |  0.14934 |   0.05850 |  756 |
| DST        | 2022-2023 | snow_any      |  0.00188 |   0.99504 |  756 |
| DST        | 2022-2023 | snow_cm_h_avg |  0.21936 |   0.32681 |  756 |
| DST        | 2022-2023 | cold_10f      |  0.04241 |   0.23338 |  756 |
| DST        | 2022-2023 | heat_10f      |  0.01273 |   0.97613 |  756 |
| DST        | 2024-2025 | wind_over_10  |  0.01121 |   0.71620 |  716 |
| DST        | 2024-2025 | gust_over_20  |  0.00065 |   0.95309 |  716 |
| DST        | 2024-2025 | rain_any      |  0.11225 |   0.39695 |  716 |
| DST        | 2024-2025 | rain_mm_h_avg |  0.03777 |   0.69594 |  716 |
| DST        | 2024-2025 | snow_any      | -0.70500 |   0.00005 |  716 |
| DST        | 2024-2025 | snow_cm_h_avg | -0.03139 |   0.96598 |  716 |
| DST        | 2024-2025 | cold_10f      |  0.08310 |   0.06579 |  716 |
| DST        | 2024-2025 | heat_10f      |  0.29625 |   0.08147 |  716 |
| K          | 2016-2021 | wind_over_10  | -0.01684 |   0.12360 | 2148 |
| K          | 2016-2021 | gust_over_20  |  0.00047 |   0.91790 | 2148 |
| K          | 2016-2021 | rain_any      | -0.05165 |   0.23195 | 2148 |
| K          | 2016-2021 | rain_mm_h_avg |  0.01248 |   0.71491 | 2148 |
| K          | 2016-2021 | snow_any      | -0.08938 |   0.45985 | 2148 |
| K          | 2016-2021 | snow_cm_h_avg |  0.01485 |   0.96745 | 2148 |
| K          | 2016-2021 | cold_10f      | -0.03467 |   0.02927 | 2148 |
| K          | 2016-2021 | heat_10f      | -0.06554 |   0.78451 | 2148 |
| K          | 2022-2023 | wind_over_10  |  0.00883 |   0.60684 |  754 |
| K          | 2022-2023 | gust_over_20  | -0.01557 |   0.08113 |  754 |
| K          | 2022-2023 | rain_any      |  0.00215 |   0.97291 |  754 |
| K          | 2022-2023 | rain_mm_h_avg | -0.00146 |   0.97481 |  754 |
| K          | 2022-2023 | snow_any      |  0.02085 |   0.85813 |  754 |
| K          | 2022-2023 | snow_cm_h_avg |  0.06100 |   0.41256 |  754 |
| K          | 2022-2023 | cold_10f      | -0.04234 |   0.12208 |  754 |
| K          | 2022-2023 | heat_10f      |  0.03269 |   0.79500 |  754 |
| K          | 2024-2025 | wind_over_10  |  0.01609 |   0.43657 |  714 |
| K          | 2024-2025 | gust_over_20  | -0.00658 |   0.46121 |  714 |
| K          | 2024-2025 | rain_any      | -0.02685 |   0.70442 |  714 |
| K          | 2024-2025 | rain_mm_h_avg | -0.04555 |   0.08326 |  714 |
| K          | 2024-2025 | snow_any      | -0.08562 |   0.48998 |  714 |
| K          | 2024-2025 | snow_cm_h_avg | -0.85936 |   0.05973 |  714 |
| K          | 2024-2025 | cold_10f      | -0.04901 |   0.03270 |  714 |
| K          | 2024-2025 | heat_10f      |  0.10412 |   0.45110 |  714 |
| QB         | 2016-2021 | wind_over_10  | -0.01491 |   0.13467 | 2151 |
| QB         | 2016-2021 | gust_over_20  |  0.00189 |   0.65548 | 2151 |
| QB         | 2016-2021 | rain_any      | -0.03266 |   0.38830 | 2151 |
| QB         | 2016-2021 | rain_mm_h_avg | -0.08309 |   0.00188 | 2151 |
| QB         | 2016-2021 | snow_any      | -0.07358 |   0.50562 | 2151 |
| QB         | 2016-2021 | snow_cm_h_avg |  0.05232 |   0.87241 | 2151 |
| QB         | 2016-2021 | cold_10f      | -0.04018 |   0.00470 | 2151 |
| QB         | 2016-2021 | heat_10f      |  0.09545 |   0.65323 | 2151 |
| QB         | 2022-2023 | wind_over_10  | -0.00978 |   0.53849 |  756 |
| QB         | 2022-2023 | gust_over_20  | -0.00400 |   0.57765 |  756 |
| QB         | 2022-2023 | rain_any      | -0.02050 |   0.72319 |  756 |
| QB         | 2022-2023 | rain_mm_h_avg | -0.03129 |   0.40687 |  756 |
| QB         | 2022-2023 | snow_any      |  0.00314 |   0.98065 |  756 |
| QB         | 2022-2023 | snow_cm_h_avg | -0.38323 |   0.00000 |  756 |
| QB         | 2022-2023 | cold_10f      | -0.04025 |   0.07571 |  756 |
| QB         | 2022-2023 | heat_10f      |  0.22904 |   0.27251 |  756 |
| QB         | 2024-2025 | wind_over_10  | -0.01290 |   0.43422 |  716 |
| QB         | 2024-2025 | gust_over_20  | -0.00224 |   0.71156 |  716 |
| QB         | 2024-2025 | rain_any      | -0.01449 |   0.82853 |  716 |
| QB         | 2024-2025 | rain_mm_h_avg | -0.01606 |   0.68706 |  716 |
| QB         | 2024-2025 | snow_any      |  0.24510 |   0.10493 |  716 |
| QB         | 2024-2025 | snow_cm_h_avg |  0.44935 |   0.59574 |  716 |
| QB         | 2024-2025 | cold_10f      | -0.05491 |   0.00277 |  716 |
| QB         | 2024-2025 | heat_10f      | -0.00753 |   0.89770 |  716 |
| RB         | 2016-2021 | wind_over_10  | -0.00707 |   0.36446 | 2156 |
| RB         | 2016-2021 | gust_over_20  |  0.00584 |   0.07241 | 2156 |
| RB         | 2016-2021 | rain_any      |  0.00108 |   0.97407 | 2156 |
| RB         | 2016-2021 | rain_mm_h_avg | -0.00196 |   0.95436 | 2156 |
| RB         | 2016-2021 | snow_any      |  0.00104 |   0.99182 | 2156 |
| RB         | 2016-2021 | snow_cm_h_avg | -0.08156 |   0.67668 | 2156 |
| RB         | 2016-2021 | cold_10f      | -0.01398 |   0.20267 | 2156 |
| RB         | 2016-2021 | heat_10f      | -0.09573 |   0.37274 | 2156 |
| RB         | 2022-2023 | wind_over_10  |  0.01223 |   0.45823 |  756 |
| RB         | 2022-2023 | gust_over_20  | -0.01209 |   0.16779 |  756 |
| RB         | 2022-2023 | rain_any      | -0.01907 |   0.69909 |  756 |
| RB         | 2022-2023 | rain_mm_h_avg | -0.02915 |   0.27467 |  756 |
| RB         | 2022-2023 | snow_any      |  0.16926 |   0.29996 |  756 |
| RB         | 2022-2023 | snow_cm_h_avg | -0.09502 |   0.38779 |  756 |
| RB         | 2022-2023 | cold_10f      | -0.01543 |   0.35978 |  756 |
| RB         | 2022-2023 | heat_10f      |  0.08308 |   0.55259 |  756 |
| RB         | 2024-2025 | wind_over_10  | -0.00127 |   0.93461 |  716 |
| RB         | 2024-2025 | gust_over_20  |  0.00354 |   0.49696 |  716 |
| RB         | 2024-2025 | rain_any      | -0.00186 |   0.97266 |  716 |
| RB         | 2024-2025 | rain_mm_h_avg | -0.01714 |   0.58644 |  716 |
| RB         | 2024-2025 | snow_any      |  0.07297 |   0.60950 |  716 |
| RB         | 2024-2025 | snow_cm_h_avg |  1.28690 |   0.06929 |  716 |
| RB         | 2024-2025 | cold_10f      | -0.01378 |   0.31957 |  716 |
| RB         | 2024-2025 | heat_10f      | -0.18803 |   0.09206 |  716 |
| TE         | 2016-2021 | wind_over_10  | -0.02189 |   0.12205 | 2146 |
| TE         | 2016-2021 | gust_over_20  | -0.00096 |   0.88760 | 2146 |
| TE         | 2016-2021 | rain_any      | -0.05641 |   0.24928 | 2146 |
| TE         | 2016-2021 | rain_mm_h_avg | -0.03616 |   0.34617 | 2146 |
| TE         | 2016-2021 | snow_any      |  0.17944 |   0.45305 | 2146 |
| TE         | 2016-2021 | snow_cm_h_avg | -0.41521 |   0.34976 | 2146 |
| TE         | 2016-2021 | cold_10f      | -0.03927 |   0.03511 | 2146 |
| TE         | 2016-2021 | heat_10f      |  0.07184 |   0.80075 | 2146 |
| TE         | 2022-2023 | wind_over_10  | -0.03000 |   0.15671 |  754 |
| TE         | 2022-2023 | gust_over_20  |  0.00576 |   0.61210 |  754 |
| TE         | 2022-2023 | rain_any      | -0.13810 |   0.08757 |  754 |
| TE         | 2022-2023 | rain_mm_h_avg |  0.01489 |   0.74421 |  754 |
| TE         | 2022-2023 | snow_any      |  0.29664 |   0.18471 |  754 |
| TE         | 2022-2023 | snow_cm_h_avg | -0.52454 |   0.00003 |  754 |
| TE         | 2022-2023 | cold_10f      | -0.03834 |   0.20778 |  754 |
| TE         | 2022-2023 | heat_10f      | -0.24843 |   0.10810 |  754 |
| TE         | 2024-2025 | wind_over_10  | -0.03312 |   0.03520 |  714 |
| TE         | 2024-2025 | gust_over_20  |  0.00175 |   0.81373 |  714 |
| TE         | 2024-2025 | rain_any      | -0.06759 |   0.39230 |  714 |
| TE         | 2024-2025 | rain_mm_h_avg |  0.01898 |   0.77370 |  714 |
| TE         | 2024-2025 | snow_any      |  0.10572 |   0.67458 |  714 |
| TE         | 2024-2025 | snow_cm_h_avg |  1.07600 |   0.37383 |  714 |
| TE         | 2024-2025 | cold_10f      | -0.06037 |   0.05438 |  714 |
| TE         | 2024-2025 | heat_10f      | -0.06355 |   0.81527 |  714 |
| WR         | 2016-2021 | wind_over_10  | -0.01190 |   0.08558 | 2156 |
| WR         | 2016-2021 | gust_over_20  | -0.00158 |   0.61728 | 2156 |
| WR         | 2016-2021 | rain_any      |  0.01616 |   0.59554 | 2156 |
| WR         | 2016-2021 | rain_mm_h_avg | -0.07142 |   0.00152 | 2156 |
| WR         | 2016-2021 | snow_any      | -0.12472 |   0.07902 | 2156 |
| WR         | 2016-2021 | snow_cm_h_avg |  0.10112 |   0.70868 | 2156 |
| WR         | 2016-2021 | cold_10f      | -0.02400 |   0.04982 | 2156 |
| WR         | 2016-2021 | heat_10f      |  0.22278 |   0.26616 | 2156 |
| WR         | 2022-2023 | wind_over_10  | -0.00215 |   0.87227 |  756 |
| WR         | 2022-2023 | gust_over_20  | -0.00830 |   0.24768 |  756 |
| WR         | 2022-2023 | rain_any      |  0.02876 |   0.58760 |  756 |
| WR         | 2022-2023 | rain_mm_h_avg | -0.03095 |   0.35270 |  756 |
| WR         | 2022-2023 | snow_any      | -0.02730 |   0.83599 |  756 |
| WR         | 2022-2023 | snow_cm_h_avg | -0.20706 |   0.01200 |  756 |
| WR         | 2022-2023 | cold_10f      | -0.03189 |   0.12886 |  756 |
| WR         | 2022-2023 | heat_10f      |  0.10102 |   0.29094 |  756 |
| WR         | 2024-2025 | wind_over_10  |  0.00294 |   0.80829 |  716 |
| WR         | 2024-2025 | gust_over_20  | -0.00376 |   0.51183 |  716 |
| WR         | 2024-2025 | rain_any      | -0.00362 |   0.94756 |  716 |
| WR         | 2024-2025 | rain_mm_h_avg | -0.05852 |   0.08312 |  716 |
| WR         | 2024-2025 | snow_any      | -0.05167 |   0.67565 |  716 |
| WR         | 2024-2025 | snow_cm_h_avg | -0.19808 |   0.63882 |  716 |
| WR         | 2024-2025 | cold_10f      | -0.03420 |   0.03727 |  716 |
| WR         | 2024-2025 | heat_10f      | -0.08595 |   0.23942 |  716 |