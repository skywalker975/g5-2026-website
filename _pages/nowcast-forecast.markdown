---
layout: default
title: "Nowcast & Forecast"
permalink: /nowcast-forecast.html
show_sidetoc: true
header_type: hero
header_img: assets/images/folium_map.webp
header_title: "Nowcast & Forecast"
subtitle: "Modellazione predittiva e proiezioni future delle crisi alimentari"
---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>

# Modellare le Crisi nel Tempo: Previsione ed Inferenza

La fase finale del progetto HERO consiste nella costruzione di modelli statistici e di Machine Learning in grado di effettuare previsioni a breve termine (**Nowcast**) e a medio/lungo termine (**Forecast**) sull'insicurezza alimentare (IPC3+). 

In questa pagina esploriamo l'analisi delle serie storiche regionali, le tecniche di anomaly detection, la modellazione predittiva e l'impatto del clustering sulla stabilità delle stime future.
{: .lead }

---

## 📈 Esplorazione delle Serie Storiche Locali

Prima di addestrare qualsiasi modello previsionale, analizziamo quantitativamente la struttura statistica di ogni singola serie temporale regionale:

```
[Serie Storica Regio] ──> [Test Stazionarietà ADF] ──> [Decomposizione STL] ──> [Cross-Correlazione CCF Lag]
```

* **Analisi di Stazionarietà (Test ADF)**: I modelli classici di forecast richiedono che la serie sia stazionaria. Applichiamo il test **Augmented Dickey-Fuller (ADF)**. In caso di non-stazionarietà (p-value $\ge 0.05$), applichiamo la differenziazione automatica di primo ($d=1$) o secondo ($d=2$) ordine, validando il risultato tramite i correlogrammi ACF/PACF.
* **Decomposizione STL (Seasonal-Trend via LOESS)**: Scomponiamo la serie in tre componenti fondamentali: **Trend** (andamento a lungo termine), **Seasonal** (fluttuazione stagionale ricorrente) e **Residuals** (rumore casuale o shock temporanei).
* **Cross-Correlazione con Lag (CCF)**: Calcoliamo la funzione di cross-correlazione tra i driver esogeni (es. piogge, conflitti) e il target IPC3+ su lag da $-12$ a $+12$ mesi. Questo ci consente di identificare la latenza temporale degli shock (es. dopo quanti mesi un'anomalia climatica produce un picco reale nell'insicurezza alimentare, creando un *early-warning*).

---

## 🛡️ Anomaly Detection e Shapelets

Per catturare shock improvvisi o pattern di vulnerabilità strutturali, HERO implementa due approcci di frontiera:

### 1. Matrix Profile (Motifs & Discords)
Calcolando il **Matrix Profile** su una finestra annuale scorrevole di $m=12$ mesi, isoliamo:
* **Motifs**: Pattern ciclici o ripetitivi di incremento di vulnerabilità.
* **Discords (Anomalie)**: Shock sistemici anomali isolati. Calcolando lo Z-score sui residui, classifichiamo uno shock come sistemico se supera una deviazione standard $Z > 2.0$.

### 2. Subsequence Classification tramite Shapelets
Estraiamo le "Shapelets", ossia brevi sequenze temporali di driver esogeni altamente predittive. Ad esempio, una Shapelet potrebbe identificare che *"un incremento improvviso dell'inflazione WFP abbinato a un calo persistente dell'NDVI per 3 mesi consecutivi"* precede storicamente un'escalation del target IPC3+. La distanza geometrica da questa Shapelet diventa la feature principale del modello di classificazione.

---

## 🔮 Modellazione Predittiva e Impatto del Clustering

La domanda cardine di HERO è: **l'uso del clustering migliora l'inferenza predittiva?** Per dimostrarlo, confrontiamo diverse strategie:

### A. Modelli Locali Indipendenti (Baseline)
Addestriamo modelli univariati locali (ARIMA/SARIMAX ottimizzati tramite AIC/BIC, Holt-Winters, Prophet) provincia per provincia. Sebbene precisi su territori ricchi di dati, questi modelli degradano bruscamente in presenza di serie storiche corte o frammentate.

### B. Global Cluster Forecasting (Transfer Learning)
* **Logica**: Utilizziamo i cluster di province (archetipi di vulnerabilità) identificati nella fase precedente.
* **Metodologia**: Concateniamo le serie storiche di tutte le province del cluster e addestriamo un unico modello globale di Machine Learning (es. **XGBoost globale** o reti neurali ricorrenti LSTM/GRU) sui dati aggregati.
* **Domain Adaptation / Trasferimento Spaziale**: Testiamo la capacità di generalizzazione del modello globale escludendo un intero paese dal cluster durante l'addestramento (es. addestramento su Afghanistan e Somalia, test su Yemen). Il modello globale dimostra di saper trasferire la conoscenza spaziale, effettuando stime accurate anche su territori privi di storico continuo.

### C. Modellazione Multivariata (VAR) e Foundation Models
* **Vector Autoregression (VAR)**: Cattura le interdipendenze multivariate proiettando il target IPC3+ in base all'evoluzione combinata di ACLED e prezzi WFP.
* **Zero-Shot con TimesFM**: Applichiamo il modello di fondazione pre-addestrato di Google `TimesFM` per valutare se un modello generalista pre-addestrato su miliardi di serie storiche possa superare i modelli statistici tradizionali in contesti fragili.

### D. Stacking Ensemble (Meta-Learning)
Integriamo modelli statistici lineari con la flessibilità di modelli non lineari di Machine Learning. Le predizioni dei modelli univariati (ARIMA), del modello multivariato (VAR) e del XGBoost globale vengono fornite in input a un meta-regressore regolarizzato (Ridge/Lasso) che apprende i pesi ottimali da attribuire a ciascuna previsione per produrre il forecast consolidato finale.

---

## 📊 Diagnostica, Spiegabilità (XAI) e Verifica

Per garantire la robustezza scientifica e l'interpretabilità dei modelli, la dashboard presenta:

1. **SHAP Summary Plot (Beeswarm)**: Applichiamo gli additivi SHAP sull'output del modello globale per classificare l'impatto dei descrittori di serie storica (`tsfresh` features come coefficienti di Fourier, autocorrelazione), svelando la "scatola nera" dell'algoritmo.
2. **Model Residuals Diagnostics (4-Panel Plot)**: Grafici che verificano che i residui del modello si comportino come *rumore bianco* (assenza di informazioni residue), analizzandone l'omoschedasticità, la distribuzione normale (Q-Q Plot) e l'assenza di autocorrelazione residua tramite il test di **Ljung-Box**.
3. **Impulse Response Function (IRF) Plot**: Subplots che tracciano l'effetto nei successivi 12 mesi di uno shock improvviso (impulso di una deviazione standard) applicato a un singolo driver esogeno (es. incremento del conflitto ACLED) sull'IPC3+.
