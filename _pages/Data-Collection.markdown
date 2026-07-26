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


#### HERO Dataset: Sources and Methodology
* ACLED: Powered by ACLED conflict logs matched with IPC hunger data, this pipeline measures how local violence directly drives food shortages. The method aggregates raw records of violent events and casualties, mapping them directly onto regional food security levels to create a single, unified dataset. The purpose is to reveal the exact link between armed conflict and rising hunger, giving AI models the conflict signals needed to catch emerging crisis hotspots early.
The purpose is to feed machine learning models with clear conflict signals, helping analysts measure how localized violence directly drives food crisis severity and population displacement.
* IPC: This pipeline collects official data from IPC (ipcinfo.org) on
Acute Food Insecurity analyses (2011–2026).
The method follows a two-stage automated process: first mapping and 
deduplicating report URLs, then extracting Key Results text and
downloading PDFs—automatically separating full reports from summary
snapshots. The purpose is to build a qualitative text corpus to
identify food crisis drivers and perform semantic comparisons across
different emergency contexts.
* WFP:
* IDP:
* RAINFALL: This pipeline collects subnational dekadal rainfall data
from HDX/CHIRPS (data.humdata.org) via HDXRainfallLoader.
The method automatically fetches the full historical -subnat-full
csv resource for each country and organizes it into structured local
directories (data/raw_rainfall/).
The purpose is to supply quantitative precipitation metrics to
support food security risk analysis and early-warning modeling.
* NDVI: Driven by data from WFP via the HDX platform, this pipeline  gathers subnational NDVI (Normalized Difference Vegetation Index) metrics to gauge plant growth and biomass density.
The method leverages the hdx-python-api to pull and structure full historical vegetation series directly into a unified dataset.
The purpose is to provide clear environmental signals on drought, crop stress, and agricultural health—giving early-warning models the physical data needed to anticipate food shortages before they escalate.
* GDELT: Sourced from the GDELT Project via Google BigQuery, this pipeline monitors global news coverage to capture real-time media signals on conflict, protests, and humanitarian responses. The method queries daily partitioned event tables and categorizes geopolitical actions using the CAMEO taxonomy to structure raw news data. The purpose is to provide early, near-real-time indicators of instability that often lead to food shortages, filling the time gap before official, structured field reports are published.


The <b>HERO</b> system organizes humanitarian data and its analytical components around a unified, ready-to-use structure. The framework combines various dimensions of risk (IPC, conflict, displacement, meteorological data, market prices, media signals, and vegetation health) by directly aligning them with food security assessment periods.

<div class="container mt-4">
<div class="row">

<!-- Evaluated Imputation Methodologies Section -->
<div class="card hero-card card-border-top-primary mt-2 mb-4">
  <div class="card-body">
    
<!-- Intestazione principale -->
  <h4 class="card-title text-primary mb-2 d-flex align-items-center">
      <span class="d-inline-flex justify-content-center me-3" style="width: 28px;">
        <i class="fas fa-calculator"></i>
      </span>
      <span>Evaluated Imputation Methodologies</span>
    </h4>
    <p class="card-text text-muted mb-4">
      To fill missing data without distorting regional variance, several structural and spatial approaches were evaluated against a distance-based behavioral pipeline:
    </p>
<!-- Griglia delle 3 Card Methodologies -->
    <div class="row align-items-stretch g-3">

<!-- Card 1: Mean/Median Imputation -->
  <div class="col-md-4 mb-3 mb-md-0">
        <div class="card h-100 hero-card card-border-top-danger shadow-sm">
          <div class="card-body d-flex flex-column p-4">
            
  <!-- Titolo della Card -->
  <div class="d-flex align-items-start mb-3" style="min-height: 3.2rem;">
              <span class="d-inline-flex justify-content-center me-3 mt-1" style="width: 24px; flex-shrink: 0;">
                <i class="fas fa-chart-line text-danger fs-5"></i>
              </span>
              <h5 class="card-title text-danger mb-0 fw-bold">Mean / Median Imputation</h5>
            </div>
            
<!-- Descrizione -->
  <p class="card-text text-muted mb-4 flex-grow-1">
              Fills missing values using the global or regional average.
            </p>
            
  <!-- Blocco inferiore allineato -->
  <div class="mt-auto pt-3 border-top">
              <div class="d-flex align-items-start mb-2">
                <span class="d-inline-flex justify-content-center me-3 mt-1" style="width: 24px; flex-shrink: 0;">
                  <i class="fas fa-circle-xmark text-danger fs-6"></i>
                </span>
                <div class="text-muted small">
                  <b>Limitation:</b> Artificially flattens natural variance and destroys critical spatial dynamics.
                </div>
              </div>
              <div class="d-flex align-items-start">
                <span class="d-inline-flex justify-content-center me-3 mt-1" style="width: 24px; flex-shrink: 0;">
                  <i class="fas fa-ban text-danger fs-6"></i>
                </span>
                <div class="text-muted small">
                  <b>Status:</b> Rejected due to heavy statistical distortion.
                </div>
              </div>
            </div>

  </div>
        </div>
      </div>
<!-- Card 2: Lat/Long Spatial Coordinates -->
      <div class="col-md-4 mb-3 mb-md-0">
        <div class="card h-100 hero-card card-border-top-warning shadow-sm">
          <div class="card-body d-flex flex-column p-4">
            
  <!-- Titolo della Card -->
  <div class="d-flex align-items-start mb-3" style="min-height: 3.2rem;">
              <span class="d-inline-flex justify-content-center me-3 mt-1" style="width: 24px; flex-shrink: 0;">
                <i class="fas fa-location-dot text-warning fs-5"></i>
              </span>
              <h5 class="card-title text-warning mb-0 fw-bold">Admin 1 Lat/Long Coordinates</h5>
            </div>
            
<!-- Descrizione -->
   <p class="card-text text-muted mb-4 flex-grow-1">
              Imputes values using pure geographic proximity (latitude and longitude centroids at Admin 1 level).
            </p>
            
<!-- Blocco inferiore allineato -->
  <div class="mt-auto pt-3 border-top">
              <div class="d-flex align-items-start mb-2">
                <span class="d-inline-flex justify-content-center me-3 mt-1" style="width: 24px; flex-shrink: 0;">
                  <i class="fas fa-triangle-exclamation text-warning fs-6"></i>
                </span>
                <div class="text-muted small">
                  <b>Limitation:</b> Geographic proximity alone fails to capture non-spatial economic or conflict drivers.
                </div>
              </div>
              <div class="d-flex align-items-start">
                <span class="d-inline-flex justify-content-center me-3 mt-1" style="width: 24px; flex-shrink: 0;">
                  <i class="fas fa-ban text-warning fs-6"></i>
                </span>
                <div class="text-muted small">
                  <b>Status:</b> Yielded lower clustering validation scores.
                </div>
              </div>
            </div>

  </div>
        </div>
      </div>

<!-- Card 3: Distance-Weighted KNN -->
<div class="col-md-4 mb-0">
        <div class="card h-100 hero-card card-border-top-success shadow-sm">
          <div class="card-body d-flex flex-column p-4">
            
<!-- Titolo della Card -->
  <div class="d-flex align-items-start mb-3" style="min-height: 3.2rem;">
              <span class="d-inline-flex justify-content-center me-3 mt-1" style="width: 24px; flex-shrink: 0;">
                <i class="fas fa-network-wired text-success fs-5"></i>
              </span>
              <h5 class="card-title text-success mb-0 fw-bold">Distance-Weighted KNN</h5>
            </div>
            
  <!-- Descrizione -->
  <p class="card-text text-muted mb-4 flex-grow-1">
              Leverages non-missing statistical profiles across indicators to find true behavioral neighbors.
            </p>
            
  <!-- Blocco inferiore allineato -->
  <div class="mt-auto pt-3 border-top">
              <div class="d-flex align-items-start mb-2">
                <span class="d-inline-flex justify-content-center me-3 mt-1" style="width: 24px; flex-shrink: 0;">
                  <i class="fas fa-circle-check text-success fs-6"></i>
                </span>
                <div class="text-muted small">
                  <b>Advantage:</b> Preserves variance while weighting closest statistical matches more heavily.
                </div>
              </div>
              <div class="d-flex align-items-start">
                <span class="d-inline-flex justify-content-center me-3 mt-1" style="width: 24px; flex-shrink: 0;">
                  <i class="fas fa-trophy text-success fs-6"></i>
                </span>
                <div class="text-muted small">
                  <b>Status:</b> Selected — achieved the highest <b>Silhouette Score</b>.
                </div>
              </div>
            </div>

  </div>
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
