---
layout: default
title: "ML approach"
permalink: /ML-Pipeline.html
show_sidetoc: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Machine learning implementation"

---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>

<!-- Main Section: HERO v6 Modelling Framework -->
<div class="container mt-5">

<h3 class="text-primary mb-3"><i class="fas fa-brain"></i> Machine Learning Framework & Modelling Objectives</h3>
<p class="text-muted">To evaluate and predict food insecurity across 52 countries, the HERO v6 architecture transitions from raw data integration to advanced predictive modelling. Grounded in a dataset of over 10,000 spatial-temporal observations, the framework answers two fundamental operational questions through distinct modeling lenses: understanding structural cross-sectional risk and tracking real-time temporal deterioration.</p>

<!-- Cards: Strategic Rounds -->
<div class="row mt-4">

<!-- Card 1: Static Inference -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-primary">
<div class="card-body">
<h4 class="card-title text-primary"><i class="fas fa-layer-group me-2"></i>Static Inference</h4>
<p class="card-text text-muted">Predicts food security status strictly from instantaneous economic, climatic, and conflict drivers without historical memory.</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-bullseye text-primary me-2"></i><b>Core Focus:</b> Explains <i>why</i> one geographic region suffers worse baseline conditions than another.</li>
<li class="mb-2"><i class="fas fa-shield-check text-primary me-2"></i><b>Honest Validation:</b> Evaluated via geographic hold-out (unseen territories) to prevent spatial correlation inflation.</li>
<li><i class="fas fa-sitemap text-primary me-2"></i><b>Deployment:</b> Best performed using <b>localized or regional models</b>, as driver impact varies by country.</li>
</ul>
</div>
</div>
</div>

<!-- Card 2: Nowcasting -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-info">
<div class="card-body">
<h4 class="card-title text-info"><i class="fas fa-clock-rotate-left me-2"></i>Nowcasting Pipeline</h4>
<p class="card-text text-muted">Combines recent historical assessments with real-time driver dynamics to update current food security levels.</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-chart-line-up text-info me-2"></i><b>Core Focus:</b> Detects <i>whether</i> an ongoing crisis is actively deteriorating or improving in real time.</li>
<li class="mb-2"><i class="fas fa-ranking-star text-info me-2"></i><b>Performance:</b> Outperforms standard historical persistence by <b>+17%</b>, correctly predicting directional change.</li>
<li><i class="fas fa-globe text-info me-2"></i><b>Deployment:</b> Best performed using a <b>single global model</b>, as temporal memory behavior is universal.</li>
</ul>
</div>
</div>
</div>

<!-- Card 3: Key Takeaway & Asymmetry -->
<div class="col-md-4 mb-4">
<div class="card h-100 hero-card card-border-top-warning">
<div class="card-body">
<h4 class="card-title text-warning"><i class="fas fa-scale-unbalanced me-2"></i>The Strategic Asymmetry</h4>
<p class="card-text text-muted">The two modeling approaches serve complementary, non-overlapping functions across different geographic contexts.</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-2"><i class="fas fa-map-location-dot text-warning me-2"></i><b>Spatial Driver Scope:</b> Relationships between drivers (conflict, prices, rainfall) and hunger are highly localized.</li>
<li class="mb-2"><i class="fas fa-hourglass-half text-warning me-2"></i><b>Temporal Dynamic Scope:</b> How crisis trajectories evolve over time follows universal mathematical patterns.</li>
<li><i class="fas fa-lightbulb text-warning me-2"></i><b>Outcome:</b> Static models require regional tailoring; Nowcasting thrives on global data scaling.</li>
</ul>
</div>
</div>
</div>

</div>

<!-- High-Level Insights Summary Card -->
<div class="card hero-card card-border-top-success mt-2 mb-4">
<div class="card-body">
<h4 class="card-title text-success"><i class="fas fa-key me-2"></i>Key Operational Drivers & Model Dynamics</h4>
<p class="card-text text-muted">Analysis of model feature importances reveals critical insights into humanitarian risk monitoring:</p>
<ul class="list-unstyled text-muted mb-0">
<li class="mb-3"><i class="fas fa-people-roof text-success me-2"></i><b>Dominant Structural Drivers:</b> Internal displacement (IDP rates) and localized conflict violence rank as the strongest physical predictors of severe food insecurity, closely followed by food price inflation and short-term rainfall anomalies.</li>
<li class="mb-3"><i class="fas fa-anchor text-success me-2"></i><b>The Power of Baseline Memory:</b> In real-time nowcasting, recent historical assessment scores act as the primary anchor, while fast-acting exogenous signals (such as 1-month rainfall changes) provide the crucial edge in anticipating sudden crisis shifts.</li>
<li class="mb-0"><i class="fas fa-vial text-success me-2"></i><b>Robust Directional Tracking:</b> Beyond static accuracy, the nowcasting framework achieves a strong correlation (<code>r = 0.53</code>) in predicting the exact direction and magnitude of food security changes, solving one of the hardest challenges in early warning systems.</li>
</ul>
</div>
</div>

</div>
