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

<!-- Data Preprocessing & Feature Refinement Workflow -->
<h4 class="text-primary fw-bold mb-2 mt-4">Data Preprocessing & Feature Refinement Workflow</h4>
<p class="text-muted mb-4">
    Prior to handling missing values, the feature space is refined to eliminate information redundancy. This two-step workflow reduces collinearity and implements an optimal imputation pipeline to preserve regional signals without distorting data variance:
</p>

<div class="container mt-4">
    <div class="row">
        <!-- Step 1 Card: Dimensionality Reduction -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-primary">
                <div class="card-body">
                    <h4 class="card-title text-primary">
                        <i class="fas fa-filter me-2"></i> STEP 1: DIMENSIONALITY REDUCTION
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">PCA on Event & Conflict Datasets</h6>
                    <ul class="list-unstyled mb-0 card-text text-muted">
                        <li class="mb-3">
                            <strong class="text-dark">Multicollinearity Mitigation:</strong><br>
                            Targets overlapping socio-political indicators from <code>GDELT</code> and <code>ACLED</code> that artificially distort distance metrics.
                        </li>
                        <li class="mb-3">
                            <strong class="text-dark">Principal Component Analysis:</strong><br>
                            Compresses highly cross-correlated event signals into orthogonal principal components while capturing maximum variance.
                        </li>
                        <li>
                            <strong class="text-dark">Noise-Free Signal Extraction:</strong><br>
                            Strips out statistical redundancy while fully retaining the underlying intensity of regional conflicts.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
 <!-- Step 2 Card: Imputation Strategy -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-danger">
                <div class="card-body">
                    <h4 class="card-title text-danger">
                        <i class="fas fa-network-wired me-2"></i> STEP 2: IMPUTATION STRATEGY
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Distance-Weighted KNN Benchmark</h6>
                    <ul class="list-unstyled mb-0 card-text text-muted">
                        <li class="mb-3">
                            <strong class="text-dark">Baseline Evaluation:</strong><br>
                            Benchmarked simple <code>mean/median</code> and geographic <code>Lat/Long</code> imputation against behavioral statistical profiling.
                        </li>
                        <li class="mb-3">
                            <strong class="text-dark">Distance-Weighted KNN:</strong><br>
                            Selected for achieving the highest <strong>Silhouette Score</strong>, leveraging non-missing profiles to find true behavioral neighbors.
                        </li>
                        <li>
                            <strong class="text-dark">Robust Execution Pipeline:</strong><br>
                            Integrates dynamic neighbor rescaling (<code>n_neighbors</code>), all-<code>NaN</code> column fallbacks, and Z-score standardization.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
