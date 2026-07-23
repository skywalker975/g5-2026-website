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
