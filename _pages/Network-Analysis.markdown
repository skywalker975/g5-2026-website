---
layout: default
title: "Network Analysis"
permalink: /Network-Analysis.html
show_sidetoc: true
header_type: hero
header_img: assets/copertine_pagine/network_analysis.png
header_title: "Network & Structural Connectivity"
subtitle: "How price shocks travel through trade corridors, and who pays the price"
---

<h1 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">The Domino Effect: Mapping How Market Shocks Spread Across Fragile Regions</h1>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
In humanitarian contexts, food insecurity never happens in isolation. A sudden price spike in one urban market can cascade through trade corridors, triggering inflationary waves in rural provinces hundreds of kilometres away, pushing millions deeper into acute food crisis (IPC Phase 3+). Project HERO's <strong>TSgraph module</strong> was built to map exactly these invisible pathways.
</p>

<div class="glass-card p-4 my-4" style="border-left: 5px solid #a855f7;">
  <p class="m-0 text-light" style="font-size: 0.95rem; line-height: 1.7;">
    <strong>📍 Case Study: Afghanistan (AFG)</strong><br>
    Throughout this page we illustrate the network analysis framework on <strong>Afghanistan's WFP food market system</strong>, in a country where rugged geography, fragmented infrastructure, and active conflict create one of the most complex trade networks in the HERO dataset. The same analysis pipeline is applied automatically to <strong>every country</strong> monitored by the platform.
  </p>
</div>

<hr class="section-divider">

## <span class="text-gradient">1. From Raw Prices to Network Signals</span>

Most analyses aggregate market data monthly, a choice that erases the very signals most relevant to early warning. HERO operates at **native temporal resolution**: daily and weekly WFP price readings, preserved to capture short-term lead-lag dynamics between markets before they are smoothed away.

<div class="my-5 p-4 glass-card">
  <h5 class="text-light text-center mb-4 font-weight-bold">Network Analysis Pipeline Architecture</h5>
  
  <div class="row g-3 text-center align-items-stretch">
    <div class="col-md-3">
      <div class="p-3 rounded h-100" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);">
        <div class="badge-premium-admin1 mb-2">Step 1</div>
        <h6 class="text-light font-weight-bold">Data Ingestion</h6>
        <p class="text-secondary small mb-0">Raw WFP market price data &amp; Log-Return conversion</p>
      </div>
    </div>
    <div class="col-md-3">
      <div class="p-3 rounded h-100" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);">
        <div class="badge-premium-admin2 mb-2">Step 2</div>
        <h6 class="text-light font-weight-bold">Dependency Estimation</h6>
        <p class="text-secondary small mb-0">Pearson Correlation, Mutual Info &amp; Transfer Entropy</p>
      </div>
    </div>
    <div class="col-md-3">
      <div class="p-3 rounded h-100" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);">
        <div class="badge-premium-admin1 mb-2">Step 3</div>
        <h6 class="text-light font-weight-bold">Filtering &amp; Topology</h6>
        <p class="text-secondary small mb-0">Statistical filter (p &lt; 0.05, r &gt; 0.7), Betweenness Centrality &amp; Degree Dist</p>
      </div>
    </div>
    <div class="col-md-3">
      <div class="p-3 rounded h-100" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);">
        <div class="badge-premium-admin2 mb-2">Step 4</div>
        <h6 class="text-light font-weight-bold">Visual Analytics</h6>
        <p class="text-secondary small mb-0">Bidirectional cross-highlighting (Leaflet Map &amp; Plotly Charts)</p>
      </div>
    </div>
  </div>
</div>

Raw price series are first converted into **log-returns** to ensure stationarity. Three complementary dependency measures are then computed for every market pair:

<div class="row g-4 my-4">
  <div class="col-md-4">
    <div class="glass-card card-border-top-info h-100 p-4">
      <div class="badge-premium-admin1 mb-2">Linear</div>
      <h5 class="font-weight-bold text-gradient mb-2">Pearson Correlation</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;">Captures instantaneous co-movement: markets that inflate and deflate in sync, regardless of distance.</p>
    </div>
  </div>
  <div class="col-md-4">
    <div class="glass-card card-border-top-warning h-100 p-4">
      <div class="badge-premium-admin2 mb-2">Non-Linear</div>
      <h5 class="font-weight-bold text-gradient mb-2">Mutual Information</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;">Detects complex, non-linear statistical dependencies invisible to standard correlation, critical in disrupted supply chains.</p>
    </div>
  </div>
  <div class="col-md-4">
    <div class="glass-card card-border-top-success h-100 p-4">
      <div class="badge-premium-admin1 mb-2">Directional</div>
      <h5 class="font-weight-bold text-gradient mb-2">Symbolic Transfer Entropy</h5>
      <p class="text-secondary mb-0" style="line-height: 1.6;">Determines <em>who drives whom</em>, measuring the direction of inflationary contagion along the trade corridor.</p>
    </div>
  </div>
</div>

Only edges that pass a dual significance filter (**p < 0.05** and **r > 0.7**) are retained in the final graph, ensuring every connection represents a statistically robust market dependency.

<hr class="section-divider">

## <span class="text-gradient">2. What the Network Reveals: Afghanistan's Market Topology</span>

Once filtered, the graph is analysed for its topological properties, structural features that reveal how resilient or fragile the regional market system truly is. The screenshot below shows the full TSgraph interface for Afghanistan, with Pearson correlation at lag 0 and a weight threshold ≥ 0.48:

<div class="my-4">
  <img src="{{ site.baseurl }}/assets/UI-NA-TSA-FORC/Network analysis/AFG_network_and_stats.png" alt="TSgraph full interface: Afghanistan market network with topology metrics" class="img-fluid rounded shadow-sm hover-lift" style="border: 1px solid rgba(255,255,255,0.1); width: 100%;">
  <p class="text-secondary small mt-2 text-center"><em>The TSgraph interface for Afghanistan (AFG): geographic Leaflet map (centre) showing the filtered market network, topological control panel (left) with real-time metrics, and three statistical panels (right), covering Distance Decay, Degree Distribution, and Assortativity scatter.</em></p>
</div>

<div class="row g-4 my-4">
  <div class="col-md-6">
    <div class="glass-card p-4 h-100">
      <h6 class="text-light mb-3">🗺️ Geographic Network (Centre Panel)</h6>
      <p class="text-secondary small">Afghanistan's filtered market network reveals a <strong>dense central cluster</strong> in the Kabul–Ghazni–Paktya corridor and a secondary cluster along the northern Kunduz–Takhar axis. Peripheral provinces (Helmand, Farah, Zabul) remain isolated; their markets operate independently from the national price system, making them <em>invisible</em> to conventional early warning based on capital-city prices.</p>
      <p class="text-secondary small mb-0"><strong>Key topological hubs:</strong> Logar, Paktya, and Gardez emerge as the top degree nodes, acting as the critical transit corridors through which inflationary shocks propagate between eastern and central Afghanistan.</p>
    </div>
  </div>
  <div class="col-md-6">
    <div class="glass-card p-4 h-100">
      <h6 class="text-light mb-3">📊 Topological Metrics (Left Panel)</h6>
      
      <div class="table-responsive my-3">
        <table class="table table-sm table-dark text-center mb-0" style="background: transparent; font-size: 0.88rem; border-color: rgba(255,255,255,0.15);">
          <thead>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.25); color: #f8fafc;">
              <th class="text-start">Metric</th>
              <th>Real Network</th>
              <th>ER</th>
              <th>WS</th>
              <th>BA</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
              <td class="text-start"><strong>&lang;k&rang;</strong> (Avg Degree)</td>
              <td>3.3</td>
              <td>3.3</td>
              <td>3.3</td>
              <td>3.3</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.08);">
              <td class="text-start"><strong>CC</strong> (Clustering Coeff)</td>
              <td><strong style="color: #4ade80;">0.538</strong></td>
              <td>0.073</td>
              <td>0.010</td>
              <td>0.125</td>
            </tr>
            <tr>
              <td class="text-start"><strong>SP</strong> (Avg Shortest Path)</td>
              <td>2.76</td>
              <td>2.98</td>
              <td>3.05</td>
              <td>2.59</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p class="text-secondary small mt-3 mb-0">The real network's clustering coefficient (0.538) is <strong>7× higher than Erdős–Rényi</strong> and 4× higher than Barabási–Albert, providing strong evidence that Afghan markets form tightly knit local clusters rather than a random mesh. The relatively short average path (2.76) combined with high clustering is the hallmark of a <strong>small-world network</strong>.</p>
    </div>
  </div>
</div>

<div class="glass-card p-4 my-4">
  <h6 class="text-light mb-3">Additional Topology Insights: Afghanistan</h6>
  <div class="row g-3">
    <div class="col-md-3 text-center">
      <p class="text-light mb-1" style="font-size: 1.5rem; font-weight: 700;">0.133</p>
      <p class="text-secondary small mb-0"><strong>Assortativity (r)</strong><br>Weakly assortative: high-degree hubs tend to connect to other hubs, forming a resilient core.</p>
    </div>
    <div class="col-md-3 text-center">
      <p class="text-light mb-1" style="font-size: 1.5rem; font-weight: 700;">10</p>
      <p class="text-secondary small mb-0"><strong>Components</strong><br>The network fragments into 10 disconnected components, showing evidence of geographic and conflict-related market isolation.</p>
    </div>
    <div class="col-md-3 text-center">
      <p class="text-light mb-1" style="font-size: 1.5rem; font-weight: 700;">71.4%</p>
      <p class="text-secondary small mb-0"><strong>Giant Component</strong><br>25 of 35 markets belong to the largest connected subgraph, representing the backbone of Afghanistan's price transmission system.</p>
    </div>
    <div class="col-md-3 text-center">
      <p class="text-light mb-1" style="font-size: 1.5rem; font-weight: 700;">8</p>
      <p class="text-secondary small mb-0"><strong>Isolated Nodes</strong><br>Eight markets are completely disconnected, operating as autonomous price islands with no detectable linkage to the national system.</p>
    </div>
  </div>
</div>

### Benchmarking Against Theoretical Models

To test whether observed trade networks exhibit genuinely non-random structure, HERO compares each filtered graph in real time against three synthetic baselines generated with identical node and edge counts:

| Model | Type | What it tests |
|---|---|---|
| **Erdős–Rényi (ER)** | Random | Are connections purely random? |
| **Watts–Strogatz (WS)** | Small-world | Do markets cluster locally? |
| **Barabási–Albert (BA)** | Scale-free | Do hubs emerge preferentially? |

Empirical networks consistently deviate from ER randomness and align more closely with BA scale-free topology, demonstrating that real humanitarian market systems are structured rather than stochastic.

<hr class="section-divider">

## <span class="text-gradient">3. Distance Decay: How Geography Shapes Market Connectivity</span>

One of the most universal regularities uncovered by the TSgraph module is **distance decay**, the exponential weakening of market linkages as geographic separation increases. But the *rate* of decay varies dramatically between countries, encoding deep structural information about infrastructure quality, terrain, and conflict-driven market fragmentation.

<div class="row g-4 my-4 align-items-center">
  <div class="col-md-7">
    <img src="{{ site.baseurl }}/assets/UI-NA-TSA-FORC/Network analysis/W_vs_dist_AFG_vs_NGA.png" alt="Distance Decay comparison: Afghanistan vs Nigeria" class="img-fluid rounded shadow-sm hover-lift" style="border: 1px solid rgba(255,255,255,0.1);">
    <p class="text-secondary small mt-2 text-center"><em>Multi-country distance decay comparison (Afghanistan in blue vs Nigeria in orange). Both show a clear declining trend, but with strikingly different decay rates. Power-law fits: AFG α = 0.229, NGA α = 0.066.</em></p>
  </div>
  <div class="col-md-5">
    <div class="glass-card p-4">
      <h6 class="text-light mb-3">Reading the Decay Curves</h6>
      <p class="text-secondary small"><strong class="text-light">Afghanistan (α = 0.229):</strong> A steep decay where market correlation drops sharply beyond ~200 km. This reflects Afghanistan's extreme terrain (Hindu Kush mountain ranges, limited paved roads) and conflict-disrupted supply lines. Distant markets are almost entirely disconnected.</p>
      <p class="text-secondary small"><strong class="text-light">Nigeria (α = 0.066):</strong> A much flatter curve; even at 1,000+ km separation, Nigerian markets maintain correlation weights around 0.5. This is consistent with Nigeria's better road infrastructure and more integrated national supply chain, but it also means that <em>price shocks propagate further and faster</em>.</p>
      <p class="text-secondary small mb-0"><strong class="text-light">Policy implication:</strong> In steep-decay countries like AFG, interventions must be hyper-local. In flat-decay countries like NGA, a single market disruption can cascade nationally.</p>
    </div>
  </div>
</div>

<hr class="section-divider">

## <span class="text-gradient">4. Bidirectional Visual Analytics</span>

The TSgraph interface connects **geographic space** (Leaflet maps) to **analytic space** (Plotly distributions) through a live cross-highlighting system. Every click propagates across both views simultaneously:

<div class="row g-4 my-4">
  <div class="col-md-6">
    <div class="glass-card p-4 h-100">
      <h6 class="text-light mb-2">📍 Map → Charts</h6>
      <p class="text-secondary small mb-0">Selecting a market on the geographic map highlights the same node across all statistical panels, instantly surfacing its degree, centrality rank, and spatial decay position.</p>
    </div>
  </div>
  <div class="col-md-6">
    <div class="glass-card p-4 h-100">
      <h6 class="text-light mb-2">📊 Charts → Map</h6>
      <p class="text-secondary small mb-0">Clicking an outlier in the scatter plots (e.g. two distant but highly correlated markets) lights up the corresponding nodes on the map, revealing non-obvious long-range trade dependencies.</p>
    </div>
  </div>
</div>

<p class="text-light font-weight-bold mt-4 mb-3">Three analytical views are available simultaneously:</p>

<div class="row g-3 my-3">
  <div class="col-md-4">
    <div class="glass-card p-3 h-100" style="border-top: 3px solid #06b6d4;">
      <h6 class="text-info font-weight-bold mb-2"><i class="fas fa-chart-line me-1"></i> Distance Decay Analysis</h6>
      <p class="text-secondary small mb-0">Exponential spatial fitting <em>W &sim; e<sup>&minus;&lambda;d</sup></em> to quantify market link decay across trade corridors.</p>
    </div>
  </div>
  <div class="col-md-4">
    <div class="glass-card p-3 h-100" style="border-top: 3px solid #f59e0b;">
      <h6 class="text-warning font-weight-bold mb-2"><i class="fas fa-project-diagram me-1"></i> Degree Distribution</h6>
      <p class="text-secondary small mb-0">Power-law distribution fitting <em>P(k) &sim; k<sup>&minus;&alpha;</sup></em> to reveal commercial market hierarchy.</p>
    </div>
  </div>
  <div class="col-md-4">
    <div class="glass-card p-3 h-100" style="border-top: 3px solid #10b981;">
      <h6 class="text-success font-weight-bold mb-2"><i class="fas fa-braille me-1"></i> Assortativity Analysis</h6>
      <p class="text-secondary small mb-0">Scatter plot of degree vs nearest-neighbour degree (<em>k vs K<sub>nn</sub></em>) to measure commercial hub connectivity.</p>
    </div>
  </div>
</div>

<hr class="section-divider">

<div class="glass-card p-4 my-4" style="border-left: 5px solid #06b6d4;">
  <p class="m-0 text-light" style="font-size: 0.95rem; line-height: 1.7;">
    <strong>🌍 Reproducibility Note:</strong> The full network analysis pipeline (graph construction, statistical filtering, topological benchmarking, distance decay fitting, and bidirectional visual analytics) is executed for <strong>every country in the HERO dataset</strong>. Cross-country comparisons (as shown for AFG vs NGA) are available via the dashboard's "Confronto Multi-Paese" modal.
  </p>
</div>
