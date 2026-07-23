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
    
<!-- Intestazione Principale -->
<h3 class="card-title text-primary fw-bold mb-2">
      Data Pipeline: Multi-Domain Aggregation Framework
    </h3>
    <p class="card-text text-muted mb-4 lead fs-6">
      Behind the IPC anchor data lies the temporal and spatial convergence of conflict, climatic, market, and social signals. 
      Every external theme is aggregated strictly to match each IPC reference period and native admin level:
    </p>
 <!-- Card Contenitore Principale -->
    <div class="card border-0 bg-light rounded-4 p-3 p-md-4">
      <div class="row g-4">

<!-- Colonna 1: Market & Economic Signals -->
<div class="col-md-4 border-end-md">
          <div class="p-2">
            <!-- Badge / Pill Header -->
            <div class="bg-primary text-white text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm">
              <i class="fas fa-chart-line me-2"></i> MARKET & ECONOMIC
              <span class="d-block text-white-50 small fw-normal">(WFP Data)</span>
            </div>
            
 <!-- Lista Punti -->
<ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">Price & Inflation Metrics:</span>
                <span class="text-muted">Calculates per-period mean market prices and mean inflation rates across all active local markets.</span>
              </li>
              <li class="mb-3">
                <span class="fw-bold text-dark">Observation Rigor:</span>
                <span class="text-muted">Tracks observation counts (<code class="small">wfp_obs_count</code>) to quantify market sampling density per window.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Mapping Quality Propagation:</span>
                <span class="text-muted">Enforces worst-case status (<code class="small">'elastic_buffer'</code> over <code class="small">'strict_pip'</code>) if any contributing market relies on spatial buffer fallback.</span>
              </li>
            </ul>
          </div>
        </div>
<!-- Colonna 2: Environmental & Vegetation -->
        <div class="col-md-4 border-end-md">
          <div class="p-2">
            <!-- Badge / Pill Header -->
            <div class="bg-warning text-dark text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm" style="background-color: #fef08a !important;">
              <i class="fas fa-cloud-sun-rain me-2"></i> CLIMATE & VEGETATION
              <span class="d-block text-muted small fw-normal">(Rainfall & NDVI)</span>
            </div>
            <!-- Lista Punti -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">Precipitation Dynamics:</span>
                <span class="text-muted">Aggregates 1-month true period sum alongside 1-month and 3-month rolling precipitation means and percentage anomalies.</span>
              </li>
              <li class="mb-3">
                <span class="fw-bold text-dark">Spatial Pixel Weighting:</span>
                <span class="text-muted">Aggregates dekadal NDVI greenness (<code class="small">vim</code>) and vegetation condition (% of normal, <code class="small">viq</code>) weighted by polygon pixel count (<code class="small">n_pixels</code>).</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Deduplication:</span>
                <span class="text-muted">Removes exact upstream duplicates prior to aggregation to prevent double-counting dekads.</span>
              </li>
            </ul>
          </div>
        </div>
<!-- Colonna 3: Conflict & Displacement -->
        <div class="col-md-4">
          <div class="p-2">
            <!-- Badge / Pill Header -->
            <div class="bg-danger text-white text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm" style="background-color: #fee2e2 !important; color: #991b1b !important;">
              <i class="fas fa-shield-halved me-2"></i> CONFLICT & DISPLACEMENT
              <span class="d-block small fw-normal" style="color: #991b1b; opacity: 0.8;">(ACLED, GDELT & IDP)</span>
            </div>
            <!-- Lista Punti -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">ACLED Event Pivoting:</span>
                <span class="text-muted">Sums conflict events and fatalities by specific event types during each IPC window into a wide schema.</span>
              </li>
              <li class="mb-3">
                <span class="fw-bold text-dark">GDELT Tone & Mentions:</span>
                <span class="text-muted">Aggregates media signals into 4 CAMEO QuadClasses, computing total events, mentions, and mentions-weighted mean tone.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">IDP Temporal Alignment:</span>
                <span class="text-muted">Matches the latest displacement snapshot prior to IPC period end, enforcing strict max-staleness thresholds.</span>
              </li>
            </ul>
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
