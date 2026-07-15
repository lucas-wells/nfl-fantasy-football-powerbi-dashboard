# NFL Wide Receiver Performance and Predictive Analytics Dashboard

An interactive Power BI dashboard analyzing NFL wide receiver performance, usage, efficiency, alignment, quarterback accuracy, and historical fantasy success profiles across the 2022-2025 NFL seasons.

This project was built as a portfolio dashboard to demonstrate data cleaning, Power Query transformations, DAX development, data modeling, predictive analysis, and interactive dashboard design using NFL fantasy football data.

## Project Overview

The dashboard evaluates how wide receivers earn fantasy production rather than only displaying final fantasy-point totals.

The analysis incorporates:

- Target volume
- Target share
- First-read usage
- Route efficiency
- Explosive receiving production
- Touchdown scoring
- Alignment tendencies
- Coverage performance
- Quarterback accuracy
- Position-based percentile rankings

The final dataset includes **578 qualified wide receiver seasons** from 2022 through 2025.

Wide receivers were included if they recorded at least **100 routes run** during the selected season.

## Dashboard Pages

The report contains four interactive pages:

1. **WR Performance Analysis**
2. **WR Predictive Analysis**
3. **Efficiency vs. Production**
4. **WR Deep Dive**

Each page answers a different analytical question, moving from league-wide trends to customizable predictive profiles and individual player-season evaluation.

## Dashboard Preview

This folder includes:

- A PDF preview of the complete dashboard
- The full Power BI `.pbix` report

The PDF can be viewed without Power BI Desktop. The PBIX file provides access to the interactive filters, slicers, tooltips, measures, and player profiles.

## Page 1: WR Performance Analysis

The first page provides a league-wide overview of wide receiver fantasy production and usage.

Key visuals include:

- Total qualified WR seasons
- Total routes analyzed
- Average PPR fantasy points per game
- Average yards per route run
- Average first-read target share
- Top WR seasons by PPR PPG
- WR2+ hit rate by WR archetype
- Average PPR PPG by archetype
- WR-season distribution by archetype

Available filters include:

- Team
- WR age
- WR archetype
- Production tier
- Season

This page helps explain how fantasy production differs across wide receiver roles, age ranges, teams, and usage archetypes.

## Page 2: WR Predictive Analysis

The second page allows users to build custom historical wide receiver profiles and evaluate how often those profiles produced WR1, WR2, or WR3 fantasy finishes.

Profile filters include:

- Targets per game
- First-read targets per game
- Active-game target share
- 17-game touchdown pace
- Explosive receiving yards per game
- Season

The page dynamically calculates:

- WR1 hit rate
- WR2+ hit rate
- WR3+ hit rate
- Number of qualifying WR seasons
- Best-performing usage thresholds
- Dynamic analytical takeaways
- WR2+ hit rate by quarterback accuracy tier

Fantasy finishes are based on PPR fantasy points per game:

- **WR1:** Top 12
- **WR2+:** Top 24
- **WR3+:** Top 36

This page is designed to test whether specific combinations of volume, target earning, explosive production, touchdown scoring, and quarterback environment historically translated into fantasy success.

## Page 3: Efficiency vs. Production

The third page examines the relationship between receiving efficiency and fantasy production.

Key visuals include:

- PPR fantasy points per game versus receiving EPA per target
- Relative production and efficiency quadrants
- Dynamic group summary
- Dynamic player-season takeaways
- Yards per route run by coverage type

The quadrant analysis separates WR seasons into four groups:

- Higher production, higher efficiency
- Higher production, lower efficiency
- Lower production, higher efficiency
- Lower production, lower efficiency

Available filters include:

- Team
- Age
- WR archetype
- Production tier
- Season

This page helps distinguish efficient players from volume-dependent producers and highlights receivers whose underlying efficiency may have exceeded their fantasy output.

## Page 4: WR Deep Dive

The fourth page provides an individual player-season profile.

Key features include:

- Dynamic player headshot
- Dynamic team logo
- Player name, team, season, and WR archetype
- PPR PPG
- Active-game target share
- Active-game first-read target share
- Yards per route run
- Season production statistics
- Target conversion profile
- Player versus WR-average comparison
- Position percentile rankings
- Alignment usage
- Dynamic player notes
- Dynamic production outlook

The comparison table evaluates each selected player across:

- PPR PPG
- Yards per route run
- Target share
- First-read target share
- Air yards per game
- Average depth of target
- Yards after catch per reception
- End-zone target pace

The Player Deep Dive page is designed to show what a receiver produced, how that production was earned, and how the player compared with qualified wide receivers from the same analytical pool.

## WR Archetype Classification

Each WR season is assigned a custom archetype based on alignment and usage.

Archetypes include:

- Boundary X
- Field Stretcher
- Mixed Alignment
- Perimeter
- Screen / Motion
- Slot

These are custom analytical classifications created for this project. They are not official NFL, team, or data-provider designations.

The classifications are intended to summarize how receivers were deployed within their offenses and provide additional context for fantasy production.

## Quarterback Accuracy Tiers

The dashboard includes a custom quarterback accuracy model used to evaluate the quality of each receiver's passing environment.

Quarterback environments are grouped into:

- Elite
- Good
- Average
- Poor
- Awful

These tiers are used to compare historical WR2+ hit rates across different quarterback environments.

The model is a custom analytical framework created for this dashboard and should not be interpreted as an official quarterback grade or ranking.

## Active-Game Usage Metrics

Target Share and First Read Target Share are adjusted for games played.

A player who missed games may have a lower raw season-long share because team totals include games in which the player did not appear. The active-game adjustment estimates the receiver's usage while active.

These measures improve player-level context but remain estimates. They do not reconstruct the exact number of team pass attempts, routes, targets, or first-read opportunities from only the games in which the player appeared.

## Player Eligibility

A WR season was included if the player recorded:

- At least 100 routes run
- A listed position of wide receiver

The qualification threshold reduces small-sample noise and keeps comparisons focused on players with meaningful seasonal involvement.

## Data Preparation

The dataset was cleaned, combined, and modeled before visualization.

Major preparation steps included:

- Combined multiple NFL seasons
- Standardized player, team, position, and metric fields
- Added and validated the 2022 season
- Verified route totals and yards per route run calculations
- Standardized season identifiers
- Corrected selected player-name and age-matching issues
- Added player metadata
- Added dynamic player headshots
- Added dynamic team logos
- Created WR archetype classifications
- Created fantasy production tiers
- Created active-game usage measures
- Created WR1, WR2, and WR3 finish rankings
- Created position percentile measures
- Created quarterback accuracy tiers
- Created dynamic player notes and production outlooks
- Built customizable predictive hit-rate calculations

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
- Data visualization
- Analytical storytelling
- Sports and fantasy football analysis

## Data Source Notice

This project was developed using NFL statistics accessed through a paid FTN Fantasy subscription.

The original downloaded source exports are not included in this repository.

This source identification does not imply that FTN Fantasy authorized, sponsored, approved, licensed, or endorsed this project or its public presentation.

No ownership of FTN Fantasy data, metrics, content, trademarks, or intellectual property is claimed.

The dashboard design, Power Query transformations, DAX calculations, visualizations, custom classifications, written analysis, and project organization were created by Lucas Wells.

Transforming, renaming, combining, or visualizing source statistics does not transfer ownership of the original source material or override the rights and terms of the original provider.

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

NFL team names, logos, league marks, uniforms, player names, player photographs, and related intellectual property belong to their respective owners.

Their appearance in this project is for identification, analytical commentary, and portfolio demonstration.

Their inclusion does not imply sponsorship, affiliation, approval, or endorsement.

Player headshots and team logos may be displayed through externally hosted image URLs. This repository does not claim ownership of those images.

## Accuracy and Methodology Disclaimer

Reasonable efforts were made to clean, validate, and present the information accurately. However, no guarantee is made regarding the accuracy, completeness, availability, or continued reliability of any statistic, calculation, classification, image, or external source.

Values may differ from official league records or other analytical platforms because of:

- Source corrections
- Differences in charting methodology
- Changes in provider definitions between seasons
- Missing or unavailable information
- Rounding
- Qualification requirements
- Player-name matching
- Team changes
- Position classifications
- Custom calculations
- Active-game estimates
- Power Query transformations
- DAX calculation logic

For example, certain metrics such as adjusted catch percentage may not be directly comparable across every season because charting definitions or catchable-target classifications may have changed.

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

## Rights and Reuse

Unless otherwise stated, the original dashboard design, written analysis, Power Query transformations, DAX measures, and custom classifications in this repository are © 2026 Lucas Wells. All rights reserved.

No permission is granted to reproduce, redistribute, sell, sublicense, or commercially exploit this project or its original components without prior written permission.

Third-party statistics, player images, team logos, trademarks, names, and other externally owned materials remain the property of their respective owners and are not licensed by this repository.

## Author

Created by **Lucas Wells** as a Power BI and sports analytics portfolio project.
