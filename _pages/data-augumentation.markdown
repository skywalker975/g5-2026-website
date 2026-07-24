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

<!-- Data Preprocessing & Robust KNN Imputation Workflow -->
<h4 class="text-primary fw-bold mb-2 mt-4">Data Preprocessing & Robust KNN Imputation Workflow</h4>
<p class="text-muted mb-4">
    Before clustering, the dataset undergoes a rigorous preparation pipeline. This process eliminates redundant features through multicollinearity screening and imputes missing values using a distance-weighted KNN framework to preserve variance and statistical integrity:
</p>

<div class="container mt-4">
    <div class="row">
        <!-- Step 1 Card: Feature Selection & Multicollinearity -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-primary">
                <div class="card-body">
                    <h4 class="card-title text-primary">
                        <i class="fas fa-filter me-2"></i> STEP 1: FEATURE SELECTION
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">VIF Screening & Multicollinearity Analysis</h6>
                    <ul class="list-unstyled mb-0 card-text text-muted">
                        <li class="mb-3">
                            <strong class="text-dark">Multicollinearity Screening:</strong><br>
                            Evaluates metrics such as Variance Inflation Factor (VIF) to detect highly redundant statistical features (e.g., overlapping AR1 coefficients).
                        </li>
                        <li class="mb-3">
                            <strong class="text-dark">Distance Distortion Prevention:</strong><br>
                            Eliminates correlated variables that would artificially inflate specific weights during distance metric calculations.
                        </li>
                        <li>
                            <strong class="text-dark">Refined Target Subset:</strong><br>
                            Isolates independent <code>target_columns</code> to ensure every feature delivers a unique, distinct behavioral signal.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
<!-- Step 2 Card: Robust KNN Imputation -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-danger">
                <div class="card-body">
                    <h4 class="card-title text-danger">
                        <i class="fas fa-network-wired me-2"></i> STEP 2: ROBUST KNN IMPUTATION
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Distance-Weighted Mathematical Pipeline</h6>
                    <ul class="list-unstyled mb-0 card-text text-muted">
                        <li class="mb-3">
                            <strong class="text-dark">Forward & Inverse Z-Score Scaling:</strong><br>
                            Standardizes data prior to Euclidean distance calculations, seamlessly transforming back to original physical metrics post-imputation.
                        </li>
                        <li class="mb-3">
                            <strong class="text-dark">Dynamic Neighbor Scaling:</strong><br>
                            Adjusts neighbor counts on the fly (<code>min(n_neighbors, Rows_available)</code>) to prevent execution crashes on small regional splits.
                        </li>
                        <li>
                            <strong class="text-dark">Distance-Weighted Coordinates:</strong><br>
                            Applies <code>weights='distance'</code> so closer behavioral profiles exert a stronger mathematical influence than distant ones.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
