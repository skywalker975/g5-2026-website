---
layout: default
title: "GLOBAL IPC TREND DASHBOARD"
permalink: /UI.html
show_sidetoc: true
header_type: hero
header_img: assets/images/header_ui_dash.jpg
header_title: "GLOBAL IPC TREND DASHBOARD"
---


<h1 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">1. Introduction & System Philosophy</h1>


<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The HERO v6 User Interface (UI) is an interactive dashboard designed to track real-time global crises. It monitors key risk factors—such as humanitarian emergencies, food insecurity, armed conflicts, price inflation, and extreme weather—across 53 high-risk countries, with deep data tracking for 20 key pilot nations.
</p>

<div class="row g-4 my-3">
  <div class="col-md-6">
    <div class="glass-card card-border-top-info h-100">
      <div class="badge-premium-admin1 mb-2">Design & Usability</div>
      <h4 class="font-weight-bold text-gradient mb-2">Built for Control Rooms</h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">It features a modern Dark Mode design (Glassmorphism) optimized for operational centers. It reduces eye strain and makes dense geospatial map data fast and easy to analyze.</p>
    </div>
  </div>
  <div class="col-md-6">
    <div class="glass-card card-border-top-warning h-100">
      <div class="badge-premium-admin2 mb-2">Architecture & Performance</div>
      <h4 class="font-weight-bold text-gradient mb-2">100% Local & Offline</h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">Every component is fast and responsive with smooth micro-animations. The system runs completely offline on a local Python HTTP server without needing containers or complex setups.</p>
    </div>
  </div>
</div>

<h2 class="font-weight-bold text-gradient mb-3 mt-5">2. Navigation Architecture: The 8 Main Views</h2>
<p class="text-secondary mb-4">
  The left sidebar is the core navigation pillar. It lets you switch instantly between 8 key operational views, each dedicated to a specific layer of analysis:
</p>

<!-- Grid Container -->
<div class="row g-4 mb-5">

  <!-- Card 1 -->
  <div class="col-md-6">
    <div class="glass-card card-border-top-secondary h-100">
      <h4 class="font-weight-bold d-flex align-items-center gap-2 mb-3" style="color: #a5b4fc;">
        🌍 Global Overview <code style="font-size: 0.8rem; background: rgba(99, 102, 241, 0.2); color: #a5b4fc; padding: 2px 8px; border-radius: 6px;">global</code>
      </h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">
        Worldwide overview featuring interactive SVG maps and real-time risk rankings across all monitored regions.
      </p>
    </div>
  </div>

  <!-- Card 2 -->
  <div class="col-md-6">
    <div class="glass-card card-border-top-warning h-100">
      <h4 class="font-weight-bold d-flex align-items-center gap-2 mb-3" style="color: #fde047;">
        📍 Country Detail <code style="font-size: 0.8rem; background: rgba(245, 158, 11, 0.2); color: #fde047; padding: 2px 8px; border-radius: 6px;">country</code>
      </h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">
        In-depth analytical suite equipped with 11 specialized sub-sections for deep country-level diagnostics.
      </p>
    </div>
  </div>

  <!-- Card 3 -->
  <div class="col-md-6">
    <div class="glass-card card-border-top-info h-100">
      <h4 class="font-weight-bold d-flex align-items-center gap-2 mb-3" style="color: #60a5fa;">
        ⚖️ Country Comparison <code style="font-size: 0.8rem; background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 2px 8px; border-radius: 6px;">compare</code>
      </h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">
        Dynamic multi-country comparison tools utilizing side-by-side time series and radar charts.
      </p>
    </div>
  </div>

  <!-- Card 4 -->
  <div class="col-md-6">
    <div class="glass-card card-border-top-success h-100">
      <h4 class="font-weight-bold d-flex align-items-center gap-2 mb-3" style="color: #34d399;">
        🗺️ Spatio-Temporal Explorer <code style="font-size: 0.8rem; background: rgba(16, 185, 129, 0.2); color: #34d399; padding: 2px 8px; border-radius: 6px;">spatiotemp</code>
      </h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">
        Dynamic global maps to visualize key thematic indicators over time and space.
      </p>
    </div>
  </div>

  <!-- Card 5 -->
  <div class="col-md-6">
    <div class="glass-card card-border-top-secondary h-100">
      <h4 class="font-weight-bold d-flex align-items-center gap-2 mb-3" style="color: #a5b4fc;">
        📈 Global Time Series (TSA) <code style="font-size: 0.8rem; background: rgba(99, 102, 241, 0.2); color: #a5b4fc; padding: 2px 8px; border-radius: 6px;">tsa-global</code>
      </h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">
        Cross-country time series analysis and trajectory clustering focused on the 20 pilot nations.
      </p>
    </div>
  </div>

  <!-- Card 6 -->
  <div class="col-md-6">
    <div class="glass-card card-border-top-warning h-100">
      <h4 class="font-weight-bold d-flex align-items-center gap-2 mb-3" style="color: #fde047;">
        🧩 Clustering & Patterns <code style="font-size: 0.8rem; background: rgba(245, 158, 11, 0.2); color: #fde047; padding: 2px 8px; border-radius: 6px;">clustering</code>
      </h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">
        Evaluates and compares sub-national clustering strategies to group similar regional profiles.
      </p>
    </div>
  </div>

  <!-- Card 7 -->
  <div class="col-md-6">
    <div class="glass-card card-border-top-info h-100">
      <h4 class="font-weight-bold d-flex align-items-center gap-2 mb-3" style="color: #60a5fa;">
        🕸️ Topological Explorer <code style="font-size: 0.8rem; background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 2px 8px; border-radius: 6px;">tsgraph</code>
      </h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">
        Topological data analysis, correlation networks, and graph structures to detect hidden risk dynamics.
      </p>
    </div>
  </div>

  <!-- Card 8 -->
  <div class="col-md-6">
    <div class="glass-card card-border-top-success h-100">
      <h4 class="font-weight-bold d-flex align-items-center gap-2 mb-3" style="color: #34d399;">
        🔀 Cluster Evolution <code style="font-size: 0.8rem; background: rgba(16, 185, 129, 0.2); color: #34d399; padding: 2px 8px; border-radius: 6px;">clustering-evolution</code>
      </h4>
      <p class="text-secondary mb-0" style="line-height: 1.6;">
        Tracks temporal shifts and transitions using Alluvial diagrams (comparing TF-IDF vs Density models).
      </p>
    </div>
  </div>

</div>


<h2 class="font-weight-bold text-gradient mb-3 mt-5">3. Detailed Breakdown of the Main Views & Sub-Sections</h2>

<!-- 3.1 Vista Panoramica Globale -->
<h3 class="font-weight-bold text-gradient mt-4 mb-3">3.1. Global Overview</h3>

<div class="row g-4 mb-5">
  <div class="col-12">
    <div class="glass-card card-border-top-info">
      <div class="badge-premium-admin1 mb-2">Interactive Map</div>
      <h4 class="font-weight-bold text-gradient mb-2">Interactive World Map</h4>
      <p class="text-secondary mb-0">Displays global risk severity by country. Clicking any nation opens a Geographic Audit Modal to verify data availability before diving into details.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div class="glass-card card-border-top-warning h-100">
      <div class="badge-premium-admin2 mb-2">Risk Matrix</div>
      <h4 class="font-weight-bold text-gradient mb-2">53+ Country Risk Ranking</h4>
      <p class="text-secondary mb-0">A sortable table ranking monitored nations based on combined scores for humanitarian emergencies, conflicts, and climate anomalies.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div class="glass-card card-border-top-secondary h-100">
      <div class="badge-premium-admin1 mb-2">Seasonal Insights</div>
      <h4 class="font-weight-bold text-gradient mb-2">Global Radar Toggle</h4>
      <p class="text-secondary mb-0">Switches the main view to comparative radar charts, highlighting lean seasons and critical seasonal months across all countries.</p>
    </div>
  </div>
</div>

<!-- 3.2 Vista Dettaglio Paese -->
<h3 class="font-weight-bold text-gradient mt-4 mb-3">3.2. Country Detail & Its 11 Sub-Sections</h3>

<p class="text-secondary mb-4">
  Selecting a country loads a dedicated header with key identifiers and grants access to 11 specialized sub-tabs:
</p>

<div class="row g-4 mb-5">

  <div class="col-md-6">
    <div class="glass-card card-border-top-info h-100">
      <div class="badge-premium-admin1 mb-2">Sub-Section 01</div>
      <h4 class="font-weight-bold text-gradient mb-2">Map & Regions</h4>
      <p class="text-secondary mb-0">Interactive sub-regional map (provinces, governorates). Clicking a province filters all national time series to that specific region.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div class="glass-card card-border-top-warning h-100">
      <div class="badge-premium-admin2 mb-2">Sub-Section 02</div>
      <h4 class="font-weight-bold text-gradient mb-2">Charts & Trends</h4>
      <p class="text-secondary mb-0">Aggregated socio-economic stability indicators. Supports switching between linear historical series and 12-month seasonal radar charts.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div class="glass-card card-border-top-secondary h-100">
      <div class="badge-premium-admin1 mb-2">Sub-Section 03</div>
      <h4 class="font-weight-bold text-gradient mb-2">Food Markets & Inflation</h4>
      <p class="text-secondary mb-0">Tracks micro-economic food prices and local inflation with high granularity—from national aggregates down to individual market locations.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div class="glass-card card-border-top-success h-100">
      <div class="badge-premium-admin1 mb-2">Sub-Section 04</div>
      <h4 class="font-weight-bold text-gradient mb-2">Media & News Sentiment</h4>
      <p class="text-secondary mb-0">Monitors media coverage volume against ground events ("forgotten wars") and tracks shifts in global news sentiment over time.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div class="glass-card card-border-top-danger h-100">
      <div class="badge-premium-admin2 mb-2">Sub-Section 05</div>
      <h4 class="font-weight-bold text-gradient mb-2">Food Insecurity (IPC)</h4>
      <p class="text-secondary mb-0">Monitors official food security crisis levels, tracking populations in acute phases to project emergency aid requirements.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div class="glass-card card-border-top-info h-100">
      <div class="badge-premium-admin1 mb-2">Sub-Section 06</div>
      <h4 class="font-weight-bold text-gradient mb-2">Conflict & Security Events</h4>
      <p class="text-secondary mb-0">Geolocated tracking of armed conflict, civilian violence, and security incidents to assess risks along humanitarian supply corridors.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div class="glass-card card-border-top-warning h-100">
      <div class="badge-premium-admin2 mb-2">Sub-Section 07</div>
      <h4 class="font-weight-bold text-gradient mb-2">Displaced Persons & Refugees</h4>
      <p class="text-secondary mb-0">Tracks population displacement flows (IDPs and refugees) and maps demographic pressure on host communities and camps.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div class="glass-card card-border-top-secondary h-100">
      <div class="badge-premium-admin1 mb-2">Sub-Section 08</div>
      <h4 class="font-weight-bold text-gradient mb-2">Rainfall Monitoring</h4>
      <p class="text-secondary mb-0">Satellite-based precipitation tracking to detect agricultural droughts and extreme rainfall events causing flash floods.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div class="glass-card card-border-top-success h-100">
      <div class="badge-premium-admin1 mb-2">Sub-Section 09</div>
      <h4 class="font-weight-bold text-gradient mb-2">Vegetation & Crop Health</h4>
      <p class="text-secondary mb-0">Evaluates crop and pasture health using vegetation indices, providing early warnings for potential harvest failures.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div class="glass-card card-border-top-danger h-100">
      <div class="badge-premium-admin2 mb-2">Sub-Section 10</div>
      <h4 class="font-weight-bold text-gradient mb-2">Spatio-Temporal Matrix</h4>
      <p class="text-secondary mb-0">Heatmaps linking provinces (Y-axis) with time (X-axis) to instantly identify where and when a crisis originated and spread.</p>
    </div>
  </div>

  <div class="col-12">
    <div class="glass-card card-border-top-info">
      <div class="badge-premium-admin1 mb-2">Sub-Section 11</div>
      <h4 class="font-weight-bold text-gradient mb-2">TSA Diagnostics & Predictive Modeling</h4>
      <p class="text-secondary mb-0">Advanced statistical engine for the selected area featuring trend-seasonality decomposition, anomaly detection, lag analysis, and Machine Learning predictive model comparisons.</p>
    </div>
  </div>

</div>

---

Explore all the data, Cartesian graphs, geospatial maps, and test the interactive scenario simulator directly on our dashboard:

<div class="text-center my-5">
    <a href="https://github.com/skywalker975/g5-2026-website" class="btn btn-premium-hero btn-lg px-5 py-3 shadow"><i class="fas fa-chart-line mr-2"></i> Explore Dashboard HERO</a>
</div>
