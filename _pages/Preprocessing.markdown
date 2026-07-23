---
layout: default
title: "Preprocessing"
permalink: /Preprocessing.html
show_sidetoc: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Preprocessing"

---


<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>


### Integrated Datasets and Architecture of HERO

The <b>HERO</b> system organizes humanitarian data and its analytical components around a unified, ready-to-use structure. The framework combines various dimensions of risk (IPC, conflict, displacement, meteorological data, market prices, media signals, and vegetation health) by directly aligning them with food security assessment periods.

<div class="container mt-4">
<div class="row">
<!-- Data Aggregation Architecture Section -->
<div class="card hero-card card-border-top-primary mt-2 mb-4">
  <div class="card-body p-4 p-md-5">
    
### Systemic Data Missingness & Blackout Dynamics

The <b>HERO</b> analytics engine performs a two-dimensional missingness diagnosis across all 7 target data sources. By mapping missing values into binary shadow indicators ($1$ for `NaN`, $0$ for observed), the pipeline uncovers both **cross-dataset co-failures** and **spatial coverage blackouts** to guide targeted imputation strategies.

<div class="container mt-4">
<div class="row">

<!-- Section: Two-Step Missingness Workflow -->
<div class="card hero-card card-border-top-primary mt-2 mb-4">
  <div class="card-body p-4 p-md-5">
    <!-- Main Header -->
    <h3 class="card-title text-primary fw-bold mb-2">
      Shadow Matrix Analysis: Two-Step Analytical Workflow
    </h3>
    <p class="card-text text-muted mb-4 lead fs-6">
      Data unavailability is rarely random. This workflow isolates structural dependencies between sensors and tracks regional data degradation to prevent operational bias during modeling:
    </p>
<!-- Main Container Card -->
    <div class="card border-0 bg-light rounded-4 p-3 p-md-4">
      <div class="row g-4">
<!-- Column 1: Step 1 - Structural Correlation Analysis -->
        <div class="col-md-6 border-end-md">
          <div class="p-2">
            <!-- Badge / Pill Header -->
            <div class="bg-primary text-white text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm">
              <i class="fas fa-network-wired me-2"></i> STEP 1: STRUCTURAL CORRELATION
              <span class="d-block text-white-50 small fw-normal">(Cross-Dataset Dependencies)</span>
            </div>
            <!-- Bullet List -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">Correlation Matrix Computation:</span>
                <span class="text-muted d-block small mt-1">Calculates a pairwise Pearson correlation matrix across the 7 binary shadow variables to measure co-missingness independently of spatial location.</span>
              </li>
              <li class="mb-3">
                <span class="fw-bold text-dark">Co-Failure Pattern Identification:</span>
                <span class="text-muted d-block small mt-1">High positive correlations (approaching +1.0) reveal systematic co-failing datasets—such as cases where conflict escalations cause simultaneous losses in both market prices and displacement data.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Bidirectional Heatmap Rendering:</span>
                <span class="text-muted d-block small mt-1">Outputs a $7 \times 7$ correlation matrix  to visually isolate interconnected clusters of missingness.</span>
              </li>
            </ul>
          </div>
        </div>
<!-- Column 2: Step 2 - Geographical Blackout Analysis -->
        <div class="col-md-6">
          <div class="p-2">
            <!-- Badge / Pill Header -->
            <div class="bg-danger text-white text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm" style="background-color: #fee2e2 !important; color: #991b1b !important;">
              <i class="fas fa-earth-americas me-2"></i> STEP 2: GEOGRAPHICAL BLACKOUT
              <span class="d-block small fw-normal" style="color: #991b1b; opacity: 0.8;">(Spatial Failure Patterns)</span>
            </div>
            <!-- Bullet List -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">Spatial Aggregation:</span>
                <span class="text-muted d-block small mt-1">Groups the shadow matrix by <code class="small">Country</code> and calculates the column mean to determine the exact percentage missingness rate per sensor within each national jurisdiction.</span>
              </li>
              <li class="mb-3">
                <span class="fw-bold text-dark">Severity Ranking & Scoring:</span>
                <span class="text-muted d-block small mt-1">Sums missingness rates across all 7 indicators to compute a <code class="small">total_failure_score</code>, sorting nations from highest to lowest overall data availability collapse.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Unidirectional Heatmap Rendering:</span>
                <span class="text-muted d-block small mt-1">Generates a spatial heatmap  to pinpoint geographical blackouts where multiple data streams systematically fail simultaneously.</span>
              </li>
            </ul>
          </div>
        </div>

</div>
    </div>

  </div>
</div>

</div>
</div>

---
<!-- Section: Structurally Coupled Missingness & Analytical Findings -->
<div class="card hero-card card-border-top-primary mt-2 mb-4">
  <div class="card-body p-4 p-md-5">
    <!-- Main Header -->
    <h3 class="card-title text-primary fw-bold mb-2">
      Key Findings: Structurally Coupled Data Missingness
    </h3>
    <p class="card-text text-muted mb-4 lead fs-6">
      Data gaps in the HERO pipeline are <b>structurally coupled</b> rather than randomly distributed. When missingness occurs, multiple indicators collapse simultaneously due to shared real-world failure mechanisms.
    </p>
<!-- Main Container Card -->
    <div class="card border-0 bg-light rounded-4 p-3 p-md-4 mb-4">
      <div class="row g-4">
<!-- Column 1: Satellite & Environmental Coupling -->
        <div class="col-md-4 border-end-md">
          <div class="p-2">
            <!-- Badge Header -->
            <div class="bg-warning text-dark text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm" style="background-color: #fef08a !important;">
              <i class="fas fa-satellite me-2"></i> EARTH-OBSERVATION
              <span class="d-block text-muted small fw-normal">(r = 0.92)</span>
            </div>
            <!-- Content -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">NDVI & CHIRPS Coupling:</span>
                <span class="text-muted d-block small mt-1">Optical vegetation (<code class="small">missing_NDVI</code>) and precipitation data (<code class="small">missing_CHIRPS</code>) exhibit a near-perfect positive correlation.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Physical Failure Mode:</span>
                <span class="text-muted d-block small mt-1">Persistent cloud cover during rainy seasons simultaneously blinds optical sensors and disrupts satellite rainfall estimates over the exact same grid.</span>
              </li>
            </ul>
          </div>
        </div>
<!-- Column 2: Geopolitical & Field Access Coupling -->
        <div class="col-md-4 border-end-md">
          <div class="p-2">
            <!-- Badge Header -->
            <div class="bg-danger text-white text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm" style="background-color: #fee2e2 !important; color: #991b1b !important;">
              <i class="fas fa-triangle-exclamation me-2"></i> INSTITUTIONAL BLACKOUTS
              <span class="d-block small fw-normal" style="color: #991b1b; opacity: 0.8;">(r = 0.60 - 0.65)</span>
            </div>
            <!-- Content -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">Ground-Truth Co-Failures:</span>
                <span class="text-muted d-block small mt-1">Conflict reports (<code class="small">ACLED</code>), market prices (<code class="small">WFP</code>), and displacement data (<code class="small">IDP</code>) fail together in tight clusters.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Operational Failure Mode:</span>
                <span class="text-muted d-block small mt-1">Conflict escalations close local markets and force humanitarian field evacuations, triggering simultaneous <b>MNAR</b> ground-data dropouts.</span>
              </li>
            </ul>
          </div>
        </div>
<!-- Column 3: Independent Anchor Datasets -->
        <div class="col-md-4">
          <div class="p-2">
            <!-- Badge Header -->
            <div class="bg-primary text-white text-center fw-bold rounded-4 py-2 px-3 mb-4 shadow-sm">
              <i class="fas fa-shield-halved me-2"></i> INDEPENDENT ANCHORS
              <span class="d-block text-white-50 small fw-normal">(r ≤ 0.19)</span>
            </div>
            <!-- Content -->
            <ul class="list-unstyled mb-0">
              <li class="mb-3">
                <span class="fw-bold text-dark">Uncoupled Indicators:</span>
                <span class="text-muted d-block small mt-1">Media signals (<code class="small">GDELT</code>) and assessment periods (<code class="small">IPC</code>) show negligible correlation with ground or satellite failures.</span>
              </li>
              <li>
                <span class="fw-bold text-dark">Robust Baseline Signals:</span>
                <span class="text-muted d-block small mt-1">These data sources operate independently of local field access or atmospheric conditions, serving as reliable anchors during major regional blackouts.</span>
              </li>
            </ul>
          </div>
        </div>
</div>
    </div>



