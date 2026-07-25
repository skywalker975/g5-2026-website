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
    Prior to handling missing values, the joint feature space is refined through targeted Principal Component Analysis (PCA) to eliminate domain redundancy, correct distance metrics, and optimize cluster interpretability.
</p>

<div class="container mt-4">
    <div class="row">
        <!-- Unified Feature Refinement Card -->
        <div class="col-12 mb-4">
            <div class="card hero-card card-border-top-primary">
                <div class="card-body">
                    <h4 class="card-title text-primary mb-4">
                        <i class="fas fa-project-diagram me-2"></i> FEATURE REFINEMENT PIPELINE
                    </h4>
                    <div class="row g-4">
                        <!-- Column 1: Subgroup Decoupling -->
                        <div class="col-md-4">
                            <div class="p-3 bg-light rounded h-100 border-start border-3 border-primary">
                                <h6 class="text-dark fw-bold mb-2">
                                    <i class="fas fa-layer-group me-2 text-primary"></i> Subgroup Decoupling
                                </h6>
                                <p class="card-text text-muted small mb-0">
                                    Applies PCA independently within isolated conflict (<strong>GDELT, ACLED</strong>) and environmental (<strong>Rainfall</strong>) subgroups to eliminate domain-specific redundancy without cross-contaminating domain semantics.
                                </p>
                            </div>
                        </div>
<!-- Column 2: Multicollinearity Mitigation -->
                        <div class="col-md-4">
                            <div class="p-3 bg-light rounded h-100 border-start border-3 border-info">
                                <h6 class="text-dark fw-bold mb-2">
                                    <i class="fas fa-drafting-compass me-2 text-info"></i> Multicollinearity Mitigation
                                </h6>
                                <p class="card-text text-muted small mb-0">
                                    Eliminates artificial over-weighting of repetitive variables by projecting correlated signals into orthogonal components, preventing severe warping of the Euclidean distance space.
                                </p>
                            </div>
                        </div>
<!-- Column 3: Cluster Explainability -->
                        <div class="col-md-4">
                            <div class="p-3 bg-light rounded h-100 border-start border-3 border-success">
                                <h6 class="text-dark fw-bold mb-2">
                                    <i class="fas fa-chart-pie me-2 text-success"></i> Cluster Explainability
                                </h6>
                                <p class="card-text text-muted small mb-0">
                                    Stabilizes cluster boundaries against local fluctuations and noise, ensuring distinct, robust, and highly interpretable drivers within each identified group.
                                </p>
                            </div>
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


| **Clustering** | Silhouette indicator |
|---|---|
| K-Means (W/o coordinates) | 0.193 | 
| Hierarchical (W/o coordinates) | 0.172 | 
| K-Means (With coordinates) | 0.166 | 
| Hierarchical (With coordinates) | 0.122 | 


<div class="container mt-4">
    <div class="row">
        <div class="col-lg-10 offset-lg-1">
            <!-- Clean Narrative Container -->
            <div class="p-4 p-md-5 rounded-3 bg-white shadow-sm border-start border-success border-4">
                <!-- Narrative Header -->
                <div class="d-flex align-items-center mb-3">
                    <span class="badge bg-success me-2 px-3 py-2 text-uppercase fs-7">Next Phase</span>
                    <h3 class="fw-bold text-dark mb-0">Step 2: Optimal k-NN Imputation</h3>
                </div>
<p class="lead text-success fw-medium mb-4">
                    Distance-weighted data reconstruction guided by cluster structure and silhouette performance.
                </p>
<!-- Fluid Narrative Body -->
                <div class="text-secondary lh-lg fs-6">
                    <p class="mb-3">
                        Following the clustering phase, silhouette score evaluation identified <strong class="text-dark">k-NN (k-Nearest Neighbors)</strong> as the optimal methodology to drive the reconstruction process. This served as the foundation for designing a distance-weighted post-restructuring imputation pipeline.
                    </p>
                    <p class="mb-3">
                        To prevent scale distortion during distance calculations, the pipeline enforces <strong class="text-dark">Z-Score scale invariance</strong>—applying forward standardization before calculating distances and inversely scaling the imputed values back to their original physical units upon completion.
                    </p>
                    <p class="mb-3">
                        System robustness is maintained through <strong class="text-dark">dynamic group safety measures</strong>: regional group-by executions safely handle all-NaN column fallbacks while dynamically rescaling the neighbor threshold based on available regional data points.
                    </p>
<p class="mb-0">
                        Finally, leveraging <strong class="text-dark">distance-weighted coordinates</strong> (<code>weights='distance'</code>) ensures that highly similar statistical profiles exert a proportionally higher mathematical influence when reconstructing missing values, preserving overall behavioral coherence.
                    </p>
                </div>

</div>
</div>
</div>
</div>


<div class="container mt-4">
    <div class="row">
        <div class="col-lg-10 offset-lg-1">
            <div class="py-3" style="color: #0b2545; font-size: 1.15rem; line-height: 1.6;">
                <p class="mb-4">
                    Following the clustering phase, silhouette score evaluation identified k-NN (k-Nearest Neighbors) as the optimal methodology to drive the reconstruction process. This served as the foundation for designing a distance-weighted post-restructuring imputation pipeline. To prevent scale distortion during distance calculations, the pipeline enforces Z-Score scale invariance—applying forward standardization before calculating distances and inversely scaling the imputed values back to their original physical units upon completion.
                </p>
<p class="mb-0">
                    System robustness is maintained through dynamic group safety measures: regional group-by executions safely handle all-NaN column fallbacks while dynamically rescaling the neighbor threshold based on available regional data points. Finally, leveraging distance-weighted coordinates (weights='distance') ensures that highly similar statistical profiles exert a proportionally higher mathematical influence when reconstructing missing values, preserving overall behavioral coherence.
                </p>

</div>
</div>
</div>
</div>
