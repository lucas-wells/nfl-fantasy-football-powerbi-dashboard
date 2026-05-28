# NFL Fantasy Football Analytics Dashboard

An interactive Power BI dashboard analyzing NFL fantasy football production, player usage, receiving efficiency, alignment tendencies, and position-based player profiles across the 2023-25 NFL seasons.

This project was built as a portfolio dashboard to demonstrate data cleaning, Power Query transformations, DAX measures, visual storytelling, and interactive business intelligence design using NFL fantasy football data.

## Project Overview

The dashboard analyzes NFL skill-position players with a focus on fantasy football performance and the underlying metrics that help explain production. Instead of only showing fantasy points, the dashboard evaluates how players earn their production through route efficiency, target share, first-read usage, alignment role, target conversion, and position-based percentile comparisons.

The report is organized into three pages:

1. **Skill-Position Analysis**
2. **Efficiency vs. Production**
3. **Player Deep Dive**

Each page answers a different analytical question, moving from broad skill-position trends to player-level scouting and comparison.

## Dashboard Preview

A PDF preview of the dashboard is included in this repository:

**`Fantasy Football Analytics Dashboard.pdf`**

The full Power BI file is also included:

**`Fantasy Football Analytics Dashboard.pbix`**

## Page 1 — Skill-Position Analysis

The first page provides a high-level overview of the player pool.

Key visuals include:

* Total players analyzed
* Average PPR fantasy points per game
* Average yards per route run
* Average first-read target share
* Players by position
* Average PPR PPG by position
* Top 8 players by PPR PPG
* Average PPR PPG by alignment role

This page is designed to summarize the dataset and show how production differs by position and offensive usage type.

## Page 2 — Efficiency vs. Production

The second page focuses on the relationship between fantasy production and receiving efficiency.

Key visuals include:

* Efficiency vs. production scatter plot
* Player quadrant analysis
* Dynamic takeaway cards
* Top players by yards per route run
* Position, team, alignment role, production tier, and season filters

This page helps identify players who are efficient volume producers, volume-based producers, efficient but underproducing players, or lower-impact fantasy options.

## Page 3 — Player Deep Dive

The third page is a player-level profile view built for individual scouting and comparison.

Key features include:

* Dynamic player headshot
* Dynamic team logo
* Player name, position, team, and season profile card
* KPI cards for:

  * PPR PPG
  * Target Share
  * First Read Target Share
  * Yards Per Route Run
* Season stats table
* Player vs. position comparison table
* Position percentile rankings
* Player alignment mix chart
* Target conversion profile
* Dynamic player notes

The Player Deep Dive page is designed to show not only what a player produced, but how they produced it and how their profile compares to positional peers.

## Key Metrics and Features

### Fantasy Production

The dashboard uses PPR fantasy scoring logic:

* 1 point per reception
* 0.1 points per rushing yard
* 0.1 points per receiving yard
* Recalculated fantasy points per game

### Player Eligibility Rules

The player pool was filtered to reduce small-sample noise.

Players were included if they met one of the following conditions:

* 100+ routes run
* Running backs with 50+ rushing attempts

The dashboard focuses on WR, RB, and TE players.

### Alignment Role Classification

Players are categorized into custom alignment roles based on where they line up most often:

* Wide-Dominant
* Slot-Dominant
* Backfield-Dominant
* Inline TE
* Off-Line / Move TE
* Mixed Alignment
* Unicorn

These roles help describe how players are deployed within their offense beyond their listed position.

### Active-Game Target Share

For the Player Deep Dive page, Target Share and First Read Target Share are adjusted for games played.

This helps better represent a player's usage when active. A player who missed games may have a lower raw season-long target share because the team total includes games they did not play. The active-game version estimates the player's role based on the games they actually played.

The adjustment keeps full-season players unchanged while scaling missed-game players based on team games and player games.

### Position Percentile Comparison

The Player vs. Position Comparison table compares the selected player against others at the same position across key metrics:

* PPR PPG
* Yards Per Route Run
* Target Share
* First Read Target Share
* Air Yards Per Game
* ADOT
* YAC Per Reception
* End Zone Targets

Percentiles are conditionally formatted to quickly identify player strengths and weaknesses.

### Dynamic Player Notes

The Player Deep Dive page includes DAX-driven player notes:

* **Fantasy Stability**
  Evaluates how stable a player's fantasy output looks based on target earning, first-read usage, and route efficiency.

* **Path to Level Up**
  Identifies the player's lowest relevant percentile metric and describes where improvement could raise their fantasy profile.

ADOT is included in the comparison table as a role/context metric, but excluded from the Path to Level Up note because higher or lower ADOT is not inherently better for fantasy production.

### Target Conversion Profile

The Player Deep Dive page includes a target conversion chart comparing the selected player to their position average in:

* Adjusted Catch Percent
* First Down Rate
* Touchdown Rate

This shows how effectively a player converts targets into meaningful receiving outcomes.

## Data Files Used

The dashboard uses the following CSV files:

```text
NFL Stats 2023-24 Fixed Games.csv
NFL Stats 2024-25.csv
NFL Stats 2025-26.csv
NFL Stats 2025-26 50+ Carry Additions.csv
PlayerHeadshotLookup_filtered.csv
```

The file below is included in the folder but was not used in the final model:

```text
NFL Stats 2023-24.csv
```

The final dashboard uses **`NFL Stats 2023-24 Fixed Games.csv`** instead of the original 2023-24 file.

## Repository Files

Main files included in this repository:

```text
Fantasy Football Analytics Dashboard.pbix
Fantasy Football Analytics Dashboard.pdf
NFL Stats 2023-24 Fixed Games.csv
NFL Stats 2024-25.csv
NFL Stats 2025-26.csv
NFL Stats 2025-26 50+ Carry Additions.csv
PlayerHeadshotLookup_filtered.csv
README.md
```

Optional/non-final file:

```text
NFL Stats 2023-24.csv
```

## Data Preparation

The data was cleaned and modeled before visualization. Major preparation steps included:

* Imported and combined multiple season CSV files
* Used the fixed 2023-24 data file for corrected games played values
* Standardized player, team, position, and metric fields
* Recalculated fantasy scoring fields
* Filtered out small-sample players
* Added qualifying running backs with 50+ rushing attempts
* Created custom alignment role classifications
* Built dynamic team logo URLs using team abbreviations
* Added a filtered player headshot lookup table
* Removed unnecessary lookup columns to reduce model size and improve performance
* Created DAX measures for active-game usage, position averages, percentiles, and dynamic notes

## Tools Used

* Power BI
* Power Query
* DAX
* CSV data cleaning
* Data modeling
* Conditional formatting
* Dynamic image URLs
* GitHub for project hosting

## Visual Design

The dashboard uses a dark sports-analytics theme with blue accents.

Design choices include:

* Dark navy page background
* Rounded visual containers
* Subtle borders
* Custom KPI icons
* Position-based color formatting
* Alignment role color formatting
* Dynamic player headshots
* Dynamic team logos
* Consistent typography and spacing across pages

## Project Purpose

This project was built to demonstrate the ability to:

* Clean and transform raw sports data
* Build a multi-page analytical dashboard
* Create custom DAX measures
* Design meaningful player evaluation metrics
* Build interactive filters and slicers
* Use conditional formatting for interpretation
* Present technical analysis in a polished, user-friendly format

The final dashboard combines fantasy football analysis with business intelligence design principles, making it useful as both a sports analytics project and a Power BI portfolio piece.

## Limitations

Some metrics, such as active-game target share and active-game first-read target share, are estimates based on games played rather than exact team play volume in only the games a player appeared in. This improves player-level role context but should be interpreted as an adjusted estimate rather than an official statistic.

Player headshots and team logos are pulled through image URL fields and may depend on external image availability.

## Author

Created by Lucas Wells as a Power BI portfolio project.
