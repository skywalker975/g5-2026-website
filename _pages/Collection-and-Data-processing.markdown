---
layout: default
title: "Data Collection and Preprocessing"
permalink: /Collection-and-Data-processing.html
show_sidetoc: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Data Collection and Preprocessing"
subtitle: "From raw data heterogeneity to spatiotemporal harmonization"
---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>

# La Sfida del Dato Umanitario: Pulizia e Armonizzazione

L'integrazione di flussi informativi globali presenta notevoli sfide tecniche. I dati provengono da sorgenti eterogenee con diverse scale spaziali (coordinate di conflitti ACLED, mercati puntuali WFP, pixel satellitari NDVI) e frequenze temporali svariate (giornaliera, settimanale, mensile). La nostra missione iniziale è stata armonizzare queste informazioni e, soprattutto, affrontare il grande "antagonista" delle analisi predittive: **il dato mancante (NaN)**.
{: .lead }

---

## Storytelling: Cosa abbiamo fatto vs Come ci siamo arrivati?

Nello sviluppo del nostro progetto, ci siamo posti una domanda fondamentale per il nostro storytelling: **dobbiamo raccontare semplicemente la pipeline finale o documentare il percorso che ci ha condotto fin qui?** 

La risposta è una via di mezzo integrata:
1. **La Destinazione (Cosa abbiamo fatto)**: Presentiamo una pipeline solida e riproducibile che normalizza e imputa i dati spaziotemporali.
2. **Il Viaggio (Come ci siamo arrivati)**: Mostriamo le criticità incontrate lungo il cammino, giustificando le scelte complesse (come il KNN geografico) rispetto a soluzioni più banali (come il *Forward Fill* temporale o l'imputazione con la media), evidenziando l'impatto distorsivo che tali soluzioni semplici avrebbero avuto sulle analisi.

---

## 🛠️ Pipeline di Preprocessing e Armonizzazione

Il flusso KDD (Knowledge Discovery in Databases) applicato si divide in tre macro-passaggi chiave:

```
[Dati Eterogenei] ──> [Normalizzazione Demografica] ──> [Allineamento Frequenze] ──> [Gestione del Dato Mancante (KNN/Country-Bounded)]
```

### 1. Join Spaziale ed Allineamento Geografico
Le coordinate geografiche dei singoli eventi di conflitto e dei mercati alimentari sono state associate alle rispettive unità amministrative provinciali (Admin 1 o Admin 2) tramite un join spaziale basato sulle coordinate poligonali ufficiali delle mappe. 

### 2. Normalizzazione Demografica (Standardizzazione per 100k Abitanti)
Per evitare bias dovuti alla grandezza delle regioni (ad esempio, un alto numero di sfollati o di scontri in province popolose che oscura la gravità relativa in province più piccole), abbiamo standardizzato i driver di conflitto (**ACLED** eventi e vittime) e le migrazioni interne (**IDP**) per **100.000 abitanti**. Gli sfollati interni (IDP) sono stati espressi anche come percentuale della popolazione totale dell'area per valutarne la densità locale dello shock.

### 3. Allineamento e Risoluzione Temporale Nativa
* **Join con il Target (IPC)**: Per alimentare i modelli predittivi standard e calcolare le correlazioni dirette con l'insicurezza alimentare (IPC), abbiamo riallineato temporalmente i driver su una griglia mensile uniforme (`MS` - Month Start).
* **Conservazione Frequenza Nativa**:
  > [!IMPORTANT]
  > Per le analisi indipendenti (come la rete di mercati WFP o l'anomaly detection sui prezzi), **abbiamo mantenuto la frequenza temporale nativa non aggregata** (giornaliera o settimanale dei prezzi) al fine di catturare con massima precisione i lag temporali a breve termine e la velocità di trasmissione degli shock macroeconomici.

---

## 🔍 La Ricostruzione dei Dati Mancanti (Imputazione)

Per colmare i buchi temporali o territoriali, HERO implementa due logiche di imputazione avanzate:

### A. Country-Bounded Reconstruction (Ricostruzione su Base Nazionale)
Gli shock macroeconomici, l'inflazione monetaria e i cicli stagionali agricoli tendono a essere simili all'interno dello stesso paese. Pertanto, la ricostruzione dell'IPC e di altri driver opera separando i dati per nazione (`groupby('Country')`). Se una provincia A presenta dati mancanti in determinati mesi, questi vengono stimati come combinazione spaziotemporale pesata dei dati storici completi delle province limitrofe appartenenti al medesimo Stato.

### B. Algoritmo `impute_missing_knn_geo_similarity`
Sfrutta un imputer KNN (`sklearn.impute.KNNImputer`) inserendo le coordinate spaziali (`latitude` e `longitude` standardizzate) direttamente nel calcolo delle distanze. Le aree vicine nello spazio geografico tendono a condividere lo stesso meteo e gli stessi mercati, garantendo un'imputazione accurata che non distorce le distribuzioni reali delle variabili. L'algoritmo riduce dinamicamente il parametro `n_neighbors` in caso di campioni storici ridotti a livello regionale.

---

## 📊 Visualizzazioni per la Diagnostica del Preprocessing

Per validare la fedeltà del preprocessing ed evitare che l'imputazione introducesse bias o distorsioni nei dati reali, abbiamo implementato tre visualizzazioni diagnostiche fondamentali nella nostra dashboard:

1. **Missingness Heatmap (Prima vs Dopo)**: Una matrice visuale che mostra in nero i dati mancanti prima dell'applicazione degli algoritmi e in bianco il dataset completamente popolato dopo il KNN spaziale e la ricostruzione nazionale.
2. **Density Plots di Controllo (KDE Plot)**: Grafici a curve di densità probabilistica che confrontano la distribuzione originale di ciascun driver (es. inflazione dei mercati, precipitazioni) con la distribuzione dopo l'imputazione. Ciò garantisce che l'algoritmo non abbia appiattito o spostato sistematicamente la forma probabilistica dei dati storici.
3. **Mappa Spaziale delle Imputazioni**: Una mappa interattiva georeferenziata con marcatori colorati in scala per identificare a colpo d'occhio le aree a maggiore intensità di ricostruzione dei dati, assicurando la trasparenza scientifica dell'intero workflow.
