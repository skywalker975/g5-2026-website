---
layout: default
title: "Forecast & Time Series Analysis"
permalink: /Forecast-and-Time-Series-Analysis.html
show_sidetoc: true
header_type: hero
header_img: assets/copertine_pagine/time_series.png
header_title: "Forecast & Time Series Analysis"
subtitle: "Predicting humanitarian crises before they peak, from signal decomposition to zero-shot AI"
---

<h1 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">Forecasting the Unthinkable: Sequential Modelling and Early Warning Systems</h1>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Humanitarian emergencies rarely strike without warning. They accumulate through the slow compounding of climate shocks, economic volatility, and social conflict over months and years. By treating the data as dynamic temporal sequences rather than static snapshots, Project HERO extracts predictive signals that can anticipate the deterioration of food security <strong>before a crisis reaches its apex</strong>.
</p>

<div class="glass-card p-4 my-4" style="border-left: 5px solid #06b6d4;">
  <p class="m-0 text-light" style="font-size: 0.95rem; line-height: 1.7;">
    <strong class="text-info"><i class="fas fa-shield-heart me-1"></i> Target Variable Definition — IPC Phase 3+:</strong> The primary target metric analyzed throughout our time-series and forecasting models is the <strong>IPC Phase 3+ proportion</strong>. Based on the <em>Integrated Food Security Phase Classification (IPC)</em> standard, IPC 3+ measures the percentage of population living under <strong>Acute Food Insecurity</strong> — combining Crisis (Phase 3), Emergency (Phase 4), and Catastrophe/Famine (Phase 5).
  </p>
</div>

<div class="glass-card p-4 my-4" style="border-left: 5px solid #a855f7;">
  <p class="m-0 text-light" style="font-size: 0.95rem; line-height: 1.7;">
    <strong>📍 Case Study: Badakhshan Province, Afghanistan (ADM1: AF17)</strong><br>
    Throughout this page we illustrate the full TSA pipeline on <strong>Badakhshan</strong>, a remote mountainous province in north-eastern Afghanistan chronically affected by food insecurity. The same battery of analyses (decomposition, autocorrelation, anomaly detection, and multi-model forecasting) has been applied systematically to <strong>every ADM1 region across all countries</strong> in the HERO dataset.
  </p>
</div>

<hr class="section-divider">

## <span class="text-gradient">1. The First Challenge: Temporal Misalignment</span>

The raw data arrives fragmented across incompatible timescales. Conflict events from ACLED are recorded daily. WFP price readings come weekly. IPC food security assessments happen sporadically, sometimes months apart. Feeding these into a coherent forecasting system requires careful temporal harmonisation.

<div class="my-5 p-4 glass-card">
  <h5 class="text-light text-center mb-4 font-weight-bold">Forecast & Anomaly Detection Pipeline</h5>
  
  <div class="row g-3 text-center align-items-stretch">
    <div class="col-md-3">
      <div class="p-3 rounded h-100" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);">
        <div class="badge-premium-admin1 mb-2">Phase 1</div>
        <h6 class="text-light font-weight-bold">Ingestion & Alignment</h6>
        <p class="text-secondary small mb-0">WFP, ACLED, CHIRPS, IPC temporal re-gridding (Monthly MS)</p>
      </div>
    </div>
    <div class="col-md-3">
      <div class="p-3 rounded h-100" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);">
        <div class="badge-premium-admin2 mb-2">Phase 2</div>
        <h6 class="text-light font-weight-bold">Signal Decomposition</h6>
        <p class="text-secondary small mb-0">STL LOESS decomposition into Trend, Seasonality & Residuals</p>
      </div>
    </div>
    <div class="col-md-3">
      <div class="p-3 rounded h-100" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);">
        <div class="badge-premium-admin1 mb-2">Phase 3</div>
        <h6 class="text-light font-weight-bold">Feature & Anomaly Profiling</h6>
        <p class="text-secondary small mb-0">tsfresh metrics & Matrix Profile (Motifs & Discords)</p>
      </div>
    </div>
    <div class="col-md-3">
      <div class="p-3 rounded h-100" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);">
        <div class="badge-premium-admin2 mb-2">Phase 4</div>
        <h6 class="text-light font-weight-bold">Multi-Layer Forecasting</h6>
        <p class="text-secondary small mb-0">SARIMAX, Causal VAR, DTW Transfer & TimesFM Zero-Shot</p>
      </div>
    </div>
  </div>
</div>

<hr class="section-divider">

## <span class="text-gradient">2. Signal Engineering: Distilling the Mathematics of a Crisis</span>

For each province, HERO computes a rich **tsfresh** feature vector, representing the mathematical signature of how that region's indicators have evolved over time.

<div class="row g-4 my-4">
  <div class="col-md-4">
    <div class="glass-card card-border-top-info h-100 p-4">
      <div class="badge-premium-admin1 mb-2">Distribution Shape</div>
      <h5 class="font-weight-bold text-gradient mb-2">Skewness & Kurtosis</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;">Measure whether a province's food security distribution skews toward extremes, serving as a key signature of structural fragility versus transient stress.</p>
    </div>
  </div>
  <div class="col-md-4">
    <div class="glass-card card-border-top-warning h-100 p-4">
      <div class="badge-premium-admin2 mb-2">Shock Persistence</div>
      <h5 class="font-weight-bold text-gradient mb-2">Hurst Exponent</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;">The Hurst exponent H quantifies long-term memory: does a drought shock fade quickly, or does it compound over the following seasons?</p>
    </div>
  </div>
  <div class="col-md-4">
    <div class="glass-card card-border-top-success h-100 p-4">
      <div class="badge-premium-admin1 mb-2">Complexity</div>
      <h5 class="font-weight-bold text-gradient mb-2">Approximate Entropy</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;">ApEn measures signal irregularity: high entropy signals unpredictable, chaotic conditions, while low entropy signals structural trends amenable to forecasting.</p>
    </div>
  </div>
</div>

<hr class="section-divider">

## <span class="text-gradient">3. Decomposing the Signal: Separating Trend from Noise</span>

Before forecasting, each time series is structurally decomposed using **STL (Seasonal and Trend decomposition using LOESS)**, a regression-based method specifically chosen for its robustness to the massive outlier presence typical of conflict zones.

<div class="row g-4 my-4 align-items-center">
  <div class="col-md-7 text-center">
    <div class="mb-2 text-start"><span class="badge bg-dark border border-secondary text-info" style="font-weight: 500; font-size: 0.75rem;"><i class="fas fa-chart-line me-1"></i> Target: IPC Phase 3+ Trajectory (%)</span></div>
    <img src="{{ site.baseurl }}/assets/UI-NA-TSA-FORC/TSA_AFG_Badakhshan_AF17/01_Statistical_Decomposition_STL.png" alt="STL Decomposition: Badakhshan IPC Target" class="img-fluid rounded shadow-sm hover-lift" style="border: 1px solid rgba(255,255,255,0.1);">
    <p class="text-secondary small mt-2 text-center"><em>STL Decomposition of Badakhshan's IPC Phase 3+ acute food insecurity target (2017–2025). The trend peaked at ~60% during 2019–2021, coinciding with the Taliban takeover and successive drought seasons. Seasonal oscillations of ±10 pp reflect the lean season cycle. Residual spikes flag the shocks the model cannot predict from structure alone.</em></p>
  </div>
  <div class="col-md-5">
    <div class="glass-card p-4">
      <h6 class="text-light mb-3">What STL Reveals</h6>
      <div class="mb-3">
        <p class="text-secondary mb-1"><strong class="text-light">📈 Trend</strong></p>
        <p class="text-secondary small mb-0">The underlying long-run trajectory of food insecurity, stripped of seasonal and random fluctuation.</p>
      </div>
      <div class="mb-3">
        <p class="text-secondary mb-1"><strong class="text-light">🌀 Seasonality</strong></p>
        <p class="text-secondary small mb-0">Recurring annual patterns, such as harvest cycles, rainy seasons, and lean periods, isolated and modelled independently.</p>
      </div>
      <div>
        <p class="text-secondary mb-1"><strong class="text-light">⚡ Residuals</strong></p>
        <p class="text-secondary small mb-0">The unexplained remainder, representing the space where <strong>systemic shocks hide</strong>. This is where the Matrix Profile operates.</p>
      </div>
    </div>
  </div>
</div>

<hr class="section-divider">

## <span class="text-gradient">4. Temporal Memory: Autocorrelation and Cross-Correlation Analysis</span>

Understanding how quickly a signal forgets its own past, and how strongly different drivers lead or follow the target, is critical to selecting the right forecasting model.

### ACF & PACF of the Differenced IPC Series

<div class="row g-4 my-4 align-items-center">
  <div class="col-md-5">
    <div class="glass-card p-4">
      <h6 class="text-light mb-3">Reading the Correlogram</h6>
      <p class="text-secondary small">After first-order differencing (d=1), the IPC Phase 3+ target series for Badakhshan shows <strong>no significant autocorrelation</strong> at any lag, as all coefficients fall within the 95% confidence band. This means the differenced series behaves like white noise: the original signal is well-described by a simple random walk with drift, and any remaining predictive power must come from <em>exogenous variables</em> rather than the series' own history.</p>
      <p class="text-secondary small mb-0">The PACF confirms this with a clean cut-off after lag 0, leaving no partial correlation structure to exploit, which presents a strong argument for moving beyond pure ARIMA toward multivariate models (VAR) or transfer learning approaches.</p>
    </div>
  </div>
  <div class="col-md-7 text-center">
    <div class="mb-2 text-start"><span class="badge bg-dark border border-secondary text-info" style="font-weight: 500; font-size: 0.75rem;"><i class="fas fa-chart-line me-1"></i> Target: IPC Phase 3+ Correlogram</span></div>
    <img src="{{ site.baseurl }}/assets/UI-NA-TSA-FORC/TSA_AFG_Badakhshan_AF17/02_Autocorrelation_ACF_PACF.png" alt="ACF and PACF of Badakhshan IPC (d=1)" class="img-fluid rounded shadow-sm hover-lift" style="border: 1px solid rgba(255,255,255,0.1);">
    <p class="text-secondary small mt-2 text-center"><em>ACF (top) and PACF (bottom) of the first-differenced IPC Phase 3+ target series. No lag exceeds the 95% significance threshold, confirming near-white-noise behaviour after differencing.</em></p>
  </div>
</div>

### Multi-Variable Autocorrelation Comparison

<div class="my-4 text-center">
  <img src="{{ site.baseurl }}/assets/UI-NA-TSA-FORC/TSA_AFG_Badakhshan_AF17/02b_Compare_Series_Autocorrelation.png" alt="Multi-variable autocorrelation comparison: Badakhshan" class="img-fluid rounded shadow-sm hover-lift" style="border: 1px solid rgba(255,255,255,0.1); width: 100%;">
  <p class="text-secondary small mt-2 text-center"><em>Autocorrelation (ACF) and Partial Autocorrelation (PACF) comparison across all 11 driver variables for Badakhshan. IPC Phase 3+ and IDP population exhibit the strongest long-memory persistence (ACF decaying slowly over 12+ months), while rainfall anomalies decay rapidly, suggesting they act as short-horizon triggers rather than sustained drivers.</em></p>
</div>

### Cross-Correlation with the IPC Target

<div class="row g-4 my-4 align-items-center">
  <div class="col-md-7 text-center">
    <div class="mb-2 text-start"><span class="badge bg-dark border border-secondary text-info" style="font-weight: 500; font-size: 0.75rem;"><i class="fas fa-chart-line me-1"></i> Target: IPC Phase 3+ Cross-Correlation</span></div>
    <img src="{{ site.baseurl }}/assets/UI-NA-TSA-FORC/TSA_AFG_Badakhshan_AF17/02c_Cross_Correlation_with_Target.png" alt="Cross-correlation (CCF) of all drivers with IPC target: Badakhshan" class="img-fluid rounded shadow-sm hover-lift" style="border: 1px solid rgba(255,255,255,0.1);">
    <p class="text-secondary small mt-2 text-center"><em>Cross-Correlation Function (CCF) between each driver and the IPC Phase 3+ target. Negative lags (left of the red line) indicate that the predictor leads the target, providing a direct measure of early warning potential.</em></p>
  </div>
  <div class="col-md-5">
    <div class="glass-card p-4">
      <h6 class="text-light mb-3">Key Lead-Lag Insights</h6>
      <p class="text-secondary small"><strong class="text-light">WFP inflation</strong> shows the strongest leading signal at lags −8 to −10 months (CCF ≈ 0.45), confirming that food price inflation precedes IPC Phase 3+ deterioration by nearly a year in Badakhshan.</p>
      <p class="text-secondary small"><strong class="text-light">Rainfall anomalies</strong> (3-month) peak at positive lags (+5 to +10), meaning they are <em>lagging indicators</em> where the drought effect materialises in the IPC Phase 3+ assessment only several months after the rainfall deficit occurs.</p>
      <p class="text-secondary small mb-0"><strong class="text-light">IDP population</strong> has the most asymmetric CCF profile: displacement drives future IPC worsening at all lead horizons, but the reverse effect decays rapidly.</p>
    </div>
  </div>
</div>

<hr class="section-divider">

## <span class="text-gradient">5. Anomaly Detection via Matrix Profile</span>

Stochastic residuals from the STL decomposition are analysed using the **Matrix Profile** algorithm, which scans the time series for two types of structural patterns.

<div class="glass-card p-4 my-4" style="border-left: 5px solid #06b6d4;">
  <h6 class="text-light mb-3">📊 Data Availability for Reliable Anomaly Detection</h6>
  <p class="text-secondary small" style="line-height: 1.7;">The Matrix Profile operates on the <strong>IPC Phase 3+ target series</strong>, representing the percentage of population in acute food insecurity, after STL residual extraction. For each ADM1 region, the input data is assembled from:</p>
  <div class="row g-3 my-2">
    <div class="col-md-4">
      <p class="text-secondary small mb-1"><strong class="text-light">IPC Assessments</strong></p>
      <p class="text-secondary small mb-0">Sporadic (2–4 per year per country). Re-gridded to monthly frequency via forward-fill interpolation. Coverage spans <strong>2017–2025</strong>, yielding ~80–96 monthly observations per region, providing the minimum viable length for subsequence-based algorithms.</p>
    </div>
    <div class="col-md-4">
      <p class="text-secondary small mb-1"><strong class="text-light">Exogenous Drivers (for context)</strong></p>
      <p class="text-secondary small mb-0">WFP prices (weekly → monthly), ACLED conflict events (daily → monthly), CHIRPS rainfall (dekadal → monthly), NDVI vegetation (bi-weekly → monthly), IDP displacement (monthly). These are used in the cross-correlation analysis to <em>interpret</em> the anomalies detected.</p>
    </div>
    <div class="col-md-4">
      <p class="text-secondary small mb-1"><strong class="text-light">Reliability Constraints</strong></p>
      <p class="text-secondary small mb-0">Matrix Profile requires <strong>at least 3× the subsequence length</strong> in total observations. With a typical window of 6–12 months, the minimum threshold is ~36 months of data. Regions with fewer than 30 valid IPC observations are flagged as <em>insufficient</em> and excluded from anomaly detection.</p>
    </div>
  </div>
</div>

| Pattern | Definition | Humanitarian Meaning |
|---|---|---|
| **Motifs** | Subsequences that recur frequently | Early warning signatures that precede IPC downgrade events |
| **Discords** | Subsequences that never recur | Isolated systemic shocks, such as conflict escalations and harvest collapses |

<div class="row g-4 my-4 align-items-center">
  <div class="col-md-8 text-center">
    <div class="mb-2 text-start"><span class="badge bg-dark border border-secondary text-info" style="font-weight: 500; font-size: 0.75rem;"><i class="fas fa-chart-line me-1"></i> Target: IPC Phase 3+ Motifs & Discords</span></div>
    <img src="{{ site.baseurl }}/assets/UI-NA-TSA-FORC/TSA_AFG_Badakhshan_AF17/04_Matrix_Profile_Anomalies_Discords.png" alt="Matrix Profile: Motifs and Discords for Badakhshan IPC" class="img-fluid rounded shadow-sm hover-lift" style="border: 1px solid rgba(255,255,255,0.1);">
    <p class="text-secondary small mt-2 text-center"><em>Top panel: the original IPC Phase 3+ time series with motif pairs (blue, orange) and the detected discord (red) highlighted. Bottom panel: the Matrix Profile distance function, where peaks represent anomalous subsequences and valleys represent recurring motifs.</em></p>
  </div>
  <div class="col-md-4">
    <div class="glass-card p-4">
      <h6 class="text-light mb-3">What the Algorithm Found</h6>
      <p class="text-secondary small"><strong class="text-light">Discord (Nov 2017):</strong> The rapid initial surge from ~35% to ~52% IPC Phase 3+ in late 2017 is flagged as the most anomalous subsequence in the entire record, marking a sudden regime shift with no historical precedent.</p>
      <p class="text-secondary small"><strong class="text-light">Motif Pair:</strong> The 2018–2019 plateau phase (blue) and the 2020–2021 spike (orange) share structural similarity, as both show a rapid rise followed by a sustained high plateau. This recurrence pattern can serve as an early warning template.</p>
    </div>
  </div>
</div>

Residuals exceeding a critical threshold (**Z-score > 2.0**) are mapped onto a multi-provincial **Anomaly Matrix** heatmap, visually revealing the spatial and temporal alignment of socio-economic collapses across regions.

<hr class="section-divider">

## <span class="text-gradient">6. Forecasting Architecture: Four Layers of Prediction</span>

No single model works everywhere. HERO uses a **stratified forecasting framework** that adapts to the data quality and structural context of each province.

<div class="row g-4 my-4">
  <div class="col-md-6">
    <div class="glass-card card-border-top-secondary h-100 p-4">
      <h5 class="font-weight-bold text-light mb-2">Layer 1: Univariate Baselines</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;"><strong>SARIMAX / Holt-Winters</strong> models are trained at ADM1/ADM2 level to capture pure autocorrelation patterns in the IPC Phase 3+ series. They set a performance benchmark for all more complex approaches.</p>
    </div>
  </div>
  <div class="col-md-6">
    <div class="glass-card card-border-top-info h-100 p-4">
      <h5 class="font-weight-bold text-light mb-2">Layer 2: Causal VAR</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;"><strong>Vector Autoregression</strong> captures cross-variable feedback loops: a conflict escalation that destroys agricultural infrastructure generating food price inflation and worsening IPC Phase 3+ in the following months.</p>
    </div>
  </div>
  <div class="col-md-6">
    <div class="glass-card card-border-top-warning h-100 p-4">
      <h5 class="font-weight-bold text-light mb-2">Layer 3: DTW Clustering + Transfer Learning</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;">In conflict zones with fragmented data, <strong>Dynamic Time Warping</strong> clusters provinces with similar IPC Phase 3+ crisis trajectories. Joint models trained on clusters are highly resistant to overfitting on thin historical records.</p>
    </div>
  </div>
  <div class="col-md-6">
    <div class="glass-card card-border-top-success h-100 p-4">
      <h5 class="font-weight-bold text-light mb-2">Layer 4: TimesFM (Zero-Shot)</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;">In areas with total data blackout, HERO tests <strong>Google's TimesFM foundation model</strong> to generate exploratory projections of IPC Phase 3+ without any local historical retraining, serving as the last resort for the most opaque crisis contexts.</p>
    </div>
  </div>
</div>

### Multi-Model Forecast Comparison

<div class="row g-4 my-4 align-items-center">
  <div class="col-md-7 text-center">
    <div class="mb-2 text-start"><span class="badge bg-dark border border-secondary text-info" style="font-weight: 500; font-size: 0.75rem;"><i class="fas fa-chart-line me-1"></i> Target: IPC Phase 3+ Multi-Model Forecast</span></div>
    <img src="{{ site.baseurl }}/assets/UI-NA-TSA-FORC/TSA_AFG_Badakhshan_AF17/05_MultiModel_Forecast_Comparison.png" alt="Multi-Model Forecast Comparison: Badakhshan IPC" class="img-fluid rounded shadow-sm hover-lift" style="border: 1px solid rgba(255,255,255,0.1);">
    <p class="text-secondary small mt-2 text-center"><em>Holt-Winters (green), SARIMAX (blue dashed), and VAR (purple) forecasts of IPC Phase 3+ against the held-out test set (black dots). The red dashed line marks the train/test split point (2024). The light purple band shows the Holt-Winters 95% confidence interval.</em></p>
  </div>
  <div class="col-md-5">
    <div class="glass-card p-4">
      <h6 class="text-light mb-3">Model Performance: Badakhshan</h6>
      <table class="table table-sm table-borderless mb-3" style="color: #94a3b8; font-size: 0.85rem;">
        <thead>
          <tr style="border-bottom: 1px solid rgba(255,255,255,0.15);">
            <th class="text-light" style="padding: 0.4rem 0.5rem;">Model</th>
            <th class="text-light text-center" style="padding: 0.4rem 0.5rem;">MAE</th>
            <th class="text-light text-center" style="padding: 0.4rem 0.5rem;">RMSE</th>
            <th class="text-light text-center" style="padding: 0.4rem 0.5rem;">R²</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid rgba(255,255,255,0.07); background: rgba(34,197,94,0.08);">
            <td style="padding: 0.4rem 0.5rem;"><strong class="text-light">Holt-Winters</strong></td>
            <td class="text-center" style="padding: 0.4rem 0.5rem;"><strong>2.06%</strong></td>
            <td class="text-center" style="padding: 0.4rem 0.5rem;"><strong>3.04%</strong></td>
            <td class="text-center" style="padding: 0.4rem 0.5rem;">−0.67</td>
          </tr>
          <tr style="border-bottom: 1px solid rgba(255,255,255,0.07);">
            <td style="padding: 0.4rem 0.5rem;">SARIMAX</td>
            <td class="text-center" style="padding: 0.4rem 0.5rem;">2.53%</td>
            <td class="text-center" style="padding: 0.4rem 0.5rem;">3.08%</td>
            <td class="text-center" style="padding: 0.4rem 0.5rem;">−0.71</td>
          </tr>
          <tr>
            <td style="padding: 0.4rem 0.5rem;">VAR</td>
            <td class="text-center" style="padding: 0.4rem 0.5rem;">8.20%</td>
            <td class="text-center" style="padding: 0.4rem 0.5rem;">8.86%</td>
            <td class="text-center" style="padding: 0.4rem 0.5rem;">−13.13</td>
          </tr>
        </tbody>
      </table>
      <p class="text-secondary small mb-0">Both univariate baselines achieve MAE around 2–3 pp, closely tracking the test data. The VAR model diverges, as its multivariate feedback structure captures macro-dynamics well but overfits on Badakhshan's short history. Both Holt-Winters and SARIMAX pass the Ljung-Box white noise test on residuals (p > 0.05).</p>
    </div>
  </div>
</div>

### SARIMAX Order Selection (AIC/BIC)

<div class="row g-4 my-4 align-items-center">
  <div class="col-md-5">
    <div class="glass-card p-4">
      <h6 class="text-light mb-3">Why ARIMA(1,1,2)×(1,1,1,12)?</h6>
      <p class="text-secondary small">HERO systematically evaluates multiple SARIMAX parameter combinations using the dual information criterion approach: <strong>AIC</strong> (Akaike) for predictive accuracy and <strong>BIC</strong> (Bayesian) for parsimony.</p>
      <p class="text-secondary small">For Badakhshan, adding a seasonal component with period 12 dramatically reduces both criteria (from ~450 to ~320), confirming the annual lean-season cycle embedded in the IPC Phase 3+ signal. The final selected order ARIMA(1,1,2)×(1,1,1,12) achieves the lowest AIC while remaining within 5 points of the BIC minimum, balancing fit quality against model complexity.</p>
    </div>
  </div>
  <div class="col-md-7">
    <img src="{{ site.baseurl }}/assets/UI-NA-TSA-FORC/TSA_AFG_Badakhshan_AF17/05b_SARIMAX_AIC_BIC_Evaluation.png" alt="SARIMAX AIC vs BIC Evaluation: Badakhshan" class="img-fluid rounded shadow-sm hover-lift" style="border: 1px solid rgba(255,255,255,0.1);">
    <p class="text-secondary small mt-2 text-center"><em>AIC (blue) and BIC (orange) across 6 candidate SARIMAX orders. Non-seasonal models (left) score substantially higher (~450), while seasonal models with s=12 (right three) cluster around 320–330, confirming the presence of a strong 12-month cycle in the IPC Phase 3+ series.</em></p>
  </div>
</div>

### Residual Diagnostics

<div class="row g-4 my-4 align-items-center">
  <div class="col-md-8">
    <img src="{{ site.baseurl }}/assets/UI-NA-TSA-FORC/TSA_AFG_Badakhshan_AF17/06_Model_Residuals_Diagnostics.png" alt="Residual Diagnostics: Holt-Winters model for Badakhshan" class="img-fluid rounded shadow-sm hover-lift" style="border: 1px solid rgba(255,255,255,0.1);">
    <p class="text-secondary small mt-2 text-center"><em>Four-panel diagnostic suite for the Holt-Winters model: standardised IPC Phase 3+ residuals over time (top-left), residual histogram with KDE and Normal overlay (top-right), Normal Q-Q plot (bottom-left), and residuals PACF (bottom-right).</em></p>
  </div>
  <div class="col-md-4">
    <div class="glass-card p-4">
      <h6 class="text-light mb-3">Diagnostic Interpretation</h6>
      <p class="text-secondary small"><strong class="text-light">Residual time series:</strong> The standardised residuals oscillate around zero without visible trend, though isolated spikes (2018, 2021, 2024) flag the same systemic shocks identified by the Matrix Profile.</p>
      <p class="text-secondary small"><strong class="text-light">Q-Q plot:</strong> Heavy tails at both extremes reveal that the residuals are leptokurtic, indicating that the model underestimates extreme events, a known challenge in conflict-affected forecasting.</p>
      <p class="text-secondary small mb-0"><strong class="text-light">PACF of residuals:</strong> All partial autocorrelations fall within the significance band, confirming the model has extracted all available temporal structure, as the residuals are white noise.</p>
    </div>
  </div>
</div>

<hr class="section-divider">

<div class="glass-card p-4 my-4" style="border-left: 5px solid #06b6d4;">
  <p class="m-0 text-light" style="font-size: 0.95rem; line-height: 1.7;">
    <strong>🌍 Reproducibility Note:</strong> The complete TSA pipeline shown above for Badakhshan (Afghanistan), including STL decomposition, ACF/PACF analysis, cross-correlation, Matrix Profile anomaly detection, SARIMAX order selection, multi-model forecasting, and residual diagnostics, is automatically executed for <strong>every ADM1 administrative region across all countries in the HERO dataset</strong>. All outputs are archived and accessible via the HERO Dashboard's TSA Diagnostics tab.
  </p>
</div>
