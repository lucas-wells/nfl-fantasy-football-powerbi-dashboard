# NFL Running Back Usage and Fantasy Production Dashboard

An interactive Power BI dashboard analyzing NFL running back fantasy production, workload, receiving involvement, rushing efficiency, goal-line usage, offensive line environment, and historical fantasy success profiles across the 2023-2025 NFL seasons.

This project was built as a portfolio dashboard to demonstrate data cleaning, Power Query transformations, DAX development, data modeling, predictive analysis, and interactive dashboard design using NFL fantasy football data.

## Project Overview

The dashboard evaluates how running backs earn fantasy production rather than only displaying final fantasy-point totals.

The analysis incorporates:

- Rushing volume
- Receiving involvement
- Goal-line usage
- Touchdown production
- Explosive rushing production
- Yards before contact
- Yards after contact
- Offensive line environment
- Running back role
- Position-based percentile rankings
- Historical RB1 and RB2 hit rates

The project combines league-wide running back analysis with customizable predictive filters and individual player-season profiles.

## Dashboard Preview

This folder includes:

- A PDF preview of the complete dashboard
- The full Power BI `.pbix` report

Repository files:

```text
Fantasy Football Running Back Deep Dive Preview.pdf
Fantasy Football Running Back Deep Dive.pbix
README.md
```

The PDF can be viewed without Power BI Desktop. The PBIX file provides access to the interactive filters, slicers, tooltips, calculations, and player profiles.

## Dashboard Sections

The report is organized around three primary areas:

1. **Running Back Performance Analysis**
2. **Running Back Predictive Analysis**
3. **Running Back Deep Dive**

Each section answers a different analytical question, moving from league-wide production trends to historical success thresholds and individual player evaluation.

## Running Back Performance Analysis

The league-wide performance section summarizes the eligible running back player pool.

Key areas include:

- Total qualified RB seasons
- Average PPR fantasy points per game
- Average rushing and receiving production
- Running back role distribution
- Fantasy production by role
- Rushing efficiency
- Receiving involvement
- Offensive line environment
- Player-season filters

This section helps explain how fantasy production differs by workload, receiving usage, rushing role, and team environment.

## Running Back Predictive Analysis

The predictive section allows users to test historical running back profiles using customizable workload, scoring, and efficiency thresholds.

Profile filters include:

- Rushing attempts per game
- Targets per game
- Goal-line attempts per game
- Total touchdowns per game
- Explosive rushing yards per game
- Yards before contact per attempt
- Yards after contact per attempt
- Run-blocking environment
- Season

The page dynamically evaluates:

- RB1 hit rate
- RB2+ hit rate
- Number of qualifying RB seasons
- Strongest individual thresholds
- Filtered player-profile results
- Run-blocking tier impact
- Dynamic analytical takeaways

Fantasy finishes are based on PPR fantasy points per game:

- **RB1:** Top 12
- **RB2+:** Top 24

This section is designed to test whether specific combinations of volume, receiving involvement, scoring opportunity, rushing efficiency, and blocking environment historically translated into fantasy success.

## Key Predictive Thresholds

The dashboard evaluates several important running back thresholds:

- 13 or more rushing attempts per game
- 3 or more targets per game
- 0.75 or more goal-line attempts per game
- 0.5 or more total touchdowns per game
- 20 or more explosive rushing yards per game
- 2.0 or more yards before contact per attempt
- 2.75 or more yards after contact per attempt

These thresholds were selected to represent major components of running back fantasy production:

- Workload
- Receiving value
- Scoring opportunity
- Explosive-play production
- Blocking environment
- Individual tackle-breaking efficiency

Threshold results describe historical relationships within the eligible dataset and do not guarantee future performance.

## Run-Blocking Environment

Each running back season is assigned a run-blocking environment tier:

- Elite
- Good
- Average
- Poor
- Awful

The tiers provide context for how much support a running back received before contact.

The dashboard compares RB2+ hit rates across these environments and evaluates how blocking quality interacts with workload, receiving usage, and fantasy production.

Run-blocking tiers are custom analytical classifications created for this project. They are not official offensive line rankings from the NFL, a team, or a data provider.

## Running Back Role Classification

Each player-season is assigned a custom running back role based on workload, receiving usage, scoring involvement, and backfield deployment.

Roles include:

- Workhorse
- Early Down
- Receiving
- Goal Line
- Change of Pace
- Committee 1A
- Committee 1B
- Handcuff

These roles are intended to summarize how a player was used within their backfield.

They are custom classifications created for this dashboard and should not be interpreted as official NFL, team, or data-provider designations.

## Running Back Deep Dive

The player deep-dive section provides an individual running back season profile.

Key features include:

- Dynamic player headshot
- Dynamic team logo
- Player name, team, season, and running back role
- PPR fantasy points per game
- Rushing volume
- Receiving involvement
- Rushing efficiency
- Season production statistics
- Player versus position comparison
- Position percentile rankings
- Rushing efficiency profile
- Receiving usage profile
- Dynamic player notes
- Dynamic analytical takeaways

The deep-dive page is designed to show what a running back produced, how that production was earned, and how the player compared with other qualified running backs.

## Player Eligibility

A running back season was included if the player recorded at least one of the following:

- 50 or more rushing attempts
- 100 or more routes run

This qualification rule captures both traditional rushing contributors and receiving-oriented running backs while reducing small-sample noise.

## Fantasy Production

The dashboard uses PPR fantasy scoring logic:

- 1 point per reception
- 0.1 points per rushing yard
- 0.1 points per receiving yard
- 6 points per rushing touchdown
- 6 points per receiving touchdown

Fantasy finishes are ranked using PPR fantasy points per game rather than total season points.

Using points per game reduces the effect of missed games and focuses the analysis on production while active.

## Receiving Involvement

Receiving usage is evaluated using metrics such as:

- Targets
- Targets per game
- Receptions
- Receiving yards
- Routes run
- Receiving touchdowns
- Target share
- Receiving efficiency

Running back receiving statistics were reviewed and supplemented where necessary to improve completeness across the qualified player pool.

Receiving opportunity is especially important in PPR formats because catches provide direct fantasy value in addition to receiving yardage and touchdown production.

## Rushing Efficiency

The dashboard evaluates both team-created and player-created rushing efficiency.

Important metrics include:

- Yards per carry
- Yards before contact per attempt
- Yards after contact per attempt
- Explosive rushing yards
- Goal-line attempts
- Rushing touchdowns
- Avoided tackles
- Rushing success rate

Yards before contact provides context for blocking quality and available running lanes.

Yards after contact provides context for the running back's ability to create additional yardage after defensive contact.

Neither metric should be evaluated in isolation because rushing efficiency is influenced by offensive line play, defensive fronts, play design, game situation, and player ability.

## Dynamic Takeaways

The dashboard includes DAX-generated takeaway cards that respond to user selections.

These takeaways identify:

- The strongest historical RB1 signal
- The strongest historical RB2+ signal
- The effect of the selected run-blocking environment
- The results of the currently filtered player profile

The notes are automatically generated analytical summaries.

They are not official scouting reports, player projections, guarantees, or statements from the NFL, a team, a player, or a data provider.

## Data Preparation

The data was cleaned, combined, supplemented, and modeled before visualization.

Major preparation steps included:

- Combined multiple NFL seasons
- Standardized player, team, position, and metric fields
- Filtered running backs using rushing-attempt and route thresholds
- Added qualifying running backs omitted from route-based exports
- Supplemented selected missing receiving statistics
- Recalculated fantasy scoring fields
- Created running back role classifications
- Created run-blocking environment tiers
- Created rushing and receiving efficiency measures
- Created RB1 and RB2 finish rankings
- Created customizable predictive hit-rate calculations
- Created position percentile measures
- Added player metadata
- Added dynamic player headshots
- Added dynamic team logos
- Created dynamic player notes and takeaway measures

Original downloaded source CSV files are not distributed through this repository.

## Tools Used

- Microsoft Power BI
- Power Query
- DAX
- Data cleaning
- Data modeling
- Conditional formatting
- Dynamic image URLs
- Interactive filters and slicers
- Sports analytics
- GitHub for project hosting

## Skills Demonstrated

- Multi-season dataset integration
- Power Query transformations
- DAX measure development
- Calculated columns
- Dynamic text measures
- Percentile calculations
- Predictive threshold analysis
- Interactive dashboard development
- Data validation
- Data visualization
- Analytical storytelling
- Sports and fantasy football analysis

## Data Source Notice

This project was developed using NFL statistics accessed through a paid FTN Fantasy subscription.

The original downloaded source exports are not included in this repository.

This source identification does not imply that FTN Fantasy authorized, sponsored, approved, licensed, or endorsed this project or its public presentation.

No ownership of FTN Fantasy data, metrics, content, trademarks, or intellectual property is claimed.

The dashboard design, Power Query transformations, DAX calculations, visualizations, custom classifications, written analysis, and project organization were created by Lucas Wells.

Transforming, renaming, combining, supplementing, or visualizing source statistics does not transfer ownership of the original source material or override the rights and terms of the original provider.

## Independent Project Disclaimer

This is an independent, noncommercial portfolio project created for educational, analytical, and demonstration purposes.

This project is not affiliated with, sponsored by, approved by, licensed by, or endorsed by:

- FTN Fantasy
- FTN Network
- The National Football League
- Any NFL team
- Any NFL player
- The NFL Players Association
- Microsoft
- Any other data provider or rights holder

References to teams, players, organizations, products, or services are used only for identification, commentary, analysis, and portfolio demonstration.

## Trademarks, Logos, and Player Images

NFL team names, team logos, league marks, uniforms, player names, player photographs, and related intellectual property belong to their respective owners.

Their appearance in this project is for identification, analytical commentary, and portfolio demonstration.

Their inclusion does not imply sponsorship, affiliation, approval, or endorsement.

Player headshots and team logos may be displayed through externally hosted image URLs. This repository does not claim ownership of those images.

Image availability may change if an external provider modifies or removes a URL.

## Accuracy and Methodology Disclaimer

Reasonable efforts were made to clean, validate, supplement, and present the information accurately.

However, no guarantee is made regarding the accuracy, completeness, availability, or continued reliability of any statistic, calculation, classification, image, or external source.

Values may differ from official league records or other analytical platforms because of:

- Source corrections
- Differences in charting methodology
- Changes in provider definitions between seasons
- Missing or unavailable information
- Supplemental data patches
- Rounding
- Qualification requirements
- Player-name matching
- Team changes
- Position classifications
- Custom calculations
- Power Query transformations
- DAX calculation logic

Run-blocking tiers, running back roles, threshold classifications, percentiles, and player notes reflect the methodology created for this project.

Other analysts may reasonably use different definitions, thresholds, or evaluation methods.

Users should independently verify any information before relying on it for an important decision.

## Fantasy and Betting Disclaimer

This dashboard is provided for informational, educational, analytical, and entertainment purposes only.

It is not intended to provide:

- Sports-betting advice
- Gambling advice
- Financial advice
- Legal advice
- Professional scouting advice
- Guaranteed fantasy football outcomes

Historical relationships, player profiles, percentile rankings, and hit rates do not guarantee future performance.

The creator is not responsible for fantasy football decisions, wagers, financial losses, roster decisions, draft decisions, or other actions taken based on this dashboard.

## Limitations

Historical hit rates describe relationships within the qualified dataset and should not be interpreted as proof that one individual metric directly causes fantasy success.

Running back production is influenced by several interacting factors, including:

- Offensive line performance
- Offensive play calling
- Receiving involvement
- Goal-line opportunity
- Game script
- Team scoring environment
- Player health
- Backfield competition
- Defensive matchup
- Individual ability

Some data-provider definitions or charting practices may differ by season.

A change in a metric across seasons may reflect a methodology change rather than a true change in player performance.

Player headshots and team logos are pulled through image URL fields and depend on external image availability.

The Power BI file may require Microsoft Power BI Desktop and internet access for certain external images or refresh operations.

## Rights and Reuse

Unless otherwise stated, the original dashboard design, written analysis, Power Query transformations, DAX measures, and custom classifications in this repository are © 2026 Lucas Wells. All rights reserved.

No permission is granted to reproduce, redistribute, sell, sublicense, or commercially exploit this project or its original components without prior written permission.

Third-party statistics, player images, team logos, trademarks, names, and other externally owned materials remain the property of their respective owners and are not licensed by this repository.

## Author

Created by **Lucas Wells** as a Power BI and sports analytics portfolio project.
