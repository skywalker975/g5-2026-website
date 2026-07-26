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
