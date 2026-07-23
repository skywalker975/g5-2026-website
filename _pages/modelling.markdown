---
layout: default
title: "Modelling Food Insecurity"
permalink: /modelling.html
show_sidetoc: true
header_type: hero
header_img: assets/images/folium_map.webp
header_title: "Modelling Food Insecurity in Space and Time"
subtitle: "Two questions — why an area suffers, and whether it's deteriorating right now"
---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>

<h1 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">Modelling Food Insecurity in Space and Time</h1>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The final stage of HERO turns the integrated dataset into predictive models. From the same drivers —
conflict, displacement, rainfall, vegetation, food prices, media — we answer <b>two different
operational questions</b>, each with its own model and its own honest test. The target throughout is the
share of a population in <b>IPC Phase 3+</b> ("Crisis or worse", a 0–100 scale).
</p>

<div class="row mt-4">

<div class="col-md-6 mb-4">
<div class="card h-100 hero-card card-border-top-primary">
<div class="card-body">
<h4 class="card-title text-primary"><i class="fas fa-layer-group me-2"></i>Static Inference — <i>"why?"</i></h4>
<p class="card-text text-muted">A cross-sectional, targeting question: from drivers alone, can we explain <b>why one area is worse than another</b>? No history, no geography — just the current conditions on the ground.</p>
</div>
</div>
</div>

<div class="col-md-6 mb-4">
<div class="card h-100 hero-card card-border-top-info">
<div class="card-body">
<h4 class="card-title text-info"><i class="fas fa-clock-rotate-left me-2"></i>Nowcasting — <i>"now?"</i></h4>
<p class="card-text text-muted">An operational, early-warning question: between two expensive IPC assessments, can we estimate an area's <b>current</b> level — <b>is it deteriorating right now</b>? — from its last reading plus the latest drivers?</p>
</div>
</div>
</div>

</div>


<hr class="section-divider">

## Method

Both rounds use the same **13 features — 11 driver rates (conflict, displacement, rainfall, vegetation,
food prices, media) plus seasonality** — and deliberately exclude country identity and coordinates, so the
model learns the driver → IPC relationship rather than memorising *which* place it is looking at.

They differ only in validation. IPC is strongly autocorrelated in space and time, so each round holds out
the dimension that would otherwise leak:

| round | validation | held out | baseline |
|---|---|---|---|
| **Static inference** | `GroupKFold` by area | whole areas (spatial hold-out) | per-country mean |
| **Nowcasting** | walk-forward rolling-origin | the future (temporal hold-out) | persistence (last value carried forward) |

<hr class="section-divider">

## Round 1 · Static Inference — explaining *why*

**Scale.** 8,457 area-months · 507 admin-1 areas · 37 countries.

Out-of-fold leaderboard (admin-1, imputed dataset):

| model | R² | MAE (pp) | RMSE (pp) |
|---|---|---|---|
| **Country-mean baseline** | **0.549** | **8.55** | 11.37 |
| XGBoost (drivers) | 0.529 | 8.77 | 11.62 |
| LightGBM | 0.519 | 8.90 | 11.75 |
| RandomForest | 0.486 | 9.11 | 12.14 |
| DecisionTree | 0.299 | 10.56 | 14.18 |

The striking result is that **the drivers-only global model does *not* beat the country-mean baseline**
(R² 0.529 vs 0.549). This is an *insight*, not a failure: a large part of "why is this area worse" is
simply *which country* it sits in — chronic structural differences the country-mean captures for free —
and forcing **one** global driver → IPC mapping to fit 37 very different contexts averages away exactly
the relationships that matter locally. That points straight at **localization**.

### Localization works — and narrative clusters help most

We re-run the round at **nine training scopes** — **global**, **regional** (a 6-region agro-climatic
map), **local** (one model per country), two **quantitative** clusters (K-Means and hierarchical, grouping
areas by the shape of their own driver time-series), and **four qualitative** clusters built from the IPC
*report text* (a TF-IDF and a dense-embedding representation, each split by K-Means and HDBSCAN). Every
row is routed to its subgroup's model, then each scope is re-compared to the global model **on exactly the
rows it scored** — an apples-to-apples "did routing help?"

| scope | overall R² | MAE (pp) | global on same rows | ΔR² |
|---|---|---|---|---|
| global | 0.529 | 8.77 | — | — |
| regional | 0.617 | 7.64 | 0.529 | +0.088 |
| **local (per-country)** | 0.589 | 7.91 | 0.445 | **+0.144** |
| cluster_kmeans (drivers) | 0.527 | 8.66 | 0.529 | −0.002 |
| cluster_hierarchical (drivers) | 0.538 | 8.51 | 0.529 | +0.009 |
| **cluster_tfidf_kmeans** (text) | **0.658** | **7.17** | 0.531 | **+0.127** |
| cluster_tfidf_hdbscan (text) | 0.657 | 7.31 | 0.533 | +0.124 |
| cluster_emb_kmeans (text) | 0.646 | 7.36 | 0.532 | +0.114 |
| cluster_emb_hdbscan (text) | 0.657 | 7.30 | 0.531 | +0.126 |

- **Local wins hardest** on the 11 data-rich countries, beating global in **all 11** (ΔR² **+0.144**);
  regional lifts pooled R² to 0.617 with near-complete coverage.
- **The driver-fingerprint clusters are flat** (ΔR² ±0.01) — not a better partition than the geography we
  already have.
- **The text-narrative clusters are the strongest cluster scopes — and even edge out the region map.**
  All four add **+0.11 to +0.13 ΔR²**. Grouping countries by *what their IPC reports are about*
  (conflict-refugee, agropastoral-water, price-inflation typologies) turns out to be a better partition
  than grouping them by agro-climatic region.

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/static_scope_box.png" alt="Static inference — per-country R² and MAE by localization scope" class="img-fluid rounded shadow-lg" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Each scope's per-country R² (left) and MAE (right) as a box; the dashed line is the global median R² — a box sitting to its right typically beats global.</small></p>
</div>

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/static_scope_comparison.png" alt="Static inference — per-country detail, one marker per scope" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Full per-country detail — for almost every country the coloured regional / local / text-cluster markers sit to the right (higher R²) and left (lower MAE) of the grey global marker.</small></p>
</div>

### What drives food insecurity

Aggregated SHAP (mean \|SHAP\|) for the global XGBoost model, by driver family:

| driver family | mean \|SHAP\| |
|---|---|
| **food prices** | 4.04 |
| **conflict** | 3.88 |
| seasonality | 3.38 |
| vegetation | 2.87 |
| displacement | 2.56 |
| media | 2.15 |
| rainfall | 1.76 |

**Food prices and conflict dominate the explanation** — matching field intuition that price shocks and
violence drive acute food insecurity. The hierarchy is stable and interpretable precisely *because* the
model can't lean on "which country": every bit of signal it uses is an actual driver relationship.

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/static_shap_beeswarm.png" alt="Static inference — SHAP beeswarm for the global model" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>SHAP beeswarm — impact of each driver on the predicted IPC 3+ share (global model, imputed).</small></p>
</div>

<hr class="section-divider">

## Round 2 · Nowcasting — tracking *now*

IPC assessments are expensive and infrequent. Between two field rounds, can we estimate an area's
**current** IPC 3+ from its **last known assessment** plus the **latest drivers**? Three nested feature
sets let us decompose *where the skill comes from*: `autoregressive` (last assessments only), `nowcast`
(+ the 11 driver levels), and `nowcast_change` (+ how fast each driver is moving). The honest measure of
value is **skill = MAE improvement over persistence**, not raw R², because persistence is already a
*strong* baseline for such a persistent target.

**Scale.** 1,487 area-months · 31 countries, pooled across 5 walk-forward origins.

| feature set | model | R² | MAE (pp) | skill vs persistence |
|---|---|---|---|---|
| **nowcast_change** | **XGBoost** | **0.749** | **5.08** | **+17.8%** |
| nowcast_change | LightGBM | 0.744 | 5.10 | +17.6% |
| nowcast | LightGBM | 0.745 | 5.13 | +17.0% |
| autoregressive (lags only) | XGBoost | 0.683 | 5.88 | +4.9% |
| **— (persistence baseline)** | — | 0.625 | 6.19 | 0.0% |
| drivers_only (no lags) | XGBoost | 0.503 | 7.66 | −23.9% |

- **Drivers + the last assessment beat naive carry-forward by +17.8% MAE** (5.08 vs 6.19 pp), lifting R²
  from 0.625 to **0.749**.
- **It holds country by country** — the model beats persistence in **17 of 21** countries.
- **It tracks real change, not just level** — change-direction correlation (predicted vs actual change
  since the last assessment) is **r = 0.54**.

### Where the skill comes from

| feature set | R² | what it adds |
|---|---|---|
| autoregressive (lags only) | 0.683 | the last assessment alone already beats persistence (0.625) |
| + driver **levels** (nowcast) | 0.742 | the biggest single jump — drivers add on top of persistence |
| + driver **changes** (nowcast_change) | 0.749 | a final nudge from *how fast* drivers are moving |

**Most of the signal is persistence** (a `drivers_only` model with no lags scores *below* the baseline),
and the value the model adds over persistence comes from the **exogenous drivers** — the strongest being
the **change in rainfall**, the leading early signal that conditions are shifting.

### A real case — Afghanistan

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_afghanistan.png" alt="Afghanistan — admin-1 nowcast vs actual, per province" class="img-fluid rounded shadow-lg" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>One panel per Afghan admin-1 province: the walk-forward nowcast (blue) tracked against the observed IPC 3+ (black). Everything right of the dashed line is out-of-sample. The nowcast follows the real trajectory — including turns — rather than flat-lining the last value, which is exactly what a useful early-warning signal must do.</small></p>
</div>

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_change_scatter.png" alt="Nowcast — predicted vs actual change since last assessment" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Predicted vs actual <i>change</i> since the previous assessment (r = 0.54): the model gets the direction and magnitude of movement, not just the level.</small></p>
</div>

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_skill_vs_baseline.png" alt="Nowcast — per-country skill over persistence" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Per-country skill (% MAE improvement over persistence) — positive almost everywhere.</small></p>
</div>

### Localization doesn't help here

Same nine scopes as the static round. Read the **ΔR² column, not "overall R²"** — each scope scores a
different subset of rows (fewer for local/cluster scopes than for global), so their raw R² isn't
comparable to each other. ΔR² fixes that: it re-scores the *global* model on that same row subset, so
"scope R² vs ΔR²'s global R²" is the honest apples-to-apples test of whether routing actually helped.

| scope | overall R² | MAE (pp) | global on same rows | ΔR² |
|---|---|---|---|---|
| **global** | **0.742** | **5.23** | — | — |
| regional | 0.734 | 5.26 | 0.742 | −0.008 |
| local (per-country) | 0.649 | 5.37 | 0.638 | +0.012 |
| cluster_kmeans (drivers) | 0.751 | 5.16 | 0.744 | +0.007 |
| cluster_hierarchical (drivers) | 0.754 | 5.16 | 0.744 | +0.010 |
| cluster_tfidf_kmeans (text) | 0.660 | 5.56 | 0.725 | −0.065 |
| cluster_tfidf_hdbscan (text) | 0.744 | 5.19 | 0.745 | −0.001 |
| cluster_emb_kmeans (text) | 0.763 | 4.91 | 0.759 | +0.004 |
| cluster_emb_hdbscan (text) | 0.746 | 5.18 | 0.752 | −0.006 |

By ΔR², every scope is within ±0.01 of global — **including the text clusters that lifted the static
model by +0.11–0.13.** `cluster_emb_kmeans`'s 0.763 looks like a win, but global scores 0.759 on that
same easier subset of rows, so the routing itself added almost nothing. This makes sense: once you
condition on an area's *own last assessment*, the "which crisis context is this" information
localization supplies — geographic, behavioural or narrative — is largely already baked in.
**The recommendation is one global model.**

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_scope_box.png" alt="Nowcast — per-country skill and MAE by localization scope" class="img-fluid rounded shadow-lg" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Skill vs persistence (left) and MAE (right) per country, by scope. Every box sits right of 0 (all scopes beat persistence), and the boxes overlap almost exactly — no scope is consistently better than global.</small></p>
</div>

### What drives the nowcast

| feature family | mean \|SHAP\| |
|---|---|
| **persistence (lags)** | 11.68 |
| **rainfall** | 2.26 |
| conflict | 1.41 |
| prices | 1.36 |
| vegetation | 1.19 |
| seasonality | 0.97 |
| displacement | 0.76 |
| media | 0.76 |

**Persistence dominates** — the last assessment outweighs every driver several times over; the nowcast is
first and foremost anchored to where the area already was. **Rainfall is the strongest exogenous signal**,
consistent with rainfall *change* being what lifts R² over the lags-only model.

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_shap_beeswarm.png" alt="Nowcast — SHAP beeswarm for the headline model" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>SHAP beeswarm for the headline <code>nowcast_change</code> XGBoost model (imputed).</small></p>
</div>

<hr class="section-divider">

## Does it scale? Admin-2

Run the identical pipeline one geographic level finer — roughly 6× the areas (~3,000+ areas, 38 countries,
36,938 static rows, 19,716 nowcast windows) — and the story doesn't just survive; the static model
**strengthens** while the nowcast **holds**.

*(Rates at admin-2 use assessed population as the denominator, so admin-1 pp and admin-2 pp are not
directly comparable. The honest comparisons are always **within** a level.)*

**Static strengthens** — at admin-2 the drivers finally *beat* the country baseline, because finer
geography exposes real within-country variation for them to explain:

| level | baseline R² | best driver model R² | drivers beat baseline? |
|---|---|---|---|
| admin-1 | 0.549 | 0.529 (XGBoost) | **no** |
| admin-2 | 0.557 | **0.610** (RandomForest) | **yes** |

**Nowcast holds** — same skill, same mechanism, localization still adds nothing:

| | admin-1 | admin-2 |
|---|---|---|
| headline model R² | 0.749 | 0.698 |
| **skill vs persistence** | **+17.8%** | **+18.5%** |
| change-direction r | 0.54 | 0.55 |
| countries beating persistence | 17/21 | **22/25** |

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/nowcast_adm2_skill.png" alt="Nowcast (admin-2) — per-country skill over persistence" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Admin-2 nowcast: per-country skill over persistence — the mechanism carries to the finer level.</small></p>
</div>

<hr class="section-divider">

## The takeaway

<div class="card hero-card card-border-top-success mt-2 mb-4">
<div class="card-body">
<h4 class="card-title text-success"><i class="fas fa-key me-2"></i>The "why" must learn its context; the "now" already remembers it</h4>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-3"><i class="fas fa-map-location-dot text-success me-2"></i><b>The "why" model wants tailoring.</b> Driver → hunger relationships are context-specific, so a single global model loses to the country prior at admin-1 — but <b>regional, local and narrative-cluster</b> routing turns that around (up to +0.14 R²), and text-narrative clusters are the single best grouping.</li>
<li class="mb-3"><i class="fas fa-globe text-success me-2"></i><b>The "now" model thrives global.</b> An area's own last assessment already encodes its local context — the very thing localization would otherwise supply — so routing to regional or local sub-models adds nothing and only starves each of data. One global nowcast beats persistence by <b>~18%</b>, tracking the direction of change at <b>r ≈ 0.54</b>.</li>
<li class="mb-0"><i class="fas fa-arrow-trend-up text-success me-2"></i><b>Both scale.</b> Taken to admin-2 — the level where targeting and early-warning decisions are actually made — the explanatory model strengthens and the operational nowcast holds.</li>
</ul>
</div>
</div>
