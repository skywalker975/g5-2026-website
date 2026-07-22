---
layout: default
title: "Data collection"
permalink: /Data-collection.html
show_sidetoc: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Data collection"

---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>


### Integrated Datasets and Architecture of HERO

The </b>HERO</b> system organizes humanitarian data and its analytical components around a unified, ready-to-use structure. The framework combines various dimensions of risk (IPC, conflict, displacement, meteorological data, market prices, media signals, and vegetation health) by directly aligning them with food security assessment periods.



---
<div class="container mt-4">
<div class="row">

<!-- Card 1: Unit of Analysis -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-primary">
<div class="card-body">
<h4 class="card-title text-primary"><i class="fas fa-bullseye"></i> Defining the Unit of Analysis</h4>
<p class="card-text text-muted">Every row in an IPC assessment represents a specific <b>spatial-temporal window</b> that acts as the unique anchor for all analysis:</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-map-marker-alt text-primary me-2"></i><b>Where:</b> A specific administrative region (e.g., Admin 1: <i>Bay Region</i> or Admin 2: <i>Baidoa District</i>).</li>
<li><i class="fas fa-calendar-alt text-primary me-2"></i><b>When:</b> A defined validity period (e.g., <i>Jan 1, 2024 – Mar 31, 2024</i>).</li>
</ul>
</div>
</div>
</div>

<!-- Card 2: Mechanics of LEFT JOIN -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-info">
<div class="card-body">
<h4 class="card-title text-info"><i class="fas fa-diagram-project"></i> Mechanics of the LEFT JOIN</h4>
<p class="card-text text-muted">Secondary drivers (ACLED, IDP, Rainfall, WFP) are attached using a <b>LEFT JOIN</b> where IPC serves as the spine table:</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-check-circle text-success me-2"></i><b>Data Available:</b> Indicators are aggregated to match the IPC time window and area, then merged into the row.</li>
<li><i class="fas fa-times-circle text-warning me-2"></i><b>Data Missing:</b> The IPC row remains intact, and missing indicator columns are populated with <code>NaN</code>.</li>
</ul>
</div>
</div>
</div>

<!-- Card 3: Why This Matters -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-warning">
<div class="card-body">
<h4 class="card-title text-warning"><i class="fas fa-shield-halved"></i> Preventing Bias & Dropped Rows</h4>
<p class="card-text text-muted">Using an <code>INNER JOIN</code> would delete entire IPC rows lacking secondary data, introducing critical hazards:</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-filter-circle-xmark text-danger me-2"></i><b>Selection Bias:</b> Models would only train on regions with rich data, ignoring remote or high-conflict areas.</li>
<li><i class="fas fa-database text-danger me-2"></i><b>Loss of Ground Truth:</b> Preserves <b>100% of target outcomes ($Y$)</b>, isolating missing drivers as <code>NaN</code> for intentional downstream imputation.</li>
</ul>
</div>
</div>
</div>

</div>
</div>
