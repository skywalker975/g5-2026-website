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


<!-- Data Preprocessing & Feature Refinement Header -->
<h4 class="text-primary fw-bold mb-2 mt-4">Data Preprocessing & Feature Refinement</h4>
<p class="text-muted mb-4">
    Prior to handling missing values, the joint feature space across ACTED, GDELT/ACLED, and Rainfall/Floods datasets is refined through targeted Principal Component Analysis (PCA) to resolve severe domain multicollinearity and ensure structural clustering stability.
</p>

<div class="container mt-4">
    <div class="row">
        <!-- Unified Card: Dimensionality Reduction & Domain Feature Decoupling -->
        <div class="col-12 mb-4">
            <div class="card hero-card card-border-top-primary">
                <div class="card-body">
                    <h4 class="card-title text-primary mb-3">
                        <i class="fas fa-compress-arrows-alt me-2"></i> FEATURE REFINEMENT & DOMAIN DECOUPLING
                    </h4>
                    <div class="row">
                        <!-- Column 1: Theoretical & Geometric Rationale -->
                        <div class="col-md-6">
                            <h6 class="text-dark fw-bold border-bottom pb-2 mb-3">
                                <i class="fas fa-calculator me-2 text-primary"></i> Distance & Geometry Protection
                            </h6>
                            <ul class="list-unstyled card-text text-muted">
                                <li class="mb-3">
                                    <strong class="text-dark">Multicollinearity Mitigation:</strong><br>
                                    Eliminates artificial over-weighting of repetitive variables, preventing severe warping of the Euclidean distance space in downstream algorithms.
                                </li>
                                <li class="mb-3">
                                    <strong class="text-dark">Isotropic Projection:</strong><br>
                                    Transforms cross-correlated axes into orthogonal, uncorrelated components that capture maximum variance while stripping redundant noise.
                                </li>
                                <li class="mb-3">
                                    <strong class="text-dark">Cluster Explainability:</strong><br>
                                    Stabilizes cluster boundaries against local fluctuations, ensuring distinct and highly interpretable drivers within each identified group.
                                </li>
                            </ul>
                        </div>
<!-- Column 2: Application to Specific Datasets -->
                        <div class="col-md-6 border-start-md">
                            <h6 class="text-dark fw-bold border-bottom pb-2 mb-3">
                                <i class="fas fa-layer-group me-2 text-primary"></i> Domain Application (Conflict & Climate)
                            </h6>
                            <ul class="list-unstyled card-text text-muted">
                                <li class="mb-3">
                                    <strong class="text-dark">Subgroup Decoupling:</strong><br>
                                    Applies PCA independently within isolated conflict (GDELT, ACLED) and environmental (ACTED, Rainfall/Floods) subgroups to avoid cross-contaminating domain semantics.
                                </li>
                                <li class="mb-3">
                                    <strong class="text-dark">Signal Compression:</strong><br>
                                    Compresses highly collinear event-tracking indicators into lean, orthogonal features prior to missing value imputation.
                                </li>
                                <li class="mb-3">
                                    <strong class="text-dark">Intensity Retention:</strong><br>
                                    Strips out spatial and temporal redundancy while fully preserving the underlying magnitude and severity of regional events.
                                </li>
                            </ul>
                        </div>
                    </div>

</div>
</div>
</div>
</div>
</div>

<!-- Overall Analytical Pipeline Workflow -->
<h4 class="text-primary fw-bold mb-2 mt-4">Analytical Pipeline: Feature-Based Clustering & Optimal Imputation</h4>
<p class="text-muted mb-4">
    To extract meaningful regional profiles without raw time-series noise, the workflow compresses dynamic data into statistical fingerprints, benchmarks two spatial scenarios across dual clustering strategies, and resolves data gaps using an optimal imputation pipeline:
</p>

<div class="container mt-4">
    <div class="row">
        <!-- Step 1 Card: Feature-Based Clustering & Spatial Scenarios -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-primary">
                <div class="card-body">
                    <h4 class="card-title text-primary">
                        <i class="fas fa-cubes me-2"></i> STEP 1: CLUSTERING & SPATIAL EXPERIMENTS
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Feature Fingerprints & Algorithmic Validation</h6>
                    <ul class="list-unstyled mb-0 card-text text-muted">
                        <li class="mb-3">
                            <strong class="text-dark">Temporal Fingerprinting:</strong><br>
                            Compresses raw sequences into statistical descriptors, ensuring phase invariance, noise filtering, and extreme dimensionality reduction.
                        </li>
                        <li class="mb-3">
                            <strong class="text-dark">Dual Data Scenarios:</strong><br>
                            Compares <strong>Scenario A</strong> (pure behavioral data) against <strong>Scenario B</strong> (behavioral data + Lat/Long) to isolate spatial proximity effects.
                        </li>
                        <li>
                            <strong class="text-dark">Cross-Algorithmic Validation:</strong><br>
                            Benchmarks <strong>Hierarchical (Bottom-Up)</strong> tree-building against <strong>K-Means (Center-Out)</strong> centroid assignment across both scenarios.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
 <!-- Step 2 Card: Optimal Distance-Weighted Imputation -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-danger">
                <div class="card-body">
                    <h4 class="card-title text-danger">
                        <i class="fas fa-network-wired me-2"></i> STEP 2: OPTIMAL KNN IMPUTATION
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Distance-Weighted Post-Restructuring Pipeline</h6>
                    <ul class="list-unstyled mb-0 card-text text-muted">
                        <li class="mb-3">
                            <strong class="text-dark">Z-Score Scale Invariance:</strong><br>
                            Applies forward Z-score standardization before distance calculations and inverse scales post-imputation back to physical units.
                        </li>
                        <li class="mb-3">
                            <strong class="text-dark">Dynamic Group Safety:</strong><br>
                            Handles regional group-by execution safely with all-<code>NaN</code> column fallbacks and dynamic neighbor rescaling (<code>min(n_neighbors, Rows_available)</code>).
                        </li>
                        <li>
                            <strong class="text-dark">Behavioral Coordinate Weights:</strong><br>
                            Uses <code>weights='distance'</code> to ensure highly similar statistical profiles exert proportional mathematical influence over missing values.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
