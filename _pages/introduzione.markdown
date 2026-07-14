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

# Il Progetto HERO: Hunger Early-warning & Risk Optimizer

La sicurezza alimentare globale è minacciata da una complessa rete di fattori interconnessi: conflitti armati, cambiamenti climatici estremi, instabilità macroeconomiche e migrazioni forzate. Il progetto **HERO (Hunger Early-warning & Risk Optimizer)** nasce con l'obiettivo di sviluppare un'architettura Big Data in grado di scomporre analiticamente queste crisi umanitarie. 

L'ipotesi di ricerca fondamentale di HERO è che **sfruttare il clustering spaziotemporale delle regioni consenta di migliorare significativamente l'inferenza e le capacità previsionali** del target di insicurezza alimentare, in particolare la classificazione delle fasi IPC (Integrated Food Security Phase Classification).
{: .lead }

---

## I Driver della Crisi: I Flussi Informativi di HERO

Per comprendere la gravità delle crisi alimentari, HERO integra e monitora diversi flussi informativi globali, ciascuno dei quali rappresenta un tassello cruciale del puzzle umanitario:

<div class="container mt-4">
    <div class="row">
        <div class="col-md-6 mb-4">
            <div class="card h-100 shadow-sm border-0">
                <div class="card-body">
                    <h4 class="card-title text-danger"><i class="fas fa-hand-fist"></i> Conflitti (ACLED)</h4>
                    <p class="card-text">
                        Tracciamento in tempo reale di eventi di violenza politica, scontri armati e attacchi contro i civili. I dati sulle vittime e la frequenza degli scontri vengono normalizzati per <b>100.000 abitanti</b> per confrontare aree demograficamente dissimili.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 shadow-sm border-0">
                <div class="card-body">
                    <h4 class="card-title text-success"><i class="fas fa-cloud-showers-water"></i> Precipitazioni (CHIRPS)</h4>
                    <p class="card-text">
                        Stima satellitare delle precipitazioni mensili accumulate e delle anomalie pluviometriche rispetto alle medie storiche trentennali, identificando precocemente l'insorgenza di siccità prolungate o alluvioni.
                    </p>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-6 mb-4">
            <div class="card h-100 shadow-sm border-0">
                <div class="card-body">
                    <h4 class="card-title text-info"><i class="fas fa-seedling"></i> Salute della Vegetazione (NDVI)</h4>
                    <p class="card-text">
                        L'indice NDVI misura la densità e il vigore vegetativo delle colture agricole. Consente di quantificare lo shock climatico agricolo prima che si traduca in una perdita effettiva del raccolto.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 shadow-sm border-0">
                <div class="card-body">
                    <h4 class="card-title text-warning"><i class="fas fa-shopping-basket"></i> Mercati Alimentari (WFP)</h4>
                    <p class="card-text">
                        I prezzi dei mercati locali forniti dal World Food Programme. L'analisi traccia il costo del paniere alimentare e l'inflazione locale dei beni di prima necessità, catturando shock sui prezzi prima della propagazione globale.
                    </p>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-6 mb-4">
            <div class="card h-100 shadow-sm border-0">
                <div class="card-body">
                    <h4 class="card-title text-secondary"><i class="fas fa-people-arrows"></i> Sfollati Interni (IDP)</h4>
                    <p class="card-text">
                        Flussi di migrazione interna provocati da shock di violenza o calamità climatiche. Questo parametro viene espresso come percentuale sulla popolazione complessiva dell'area per valutare la pressione demografica residua.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 shadow-sm border-0">
                <div class="card-body">
                    <h4 class="card-title text-dark"><i class="fas fa-newspaper"></i> Sentiment e Notizie (GDELT)</h4>
                    <p class="card-text">
                        Il flusso globale dei media indicizzato per QuadClass. Attraverso l'estrazione quantitativa del tono (sentiment) e del volume di salienza delle notizie, monitoriamo la percezione esterna della crisi.
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

### L'Integrazione della Text Mining: La BOW di Manuel
Un elemento innovativo introdotto in HERO riguarda l'analisi testuale applicata ai flussi di notizie storiche. Ipotizziamo che le sole variabili quantitative non colgano appieno il sentiment ed il contesto dei conflitti latenti. Attraverso l'integrazione di una metodologia basata sulla **Bag of Words (BOW)** sviluppata da Manuel sui flussi GDELT, andiamo a classificare i driver testuali principali. Le parole chiave e la frequenza semantica legata a parole come *"scarsità"*, *"siccità"*, *"attacco"*, o *"embargo"* vengono convertite in variabili numeriche dense, fornendo un "termometro" mediatico immediato che precede la crisi reale.

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

<div class="text-center my-4">
    <a href="https://github.com/skywalker975/g5-2026-website" class="btn btn-primary btn-lg px-5 py-3 shadow"><i class="fas fa-chart-line mr-2"></i> Esplora la Dashboard HERO</a>
</div>
