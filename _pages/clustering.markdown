---
layout: default
title: "Clustering Spaziotemporale"
permalink: /clustering.html
show_sidetoc: true
header_type: hero
header_img: assets/images/folium_map.webp
header_title: "Clustering Spaziotemporale"
subtitle: "Identificare gli archetipi della vulnerabilità umanitaria"
---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>

# Mappare gli Archetipi di Crisi tramite Clustering

Il cuore metodologico del progetto HERO risiede nell'aggregazione spaziotemporale delle regioni. Invece di trattare ogni provincia come un'entità isolata (il che porterebbe ad addestrare modelli locali instabili in aree con dati scarsi), **raggruppiamo i territori in base alle loro similarità strutturali e dinamiche**. 

Questo processo ci consente di identificare specifici **"archetipi di vulnerabilità"** e di abilitare la modellazione predittiva globale (*Global Forecasting*), trasferendo la conoscenza da province ricche di dati ad aree che presentano lacune storiche significative.
{: .lead }

---

## 🔬 Confronto tra Strategie di Clustering

Per raggruppare i territori, abbiamo implementato ed esplorato tre diverse strategie logiche:

```
                  ┌──> 1. Clustering Vanilla (Statico: Medie Storiche)
                  │
[Dataset HERO] ───┼──> 2. Timeseries-based Clustering (Dinamico: DTW / tsfresh)
                  │
                  └──> 3. NLP-based Clustering (Semantico: GDELT / BOW)
```

### 1. Clustering Vanilla (Statico / Cross-Sectional)
* **Logica**: Il fattore tempo viene collassato calcolando i valori medi storici standardizzati di tutti i driver per ciascun territorio.
* **Vantaggi/Limiti**: È molto semplice e identifica la pura magnitudo delle crisi (es. "Regioni a forte intensità di conflitto statico" vs "Regioni ad alta vulnerabilità climatica"). Tuttavia, perde completamente l'andamento sequenziale, la stagionalità e la dinamica temporale degli shock.

### 2. Timeseries-Based Clustering (Dinamico)
Tratta le osservazioni come sequenze ordinate nel tempo per catturare la forma e la struttura delle serie storiche dei driver. Utilizza due approcci complementari:
* **Feature-Based (`tsfresh` + CBD)**: Estrae centinaia di feature strutturali (trend lineari, coefficienti di Fourier, esponente di Hurst) dalle serie storiche e applica test di ipotesi per selezionare solo le feature correlate al target IPC3+. Utilizza anche la *Compression-Based Dissimilarity (CBD)* per calcolare la dissimiliarità in base alla comprimibilità incrociata delle serie.
* **Shape-Based (Dynamic Time Warping - DTW)**: Calcola la distanza geometrica allineando i punti sull'asse temporale in modo flessibile. Se due province subiscono la stessa crisi di prezzi o pioggia ma con 2 mesi di ritardo l'una rispetto all'altra, il DTW ne riconosce la somiglianza deformando l'allineamento temporale.

### 3. NLP-Based Clustering (Semantico)
* **Logica**: Raggruppa i territori in base al profilo semantico dei flussi di notizie. Sfruttando la **Bag of Words (BOW)** dei termini estratti dagli articoli georeferenziati di GDELT, andiamo a creare un profilo tematico e di sentiment dei media che definisce l'attenzione e il tipo di emergenza di cui parlano i canali informativi locali ed internazionali.

---

## 🛠️ Confronto tra Tecniche e Algoritmi

Abbiamo valutato le performance geometriche e di interpretabilità di diversi algoritmi di clustering:

* **Hierarchical Clustering (WARD Linkage)**: Ideale per ricostruire la gerarchia di somiglianza. Il metodo di collegamento WARD minimizza la varianza interna dei cluster, producendo dendrogrammi puliti che mostrano visivamente come le province si aggregano a vari livelli di dettaglio.
* **K-Means**: Utilizzato come baseline robusta per la partizione geometrica dello spazio vettoriale ridotto tramite PCA. È veloce ma assume cluster sferici e risente degli outlier spaziotemporali.
* **DBSCAN (Density-Based)**: Utilizzato specificamente per la rilevazione di anomalie geografiche (*Spatial Outlier Detection*). DBSCAN identifica le province atipiche (classificate come rumore) che, pur trovandosi vicino a aree colpite da forti crisi, mostrano comportamenti discordanti e quindi dinamiche di resilienza locale.

---

## 🌍 Analisi Geografica Multilivello

Il clustering in HERO ci ha permesso di effettuare confronti a tre diversi livelli della gerarchia geografica:

<div class="row mt-4">
    <div class="col-md-4">
        <div class="card h-100 shadow-sm border-light">
            <div class="card-body">
                <h5 class="card-title text-primary"><i class="fas fa-globe"></i> Confronto tra Paesi</h5>
                <p class="card-text text-muted">
                    Analisi macroeconomica e geopolitica a livello nazionale. Consente di raggruppare interi stati sotto profili di stabilità o vulnerabilità sistemica strutturale.
                </p>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card h-100 shadow-sm border-light">
            <div class="card-body">
                <h5 class="card-title text-success"><i class="fas fa-map-marked-alt"></i> Confronto Intra-Paese</h5>
                <p class="card-text text-muted">
                    Confronto tra regioni dello stesso Stato. Mostra la disparità interna, isolando ad esempio le province colpite da conflitti attivi da quelle soggette solo a shock climatici stagionali.
                </p>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card h-100 shadow-sm border-light">
            <div class="card-body">
                <h5 class="card-title text-info"><i class="fas fa-project-diagram"></i> Confronto Cross-Regionale</h5>
                <p class="card-text text-muted">
                    Confronto tra province di paesi diversi. Rivela "gemelli di vulnerabilità" (es. una provincia dello Yemen e una della Somalia che, pur geograficamente distanti, condividono gli stessi identici driver di siccità e instabilità dei prezzi).
                </p>
            </div>
        </div>
    </div>
</div>

---

## 📊 Visualizzazioni Chiave per l'Esplorazione dei Cluster

Per rendere questi raggruppamenti comprensibili, la nostra piattaforma di Visual Analytics integra:

1. **Dendrogramma Gerarchico Spaziotemporale**: Grafico ad albero basato su feature tsfresh e distanze DTW che illustra la tassonomia di aggregazione dei territori.
2. **Heatmap delle Distanze di Forma DTW**: Matrice simmetrica $N \times N$ colorata con scale di colore divergenti per visualizzare graficamente la dissimilarità di forma temporale tra tutte le province.
3. **Scatter Plot PCA dei Cluster**: Proiezione bidimensionale dello spazio delle feature per valutare la separabilità geometrica e la densità delle province all'interno dei rispettivi cluster di appartenenza.
4. **Mappe Choropleth Nazionali e Regionali**: Mappe tematiche geografiche che colorano le regioni in base al cluster dinamico di appartenenza, evidenziando a colpo d'occhio la contiguità spaziale dei comportamenti dinamici estratti.
