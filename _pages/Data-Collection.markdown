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

The <b>HERO</b> system organizes humanitarian data and its analytical components around a unified, ready-to-use structure. The framework combines various dimensions of risk (IPC, conflict, displacement, meteorological data, market prices, media signals, and vegetation health) by directly aligning them with food security assessment periods.

<div class="container mt-4">
<div class="row">

<!-- Card 1: Unit of Analysis -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-primary">
<div class="card-body">
<h4 class="card-title text-primary"><i class="fas fa-bullseye"></i> The Unit of Analysis</h4>
<p class="card-text text-muted">Every assessment in the analysis relies on a unique combination of <b>space and time</b>. A specific geographic region (such as a province or district) is observed within a defined time frame, establishing the essential anchor around which all other system information revolves.</p>
</div>
</div>
</div>

<!-- Card 2: Mechanics of LEFT JOIN -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-info">
<div class="card-body">
<h4 class="card-title text-info"><i class="fas fa-diagram-project"></i> Data Integration</h4>
<p class="card-text text-muted">All external drivers (conflict, precipitation, markets, and displacement) are attached to this central framework. If information is available for a given driver, it is integrated; if a source lacks data for that period, the primary assessment is still preserved while marking the missing value.</p>
</div>
</div>
</div>

<!-- Card 3: Why This Matters -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-warning">
<div class="card-body">
<h4 class="card-title text-warning"><i class="fas fa-shield-halved"></i> Why It Matters</h4>
<p class="card-text text-muted">Keeping food security assessments at the core prevents dropping remote or conflict-affected regions simply because secondary data is unavailable. This approach ensures complete spatial coverage, leaving the task of reconstructing missing data transparently to downstream steps.</p>
</div>
</div>
</div>


</div>
</div>

---

<div class="comparison-table-wrapper">
    <div class="row text-center mb-3">
        <div class="col-md-6 mb-2">
            <span class="badge-premium-admin1 shadow-sm"><i class="fas fa-layer-group"></i> ADMIN LEVEL 1 (Regional / Provincial)</span>
        </div>
        <div class="col-md-6 mb-2">
            <span class="badge-premium-admin2 shadow-sm"><i class="fas fa-map-pin"></i> ADMIN LEVEL 2 (District / Departmental)</span>
        </div>
    </div>
    <div class="row mt-3">
        <div class="col-md-6 border-right">
            <ul class="lead" style="font-size: 0.95rem; line-height: 1.6;">
                <li><b>Data Size:</b> ~10,024 spatiotemporal observations.</li>
                <li><b>Media Integration (GDELT):</b> Includes media signals and sentiment extracted via GDELT (news tone and salience have historically only been geolocatable at the Admin 1 level).</li>
                <li><b>Preferred Use:</b> Ideal for global macro-clustering, identifying national archetypes, and generalizing predictive models across inter-regional scales.</li>
            </ul>
        </div>
        <div class="col-md-6">
            <ul class="lead" style="font-size: 0.95rem; line-height: 1.6;">
                <li><b>Data Size:</b> ~42,957 observations (4 times more granular).</li>
                <li><b>Media Integration:</b> Does not include GDELT data (news flows are not localized at the district level).</li>
                <li><b>Preferred Use:</b> Perfect for digital micro-mapping, local food security tracking, and detecting micro-anomalies in district-level resilience or vulnerability.</li>
            </ul>
        </div>
    </div>
</div>
