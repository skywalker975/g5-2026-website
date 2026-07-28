---
layout: default
title: "Interactive Decision Support Dashboard"
permalink: /UI.html
show_sidetoc: true
header_type: hero
header_img: assets/copertine_pagine/dashboard.png
header_title: "Interactive Decision Support Dashboard"
subtitle: "Real-time humanitarian intelligence across 53 nations — from global overview to sub-national diagnostics"
---

<h1 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">HERO v6: A Command-Level Interface for Global Humanitarian Monitoring</h1>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The HERO v6 dashboard is not just a data visualisation tool — it is an operational decision-support environment. Designed for analysts, humanitarian coordinators, and researchers working across multiple crisis theatres simultaneously, it integrates food insecurity metrics, conflict activity, market inflation, population displacement, and satellite climate data into a single, coherent interface spanning <strong>53 high-vulnerability nations</strong> with deep diagnostics for 20 primary pilot countries.
</p>

<div class="row g-4 my-4">
  <div class="col-md-6">
    <div class="glass-card card-border-top-info h-100 p-4">
      <div class="badge-premium-admin1 mb-2">Usability & Ergonomics</div>
      <h4 class="font-weight-bold text-gradient mb-2">Engineered for Operations Centres</h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">The interface uses a Glassmorphism Dark Mode aesthetic specifically chosen to minimise eye strain during extended operational shifts, while optimising high-density geospatial rendering performance.</p>
    </div>
  </div>
  <div class="col-md-6">
    <div class="glass-card card-border-top-warning h-100 p-4">
      <div class="badge-premium-admin2 mb-2">Architecture & Security</div>
      <h4 class="font-weight-bold text-gradient mb-2">100% Offline & Containerless</h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">The entire suite runs locally via a standalone Python HTTP server (<code>run_ui.bat</code> on port 8080). No cloud dependencies. No external containers. Full data operational security.</p>
    </div>
  </div>
</div>

<div class="text-center my-5">
  <a href="http://epimelesi.isti.cnr.it:8080/UI/" target="_blank" class="btn btn-premium-hero btn-lg px-5 py-3 shadow" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; text-transform: uppercase; letter-spacing: 1px;">
    Explore HERO Interactive Dashboard
  </a>
</div>

<hr class="section-divider">

## <span class="text-gradient">1. System Navigation: Eight Operational Views</span>

<p class="text-secondary mb-4">
The left navigation sidebar provides instant access to 8 core analytical perspectives, structured to support both macro-level global overviews and sub-national granular diagnostics.
</p>

<div class="row g-4 mb-5">
  <div class="col-md-6 col-lg-3">
    <div class="glass-card card-border-top-secondary h-100 p-3">
      <h5 class="font-weight-bold text-light mb-2">1. Global Overview</h5>
      <p class="text-secondary small mb-0">Worldwide SVG risk map with real-time crisis severity rankings across all monitored countries.</p>
    </div>
  </div>
  <div class="col-md-6 col-lg-3">
    <div class="glass-card card-border-top-warning h-100 p-3">
      <h5 class="font-weight-bold text-light mb-2">2. Country Detail</h5>
      <p class="text-secondary small mb-0">Sub-national analytical suite with 11 domain-specific diagnostic tabs per country.</p>
    </div>
  </div>
  <div class="col-md-6 col-lg-3">
    <div class="glass-card card-border-top-info h-100 p-3">
      <h5 class="font-weight-bold text-light mb-2">3. Country Compare</h5>
      <p class="text-secondary small mb-0">Multi-country time series overlay and seasonal radar comparisons across simultaneous crises.</p>
    </div>
  </div>
  <div class="col-md-6 col-lg-3">
    <div class="glass-card card-border-top-success h-100 p-3">
      <h5 class="font-weight-bold text-light mb-2">4. Spatio-Temporal</h5>
      <p class="text-secondary small mb-0">Global thematic heatmaps for tracking crisis propagation across custom indicators over time.</p>
    </div>
  </div>
  <div class="col-md-6 col-lg-3">
    <div class="glass-card card-border-top-secondary h-100 p-3">
      <h5 class="font-weight-bold text-light mb-2">5. Global TSA</h5>
      <p class="text-secondary small mb-0">Trajectory clustering and time series diagnostics across all 20 primary pilot nations simultaneously.</p>
    </div>
  </div>
  <div class="col-md-6 col-lg-3">
    <div class="glass-card card-border-top-warning h-100 p-3">
      <h5 class="font-weight-bold text-light mb-2">6. Sub-National Clustering</h5>
      <p class="text-secondary small mb-0">Evaluates and compares provincial clustering strategies within any selected country.</p>
    </div>
  </div>
  <div class="col-md-6 col-lg-3">
    <div class="glass-card card-border-top-info h-100 p-3">
      <h5 class="font-weight-bold text-light mb-2">7. Topological Explorer</h5>
      <p class="text-secondary small mb-0">Graph network analysis of cross-variable causal shock corridors and market connectivity.</p>
    </div>
  </div>
  <div class="col-md-6 col-lg-3">
    <div class="glass-card card-border-top-success h-100 p-3">
      <h5 class="font-weight-bold text-light mb-2">8. Cluster Evolution</h5>
      <p class="text-secondary small mb-0">Alluvial flow tracking of risk state transitions over time — how provinces migrate between crisis phases.</p>
    </div>
  </div>
</div>

<hr class="section-divider">

## <span class="text-gradient">2. Sub-National Diagnostics: 11 Country Modules</span>

<p class="text-secondary mb-4">
Selecting any country loads a vertically partitioned analytical suite with 11 domain-specific modules — each designed to address a distinct dimension of humanitarian risk.
</p>

<div class="row g-3 mb-5">
  <div class="col-md-6">
    <div class="glass-card p-3 h-100">
      <ul class="list-group list-group-flush bg-transparent">
        <li class="list-group-item bg-transparent text-secondary border-secondary"><strong class="text-light">Map & Regions:</strong> Vector sub-regional map for filtering and drilling into provincial time series.</li>
        <li class="list-group-item bg-transparent text-secondary border-secondary"><strong class="text-light">Charts & Trends:</strong> Aggregated stability metrics with linear trajectory and 12-month radar views.</li>
        <li class="list-group-item bg-transparent text-secondary border-secondary"><strong class="text-light">WFP Food Markets:</strong> Three-tier micro-market inflation explorer — National, Map, and Single Market resolution.</li>
        <li class="list-group-item bg-transparent text-secondary border-secondary"><strong class="text-light">GDELT News Analytics:</strong> Media salience vs. ground events toggle, with news sentiment tone tracking.</li>
        <li class="list-group-item bg-transparent text-secondary border-secondary"><strong class="text-light">Food Insecurity (IPC):</strong> Acute population shares across IPC Crisis Phases 3 to 5, over time.</li>
        <li class="list-group-item bg-transparent text-secondary border-secondary"><strong class="text-light">ACLED Security Events:</strong> Geolocated conflict tracking along humanitarian access corridors.</li>
      </ul>
    </div>
  </div>
  <div class="col-md-6">
    <div class="glass-card p-3 h-100">
      <ul class="list-group list-group-flush bg-transparent">
        <li class="list-group-item bg-transparent text-secondary border-secondary"><strong class="text-light">IDP Displacement:</strong> Demographic tracking of internally displaced persons and cross-border refugee flows.</li>
        <li class="list-group-item bg-transparent text-secondary border-secondary"><strong class="text-light">CHIRPS Rainfall:</strong> Satellite precipitation metrics for drought onset and flash flood detection.</li>
        <li class="list-group-item bg-transparent text-secondary border-secondary"><strong class="text-light">NDVI Crop Health:</strong> Vegetation index time series for agricultural failure early warning.</li>
        <li class="list-group-item bg-transparent text-secondary border-secondary"><strong class="text-light">Spatio-Temporal Matrix:</strong> Heatmaps tracking space-time crisis propagation across provinces simultaneously.</li>
        <li class="list-group-item bg-transparent text-secondary border-secondary"><strong class="text-light">TSA Diagnostics:</strong> Statistical engine featuring STL decomposition, Matrix Profile anomaly detection, and ML model error metrics.</li>
      </ul>
    </div>
  </div>
</div>

<hr class="section-divider">

## <span class="text-gradient">3. Data Integrity & Reporting</span>

<div class="row g-4 mb-5">
  <div class="col-md-6">
    <div class="glass-card card-border-top-info h-100 p-4">
      <h5 class="font-weight-bold text-light mb-2">🔍 Geographic Data Audit</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;">Clicking any country on the global map opens the <strong>Geographic Audit Modal</strong> — a real-time completeness dashboard that verifies data availability rates for CHIRPS, ACLED, and WFP coverage before launching full country diagnostics. Analysts see exactly what data is present before committing to an analysis.</p>
    </div>
  </div>
  <div class="col-md-6">
    <div class="glass-card card-border-top-success h-100 p-4">
      <h5 class="font-weight-bold text-light mb-2">📦 Unified JSZip Master Export</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;">A one-click master export tool (<code>Save All Country HTML</code>) powered by JSZip compiles all country charts, market time series, and sub-tab dashboards into a single organised ZIP package in under a second — ready for offline briefings and field reporting.</p>
    </div>
  </div>
</div>


