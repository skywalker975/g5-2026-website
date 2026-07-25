---
layout: default
title: "Modelling Food Insecurity"
permalink: /modelling.html
show_sidetoc: true
header_type: hero
header_img: assets/images/folium_map.webp
header_title: "Modelling Food Insecurity in Space and Time"
subtitle: "Two questions: why an area suffers, and whether it is getting worse right now"
---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>

<h1 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">Modelling Food Insecurity in Space and Time</h1>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The last stage of HERO turns the combined dataset into models. We use the same drivers for both models: conflict, displacement, rainfall, vegetation, food prices, and media coverage. From these drivers we answer two separate questions, and each question has its own model. In both cases the thing we predict is the share of the population in acute food insecurity, meaning IPC Phase 3 or above.
</p>

<div class="row mt-4">

<div class="col-md-6 mb-4">
<div class="card h-100 hero-card card-border-top-primary">
<div class="card-body">
<h4 class="card-title text-primary"><i class="fas fa-layer-group me-2"></i>What explains global hunger?</h4>
<p class="card-text text-muted">Why is one area worse off than another? Using the drivers alone, we try to explain the level of acute food insecurity in each area, and to learn which drivers matter most.</p>
</div>
</div>
</div>

<div class="col-md-6 mb-4">
<div class="card h-100 hero-card card-border-top-info">
<div class="card-body">
<h4 class="card-title text-info"><i class="fas fa-clock-rotate-left me-2"></i>What are hunger levels right now?</h4>
<p class="card-text text-muted">IPC assessments are expensive and slow. Most areas are updated only once or twice a year, so a sudden shock can go unseen for months. Between two assessments, we estimate the current level of acute food insecurity from the latest drivers.</p>
</div>
</div>
</div>

</div>

<p style="text-align: justify;">
Both models are built the same way. They use 13 features drawn from conflict, displacement, rainfall, vegetation, food prices, media coverage, and the time of year. We leave out the country name and the map coordinates on purpose. That way the model has to learn how the drivers relate to hunger, instead of simply memorising where each area is.
</p>

<hr class="section-divider">

## <i class="fas fa-layer-group text-primary me-2"></i><span class="text-gradient">What explains global hunger?</span>

To test this fairly, we hold out whole areas. The model trains on some areas and is scored on other areas it has never seen. This stops it from simply recalling an area's usual level.

### <i class="fas fa-earth-africa text-primary me-2"></i><span class="text-gradient">Hunger depends on context</span>

The same drop in rainfall, the same level of conflict, or the same number of displaced people can mean very different things in the Sahel, the Horn of Africa, Central America, or Yemen. A single global model has to apply one rule across 37 very different settings, and that averages out the local patterns that actually matter.

On top of that, much of why one area is worse than another comes down to which country it is in. These long-standing differences between countries are already captured by a simple baseline: the average level of each country. So the global model that uses drivers only does not beat that country-average baseline.

<div class="comparison-table-wrapper" markdown="1">

| model | R² | MAE (pp) | RMSE (pp) |
|---|---|---|---|
| **Country-average baseline** | **0.549** | **8.55** | 11.37 |
| XGBoost (drivers) | 0.529 | 8.77 | 11.62 |
| LightGBM | 0.519 | 8.90 | 11.75 |
| RandomForest | 0.486 | 9.11 | 12.14 |

</div>

*Based on 8,457 area-months, 507 admin-1 areas, and 37 countries.*

The lesson is not that the drivers are weak. It is that the useful signal sits inside countries and regions, not in one global rule. This points to localisation: training the model on smaller groups of similar areas.

### <i class="fas fa-sitemap text-primary me-2"></i><span class="text-gradient">Localisation works, and the report text helps most</span>

To localise, we retrain the same model at nine different scopes. A scope is simply the set of areas each model is allowed to learn from. These range from one global model, to six geographic regions, to one model per country. We also try grouping areas in two other ways: by the values of their drivers, and by what their IPC reports actually talk about.

<div class="comparison-table-wrapper">
<table>
<thead>
<tr><th>scope</th><th>R²</th><th>MAE (pp)</th><th>gain over global</th></tr>
</thead>
<tbody>
<tr><td>global</td><td>0.529</td><td>8.77</td><td>—</td></tr>
<tr><td>regional</td><td>0.617</td><td>7.64</td><td>+0.088</td></tr>
<tr><td><b>local (per country)</b></td><td><b>0.589</b></td><td><b>7.91</b></td><td><b>+0.144</b></td></tr>
<tr><td>driver clusters (k-means)</td><td>0.527</td><td>8.66</td><td>−0.002</td></tr>
<tr><td>driver clusters (hierarchical)</td><td>0.538</td><td>8.51</td><td>+0.009</td></tr>
<tr class="highlight-row"><td>report text (tf-idf, k-means)</td><td>0.658</td><td>7.17</td><td>+0.127</td></tr>
<tr><td>report text (tf-idf, hdbscan)</td><td>0.657</td><td>7.31</td><td>+0.124</td></tr>
<tr><td>report text (embeddings, k-means)</td><td>0.646</td><td>7.36</td><td>+0.114</td></tr>
<tr><td>report text (embeddings, hdbscan)</td><td>0.657</td><td>7.30</td><td>+0.126</td></tr>
</tbody>
</table>
</div>

*The last column is the gain over the global model measured on the same areas, so the comparison is fair.*

Two results stand out.

- **Grouping areas by what their IPC reports describe works best.** Reports tend to fall into clear types, such as conflict and refugees, farming and water, or prices and inflation. Grouping countries by these types beats both the geographic regions and the driver-value groups.
- **A country's own model wins where there is enough data.** For the 11 countries with enough history to train their own model, the country model beats the global one in all 11.

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/static_scope_comparison.png" alt="Static inference, per-country detail, one marker per scope" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>For almost every country the coloured regional, local and text-cluster markers sit to the right (higher R²) and to the left (lower MAE) of the grey global marker.</small></p>
</div>

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/static_scope_box.png" alt="Static inference, per-country R² and MAE by scope" class="img-fluid rounded shadow-lg" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Each scope's per-country R² (left) and MAE (right). The dashed line is the global median R². A box sitting to its right usually beats global.</small></p>
</div>

### <i class="fas fa-magnifying-glass-chart text-primary me-2"></i><span class="text-gradient">What drives acute food insecurity</span>

> "Explainability is even more important than performance." — a WFP data scientist

In humanitarian work, decisions affect lives, so the results have to be explainable. Decision-makers need to see why the model expects hunger to rise or fall before they act on it.

The table below ranks the driver families by how much they move the model's prediction, using SHAP values.

<div class="comparison-table-wrapper" markdown="1">

| driver family | importance |
|---|---|
| **food prices** | 4.04 |
| **conflict** | 3.88 |
| seasonality | 3.38 |
| vegetation | 2.87 |
| displacement | 2.56 |
| media | 2.15 |
| rainfall | 1.76 |

</div>

Food prices and conflict are the two strongest drivers. This matches what global reports say: economic pressure and violence are among the main causes of acute food insecurity. The chart below shows that more violent events and higher food prices push the predicted level of hunger up, and lower values push it down.

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/static_shap_beeswarm.png" alt="Static inference, SHAP chart for the global model" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>How each driver affects the predicted share of the population in IPC Phase 3 or above (global model).</small></p>
</div>

<hr class="section-divider">

## <i class="fas fa-clock-rotate-left text-info me-2"></i><span class="text-gradient">What are hunger levels right now?</span>

IPC assessments are thorough, but they are slow and costly, so most areas are reassessed only once or twice a year. The question here is simple: can we estimate an area's current level of hunger from its last known assessment plus the latest drivers?

To keep this fair, we only ever train on the past and test on the future. The model never sees data from after the point it is predicting.

### <i class="fas fa-anchor text-info me-2"></i><span class="text-gradient">Hunger is sticky</span>

Levels of acute food insecurity are persistent. Where an area stood at its last assessment tells you a lot about where it stands now. Crises can still shift sharply, but the last known level is a strong starting point, which is why simply carrying it forward is a baseline that is hard to beat.

Our nowcast builds on more than the single last value. It uses the last two assessments and the recent trend between them, then adds the latest drivers on top. Doing so lowers the average error by about 18 percent compared with carrying the last value forward, and the nowcast follows the direction of change instead of staying flat. When an area is getting worse, the nowcast tends to move with it.

<div class="comparison-table-wrapper">
<table>
<thead>
<tr><th>approach</th><th>R²</th><th>MAE (pp)</th><th>vs carry-forward</th></tr>
</thead>
<tbody>
<tr class="highlight-row"><td>recent assessments + drivers + driver changes</td><td>0.749</td><td>5.08</td><td>+17.8%</td></tr>
<tr><td>recent assessments only</td><td>0.683</td><td>5.88</td><td>+4.9%</td></tr>
<tr><td>carry the last value forward</td><td>0.625</td><td>6.19</td><td>0.0%</td></tr>
<tr><td>drivers only, no history</td><td>0.503</td><td>7.66</td><td>−23.9%</td></tr>
</tbody>
</table>
</div>

*Based on 1,487 area-months across 31 countries, pooled over five rolling test periods.*

- The nowcast beats the carry-forward baseline in 17 of 21 countries.
- It tracks real change, not just the level. The match between predicted change and actual change since the last assessment is r = 0.54.

### <i class="fas fa-plus text-info me-2"></i><span class="text-gradient">What the drivers add</span>

The recent assessments do most of the work, and the drivers add the edge that catches movement.

<div class="comparison-table-wrapper" markdown="1">

| what the model knows | R² |
|---|---|
| recent assessments only | 0.683 |
| + the current drivers | 0.742 |
| + how fast the drivers are changing | 0.749 |

</div>

A model with drivers but no history does worse than carry-forward, which confirms that the recent assessments are the anchor. The extra accuracy the drivers bring comes from picking up movement, and the strongest early signal is the change in rainfall.

### <i class="fas fa-chart-line text-info me-2"></i><span class="text-gradient">A real example: Afghanistan</span>

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_afghanistan.png" alt="Afghanistan, nowcast vs actual, per province" class="img-fluid rounded shadow-lg" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>One panel per Afghan province. The nowcast (blue) is tracked against the observed IPC level (black). Everything to the right of the dashed line is out of sample. The nowcast follows the real path, including the turns, rather than holding the last value flat.</small></p>
</div>

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_change_scatter.png" alt="Nowcast, predicted vs actual change since last assessment" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Predicted change against actual change since the previous assessment (r = 0.54). The model gets both the direction and the size of the movement, not just the level.</small></p>
</div>

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_skill_vs_baseline.png" alt="Nowcast, per-country improvement over carry-forward" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Per-country improvement over carry-forward. Positive almost everywhere.</small></p>
</div>

### <i class="fas fa-globe text-info me-2"></i><span class="text-gradient">One global model is enough</span>

For the "why" question, tailoring the model to regions or countries helped a lot. For the "now" question it does not. We tested the same nine scopes, and every one of them lands within about 0.01 of the global model on the same areas. The reason is simple: once the model knows an area's own last value, it already knows most of what a regional or country model could add. So for nowcasting, one global model is the right choice.

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_scope_box.png" alt="Nowcast, per-country skill and MAE by scope" class="img-fluid rounded shadow-lg" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Improvement over carry-forward (left) and MAE (right) per country, by scope. Every box sits to the right of zero, so every scope beats carry-forward, and the boxes overlap almost exactly, so no scope is clearly better than global.</small></p>
</div>

### <i class="fas fa-magnifying-glass-chart text-info me-2"></i><span class="text-gradient">What drives the nowcast</span>

<div class="comparison-table-wrapper" markdown="1">

| feature family | importance |
|---|---|
| **recent assessments** | 11.68 |
| **rainfall** | 2.26 |
| conflict | 1.41 |
| prices | 1.36 |
| vegetation | 1.19 |
| seasonality | 0.97 |
| displacement | 0.76 |
| media | 0.76 |

</div>

The recent assessments matter far more than any driver. The nowcast is first anchored to where the area already was. Among the drivers, rainfall is the strongest, which fits the earlier finding that a change in rainfall is the best early sign that conditions are shifting.

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_shap_beeswarm.png" alt="Nowcast, SHAP chart for the main model" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>SHAP chart for the main nowcasting model.</small></p>
</div>

<hr class="section-divider">

## <i class="fas fa-arrow-trend-up text-secondary me-2"></i><span class="text-gradient">Does it scale? Admin-2</span>

Admin-1 areas are provinces. Admin-2 areas are the districts inside them, so this is a finer view. Running the same pipeline one level down is a good test, because this is the level where targeting and early-warning decisions are actually made.

**The "why" model gets stronger.** At the district level the drivers finally beat the country-average baseline, because a finer view reveals real differences inside each country for the drivers to explain.

<div class="comparison-table-wrapper" markdown="1">

| level | baseline R² | best driver model R² | drivers beat baseline? |
|---|---|---|---|
| admin-1 | 0.549 | 0.529 | no |
| admin-2 | 0.557 | **0.610** | yes |

</div>

**The "now" model holds.** Same improvement over carry-forward, same behaviour, and localisation still adds nothing.

<div class="comparison-table-wrapper" markdown="1">

| | admin-1 | admin-2 |
|---|---|---|
| main model R² | 0.749 | 0.698 |
| **improvement over carry-forward** | **+17.8%** | **+18.5%** |
| change-direction r | 0.54 | 0.55 |
| countries beating carry-forward | 17/21 | **22/25** |

</div>

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_adm2_skill.png" alt="Nowcast at admin-2, per-country improvement over carry-forward" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Admin-2 nowcast: per-country improvement over carry-forward. The result carries to the finer level.</small></p>
</div>

<hr class="section-divider">

## <i class="fas fa-key text-success me-2"></i><span class="text-gradient">The takeaway</span>

<div class="card hero-card card-border-top-success mt-2 mb-4">
<div class="card-body">
<h4 class="card-title text-success"><i class="fas fa-key me-2"></i>The "why" model needs local context; the "now" model already carries it</h4>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-3"><i class="fas fa-map-location-dot text-success me-2"></i><b>Explaining hunger needs tailoring.</b> The link between drivers and hunger depends on context, so a single global model loses to the simple country average. Regional, country and report-text models turn that around, adding up to +0.14 R², and grouping by report text is the single best grouping.</li>
<li class="mb-3"><i class="fas fa-globe text-success me-2"></i><b>Estimating hunger now does not.</b> Hunger is persistent, so an area's last known level is a strong starting point that already carries its local context. That is why regional or country models add little: one global model is enough, beating carry-forward by about 18 percent and tracking the direction of change at r = 0.54.</li>
<li class="mb-0"><i class="fas fa-arrow-trend-up text-success me-2"></i><b>Both scale.</b> Taken to admin-2, the level where targeting and early-warning decisions are actually made, the "why" model gets stronger and the "now" model holds.</li>
</ul>
</div>
</div>

<hr class="section-divider">

## <i class="fas fa-map-location-dot text-info me-2"></i><span class="text-gradient">The nowcast, live</span>

Everything above is a summary of the backtest. The map below shows the model's actual output. Each admin-1 area is coloured by its latest nowcast of the IPC Phase 3 or above share. Hover an area to see its trend, with the observed IPC assessments (solid) and the nowcast (line), and a dotted connector from the last real assessment to the latest nowcast. Click a province to zoom in. For Cameroon and DR Congo this drills into the admin-2 layer, the same model one level finer, at the resolution where decisions are actually made.

<div class="my-4 wide-breakout">
    <iframe src="{{ site.baseurl }}/assets/charts/nowcast_map.html" width="100%" height="720px" style="border: 1px solid #e0e0e0; border-radius: 0.5rem;" loading="lazy" title="HERO admin-1 nowcast map with admin-2 drill-down"></iframe>
    <p class="text-muted mt-2"><small>Latest nowcast of the IPC Phase 3 or above share (% of population). Admin-1 for all four countries. Click Cameroon or DR Congo provinces to drill into admin-2. Afghanistan and Somalia show admin-1 only, because their admin-2 boundaries do not line up with the assessment data.</small></p>
</div>
