# NFL Fantasy Football Analytics Dashboard

An interactive Power BI dashboard analyzing NFL fantasy football production, player usage, receiving efficiency, alignment tendencies, and position-based player profiles across the 2023-2025 NFL seasons.

This project was built as a portfolio dashboard to demonstrate data cleaning, Power Query transformations, DAX measures, visual storytelling, and interactive business intelligence design using NFL fantasy football data.

## Project Overview

The dashboard analyzes NFL skill-position players with a focus on fantasy football performance and the underlying metrics that help explain production.

Instead of only displaying fantasy points, the dashboard evaluates how players earn their production through route efficiency, target share, first-read usage, alignment role, target conversion, and position-based percentile comparisons.

The report is organized into three pages:

1. **Skill-Position Analysis**
2. **Efficiency vs. Production**
3. **Player Deep Dive**

Each page answers a different analytical question, moving from broad skill-position trends to player-level scouting and comparison.

## Dashboard Preview

A PDF preview of the dashboard is included in this repository:

**`Fantasy Football Analytics Dashboard.pdf`**

The complete Power BI report is included as:

**`Fantasy Football Analytics Dashboard.pbix`**

## Page 1 - Skill-Position Analysis

The first page provides a high-level overview of the eligible player pool.

Key visuals include:

- Total player seasons analyzed
- Average PPR fantasy points per game
- Average yards per route run
- Average first-read target share
- Player seasons by position
- Average PPR PPG by position
- Top eight player seasons by PPR PPG
- Average PPR PPG by alignment role

This page summarizes the dataset and shows how production differs by position and offensive usage type.

## Page 2 - Efficiency vs. Production

The second page focuses on the relationship between fantasy production and receiving efficiency.

Key visuals include:

- Efficiency versus production scatter plot
- Player quadrant analysis
- Dynamic takeaway cards
- Top player seasons by yards per route run
- Position, team, alignment role, production tier, and season filters

This page helps identify efficient volume producers, volume-dependent producers, efficient but underproducing players, and lower-impact fantasy options.

## Page 3 - Player Deep Dive

The third page provides an individual player-season profile for scouting and comparison.

Key features include:

- Dynamic player headshot
- Dynamic team logo
- Player name, position, team, and season profile card
- KPI cards for:
  - PPR PPG
  - Target Share
  - First Read Target Share
  - Yards Per Route Run
- Season statistics table
- Player versus position comparison table
- Position percentile rankings
- Player alignment mix chart
- Target conversion profile
- Dynamic player notes

The Player Deep Dive page is designed to show not only what a player produced, but how they produced it and how their profile compares with positional peers.

## Key Metrics and Features

### Fantasy Production

The dashboard uses PPR fantasy scoring logic:

- 1 point per reception
- 0.1 points per rushing yard
- 0.1 points per receiving yard
- 6 points per rushing or receiving touchdown
- Recalculated fantasy points per game

### Player Eligibility Rules

The player pool was filtered to reduce small-sample noise.

Players were included if they met one of the following conditions:

- 100 or more routes run
- Running backs with 50 or more rushing attempts

The dashboard focuses on wide receivers, running backs, and tight ends.

### Alignment Role Classification

Players are categorized into custom alignment roles based on where they line up most frequently:

- Wide-Dominant
- Slot-Dominant
- Backfield-Dominant
- Inline TE
- Off-Line / Move TE
- Mixed Alignment
- Unicorn

These classifications are custom analytical categories created for this project. They summarize player deployment and should not be interpreted as official NFL, team, or data-provider designations.

### Active-Game Target Share

For the Player Deep Dive page, Target Share and First Read Target Share are adjusted for games played.

A player who missed games may have a lower raw season-long target share because the team total includes games in which the player did not appear. The active-game adjustment estimates the player's role based on the games they played.

The adjustment keeps full-season players unchanged while scaling missed-game players according to team games and player games.

These measures are custom estimates. They do not reconstruct the exact number of team pass plays, routes, targets, or first-read opportunities from only the games in which the player appeared.

### Position Percentile Comparison

The Player versus Position Comparison table evaluates the selected player against others at the same position across the following metrics:

- PPR PPG
- Yards Per Route Run
- Target Share
- First Read Target Share
- Air Yards Per Game
- ADOT
- YAC Per Reception
- End Zone Targets

Percentiles are conditionally formatted to quickly identify player strengths and weaknesses.

Percentiles are calculated within the eligible player pool included in this dashboard. They may differ from values produced by other platforms because of differences in qualification requirements, source data, seasons, positions, and calculation methodology.

### Dynamic Player Notes

The Player Deep Dive page includes automatically generated DAX-based player notes.

#### Fantasy Stability

Evaluates how stable a player's fantasy production appears based on target earning, first-read usage, and route efficiency.

#### Path to Level Up

Identifies the player's lowest relevant percentile metric and describes an area in which improvement could strengthen the player's fantasy profile.

These notes are automated analytical summaries. They are not official scouting reports, projections, guarantees, or statements made by the NFL, a team, a player, or a data provider.

ADOT is included in the comparison table as a role and context metric, but it is excluded from the Path to Level Up note because a higher or lower ADOT is not inherently better for fantasy production.

### Target Conversion Profile

The Player Deep Dive page includes a target conversion chart comparing the selected player with their position average in:

- Adjusted Catch Percent
- First Down Rate
- Touchdown Rate

This chart shows how effectively a player converts targets into meaningful receiving outcomes.

Differences between seasons may reflect changes in charting methodology, data-provider definitions, sample size, or data availability. Cross-season comparisons should therefore be interpreted carefully.

## Repository Contents

The public repository contains the following project materials:

```text
Fantasy Football Analytics Dashboard.pbix
Fantasy Football Analytics Dashboard.pdf
README.md
```

The original downloaded source exports are not included in the repository.

## Data Preparation

The data was cleaned, transformed, and modeled before visualization.

Major preparation steps included:

- Imported and combined multiple NFL seasons
- Standardized player, team, position, and metric fields
- Corrected selected games-played values
- Recalculated fantasy scoring fields
- Filtered out small-sample players
- Added qualifying running backs with 50 or more rushing attempts
- Created custom alignment role classifications
- Built dynamic team logo URLs using team abbreviations
- Added player metadata and headshot lookup logic
- Removed unnecessary lookup columns to reduce model size
- Created DAX measures for active-game usage
- Created position averages and percentile calculations
- Created dynamic player notes and classifications

The source statistics were cleaned, renamed, filtered, combined, and transformed for this project. These modifications may cause values, labels, or classifications to differ from the original source.

## Tools Used

- Microsoft Power BI
- Power Query
- DAX
- Data cleaning
- Data modeling
- Conditional formatting
- Dynamic image URLs
- GitHub for project hosting

## Visual Design

The dashboard uses a dark sports-analytics theme with blue accents.

Design choices include:

- Dark navy page background
- Rounded visual containers
- Subtle borders
- Custom KPI icons
- Position-based color formatting
- Alignment-role color formatting
- Dynamic player headshots
- Dynamic team logos
- Consistent typography and spacing across pages

## Project Purpose

This project was built to demonstrate the ability to:

- Clean and transform raw sports data
- Build a multi-page analytical dashboard
- Create custom DAX measures
- Design meaningful player-evaluation metrics
- Build interactive filters and slicers
- Use conditional formatting to improve interpretation
- Present technical analysis in a polished and accessible format

The final dashboard combines fantasy football analysis with business intelligence design principles, making it useful as both a sports analytics project and a Power BI portfolio piece.

## Data Source Notice

This project was developed using NFL statistics accessed through a paid FTN Fantasy subscription.

This statement is provided solely to identify the source through which certain statistics were accessed. It does not represent or imply that FTN Fantasy authorized, sponsored, approved, licensed, or endorsed this project or its public presentation.

The original downloaded FTN Fantasy source exports are not included in this repository.

No ownership of FTN Fantasy data, metrics, content, trademarks, or intellectual property is claimed. No license or right to redistribute FTN Fantasy source materials is claimed or granted through this repository.

The dashboard contains original report design, data-modeling work, Power Query transformations, DAX calculations, visualizations, classifications, and written analysis created by Lucas Wells.

The transformation, renaming, calculation, or visualization of source statistics does not transfer ownership of the original data or override any rights or terms held by the original provider.

Anyone using this repository remains responsible for complying with any applicable provider terms, licenses, intellectual-property rights, and laws.

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

References to organizations, teams, players, products, or services are used only for identification, commentary, analysis, and portfolio demonstration.

## Trademarks, Logos, and Player Images

NFL team names, team logos, league marks, uniforms, player names, player photographs, and related intellectual property belong to their respective owners.

Their appearance in this project is for identification, analytical commentary, and portfolio demonstration. Their inclusion does not imply sponsorship, affiliation, approval, or endorsement.

Player headshots and team logos may be displayed through externally hosted image URLs. This repository does not claim ownership of those images.

Image availability may change if an external provider modifies or removes a URL.

Nothing in this repository grants users the right to separately reproduce, sell, distribute, or commercially exploit third-party logos, photographs, trademarks, statistics, or other protected material.

## Accuracy and Methodology Disclaimer

Reasonable efforts were made to clean, verify, and present the information accurately. However, no guarantee is made regarding the accuracy, completeness, availability, or continued reliability of any statistic, image, calculation, classification, or external source.

Values may differ from official league records or other analytical platforms because of:

- Source corrections
- Charting methodology
- Differences between data providers
- Missing or unavailable data
- Rounding
- Qualification requirements
- Name matching
- Team changes
- Position classifications
- Custom calculations
- Estimated active-game adjustments
- Power Query transformations
- DAX calculation logic

The creator does not warrant that the dashboard or its underlying model is free from errors.

Users should independently verify any value before relying on it for an important decision.

## Fantasy, Betting, and Financial Disclaimer

This dashboard is provided for informational, educational, analytical, and entertainment purposes only.

It is not intended to provide:

- Sports-betting advice
- Gambling advice
- Financial advice
- Investment advice
- Legal advice
- Professional scouting advice
- Guaranteed fantasy football outcomes

Historical relationships, classifications, percentile rankings, and calculated hit rates do not guarantee future performance.

The creator is not responsible for fantasy football decisions, wagers, financial losses, roster decisions, draft decisions, or other actions taken based on this dashboard.

## Limitations

Some metrics, including active-game target share and active-game first-read target share, are estimates based on games played rather than exact team play volume from only the games in which a player appeared.

This improves player-level role context but should be interpreted as an adjusted estimate rather than an official statistic.

Custom alignment roles, fantasy production tiers, percentiles, player notes, and other classifications reflect the methodology created for this project. Other analysts may reasonably use different definitions or thresholds.

Some data-provider definitions or charting practices may differ by season. A change in a metric across seasons may reflect a methodology change rather than a true change in player performance.

Player headshots and team logos are pulled through image URL fields and depend on external image availability.

The Power BI file may require Microsoft Power BI Desktop and internet access for certain external images or refresh operations.

## No Warranty and Limitation of Responsibility

This repository and its contents are provided on an "as is" and "as available" basis, without warranties of any kind.

To the fullest extent permitted by applicable law, the creator is not responsible for:

- Errors or omissions
- Inaccurate or incomplete information
- Broken external links
- Missing images
- Data-provider changes
- Power BI compatibility issues
- Decisions made using the dashboard
- Direct or indirect losses arising from use of the project

This disclaimer does not replace or override any applicable license, contract, provider terms, law, or rights held by a third party.

## Removal or Correction Requests

Good-faith requests concerning attribution, factual corrections, licensing, trademarks, logos, player images, or other protected material may be submitted through the repository's GitHub contact or issue features.

Where appropriate, disputed material may be corrected, attributed, replaced, or removed.

## Author

Created by Lucas Wells as a Power BI portfolio project.
