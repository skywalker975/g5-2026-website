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
## Data Preprocessing & Feature Refinement
<p style="text-align: justify;">
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
## Analytical Pipeline: Feature-Based Clustering & Optimal Imputation
<p style="text-align: justify;">
    To extract meaningful regional profiles without raw time-series noise, the workflow compresses dynamic data into statistical fingerprints, benchmarks two spatial scenarios across dual clustering strategies, and resolves data gaps using an optimal imputation pipeline:
</p>

                
<p style="text-align: justify;">
                    The initial phase focuses on feature fingerprints and algorithmic validation, starting with temporal fingerprinting. This process compresses raw sequences into statistical descriptors, ensuring phase invariance, effective noise filtering, and extreme dimensionality reduction. To isolate spatial proximity effects, the pipeline evaluates dual data scenarios, directly comparing Scenario A (pure behavioral data) against Scenario B (behavioral data combined with Latitude and Longitude coordinates).
                </p>

<p style="text-align: justify;">
                 To assess structural stability across both datasets, cross-algorithmic validation is performed. This benchmarks a Hierarchical (Bottom-Up) tree-building approach against a K-Means (Center-Out) centroid assignment strategy. Evaluating how both algorithms handle behavioral parameters with and without spatial coordinates establishes a clear baseline for clustering quality before downstream reconstruction.
                </p>

</div>
</div>
</div>
</div>


| **Clustering** | Silhouette indicator |
|---|---|
| K-Means (W/o coordinates) | 0.193 | 
| Hierarchical (W/o coordinates) | 0.172 | 
| K-Means (With coordinates) | 0.166 | 
| Hierarchical (With coordinates) | 0.122 | 




<p style="text-align: justify;">
                    Following the clustering phase, silhouette score evaluation identified k-NN (k-Nearest Neighbors) as the optimal methodology to drive the reconstruction process. This served as the foundation for designing a distance-weighted post-restructuring imputation pipeline. To prevent scale distortion during distance calculations, the pipeline enforces Z-Score scale invariance—applying forward standardization before calculating distances and inversely scaling the imputed values back to their original physical units upon completion.
                </p>
<p style="text-align: justify;">
                    System robustness is maintained through dynamic group safety measures: regional group-by executions safely handle all-NaN column fallbacks while dynamically rescaling the neighbor threshold based on available regional data points. Finally, leveraging distance-weighted coordinates (weights='distance') ensures that highly similar statistical profiles exert a proportionally higher mathematical influence when reconstructing missing values, preserving overall behavioral coherence.
                </p>





<!-- Contenitore Mappa Interattiva -->


<div class="my-4">
<iframe src="{{ site.baseurl }}/assets/charts/mappa_mondiale_admin1_clusters_v2.html" style="width: 100%; height: 640px; border: 1px solid #e0e0e0; border-radius: 0.5rem;" loading="lazy" title="HERO Map Clustering-2 drill-down"></iframe>
</div>

