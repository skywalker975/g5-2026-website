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
</div></div>
</div>
</div>

</div>
</div>

---
<div class="comparison-table-wrapper">
    <div class="row text-center mb-3">
        <div class="col-md-6 mb-2">
            <span class="badge-premium-admin1 shadow-sm"><i class="fas fa-layer-group"></i> ADMIN LEVEL 1 (Regionale / Provinciale)</span>
        </div>
        <div class="col-md-6 mb-2">
            <span class="badge-premium-admin2 shadow-sm"><i class="fas fa-map-pin"></i> ADMIN LEVEL 2 (Distrettuale / Dipartimentale)</span>
        </div>
    </div>
    <div class="row mt-3">
        <div class="col-md-6 border-right">
            <ul class="lead" style="font-size: 0.95rem; line-height: 1.6;">
                <li><b>Dimensione Dati:</b> ~10.024 osservazioni spaziotemporali.</li>
                <li><b>Integrazione Media (GDELT):</b> Include i segnali e il sentiment estratti dai media tramite GDELT (il tono e la salienza delle notizie sono storicamente georeferenziabili solo a livello Admin 1).</li>
                <li><b>Uso Prediletto:</b> Ideale per il macro-clustering globale, l'identificazione di archetipi nazionali e la generalizzazione di modelli predittivi su scala inter-regionale.</li>
            </ul>
        </div>
        <div class="col-md-6">
            <ul class="lead" style="font-size: 0.95rem; line-height: 1.6;">
                <li><b>Dimensione Dati:</b> ~42.957 osservazioni (4 volte più granulare).</li>
                <li><b>Integrazione Media:</b> Non include i dati GDELT (i flussi giornalistici non sono localizzati a livello distrettuale).</li>
                <li><b>Uso Prediletto:</b> Perfetto per la micro-cartografia digitale, il tracciamento locale della sicurezza alimentare e la rilevazione di micro-anomalie di resilienza o vulnerabilità distrettuale.</li>
            </ul>
        </div>
    </div>
</div>

