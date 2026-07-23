---
layout: default
title: "Preprocessing"
permalink: /Preprocessing.html
show_sidetoc: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Preprocessing"

---


<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>


### Integrated Datasets and Architecture of HERO

The <b>HERO</b> system organizes humanitarian data and its analytical components around a unified, ready-to-use structure. The framework combines various dimensions of risk (IPC, conflict, displacement, meteorological data, market prices, media signals, and vegetation health) by directly aligning them with food security assessment periods.

<div class="container mt-4">
<div class="row">
<!-- Data Aggregation Architecture Section -->
<div class="card hero-card card-border-top-primary mt-2 mb-4">
  <div class="card-body p-4 p-md-5">
    
### Systemic Data Missingness & Blackout Dynamics

The <b>HERO</b> analytics engine performs a two-dimensional missingness diagnosis across all 7 target data sources. By mapping missing values into binary shadow indicators ($1$ for `NaN`, $0$ for observed), the pipeline uncovers both **cross-dataset co-failures** and **spatial coverage blackouts** to guide targeted imputation strategies.

<div class="container mt-4">
<div class="row">

<!-- Section: Two-Step Missingness Workflow -->
<div class="card hero-card card-border-top-primary mt-2 mb-4">
  <div class="card-body p-4 p-md-5">
    <!-- Main Header -->
    <h3 class="card-title text-primary fw-bold mb-2">
      Shadow Matrix Analysis: Two-Step Analytical Workflow
    </h3>
    <p class="card-text text-muted mb-4 lead fs-6">
      Data unavailability is rarely random. This workflow isolates structural dependencies between sensors and tracks regional data degradation to prevent operational bias during modeling:
    </p>
<!-- Main Container Card -->
    <div class="card border-0 bg-light rounded-4 p-3 p-md-4">
      <div class="row g-4">
<!-- Column 1: Step 1 - Structural Correlation Analysis -->
        <div class="col-md-6 border-end-md">
          <div class="p-2">
            <!-- Badge / Pill Header -->
            <div class="bg-primary text-white text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm">
              <i class="fas fa-network-wired me-2"></i> STEP 1: STRUCTURAL CORRELATION
              <span class="d-block text-white-50 small fw-normal">(Cross-Dataset Dependencies)</span>
            </div>
            <!-- Bullet List -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">Correlation Matrix Computation:</span>
                <span class="text-muted d-block small mt-1">Calculates a pairwise Pearson correlation matrix across the 7 binary shadow variables (<code class="small">missing_cols</code>) to measure co-missingness independently of spatial location.</span>
              </li>
              <li class="mb-3">
                <span class="fw-bold text-dark">Co-Failure Pattern Identification:</span>
                <span class="text-muted d-block small mt-1">High positive correlations (approaching $+1.0$) reveal systematic co-failing datasets—such as cases where conflict escalations cause simultaneous losses in both market prices and displacement data.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Bidirectional Heatmap Rendering:</span>
                <span class="text-muted d-block small mt-1">Outputs a $7 \times 7$ correlation matrix (<code class="small">coolwarm</code> palette, bounded from $-1$ to $+1$) to visually isolate interconnected clusters of missingness.</span>
              </li>
            </ul>
          </div>
        </div>
<!-- Column 2: Step 2 - Geographical Blackout Analysis -->
        <div class="col-md-6">
          <div class="p-2">
            <!-- Badge / Pill Header -->
            <div class="bg-danger text-white text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm" style="background-color: #fee2e2 !important; color: #991b1b !important;">
              <i class="fas fa-earth-americas me-2"></i> STEP 2: GEOGRAPHICAL BLACKOUT
              <span class="d-block small fw-normal" style="color: #991b1b; opacity: 0.8;">(Spatial Failure Patterns)</span>
            </div>
            <!-- Bullet List -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">Spatial Aggregation:</span>
                <span class="text-muted d-block small mt-1">Groups the shadow matrix by <code class="small">Country</code> and calculates the column mean to determine the exact percentage missingness rate per sensor within each national jurisdiction.</span>
              </li>
              <li class="mb-3">
                <span class="fw-bold text-dark">Severity Ranking & Scoring:</span>
                <span class="text-muted d-block small mt-1">Sums missingness rates across all 7 indicators to compute a <code class="small">total_failure_score</code>, sorting nations from highest to lowest overall data availability collapse.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Unidirectional Heatmap Rendering:</span>
                <span class="text-muted d-block small mt-1">Generates a spatial heatmap (<code class="small">YlOrRd</code> palette, bounded from $0$ to $1$) to pinpoint geographical blackouts where multiple data streams systematically fail simultaneously.</span>
              </li>
            </ul>
          </div>
        </div>

</div>
    </div>

  </div>
</div>

</div>
</div>

---

<!-- Section: Missing Data Dynamics & Imputation Tactics -->
<div class="card hero-card card-border-top-primary mt-2 mb-4">
  <div class="card-body p-4 p-md-5">
    <!-- Main Header -->
    <h3 class="card-title text-primary fw-bold mb-2">
      Data Missingness Dynamics & Imputation Architecture
    </h3>
    <p class="card-text text-muted mb-4 lead fs-6">
      Data is never missing by accident: missingness carries actionable operational context. By identifying whether gaps stem from logistical blackouts, political hurdles, or cloud cover, the pipeline deploys targeted mitigation strategies to prevent real-world distortion.
    </p>
 <!-- Main Container Card -->
    <div class="card border-0 bg-light rounded-4 p-3 p-md-4">
      <div class="row g-4">
<!-- Column 1: Real-World Missingness Drivers -->
        <div class="col-md-4 border-end-md">
          <div class="p-2">
            <!-- Badge / Pill Header -->
            <div class="bg-danger text-white text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm" style="background-color: #fee2e2 !important; color: #991b1b !important;">
              <i class="fas fa-triangle-exclamation me-2"></i> MISSINGNESS DRIVERS
              <span class="d-block small fw-normal" style="color: #991b1b; opacity: 0.8;">(Real-World Root Causes)</span>
            </div>
            <!-- Bullet List -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">Institutional & Geopolitical Blackouts:</span>
                <span class="text-muted d-block small mt-1">Missing WFP, ACLED, or IDP reports in unstable areas are <b>MNAR</b> (Missing Not At Random). Active conflict or governance collapse closes markets and forces field staff evacuations, disrupting data pipelines.</span>
              </li>
              <li class="mb-3">
                <span class="fw-bold text-dark">Environmental & Satellite Interference:</span>
                <span class="text-muted d-block small mt-1">Lost NDVI or CHIRPS signals are driven by physical factors (<b>MAR</b> - Missing At Random). Persistent cloud cover during rainy seasons blinds optical sensors, creating systematic yet predictable gaps.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Cascading Co-Missingness:</span>
                <span class="text-muted d-block small mt-1">Gaps are structurally correlated. When a crisis isolates a region, multiple indicators collapse simultaneously (e.g., market prices, displacement tracking, and conflict reports vanish together).</span>
              </li>
            </ul>
          </div>
        </div>
<!-- Column 2: Reconstruction Tactics -->
        <div class="col-md-4 border-end-md">
          <div class="p-2">
            <!-- Badge / Pill Header -->
            <div class="bg-primary text-white text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm">
              <i class="fas fa-wand-magic-sparkles me-2"></i> IMPUTATION TACTICS
              <span class="d-block text-white-50 small fw-normal">(Data Reconstruction Pipeline)</span>
            </div>
            <!-- Bullet List -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">Behavioral KNN Imputation:</span>
                <span class="text-muted d-block small mt-1">Fills missing points by finding statistical "behavioral neighbors." Rather than relying solely on geographic distance, it evaluates matching profiles across secondary metrics (e.g., inflation spikes or rainfall anomalies).</span>
              </li>
              <li class="mb-3">
                <span class="fw-bold text-dark">Capped Temporal Carry-Forward:</span>
                <span class="text-muted d-block small mt-1">For slow-moving metrics like IDP counts, the latest valid snapshot is carried forward up to a strict maximum threshold (<code class="small">idp_staleness_days</code>), halting propagation before data becomes stale.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Pixel-Weighted Aggregation (NDVI):</span>
                <span class="text-muted d-block small mt-1">Missing vegetation indices within IPC periods are re-aggregated using spatial area weights (<code class="small">n_pixels</code>), ensuring larger sub-regions carry proportionate weight in estimated averages.</span>
              </li>
            </ul>
          </div>
        </div>
 <!-- Column 3: Model Safeguards & Anti-Bias Rules -->
        <div class="col-md-4">
          <div class="p-2">
            <!-- Badge / Pill Header -->
            <div class="bg-warning text-dark text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm" style="background-color: #fef08a !important;">
              <i class="fas fa-shield-cat me-2"></i> MODEL SAFEGUARDS
              <span class="d-block text-muted small fw-normal">(Anti-Distortion Rules)</span>
            </div>
            <!-- Bullet List -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">Rejection of Global Averages:</span>
                <span class="text-muted d-block small mt-1">Replacing missing values with mean or median averages artificially flattens variance and erases local crisis signals. This approach was explicitly rejected during benchmarking.</span>
              </li>
              <li class="mb-3">
                <span class="fw-bold text-dark">Neutral Tone Non-Imputation:</span>
                <span class="text-muted d-block small mt-1">For news indicators (GDELT), zero media coverage does not equal a "neutral" sentiment. Media tone is never imputed to zero in the absence of mentions, preserving signal integrity.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Strict Admin Isolation (No Fallback):</span>
                <span class="text-muted d-block small mt-1">Regional (ADM1) and district (ADM2) processing remain completely isolated. Missing district data is never filled with regional averages, preventing false geographic precision.</span>
              </li>
            </ul>
          </div>
        </div>

</div>
    </div>

  </div>
</div>
