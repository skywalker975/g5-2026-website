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

<h3 class="text-primary mb-3"><i class="fas fa-filter"></i> Data Preprocessing & Feature Refinement</h3>
<p class="text-muted">Prior to handling missing values, the feature space is refined to eliminate information redundancy. Strong correlations among statistical indicators can artificially distort distance metrics. By applying **Principal Component Analysis (PCA)** to a specific subset of variables, dimensionality is reduced by extracting principal components that capture maximum variance, ensuring distinct, noise-free behavioral signals for the model.</p>


<div class="mt-3">
  <h4 class="h6 text-secondary fw-bold mb-2">Focus on Event & Conflict Datasets</h4>
  <p class="text-muted">
    The core feature selection effort focused on normalized indicators from <strong>GDELT</strong> and <strong>ACLED conflict data</strong>. Because these datasets track heavily overlapping socio-political events, raw features exhibited severe cross-correlation and multicollinearity. Applying PCA to this specific subgroup allowed us to compress highly collinear event signals into orthogonal principal components, stripping out redundancy while fully retaining the underlying intensity of regional conflicts.
  </p>
</div>

<h3 class="text-primary mt-4 mb-3"><i class="fas fa-calculator"></i> Evaluated Imputation Methodologies</h3>
<p class="text-muted">To fill missing data without distorting regional variance, several structural and spatial approaches were evaluated against a distance-based behavioral pipeline:</p>

<div class="row">

<!-- Card 1: Mean/Median Imputation -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-danger">
<div class="card-body">
<h4 class="card-title text-danger"><i class="fas fa-chart-line-down"></i> Mean / Median Imputation</h4>
<p class="card-text text-muted">Fills missing values using the global or regional average.</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-times-circle text-danger me-2"></i><b>Limitation:</b> Artificially flattens natural variance and destroys critical spatial dynamics.</li>
<li><i class="fas fa-ban text-danger me-2"></i><b>Status:</b> Rejected due to heavy statistical distortion.</li>
</ul>
</div>
</div>
</div>

<!-- Card 2: Lat/Long Spatial Coordinates -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-warning">
<div class="card-body">
<h4 class="card-title text-warning"><i class="fas fa-location-dot"></i> Admin 1 Lat/Long Coordinates</h4>
<p class="card-text text-muted">Imputes values using pure geographic proximity (latitude and longitude centroids at Admin 1 level).</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-exclamation-triangle text-warning me-2"></i><b>Limitation:</b> Geographic proximity alone fails to capture non-spatial economic or conflict drivers.</li>
<li><i class="fas fa-ban text-warning me-2"></i><b>Status:</b> Yielded lower clustering validation scores.</li>
</ul>
</div>
</div>
</div>

<!-- Card 3: Selected Strategy - Behavioral KNN -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-success">
<div class="card-body">
<h4 class="card-title text-success"><i class="fas fa-network-wired"></i> Distance-Weighted KNN</h4>
<p class="card-text text-muted">Leverages non-missing statistical profiles across indicators to find true behavioral neighbors.</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-check-circle text-success me-2"></i><b>Advantage:</b> Preserves variance while weighting closest statistical matches more heavily.</li>
<li><i class="fas fa-trophy text-success me-2"></i><b>Status:</b> Selected — achieved the highest <b>Silhouette Score</b>.</li>
</ul>
</div>
</div>
</div>

</div>

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
