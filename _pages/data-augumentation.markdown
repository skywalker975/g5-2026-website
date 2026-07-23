---
layout: default
title: "Data augumentation"
permalink: /data-augumentation.html
show_sidetoc: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Data augumentation"
subtitle: "Handling missing data"
---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>

<!-- Sub-section: Feature Selection & Imputation Methodology -->
<div class="container mt-5">

<h1 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">Data Preprocessing & Feature Refinement</h1>

<p class="text-muted">Prior to handling missing values, the feature space is refined to eliminate information redundancy. Strong correlations among statistical indicators can artificially distort distance metrics. By applying <strong>Principal Component Analysis (PCA)</strong> to a specific subset of variables, dimensionality is reduced by extracting principal components that capture maximum variance, ensuring distinct, noise-free behavioral signals for the model.</p>


<div class="mt-3">
  <h4 class="h6 text-secondary fw-bold mb-2">Focus on Event & Conflict Datasets</h4>
  <p class="text-muted">
    The core feature selection effort focused on normalized indicators from <strong>GDELT</strong> and <strong>ACLED conflict data</strong>. Because these datasets track heavily overlapping socio-political events, raw features exhibited severe cross-correlation and multicollinearity. Applying PCA to this specific subgroup allowed us to compress highly collinear event signals into orthogonal principal components, stripping out redundancy while fully retaining the underlying intensity of regional conflicts.
  </p>
</div>

<hr class="section-divider">

<!-- Evaluated Imputation Methodologies Section -->
<div class="card hero-card card-border-top-primary mt-2 mb-4">
  <div class="card-body">
    
<!-- Intestazione principale -->
<h4 class="card-title text-primary mb-2">
      <i class="fas fa-calculator me-4"></i>Evaluated Imputation Methodologies
    </h4>
    <p class="card-text text-muted mb-4">
      To fill missing data without distorting regional variance, several structural and spatial approaches were evaluated against a distance-based behavioral pipeline:
    </p>

<!-- Griglia delle 3 Card Methodologies -->
<div class="row align-items-stretch">

<!-- Card 1: Mean/Median Imputation -->
<div class="col-md-4 mb-3 mb-md-0">
        <div class="card h-100 hero-card card-border-top-danger shadow-sm">
          <div class="card-body d-flex flex-column p-4">
            
<h5 class="card-title text-danger mb-3 d-flex align-items-start" style="min-height: 3rem;">
              <i class="fas fa-chart-line me-4 mt-1"></i>
              <span>Mean / Median Imputation</span>
            </h5>
            
<p class="card-text text-muted mb-4">
              Fills missing values using the global or regional average.
            </p>
            
<div class="mt-auto pt-3 border-top">
              <p class="mb-2 text-muted">
                <i class="fas fa-circle-xmark text-danger me-4"></i><b>Limitation:</b> Artificially flattens natural variance and destroys critical spatial dynamics.
              </p>
              <p class="mb-0 text-muted">
                <i class="fas fa-ban text-danger me-4"></i><b>Status:</b> Rejected due to heavy statistical distortion.
              </p>
            </div>

</div>
    </div>
      </div>

<!-- Card 2: Lat/Long Spatial Coordinates -->
<div class="col-md-4 mb-3 mb-md-0">
        <div class="card h-100 hero-card card-border-top-warning shadow-sm">
          <div class="card-body d-flex flex-column p-4">
            
<h5 class="card-title text-warning mb-3 d-flex align-items-start" style="min-height: 3rem;">
              <i class="fas fa-location-dot me-4 mt-1"></i>
              <span>Admin 1 Lat/Long Coordinates</span>
            </h5>
            
<p class="card-text text-muted mb-4">
              Imputes values using pure geographic proximity (latitude and longitude centroids at Admin 1 level).
            </p>
            
<div class="mt-auto pt-3 border-top">
              <p class="mb-2 text-muted">
                <i class="fas fa-triangle-exclamation text-warning me-4"></i><b>Limitation:</b> Geographic proximity alone fails to capture non-spatial economic or conflict drivers.
              </p>
              <p class="mb-0 text-muted">
                <i class="fas fa-ban text-warning me-4"></i><b>Status:</b> Yielded lower clustering validation scores.
              </p>
            </div>

</div>
    </div>
      </div>

<!-- Card 3: Distance-Weighted KNN -->
<div class="col-md-4 mb-0">
        <div class="card h-100 hero-card card-border-top-success shadow-sm">
          <div class="card-body d-flex flex-column p-4">
            
<h5 class="card-title text-success mb-3 d-flex align-items-start" style="min-height: 3rem;">
              <i class="fas fa-network-wired me-4 mt-1"></i>
              <span>Distance-Weighted KNN</span>
            </h5>
            
<p class="card-text text-muted mb-4">
              Leverages non-missing statistical profiles across indicators to find true behavioral neighbors.
            </p>
            
<div class="mt-auto pt-3 border-top">
              <p class="mb-2 text-muted">
                <i class="fas fa-circle-check text-success me-4"></i><b>Advantage:</b> Preserves variance while weighting closest statistical matches more heavily.
              </p>
              <p class="mb-0 text-muted">
                <i class="fas fa-trophy text-success me-4"></i><b>Status:</b> Selected — achieved the highest <b>Silhouette Score</b>.
              </p>
            </div>

</div>
    </div>
      </div>

</div>

  </div>
</div>

<hr class="section-divider">

<!-- Implementation Details -->
<div class="card hero-card card-border-top-primary mt-2 mb-4">
<div class="card-body">
<h4 class="card-title text-primary"><i class="fas fa-shield-halved me-2"></i>Why This KNN Pipeline is Optimal</h4>
<p class="card-text text-muted">Beyond maximizing the Silhouette Score, the custom execution pipeline guarantees stability across sparse humanitarian datasets:</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-3"><i class="fas fa-layer-group text-primary me-2"></i><b>Safe Grouping & Fallbacks:</b> Prevents execution crashes during group-by operations (e.g., country-by-country) by detecting and skipping fully missing (all-<code>NaN</code>) indicator columns.</li>
<li class="mb-3"><i class="fas fa-sliders text-primary me-2"></i><b>Dynamic Neighbor Rescaling:</b> Automatically adjusts neighbor count <code>Neighbors = min(n_neighbors, Rows_available)</code> when a specific administrative group contains fewer records than requested.</li>
<li class="mb-0"><i class="fas fa-scale-balanced text-primary me-2"></i><b>Forward & Inverse Z-Score Scaling:</b> Standardizes features before computing Euclidean distances so large scales do not dominate, then seamlessly converts back to original physical metrics post-imputation.</li>
</ul>
</div>
</div>
