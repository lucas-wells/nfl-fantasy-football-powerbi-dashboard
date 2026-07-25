# NFL Tight End Usage and Fantasy Production Dashboard

An interactive Power BI dashboard analyzing NFL tight end fantasy production, receiving usage, efficiency, alignment, quarterback accuracy, deployment archetypes, and historical fantasy success profiles across the 2022-2025 NFL seasons.

This portfolio project demonstrates Power Query transformations, DAX development, data modeling, custom classifications, predictive analysis, and interactive dashboard design using NFL fantasy football data.

## Project Overview

The dashboard examines how tight ends earn fantasy production rather than only displaying final fantasy-point totals.

The analysis includes:

* Target and first-read involvement
* Route participation
* Receiving efficiency
* Alignment tendencies
* Tight end deployment archetypes
* Quarterback accuracy
* Historical Top-12 and Top-6 hit rates
* Position-based percentile comparisons
* Individual player-season profiles

## Repository Files

* `Fantasy Football Tight End Deep Dive Preview.pdf`
* `Fantasy Football Tight End Deep Dive.pbix`
* `README.md`

The PDF provides a static preview of the dashboard. The PBIX file contains the complete interactive report, including filters, slicers, tooltips, DAX measures, and player profiles.

## Dashboard Pages

The report contains four interactive pages:

1. Performance Overview
2. Efficiency vs. Production
3. TE Predictive Analysis
4. Player Deep Dive

## Performance Overview

The Performance Overview page summarizes the qualified tight end player pool.

Key visuals and metrics include:

* Qualified tight end seasons
* Total routes analyzed
* Average PPR fantasy points per game
* Average yards per route run
* Average first-read target share
* Top tight end seasons by PPR PPG
* Average PPR PPG by archetype
* Player distribution by archetype
* Top-12 hit rate by tight end archetype

Available filters include:

* Team
* Age
* Tight end archetype
* Fantasy production tier
* Season

This page provides a league-wide view of how fantasy production differs across tight end roles, age groups, teams, and deployment styles.

## Efficiency vs. Production

The Efficiency vs. Production page evaluates the relationship between receiving efficiency and fantasy scoring.

Key features include:

* Receiving EPA per target versus PPR fantasy points per game
* Production and efficiency quadrants
* Dynamic group summaries
* Identification of volume-driven producers
* Identification of efficient but underused players
* Yards per route run by coverage type

The quadrant analysis separates tight end seasons into four groups:

* Higher production and higher efficiency
* Higher production and lower efficiency
* Lower production and higher efficiency
* Lower production and lower efficiency

This page helps distinguish efficient receiving performance from production driven primarily by volume or scoring opportunities.

## TE Predictive Analysis

The predictive page allows users to build custom historical tight end profiles and evaluate how frequently those profiles produced strong fantasy finishes.

Profile filters include:

* Targets per game
* First-read targets per game
* Route participation
* 17-game touchdown pace
* Yards per route run
* Season

The page dynamically evaluates:

* Top-12 hit rate
* Top-6 hit rate
* Number of qualifying tight end seasons
* Hit rates for individual usage thresholds
* Results for the selected combination of filters
* Top-12 hit rate by quarterback accuracy tier
* Dynamic analytical takeaways

Fantasy finishes are ranked using PPR fantasy points per game:

* **Top-12:** TE1 finish
* **Top-6:** High-end TE1 finish

The purpose of this page is to test whether specific combinations of volume, first-read involvement, route participation, scoring opportunity, and efficiency historically translated into fantasy success.

Historical hit rates describe relationships within the qualified dataset and do not guarantee future results.

## Quarterback Accuracy Tiers

Each qualifying tight end season is assigned a quarterback accuracy environment:

* Elite
* Good
* Average
* Poor
* Awful

The quarterback accuracy framework uses passing-environment metrics to provide context for the quality of each tight end's target opportunities.

The predictive page compares Top-12 hit rates across these quarterback environments.

These tiers are custom analytical classifications created for this dashboard. They are not official quarterback rankings or grades from the NFL, an NFL team, or a data provider.

## Tight End Archetypes

Each player-season is assigned a custom archetype based on alignment, route participation, and offensive deployment.

Archetypes include:

* Versatile
* Slot
* Split-Out
* Traditional
* Blocking
* Low Usage

These categories summarize how each tight end was used within the offense.

They are custom analytical classifications and should not be interpreted as official NFL, team, or data-provider designations.

## Player Deep Dive

The Player Deep Dive page provides an individual tight end season profile.

Key features include:

* Dynamic player headshot
* Dynamic team logo
* Player name, team, season, and archetype
* PPR fantasy points per game
* Active-game target share
* Active-game first-read target share
* Yards per route run
* Season production statistics
* Player alignment mix
* Target conversion profile
* Player versus receiving-tight-end averages
* Position percentile rankings
* Dynamic player notes
* Dynamic production outlook

Available filters include:

* Player
* Team
* Season
* Tight end archetype
* Quarterback accuracy tier

This page is designed to show what a tight end produced, how that production was earned, how the player was deployed, and how the player compared with other qualified receiving tight ends.

## Active-Game Usage Metrics

Target share and first-read target share are adjusted to better represent a player's usage while active.

A player who misses games may have a lower raw season-long share because team totals include games in which the player did not appear.

The active-game measures provide improved player-level context, but they remain estimates and do not reconstruct every team passing opportunity from only the games in which the player played.

## Player Eligibility

A tight end season was included if the player recorded at least 100 routes during the selected season.

This threshold reduces small-sample noise and focuses the primary analysis on players with meaningful receiving involvement.

## Data Preparation

The data was cleaned, combined, and modeled before visualization.

Major preparation steps included:

* Combined multiple NFL seasons
* Standardized player, team, position, season, and metric fields
* Filtered the dataset using the route qualification threshold
* Corrected selected games-played and historical data issues
* Created tight end archetype classifications
* Created quarterback accuracy tiers
* Created active-game usage measures
* Created Top-12 and Top-6 finish rankings
* Created customizable predictive hit-rate calculations
* Created position percentile measures
* Added player metadata
* Added dynamic player headshots and team logos
* Created dynamic notes and analytical takeaway measures

Original downloaded source CSV files are not distributed through this repository.

## Tools and Skills Demonstrated

* Microsoft Power BI
* Power Query
* DAX
* Data cleaning and transformation
* Data modeling
* Calculated columns and measures
* Dynamic text measures
* Percentile calculations
* Predictive threshold analysis
* Custom player classifications
* Interactive filters and slicers
* Data visualization
* Analytical storytelling
* Sports and fantasy football analysis

## Data Source Notice

This project was developed using NFL statistics accessed through a paid FTN Fantasy subscription.

The original source exports are not included in this repository.

This source identification does not imply that FTN Fantasy authorized, sponsored, approved, licensed, or endorsed this project.

The dashboard design, Power Query transformations, DAX calculations, visualizations, custom classifications, written analysis, and project organization were created by Lucas Wells.

## Disclaimer

This is an independent, noncommercial portfolio project created for educational, analytical, and demonstration purposes.

It is not affiliated with or endorsed by FTN Fantasy, the National Football League, any NFL team, any NFL player, the NFL Players Association, Microsoft, or another data provider.

NFL team names, logos, player names, photographs, and related intellectual property belong to their respective owners. Their appearance is for identification and analytical commentary only.

Reasonable efforts were made to clean and validate the data, but no guarantee is made regarding the accuracy or completeness of every statistic, calculation, classification, or external image.

Historical fantasy relationships and hit rates do not guarantee future performance and should not be interpreted as betting, gambling, financial, legal, or professional scouting advice.

## Rights and Reuse

Unless otherwise stated, the original dashboard design, written analysis, Power Query transformations, DAX measures, and custom classifications are © 2026 Lucas Wells. All rights reserved.

Third-party statistics, trademarks, logos, player images, and other externally owned materials remain the property of their respective owners.

## Author

Created by **Lucas Wells** as a Power BI and sports analytics portfolio project.
