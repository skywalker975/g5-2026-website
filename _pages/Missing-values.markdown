---
layout: default
title: "Missing values"
permalink: /Missing-values.html
show_sidetoc: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Missing values"

---


<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>


<!-- Integrated Datasets and Architecture Section -->
<h3>Integrated Datasets and Architecture of HERO</h3>
<p class="text-muted">
    The <b>HERO</b> system organizes humanitarian data and its analytical components around a unified, ready-to-use structure. The framework combines various dimensions of risk (IPC, conflict, displacement, meteorological data, market prices, media signals, and vegetation health) by directly aligning them with food security assessment periods.
</p>

<!-- Systemic Data Missingness Section -->
<h3 class="mt-4">Systemic Data Missingness & Blackout Dynamics</h3>
<p class="text-muted">
    The <b>HERO</b> analytics engine performs a two-dimensional missingness diagnosis across all 7 target data sources. By mapping missing values into binary shadow indicators ($1$ for <code>NaN</code>, $0$ for observed), the pipeline uncovers both <b>cross-dataset co-failures</b> and <b>spatial coverage blackouts</b> to guide targeted imputation strategies.
</p>

<!-- Two-Step Analytical Workflow -->
<h4 class="text-primary fw-bold mb-2 mt-4">Shadow Matrix Analysis: Two-Step Analytical Workflow</h4>
<p class="text-muted mb-4">
    Data unavailability is rarely random. This workflow isolates structural dependencies between sensors and tracks regional data degradation to prevent operational bias during modeling:
</p>

<div class="container mt-4">
    <div class="row">
        <!-- Step 1 Card -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-primary">
                <div class="card-body">
                    <h4 class="card-title text-primary">
                        <i class="fas fa-network-wired me-2"></i> STEP 1: STRUCTURAL CORRELATION
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Cross-Dataset Dependencies</h6>
                    <ul class="list-unstyled mb-0 card-text text-muted">
                        <li class="mb-3">
                            <strong class="text-dark">Correlation Matrix Computation:</strong><br>
                            Calculates a pairwise Pearson correlation matrix across the 7 binary shadow variables to measure co-missingness independently of spatial location.
                        </li>
                        <li class="mb-3">
                            <strong class="text-dark">Co-Failure Pattern Identification:</strong><br>
                            High positive correlations (approaching +1.0) reveal systematic co-failing datasets—such as cases where conflict escalations cause simultaneous losses in both market prices and displacement data.
                        </li>
                        <li>
                            <strong class="text-dark">Bidirectional Heatmap Rendering:</strong><br>
                            Outputs a $7 \times 7$ correlation matrix to visually isolate interconnected clusters of missingness.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
<!-- Step 2 Card -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-danger">
                <div class="card-body">
                    <h4 class="card-title text-danger">
                        <i class="fas fa-earth-americas me-2"></i> STEP 2: GEOGRAPHICAL BLACKOUT
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Spatial Failure Patterns</h6>
                    <ul class="list-unstyled mb-0 card-text text-muted">
                        <li class="mb-3">
                            <strong class="text-dark">Spatial Aggregation:</strong><br>
                            Groups the shadow matrix by <code>Country</code> and calculates the column mean to determine the exact percentage missingness rate per sensor within each national jurisdiction.
                        </li>
                        <li class="mb-3">
                            <strong class="text-dark">Severity Ranking & Scoring:</strong><br>
                            Sums missingness rates across all 7 indicators to compute a <code>total_failure_score</code>, sorting nations from highest to lowest overall data availability collapse.
                        </li>
                        <li>
                            <strong class="text-dark">Unidirectional Heatmap Rendering:</strong><br>
                            Generates a spatial heatmap to pinpoint geographical blackouts where multiple data streams systematically fail simultaneously.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>


<!-- Two-Step Missingness Analysis Workflow -->
<h4 class="text-primary fw-bold mb-2 mt-4">Missingness Analysis: Two-Step Analytical Workflow</h4>
<p class="text-muted mb-4">
    Data unavailability is rarely random. This workflow tests whether missing data points structurally depend on other observed features (MAR) or occur purely stochastically (MCAR), guiding the appropriate imputation strategy:
</p>

<div class="container mt-4">
    <div class="row">
        <!-- Step 1 Card -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-primary">
                <div class="card-body">
                    <h4 class="card-title text-primary">
                        <i class="fas fa-brain me-2"></i> STEP 1: MULTIVARIATE MODELING
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Logistic Regression & Predictability of Absence</h6>
                    <ul class="list-unstyled mb-0 card-text text-muted">
                        <li class="mb-3">
                            <strong class="text-dark">Dummy Target Creation:</strong><br>
                            Maps data unavailability into a binary indicator (<code>1</code> if missing/<code>NaN</code>, <code>0</code> if observed).
                        </li>
                        <li class="mb-3">
                            <strong class="text-dark">Classifier Training:</strong><br>
                            Trains a Logistic Regression model using all other numerical features to predict target missingness on a test split.
                        </li>
                        <li>
                            <strong class="text-dark">ROC AUC Evaluation:</strong><br>
                            An <strong>AUC > 0.6</strong> demonstrates predictable missingness and rejects MCAR (supporting MAR/MNAR). An AUC near 0.5 indicates stochastic missingness.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
<!-- Step 2 Card -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-danger">
                <div class="card-body">
                    <h4 class="card-title text-danger">
                        <i class="fas fa-chart-bar me-2"></i> STEP 2: UNIVARIATE VERIFICATION
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Welch's T-Test Across Individual Features</h6>
                    <ul class="list-unstyled mb-0 card-text text-muted">
                        <li class="mb-3">
                            <strong class="text-dark">Group Separation:</strong><br>
                            Splits the dataset for each predictor into two distinct cohorts: missing target group vs. observed target group.
                        </li>
                        <li class="mb-3">
                            <strong class="text-dark">Mean Difference Testing:</strong><br>
                            Executes an independent sample Welch's t-test (unequal variances) to isolate statistical shifts between both cohorts.
                        </li>
                        <li>
                            <strong class="text-dark">Statistical Significance:</strong><br>
                            A <strong>p-value < 0.05</strong> highlights that a specific predictor directly influences missingness likelihood, supporting the MAR hypothesis.
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>



<!-- Key Findings Section -->
<h3 class="text-primary fw-bold mb-2 mt-5">Key Findings: Structurally Coupled Data Missingness</h3>
<p class="text-muted mb-4">
    Data gaps in the HERO pipeline are <b>structurally coupled</b> rather than randomly distributed. When missingness occurs, multiple indicators collapse simultaneously due to shared real-world failure mechanisms.
</p>

<!-- 1. Structural Topology -->
<h4 class="fw-bold text-dark mt-4 mb-3"><i class="fas fa-network-wired me-2 text-primary"></i> 1. Structural Topology (Correlation Heatmap)</h4>
<p class="text-muted mb-3">The infrastructure collapses into isolated functional blocks:</p>

<div class="container">
    <div class="row">
        <!-- Environmental Sensors Card -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-warning">
                <div class="card-body">
                    <h4 class="card-title text-warning">
                        <i class="fas fa-satellite me-2"></i> Environmental Sensors
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Strong Correlation (r = 0.92)</h6>
                    <p class="card-text text-muted">
                        A high correlation of <b>0.92</b> between <code>missing_NDVI</code> and <code>missing_CHIRPS</code>. The failure of optical vegetation monitoring is directly accompanied by rainfall measurement blackouts.
                    </p>
                </div>
            </div>
        </div>
<!-- Socio-Political Sensors Card -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-danger">
                <div class="card-body">
                    <h4 class="card-title text-danger">
                        <i class="fas fa-triangle-exclamation me-2"></i> Socio-Political Sensors
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Critical Correlations (r = 0.60 - 0.65)</h6>
                    <p class="card-text text-muted">
                        Critical correlations between <b>ACLED and WFP (0.65)</b> as well as <b>ACLED and IDP (0.60)</b>. When tracking of armed conflicts is lost, market reporting and internally displaced person metrics collapse simultaneously.
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/Unknown.png"  style="max-width: 100%; border: 1px solid #e0e0e0;">

<!-- 2. Temporal Dynamics -->
<h4 class="fw-bold text-dark mt-4 mb-3"><i class="fas fa-chart-line me-2 text-primary"></i> 2. Temporal Dynamics (Time Series)</h4>
<p class="text-muted mb-3">Shadow vectors over time confirm distinct underlying causes for missingness:</p>

<div class="container">
    <div class="row">
        <!-- Cyclic Environmental Pattern Card -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-success">
                <div class="card-body">
                    <h4 class="card-title text-success">
                        <i class="fas fa-arrows-rotate me-2"></i> Cyclic Environmental Pattern (MAR)
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Periodic Natural Interference</h6>
                    <p class="card-text text-muted">
                        NDVI and CHIRPS exhibit periodic and overlapping blackouts (missingness rates generally &lt; 0.4), attributable to consistent atmospheric and optical barriers over time.
                    </p>
                </div>
            </div>
        </div>
 <!-- Synchronous Institutional Collapse Card -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-danger">
                <div class="card-body">
                    <h4 class="card-title text-danger">
                        <i class="fas fa-building-circle-xmark me-2"></i> Synchronous Institutional Collapse (MNAR/MAR)
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Catastrophic Pipeline Failures (Peaks at 1.0)</h6>
                    <p class="card-text text-muted">
                        ACLED, WFP, and IDP time series record sudden, prolonged, and simultaneous infrastructure collapses. The lack of periodicity rules out natural noise and highlights severe failures in institutional data pipelines.
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- 3. Geographic Fragmentation -->
<h4 class="fw-bold text-dark mt-4 mb-3"><i class="fas fa-earth-americas me-2 text-primary"></i> 3. Geographic Fragmentation</h4>
<p class="text-muted mb-3">Spatial distribution reveals structural gaps that standard imputation cannot address:</p>

<div class="container">
    <div class="row">
        <!-- ACLED Isolation Card -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-danger">
                <div class="card-body">
                    <h4 class="card-title text-danger">
                        <i class="fas fa-shield-cat me-2"></i> ACLED Isolation
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Systemic Failure Rate 1.0 (17/18 Countries)</h6>
                    <p class="card-text text-muted">
                        A systemic failure rate obliterates data across 17 out of 18 nations. Data survives exclusively in CAF (Central African Republic) and partially in KEN. This represents a purely <b>MNAR</b> dropout driven by geopolitical barriers.
                    </p>
                </div>
            </div>
        </div>
<!-- IDP Blackouts Card -->
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-info">
                <div class="card-body">
                    <h4 class="card-title text-info">
                        <i class="fas fa-people-roof me-2"></i> IDP Blackouts
                    </h4>
                    <h6 class="card-subtitle mb-3 text-muted">Deterministic Data Absence</h6>
                    <p class="card-text text-muted">
                        A similar dynamic affects internally displaced persons data, which is deterministically missing across large dataset clusters (e.g., <code>SLV</code>, <code>GTM</code>, <code>ZWE</code>).
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

<img src="{{ site.baseurl }}/assets/images/Gemini_Generated_Image_mytpddmytpddmytp.png"  style="max-width: 100%; border: 1px solid #e0e0e0;">
