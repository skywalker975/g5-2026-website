---
layout: default
title: "GLOBAL IPC TREND DASHBOARD"
permalink: /UI.html
show_sidetoc: true
header_type: hero
header_img: assets/images/folium_map.webp
header_title: "GLOBA IPC TREND DASHBOARD"
---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>

<h1 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">Introduction & System Philosophy</h1>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The HERO v6 User Interface (UI) is an interactive dashboard designed to track real-time global crises. It monitors key risk factors—such as humanitarian emergencies, food insecurity, armed conflicts, price inflation, and extreme weather—across 53 high-risk countries, with deep data tracking for 20 key pilot nations.
</p>

<div style="background-color: #e8f4fa; border-left: 5px solid #0284c7; border-radius: 6px; padding: 1.25rem 1.5rem; margin-top: 1.5rem; margin-bottom: 1.25rem;">
<div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #0369a1; margin-bottom: 0.35rem;">Design & Usability</div>
<h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #0369a1;">Built for Control Rooms</h4>
<p class="text-muted mb-0">It features a modern Dark Mode design (Glassmorphism) optimized for operational centers. It reduces eye strain and makes dense geospatial map data fast and easy to analyze.</p>
</div>

<div style="background-color: #fff8e1; border-left: 5px solid #e0a800; border-radius: 6px; padding: 1.25rem 1.5rem; margin-bottom: 1.5rem;">
<div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #a16207; margin-bottom: 0.35rem;">Architecture & Performance</div>
<h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #a16207;">100% Local & Offline</h4>
<p class="text-muted mb-0">Every component is fast and responsive with smooth micro-animations. The system runs completely offline on a local Python HTTP server without needing containers or complex setups.</p>
</div>

<h2 class="font-weight-bold mb-3">2. Navigation Architecture: The 8 Main Views</h2>
<p class="text-muted mb-4">
  The left sidebar is the core navigation pillar. It lets you switch instantly between 8 key operational views, each dedicated to a specific layer of analysis:
</p>

<!-- Grid Container (Bootstrap Row) -->
<div class="row g-4">

  <!-- Card 1 -->
  <div class="col-md-6">
    <div style="background: #ffffff; border-radius: 12px; padding: 1.5rem; border-top: 4px solid #7c3aed; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%;">
      <h4 style="color: #7c3aed; font-weight: 700; display: flex; align-items: center; gap: 8px; margin-bottom: 0.75rem;">
        🌍 Global Overview <code style="font-size: 0.8rem; background: #f3e8ff; color: #7c3aed; padding: 2px 6px; border-radius: 4px;">global</code>
      </h4>
      <p class="text-muted mb-0" style="line-height: 1.6;">
        Worldwide overview featuring interactive SVG maps and real-time risk rankings across all monitored regions.
      </p>
    </div>
  </div>

  <!-- Card 2 -->
  <div class="col-md-6">
    <div style="background: #ffffff; border-radius: 12px; padding: 1.5rem; border-top: 4px solid #ea580c; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%;">
      <h4 style="color: #ea580c; font-weight: 700; display: flex; align-items: center; gap: 8px; margin-bottom: 0.75rem;">
        📍 Country Detail <code style="font-size: 0.8rem; background: #ffedd5; color: #ea580c; padding: 2px 6px; border-radius: 4px;">country</code>
      </h4>
      <p class="text-muted mb-0" style="line-height: 1.6;">
        In-depth analytical suite equipped with 11 specialized sub-sections for deep country-level diagnostics.
      </p>
    </div>
  </div>

  <!-- Card 3 -->
  <div class="col-md-6">
    <div style="background: #ffffff; border-radius: 12px; padding: 1.5rem; border-top: 4px solid #2563eb; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%;">
      <h4 style="color: #2563eb; font-weight: 700; display: flex; align-items: center; gap: 8px; margin-bottom: 0.75rem;">
        ⚖️ Country Comparison <code style="font-size: 0.8rem; background: #dbeafe; color: #2563eb; padding: 2px 6px; border-radius: 4px;">compare</code>
      </h4>
      <p class="text-muted mb-0" style="line-height: 1.6;">
        Dynamic multi-country comparison tools utilizing side-by-side time series and radar charts.
      </p>
    </div>
  </div>

  <!-- Card 4 -->
  <div class="col-md-6">
    <div style="background: #ffffff; border-radius: 12px; padding: 1.5rem; border-top: 4px solid #059669; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%;">
      <h4 style="color: #059669; font-weight: 700; display: flex; align-items: center; gap: 8px; margin-bottom: 0.75rem;">
        🗺️ Spatio-Temporal Explorer <code style="font-size: 0.8rem; background: #d1fae5; color: #059669; padding: 2px 6px; border-radius: 4px;">spatiotemp</code>
      </h4>
      <p class="text-muted mb-0" style="line-height: 1.6;">
        Dynamic global maps to visualize key thematic indicators over time and space.
      </p>
    </div>
  </div>

  <!-- Card 5 -->
  <div class="col-md-6">
    <div style="background: #ffffff; border-radius: 12px; padding: 1.5rem; border-top: 4px solid #7c3aed; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%;">
      <h4 style="color: #7c3aed; font-weight: 700; display: flex; align-items: center; gap: 8px; margin-bottom: 0.75rem;">
        📈 Global Time Series (TSA) <code style="font-size: 0.8rem; background: #f3e8ff; color: #7c3aed; padding: 2px 6px; border-radius: 4px;">tsa-global</code>
      </h4>
      <p class="text-muted mb-0" style="line-height: 1.6;">
        Cross-country time series analysis and trajectory clustering focused on the 20 pilot nations.
      </p>
    </div>
  </div>

  <!-- Card 6 -->
  <div class="col-md-6">
    <div style="background: #ffffff; border-radius: 12px; padding: 1.5rem; border-top: 4px solid #ea580c; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%;">
      <h4 style="color: #ea580c; font-weight: 700; display: flex; align-items: center; gap: 8px; margin-bottom: 0.75rem;">
        🧩 Clustering & Patterns <code style="font-size: 0.8rem; background: #ffedd5; color: #ea580c; padding: 2px 6px; border-radius: 4px;">clustering</code>
      </h4>
      <p class="text-muted mb-0" style="line-height: 1.6;">
        Evaluates and compares sub-national clustering strategies to group similar regional profiles.
      </p>
    </div>
  </div>

  <!-- Card 7 -->
  <div class="col-md-6">
    <div style="background: #ffffff; border-radius: 12px; padding: 1.5rem; border-top: 4px solid #2563eb; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%;">
      <h4 style="color: #2563eb; font-weight: 700; display: flex; align-items: center; gap: 8px; margin-bottom: 0.75rem;">
        🕸️ Topological Explorer <code style="font-size: 0.8rem; background: #dbeafe; color: #2563eb; padding: 2px 6px; border-radius: 4px;">tsgraph</code>
      </h4>
      <p class="text-muted mb-0" style="line-height: 1.6;">
        Topological data analysis, correlation networks, and graph structures to detect hidden risk dynamics.
      </p>
    </div>
  </div>

  <!-- Card 8 -->
  <div class="col-md-6">
    <div style="background: #ffffff; border-radius: 12px; padding: 1.5rem; border-top: 4px solid #059669; box-shadow: 0 4px 12px rgba(0,0,0,0.05); height: 100%;">
      <h4 style="color: #059669; font-weight: 700; display: flex; align-items: center; gap: 8px; margin-bottom: 0.75rem;">
        🔀 Cluster Evolution <code style="font-size: 0.8rem; background: #d1fae5; color: #059669; padding: 2px 6px; border-radius: 4px;">clustering-evolution</code>
      </h4>
      <p class="text-muted mb-0" style="line-height: 1.6;">
        Tracks temporal shifts and transitions using Alluvial diagrams (comparing TF-IDF vs Density models).
      </p>
    </div>
  </div>

</div>




<h2 class="font-weight-bold mb-3">3. Detailed Breakdown of the Main Views & Sub-Sections</h2>

<!-- 3.1 Vista Panoramica Globale -->
<h3 class="font-weight-bold mt-4 mb-3">3.1. Global Overview</h3>

<div class="row g-4 mb-5">
  <div class="col-12">
    <div style="background-color: #e8f4fa; border-left: 5px solid #0284c7; border-radius: 6px; padding: 1.25rem 1.5rem;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #0369a1; margin-bottom: 0.35rem;">Interactive Map</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #0369a1;">Interactive World Map</h4>
      <p class="text-muted mb-0">Displays global risk severity by country. Clicking any nation opens a Geographic Audit Modal to verify data availability before diving into details.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div style="background-color: #fff8e1; border-left: 5px solid #e0a800; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #a16207; margin-bottom: 0.35rem;">Risk Matrix</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #a16207;">53+ Country Risk Ranking</h4>
      <p class="text-muted mb-0">A sortable table ranking monitored nations based on combined scores for humanitarian emergencies, conflicts, and climate anomalies.</p>
    </div>
  </div>

  <div class="col-md-6">
    <div style="background-color: #f3e8ff; border-left: 5px solid #7c3aed; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #6b21a8; margin-bottom: 0.35rem;">Seasonal Insights</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #6b21a8;">Global Radar Toggle</h4>
      <p class="text-muted mb-0">Switches the main view to comparative radar charts, highlighting lean seasons and critical seasonal months across all countries.</p>
    </div>
  </div>
</div>

<!-- 3.2 Vista Dettaglio Paese -->
<h3 class="font-weight-bold mt-4 mb-3">3.2. Country Detail & Its 11 Sub-Sections</h3>

<p class="text-muted mb-4">
  Selecting a country loads a dedicated header with key identifiers and grants access to 11 specialized sub-tabs:
</p>

<div class="row g-4">

  <!-- Sub-tab 1 -->
  <div class="col-md-6">
    <div style="background-color: #e8f4fa; border-left: 5px solid #0284c7; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #0369a1; margin-bottom: 0.35rem;">Sub-Section 01</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #0369a1;">Map & Regions</h4>
      <p class="text-muted mb-0">Interactive sub-regional map (provinces, governorates). Clicking a province filters all national time series to that specific region.</p>
    </div>
  </div>

  <!-- Sub-tab 2 -->
  <div class="col-md-6">
    <div style="background-color: #fff8e1; border-left: 5px solid #e0a800; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #a16207; margin-bottom: 0.35rem;">Sub-Section 02</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #a16207;">Charts & Trends</h4>
      <p class="text-muted mb-0">Aggregated socio-economic stability indicators. Supports switching between linear historical series and 12-month seasonal radar charts.</p>
    </div>
  </div>

  <!-- Sub-tab 3 -->
  <div class="col-md-6">
    <div style="background-color: #f3e8ff; border-left: 5px solid #7c3aed; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #6b21a8; margin-bottom: 0.35rem;">Sub-Section 03</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #6b21a8;">Food Markets & Inflation</h4>
      <p class="text-muted mb-0">Tracks micro-economic food prices and local inflation with high granularity—from national aggregates down to individual market locations.</p>
    </div>
  </div>

  <!-- Sub-tab 4 -->
  <div class="col-md-6">
    <div style="background-color: #ecfdf5; border-left: 5px solid #059669; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #047857; margin-bottom: 0.35rem;">Sub-Section 04</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #047857;">Media & News Sentiment</h4>
      <p class="text-muted mb-0">Monitors media coverage volume against ground events ("forgotten wars") and tracks shifts in global news sentiment over time.</p>
    </div>
  </div>

  <!-- Sub-tab 5 -->
  <div class="col-md-6">
    <div style="background-color: #fff1f2; border-left: 5px solid #e11d48; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #be123c; margin-bottom: 0.35rem;">Sub-Section 05</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #be123c;">Food Insecurity (IPC)</h4>
      <p class="text-muted mb-0">Monitors official food security crisis levels, tracking populations in acute phases to project emergency aid requirements.</p>
    </div>
  </div>

  <!-- Sub-tab 6 -->
  <div class="col-md-6">
    <div style="background-color: #e8f4fa; border-left: 5px solid #0284c7; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #0369a1; margin-bottom: 0.35rem;">Sub-Section 06</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #0369a1;">Conflict & Security Events</h4>
      <p class="text-muted mb-0">Geolocated tracking of armed conflict, civilian violence, and security incidents to assess risks along humanitarian supply corridors.</p>
    </div>
  </div>

  <!-- Sub-tab 7 -->
  <div class="col-md-6">
    <div style="background-color: #fff8e1; border-left: 5px solid #e0a800; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #a16207; margin-bottom: 0.35rem;">Sub-Section 07</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #a16207;">Displaced Persons & Refugees</h4>
      <p class="text-muted mb-0">Tracks population displacement flows (IDPs and refugees) and maps demographic pressure on host communities and camps.</p>
    </div>
  </div>

  <!-- Sub-tab 8 -->
  <div class="col-md-6">
    <div style="background-color: #f3e8ff; border-left: 5px solid #7c3aed; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #6b21a8; margin-bottom: 0.35rem;">Sub-Section 08</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #6b21a8;">Rainfall Monitoring</h4>
      <p class="text-muted mb-0">Satellite-based precipitation tracking to detect agricultural droughts and extreme rainfall events causing flash floods.</p>
    </div>
  </div>

  <!-- Sub-tab 9 -->
  <div class="col-md-6">
    <div style="background-color: #ecfdf5; border-left: 5px solid #059669; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #047857; margin-bottom: 0.35rem;">Sub-Section 09</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #047857;">Vegetation & Crop Health</h4>
      <p class="text-muted mb-0">Evaluates crop and pasture health using vegetation indices, providing early warnings for potential harvest failures.</p>
    </div>
  </div>

  <!-- Sub-tab 10 -->
  <div class="col-md-6">
    <div style="background-color: #fff1f2; border-left: 5px solid #e11d48; border-radius: 6px; padding: 1.25rem 1.5rem; height: 100%;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #be123c; margin-bottom: 0.35rem;">Sub-Section 10</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #be123c;">Spatio-Temporal Matrix</h4>
      <p class="text-muted mb-0">Heatmaps linking provinces (Y-axis) with time (X-axis) to instantly identify where and when a crisis originated and spread.</p>
    </div>
  </div>

  <!-- Sub-tab 11 -->
  <div class="col-12">
    <div style="background-color: #e8f4fa; border-left: 5px solid #0284c7; border-radius: 6px; padding: 1.25rem 1.5rem;">
      <div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #0369a1; margin-bottom: 0.35rem;">Sub-Section 11</div>
      <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #0369a1;">TSA Diagnostics & Predictive Modeling</h4>
      <p class="text-muted mb-0">Advanced statistical engine for the selected area featuring trend-seasonality decomposition, anomaly detection, lag analysis, and Machine Learning predictive model comparisons.</p>
    </div>
  </div>

</div>
