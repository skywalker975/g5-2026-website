---
layout: default
title: "Introduzione"
permalink: /introduzione.html
show_sidetoc: true
header_type: hero
header_img: assets/images/folium_map.webp
header_title: "HERO"
subtitle: "Hunger Early-warning & Risk Optimizer"
---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>

# <span class="text-gradient">HERO: Hunger Early-warning & Risk Optimizer</span>

Global food security is threatened by a complex web of interconnected factors: armed conflict, extreme climate change, macroeconomic instability, and forced migration. The HERO project (Hunger Early-warning & Risk Optimizer) was created with the goal of developing a Big Data architecture capable of analytically dissecting these humanitarian crises.

HERO’s primary objective is to move beyond merely describing global hunger and shift toward a highly analytical, predictive approach. The project leverages Big Data architecture and a Machine Learning model to identify the root causes driving food crises and determining their severity on the IPC (Integrated Food Security Phase Classification) scale.
To achieve this, HERO integrates and analyzes diverse global data streams—ranging from socioeconomic dynamics (such as conflict, political instability, and market fluctuations) to climate and environmental drivers (such as drought and precipitation anomalies).
The analysis is conducted at the regional level (Admin1). This choice makes it possible to overcome the severe data scarcity found at the local level (Admin2), ensuring a robust, continuous dataset enriched with global geopolitical indicators that would otherwise be lost at finer resolutions.
In this way, HERO goes beyond capturing a snapshot of the current situation to provide an early-warning tool capable of forecasting evolving risks. This enables humanitarian organizations and policymakers to plan timely, targeted, data-driven interventions before an emergency turns into a catastrophe.



---

## Drivers

To understand the severity of food crises, HERO integrates and monitors various global information flows, each representing a crucial piece of the humanitarian puzzle:

<div class="container mt-4">
    <div class="row">
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-danger">
                <div class="card-body">
                    <h4 class="card-title text-danger"><i class="fas fa-hand-fist"></i> Conflitti (ACLED)</h4>
                    <p class="card-text text-muted">
                        Real-time tracking of political violence events, armed clashes, and attacks against civilians. Data on casualties and the frequency of clashes are normalized per </b>100,000 inhabitants</b> to compare demographically dissimilar areas.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-success">
                <div class="card-body">
                    <h4 class="card-title text-success"><i class="fas fa-cloud-showers-water"></i> Precipitazioni (CHIRPS)</h4>
                    <p class="card-text text-muted">
                        Satellite-based estimation of monthly accumulated rainfall and rainfall anomalies compared to thirty-year historical averages, enabling early identification of prolonged droughts or floods.
                    </p>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-info">
                <div class="card-body">
                    <h4 class="card-title text-info"><i class="fas fa-seedling"></i> Salute della Vegetazione (NDVI)</h4>
                    <p class="card-text text-muted">
                        The NDVI index measures the density and vigor of agricultural crops. It allows for the quantification of agricultural climate shocks before they translate into actual yield loss.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-warning">
                <div class="card-body">
                    <h4 class="card-title text-warning"><i class="fas fa-shopping-basket"></i> Mercati Alimentari (WFP)</h4>
                    <p class="card-text text-muted">
                        Local market prices provided by the World Food Programme. The analysis tracks the cost of the food basket and local inflation of basic necessities, capturing price shocks before they propagate globally."
                    </p>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-secondary">
                <div class="card-body">
                    <h4 class="card-title text-secondary" style="color: #4f46e5 !important;"><i class="fas fa-people-arrows"></i> Sfollati Interni (IDP)</h4>
                    <p class="card-text text-muted">
                        Internal migration flows driven by violence shocks or climate disasters. This parameter is expressed as a percentage of the overall population of the area to assess the residual demographic pressure.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-dark">
                <div class="card-body">
                    <h4 class="card-title text-dark"><i class="fas fa-newspaper"></i> Sentiment e Notizie (GDELT)</h4>
                    <p class="card-text text-muted">
                        Global media flows indexed by QuadClass. Through the quantitative extraction of news tone (sentiment) and salience volume, we monitor the external perception of the crisis.
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

### The Integration of Text Mining: Manuel's BOW
An innovative element introduced in HERO concerns textual analysis applied to historical news flows. We hypothesize that quantitative variables alone do not fully capture the sentiment and context of latent conflicts. Through the integration of a Bag of Words (BOW) methodology developed by Manuel on GDELT flows, we classify the main textual drivers. Keywords and semantic frequencies related to terms like "scarcity", "drought", "attack", or "embargo" are converted into dense numerical variables, providing an immediate media "thermometer" that precedes the actual crisis.

---

## <span class="text-gradient">Risoluzione Territoriale: Admin 1 vs Admin 2</span>

Un pilastro fondamentale dell'architettura dati di HERO è la flessibilità della risoluzione spaziale. Per mappare e analizzare le dinamiche dell'insicurezza alimentare, il nostro sistema organizza e confronta i dati a due livelli amministrativi distinti:

<div class="comparison-table-wrapper">
    <div class="row text-center mb-3">
        <div class="col-md-6 mb-2">
            <span class="badge-premium-admin1 shadow-sm"><i class="fas fa-layer-group"></i> ADMIN LEVEL 1 (Regionale / Provinciale)</span>
        </div>
        <div class="col-md-6 mb-2">
            <span class="badge-premium-admin2 shadow-sm"><i class="fas fa-map-pin"></i> ADMIN LEVEL 2 (Distrettuale / Dipartimentale)</span>
        </div>
    </div>
    <div class="row mt-3">
        <div class="col-md-6 border-right">
            <ul class="lead" style="font-size: 0.95rem; line-height: 1.6;">
                <li><b>Dimensione Dati:</b> ~10.024 osservazioni spaziotemporali.</li>
                <li><b>Integrazione Media (GDELT):</b> Include i segnali e il sentiment estratti dai media tramite GDELT (il tono e la salienza delle notizie sono storicamente georeferenziabili solo a livello Admin 1).</li>
                <li><b>Uso Prediletto:</b> Ideale per il macro-clustering globale, l'identificazione di archetipi nazionali e la generalizzazione di modelli predittivi su scala inter-regionale.</li>
            </ul>
        </div>
        <div class="col-md-6">
            <ul class="lead" style="font-size: 0.95rem; line-height: 1.6;">
                <li><b>Dimensione Dati:</b> ~42.957 osservazioni (4 volte più granulare).</li>
                <li><b>Integrazione Media:</b> Non include i dati GDELT (i flussi giornalistici non sono localizzati a livello distrettuale).</li>
                <li><b>Uso Prediletto:</b> Perfetto per la micro-cartografia digitale, il tracciamento locale della sicurezza alimentare e la rilevazione di micro-anomalie di resilienza o vulnerabilità distrettuale.</li>
            </ul>
        </div>
    </div>
</div>

> [!TIP]
> **Scelta Metodologica**: La scomposizione su due livelli consente ad HERO di passare da una visione strategica e mediatica macroscopica (Admin 1) a una pianificazione tattica e umanitaria locale (Admin 2).

---

## Data Visualization & Visual Analytics: Perché la UI è Essenziale

Nel campo delle crisi umanitarie, i dati grezzi possono risultare opachi o difficili da interpretare per i decisori politici (policy makers) ed esperti delle agenzie internazionali. La piattaforma di visualizzazione web di HERO non è semplicemente un visualizzatore di grafici, ma rappresenta uno strumento essenziale di **Visual Analytics** per diversi motivi chiave:

* **Scomposizione Multidimensionale**: Permette di analizzare simultaneamente l'andamento dell'insicurezza alimentare (IPC3+) a fianco dei driver climatici e di conflitto, agevolando l'identificazione di trend convergenti.
* **Diagnostica e Trasparenza**: Consente di confrontare immediatamente la qualità del dato pre-elaborato (raw vs imputed) per assicurare l'affidabilità delle stime.
* **Analisi di Scenario "What-If"**: Offre un simulatore basato su modelli VAR (Vector Autoregression) in cui gli utenti possono inserire shock sintetici (es. siccità prolungata del 30% o impennata di conflitti) e osservare interattivamente la risposta predittiva dell'IPC per i successivi 6 mesi.

> [!NOTE]
> La UI interattiva consente a chi pianifica gli aiuti umanitari di esplorare scenari futuri in modo intuitivo, traducendo modelli matematici complessi in decisioni pratiche.

### Visualizzazioni di Alto Livello: L'Evoluzione delle Heatmap
Un esempio chiave dell'efficacia delle visualizzazioni di HERO è rappresentato dalle Heatmap dinamiche. Queste mappe di calore bidimensionali tracciano l'evoluzione temporale della gravità alimentare nei diversi territori. A colpo d'occhio, l'analista può visualizzare lo scivolamento di intere regioni verso le fasi più critiche dell'IPC3+ (contrassegnate da tonalità via via più intense), identificando la velocità di propagazione geografica delle crisi.

---

## 🚀 Accedi alla Piattaforma HERO

Puoi esplorare tutti i dati, i grafici cartesiani, le mappe geospaziali e testare il simulatore di scenari interattivo direttamente sulla nostra dashboard:

<div class="text-center my-5">
    <a href="https://github.com/skywalker975/g5-2026-website" class="btn btn-premium-hero btn-lg px-5 py-3 shadow"><i class="fas fa-chart-line mr-2"></i> Esplora la Dashboard HERO</a>
</div>
