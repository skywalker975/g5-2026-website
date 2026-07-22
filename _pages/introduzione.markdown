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

## I Driver della Crisi: I Flussi Informativi di HERO

Per comprendere la gravità delle crisi alimentari, HERO integra e monitora diversi flussi informativi globali, ciascuno dei quali rappresenta un tassello cruciale del puzzle umanitario:

<div class="container mt-4">
    <div class="row">
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-danger">
                <div class="card-body">
                    <h4 class="card-title text-danger"><i class="fas fa-hand-fist"></i> Conflitti (ACLED)</h4>
                    <p class="card-text text-muted">
                        Tracciamento in tempo reale di eventi di violenza politica, scontri armati e attacchi contro i civili. I dati sulle vittime e la frequenza degli scontri vengono normalizzati per <b>100.000 abitanti</b> per confrontare aree demograficamente dissimili.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-success">
                <div class="card-body">
                    <h4 class="card-title text-success"><i class="fas fa-cloud-showers-water"></i> Precipitazioni (CHIRPS)</h4>
                    <p class="card-text text-muted">
                        Stima satellitare delle precipitazioni mensili accumulate e delle anomalie pluviometriche rispetto alle medie storiche trentennali, identificando precocemente l'insorgenza di siccità prolungate o alluvioni.
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
                        L'indice NDVI misura la densità e il vigore vegetativo delle colture agricole. Consente di quantificare lo shock climatico agricolo prima che si traduca in una perdita effettiva del raccolto.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-warning">
                <div class="card-body">
                    <h4 class="card-title text-warning"><i class="fas fa-shopping-basket"></i> Mercati Alimentari (WFP)</h4>
                    <p class="card-text text-muted">
                        I prezzi dei mercati locali forniti dal World Food Programme. L'analisi traccia il costo del paniere alimentare e l'inflazione locale dei beni di prima necessità, catturando shock sui prezzi prima della propagazione globale.
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
                        Flussi di migrazione interna provocati da shock di violenza o calamità climatiche. Questo parametro viene espresso come percentuale sulla popolazione complessiva dell'area per valutare la pressione demografica residua.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-dark">
                <div class="card-body">
                    <h4 class="card-title text-dark"><i class="fas fa-newspaper"></i> Sentiment e Notizie (GDELT)</h4>
                    <p class="card-text text-muted">
                        Il flusso globale dei media indicizzato per QuadClass. Attraverso l'estrazione quantitativa del tono (sentiment) e del volume di salienza delle notizie, monitoriamo la percezione esterna della crisi.
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>


---

<div class="storytelling-hero-wrapper text-center mb-5">
    <span class="badge-premium-admin1 shadow-sm mb-2"><i class="fas fa-quote-left"></i> DATA STORYTELLING</span>
    <h1 class="text-gradient font-weight-bold">From Words to Data: Mapping Famine Drivers Through Term Frequency</h1>
</div>

<p class="lead" style="font-size: 1.1rem; line-height: 1.7; text-align: justify;">
In IPC reports, words are never neutral: their recurrence forms the digital footprint of a real-world emergency. Textual analysis reveals that the bigram <b>'food insecurity'</b> dominates the dataset with 1,068 occurrences, frequently paired with critical terms like <b>'acute'</b> (658) and <b>'malnutrition'</b> (154). However, it is the underlying drivers that shape this semantic map. The frequency of words like <b>'price'</b> (524) highlights economic shocks and barriers to food access, while the agricultural production cluster (<i>'production'</i>, <i>'harvest'</i>, <i>'crop'</i>) captures the immediate impact of climate factors on the ground. In this context, counting words means mapping the boundaries of hunger.
</p>

---

## <span class="text-gradient">The Crisis Algorithm: Drivers of Food Insecurity</span>

Behind the IPC data architecture lies the convergence of macroeconomic, climatic, and social forces. By analyzing the semantic patterns within the reports, the primary catalysts of hunger emerge clearly across three interconnected macro-drivers:

<div class="comparison-table-wrapper">
    <div class="row text-center mb-3">
        <div class="col-md-4 mb-2">
            <span class="badge-premium-admin1 shadow-sm"><i class="fas fa-chart-line"></i> ECONOMIC SHOCKS (Access)</span>
        </div>
        <div class="col-md-4 mb-2">
            <span class="badge-premium-admin2 shadow-sm"><i class="fas fa-cloud-sun-rain"></i> CLIMATE FACTORS (Availability)</span>
        </div>
        <div class="col-md-4 mb-2">
            <span class="badge-premium-admin1 shadow-sm"><i class="fas fa-shield-alt"></i> STRUCTURAL INSTABILITY (Vulnerability)</span>
        </div>
    </div>
    <div class="row mt-3">
        <div class="col-md-4 border-right">
            <ul class="lead" style="font-size: 0.95rem; line-height: 1.6;">
                <li><b>Key Words:</b> <i>price</i> (524), <i>food price</i> (221), <i>access</i> (399), <i>income</i>, <i>market</i>.</li>
                <li><b>Market Dynamics:</b> Hunger unfolds primarily as a purchasing power crisis. Inflationary spikes build invisible financial barriers: food remains on shelves but becomes entirely unaffordable for vulnerable households.</li>
            </ul>
        </div>
        <div class="col-md-4 border-right">
            <ul class="lead" style="font-size: 0.95rem; line-height: 1.6;">
                <li><b>Key Words:</b> <i>production</i> (346), <i>harvest</i> (316), <i>crop</i> (315), <i>drought</i>, <i>rain</i>.</li>
                <li><b>Agricultural Collapse:</b> This reflects the systemic breakdown of local livelihoods (<i>livelihood</i>, 450). Weather anomalies and droughts destroy crops upstream, triggering physical supply deficits and rural income loss.</li>
            </ul>
        </div>
        <div class="col-md-4">
            <ul class="lead" style="font-size: 0.95rem; line-height: 1.6;">
                <li><b>Key Words:</b> <i>conflict</i>, <i>displacement</i>, <i>humanitarian assistance</i> (140), <i>food consumption</i> (195).</li>
                <li><b>Breaking Point:</b> Conflicts and forced displacement shatter local trade networks and drive populations to flee. At this tipping point, food consumption plummces, making external humanitarian aid vital to bridge survival deficits.</li>
            </ul>
        </div>
    </div>
</div>


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
