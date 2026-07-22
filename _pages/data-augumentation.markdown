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
<p class="text-muted">Before addressing missing values, the feature space is refined to eliminate redundancy. High correlation between statistical indicators can artificially inflate their weight during distance calculations. A rigorous multicollinearity screening (VIF analysis) isolates a final subset of independent features, ensuring every metric provides a distinct behavioral signal to the model.</p>

<h3 class="text-primary mt-4 mb-3"><i class="fas fa-calculator"></i> Evaluated Imputation Methodologies</h3>
<p class="text-muted">To fill missing data without distorting regional variance, several standard approaches were evaluated against a distance-based pipeline:</p>

<div class="row">

<!-- Card 1: Mean/Median Imputation -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-danger">
<div class="card-body">
<h4 class="card-title text-danger"><i class="fas fa-chart-line-down"></i> Mean / Median Imputation</h4>
<p class="card-text text-muted">Fills missing values using the global or regional average.</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-times-circle text-danger me-2"></i><b>Limitation:</b> Artificially flattens natural variance and destroys spatial dynamics.</li>
<li><i class="fas fa-ban text-danger me-2"></i><b>Status:</b> Rejected due to heavy statistical distortion.</li>
</ul>
</div>
</div>
</div>

<!-- Card 2: Simple Forward/Backward Fill -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-warning">
<div class="card-body">
<h4 class="card-title text-warning"><i class="fas fa-arrows-left-right"></i> Time-Series Propagation</h4>
<p class="card-text text-muted">Propagates the last known observation forward or backward in time.</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-exclamation-triangle text-warning me-2"></i><b>Limitation:</b> Fails when entire baseline periods are missing or during rapid crisis shifts.</li>
<li><i class="fas fa-ban text-warning me-2"></i><b>Status:</b> Insufficient for sparse or irregular assessments.</li>
</ul>
</div>
</div>
</div>

<!-- Card 3: Selected Strategy - KNN -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-success">
<div class="card-body">
<h4 class="card-title text-success"><i class="fas fa-network-wired"></i> Distance-Weighted KNN</h4>
<p class="card-text text-muted">Leverages non-missing statistical profiles to find similar spatial-temporal units.</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-check-circle text-success me-2"></i><b>Advantage:</b> Preserves variance; closer behavioral neighbors exert a stronger influence.</li>
<li><i class="fas fa-star text-success me-2"></i><b>Status:</b> Selected as the core imputation engine.</li>
</ul>
</div>
</div>
</div>

</div>

<!-- Implementation Details -->
<div class="card hero-card card-border-top-primary mt-2 mb-4">
<div class="card-body">
<h4 class="card-title text-primary"><i class="fas fa-shield-halved"></i> Why This KNN Pipeline is Optimal</h4>
<p class="card-text text-muted">Rather than running a naive KNN, the system executes a custom, robust transformation pipeline tailored for regional food security data:</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-layer-group text-primary me-2"></i><b>Safe Grouping & Fallbacks:</b> Prevents execution crashes during group-by operations (e.g., country-by-country) by detecting and skipping fully missing (all-<code>NaN</code>) indicator columns.</li>
<li class="mb-2"><i class="fas fa-sliders text-primary me-2"></i><b>Dynamic Neighbor Rescaling:</b> Automatically adjusts the neighbor count $\text{Neighbors}_{\text{actual}} = \min(n_{\text{neighbors}}, \text{Rows}_{\text{available}})$ when a specific country or administrative group contains fewer records than required.</li>
<li class="mb-2"><i class="fas fa-scale-balanced text-primary me-2"></i><b>Forward & Inverse Z-Score Scaling:</b> Standardizes features before computing Euclidean distances so large scales do not dominate, then seamlessly converts back to original physical metrics post-imputation.</li>
</ul>
</div>
</div>

</div>
