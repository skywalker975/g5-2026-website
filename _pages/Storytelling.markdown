---
layout: default
title: "Storytelling"
permalink: /Storytelling.html
show_sidetoc: true
header_type: hero
header_img: assets/images/folium_map.webp
header_title: "HERO"
subtitle: "Hunger Early-warning & Risk Optimizer"
---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>

# Introduction
# <span class="text-gradient">Zero Hunger by 2030: a promise still unfulfilled</span>
In 2015, all United Nations Member States adopted the 2030 Agenda for Sustainable Development, whose second goal — "Zero Hunger" (SDG 2) — commits the international community to «end hunger, achieve food security and improved nutrition and promote sustainable agriculture». Over a decade later, that promise remains dramatically distant.
{: .lead }
In 2024, approximately 673 million people were still undernourished, and in 2025, 266 million in 47 countries were facing acute food insecurity; in the same year, famine was confirmed in certain areas of the Gaza Strip and Sudan. Hunger, in short, remains a present-day emergency.
{: .lead }
It is precisely to tackle this urgent challenge that the HERO project was born. HERO aims to leverage advanced data analysis and predictive modeling to infer the root causes of food crises before they escalate, providing actionable insights to help the global community stay on track toward achieving Zero Hunger.
# Paris's agreement
The Paris Agreement is a legally binding international climate treaty adopted in 2015 that aims to limit global temperature increase to 1.5°C above pre-industrial levels. It drives action through a five-year cycle where countries submit increasingly ambitious Nationally Determined Contributions (NDCs) to reduce greenhouse gas emissions and build climate resilience. The treaty establishes a framework for developed nations to provide financial, technological, and capacity-building support to vulnerable countries. Global progress is rigorously tracked via an Enhanced Transparency Framework and a Global Stocktake, collectively accelerating the worldwide transition toward zero-carbon economies.

# Food Insecurity

### Trends of food insecurity
MODIFICA: SUDAN HA DOPPIO PUNTO NEL GRAFICO (AGGREGATO E SINGOLO)
- Grafico (assets/toADD/sito/HTI_vs_SSD_SDN.html)
  .haiti trend crescente, sud sudan trend stabile ma con oscillazioni
  .sudan inizio livelli bassi di insicurezza alimientari e shock da 15/4/23 in poi
  The graph illustrates the aggregated percentage of the population experiencing IPC
  Phase 3+ food insecurity across three nations from 2017 to 2026. Haiti demonstrates a
  sustained, secular upward trend, with acute food insecurity climbing steadily from below 20%
  in late 2017 to over 50% by 2026. In contrast, South Sudan exhibits a stable longitudinal
  baseline but is characterized by severe, high-amplitude oscillations, repeatedly fluctuating
  between approximately 35% and 65%. Sudan presents a distinctly different trajectory: the
  country maintained comparatively low levels of food insecurity (remaining under 25%) until
  early 2023. Following the onset of systemic conflict on April 15, 2023, Sudan experienced a
  massive structural shock, resulting in a sudden, sharp escalation in food insecurity that
  peaked near 55%, completely destabilizing its previous baseline.
  
-grafico( assets/toADD/sito/SDN_3+.html)
  .aggiungere linea rossa 15/4/23 in poi (inizio shock)
  .descrizione guerra in sudan: The Sudanese civil war, initiated in April 2023, is a violent power struggle between the Sudanese Armed Forces (SAF) and the Rapid Support Forces (RSF) following a 2021 coup. The conflict has triggered a catastrophic humanitarian crisis resulting in the displacement of over 14 million people. It has produced extreme food insecurity metrics, with 25 million individuals affected by severe shortages and famine, severely compounding the difficulty of clustering and analyzing accurate humanitarian reports on the ground. Current fatality estimates reach up to 400,000
 
 testo: Prior to the conflict's onset, the percentage of the aggregated population experiencing IPC Phase 3+ acute food insecurity oscillated within a relatively stable, though concerning, baseline between roughly 13% and 25% from July 2019 through early 2023.
Following the start of the conflict in early 2023, the data exhibits a violent upward inflection point. By July 2023, the insecurity metric breaches 40%, demonstrating an immediate and severe degradation of logistical and agricultural stability. This sharp escalation continues unabated, propelling the food insecurity level to a devastating peak of nearly 55% by mid-2024. While there is a slight regression following this peak, the baseline has been fundamentally destabilized; the metric remains structurally elevated well above 40% through January 2026, indicating a prolonged, systemic humanitarian crisis with no return to pre-war levels.

-grafico Afghanistan (assets/toADD/sito/AFG_IPC3+.html)
 .trend stabile basso
 .shock 5/2021 ritiro truppe USA e poi diminuzione trend
testo:The graph presented tracks the aggregated percentage of the population facing IPC Phase 3+ acute food insecurity. Initially, the metric fluctuates around a relatively stable, low baseline. This stability is violently disrupted by a massive structural shock beginning in May 2021, coinciding with the withdrawal of US troops. This geopolitical event acts as a catalyst for a sharp escalation in acute food insecurity, driving the population percentage to a peak of nearly 55%. Following this acute crisis phase, the data demonstrates a steady, though volatile, downward trajectory, with food insecurity levels progressively declining through 2026 to settle back near 20%.

 - Stagionalità Sus Sudan (assets/toADD/sito/01_Statistical_Decomposition_STL.png)
   .stagionalità visibile fino a 2020 (COVID) e poi si perde il dato
   .ha senso metterlo?
   testo: The Seasonal and Trend-Loess (STL) decomposition illustrates a drastic structural break in the time series data. Through 2018 and 2019, the seasonal component exhibits a distinct, regular periodicity with a pronounced amplitude, indicating a strong underlying cyclical pattern. However, corresponding with the systemic shock of the COVID-19 pandemic in 2020, this established cyclicality abruptly deteriorates. The seasonal signal heavily flattens and loses its predictable rhythmic structure, demonstrating that the standard temporal patterns were completely disrupted and the historical seasonal signature was effectively erased from the data post-2020.


# Project description
<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/Progetto-Hero.png" alt="Heatmap of Food Insecurity Drivers by Country" class="img-fluid rounded shadow-lg" style="max-width: 100%; border: 1px solid #e0e0e0;">
</div>

# <span class="text-gradient">HERO: Hunger Early-warning & Risk Optimizer</span>

Global food security is threatened by a complex web of interconnected factors: armed conflict, extreme climate change, macroeconomic instability, and forced migration. The HERO project (Hunger Early-warning & Risk Optimizer) was created with the goal of developing a Big Data architecture capable of analytically dissecting these humanitarian crises.

HERO’s primary objective is to move beyond merely describing global hunger and shift toward a highly analytical, predictive approach. The project leverages Big Data architecture and a Machine Learning model to identify the root causes driving food crises and determining their severity on the IPC (Integrated Food Security Phase Classification) scale.
To achieve this, HERO integrates and analyzes diverse global data streams—ranging from socioeconomic dynamics (such as conflict, political instability, and market fluctuations) to climate and environmental drivers (such as drought and precipitation anomalies).
The analysis is conducted at the regional level (Admin1). This choice makes it possible to overcome the severe data scarcity found at the local level (Admin2), ensuring a robust, continuous dataset enriched with global geopolitical indicators that would otherwise be lost at finer resolutions (Cit. Alice Giorgio | Data scientist | WFP, data in our area are a mess and missing data are the main aspect to adress).
In this way, HERO goes beyond capturing a snapshot of the current situation to provide an early-warning tool capable of forecasting evolving risks. This enables humanitarian organizations and policymakers to plan timely, targeted, data-driven interventions before an emergency turns into a catastrophe.

-- METTERE IMMAGINE ANIMATA PAESI CHE SI SPENGONO E ACCENDONO NEL TEMPO -- paesi nelle varie fasi (rosso tenue fasi iniziali e rosso scuro fasi più gravi)



-- why we move from national to admin1 level analysis
### Events of extreme levels of food insecurity (IPC Phase 5)
<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/toADD/sito/SSD_temporal_anomalies.png" alt="Static inference, per-country detail, one marker per scope" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>We shift to admin1-level analysis to capture sub-national variances and cross-border similarities that broad national averages obscure. While admin2 provides better granularity, severe data sparsity renders it analytically unviable. Admin1 strikes the optimal balance, ensuring robust data availability while retaining sufficient detail to expose localized anomalies.</small></p>
</div> 

# Food Insecurity through the lens of its Main Drivers
## Drivers description

To understand the severity of food crises, HERO integrates and monitors various global information flows, each representing a crucial piece of the humanitarian puzzle:

<div class="container mt-4">
    <div class="row">
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-danger">
                <div class="card-body">
                    <h4 class="card-title text-danger"><i class="fas fa-hand-fist"></i> Conflicts (ACLED)</h4>
                    <p class="card-text text-muted">
                        Real-time tracking of political violence events, armed clashes, and attacks against civilians. Data on casualties and the frequency of clashes are normalized per </b>100,000 inhabitants</b> to compare demographically dissimilar areas.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-success">
                <div class="card-body">
                    <h4 class="card-title text-success"><i class="fas fa-cloud-showers-water"></i> Precipitation (CHIRPS)</h4>
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
                    <h4 class="card-title text-info"><i class="fas fa-seedling"></i> Vegetation Health (NDVI)</h4>
                    <p class="card-text text-muted">
                        The NDVI index measures the density and vigor of agricultural crops. It allows for the quantification of agricultural climate shocks before they translate into actual yield loss.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-warning">
                <div class="card-body">
                    <h4 class="card-title text-warning"><i class="fas fa-shopping-basket"></i> Food Markets (WFP)</h4>
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
                    <h4 class="card-title text-secondary" style="color: #4f46e5 !important;"><i class="fas fa-people-arrows"></i> Internally Displaced Persons (IDP)</h4>
                    <p class="card-text text-muted">
                        Internal migration flows driven by violence shocks or climate disasters. This parameter is expressed as a percentage of the overall population of the area to assess the residual demographic pressure.
                    </p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4">
            <div class="card h-100 hero-card card-border-top-dark">
                <div class="card-body">
                    <h4 class="card-title text-dark"><i class="fas fa-newspaper"></i> Sentiment and news (GDELT)</h4>
                    <p class="card-text text-muted">
                        Global media flows indexed by QuadClass. Through the quantitative extraction of news tone (sentiment) and salience volume, we monitor the external perception of the crisis.
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

### Trends of food insecurity x trends of drivers+
- Inserire grafici drivers (AFFIANCARLI UNO A ALTRO E NON SOVRAPPORLI)
- confrontare i trends dei drivers con trends food insecurity (c'è una correlazione)

### Seasonality of food insecurity x trends of drivers+
-Inserire grafici (AFFIANCARLI UNO A ALTRO E NON SOVRAPPORLI)
-possiamo far vedere stagionalità (CHIRPS E NDVI)
-anche i drivers meno sensibili a stagionalità hanno stagionalità (ACLED e IDP)

### Missing data
-grafico (assets/toADD/sito/datiMancanti.html)
 .alta presenza di valori nulli (specialmente ACLED)
 .paesi con molti valori nulli e altri con meno.
 .**CITAZIONE INTERVISTA** "i missing values sono un pain point"
 .problemi per modelli predittivi.
 .presenza maggiore di valori nulli a livello admin2
 .importante capire origine valori nulli (blackout ACLED per assenza conflitti o mancata rilevazione per via dei conflitti?          mancanza rilevazione WFP per presenza conflitti?)
  **citazione intervista**: "Since we don't know the root causes of the missing data, performing imputation could compromise explainability. This can be partly linked to the shadow matrix (Acled). It could also be cross-referenced with external data. Missing values are the main issue in our analysis. If IDP is missing, it could mean several things: it's too dangerous, or the surveys cover very few people."
The prevalence of missing values constitutes the primary obstacle in this analysis, representing a significant "pain point" that severely degrades the performance and reliability of predictive models. As evidenced by the missingness matrix, there is a high concentration of null values characterized by stark disparities across different countries. Furthermore, data sparsity increases significantly at the admin2 level compared to broader aggregations, with the ACLED dataset being particularly compromised.
Understanding the precise origin of these missing values is critical before applying any statistical interventions. As noted in stakeholder interviews, implementing blind imputation without knowing the underlying causes of the data gaps actively harms the explainability of the models. The absence of data is rarely random; for instance, an ACLED blackout could signify a genuine absence of conflict, or conversely, a situation so violently unstable that on-the-ground reporting has collapsed. Similarly, missing IDP or WFP data often translates to environments that are too dangerous for humanitarian surveyors to operate in, or situations where survey sample sizes are critically low. To mitigate these structural blind spots, analytical strategies must cross-reference external data sources—as suggested by Manuel—or utilize shadow matrices for datasets like ACLED to explicitly capture and model the missingness itself, rather than arbitrarily filling the voids.

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}assets/images/ANALISI_NULLI_correlazione_strutturale.png" alt="sbd-pattern" class="full-width-image">
     <p class="text-muted mt-2"><small>

The structural analysis of missingness reveals that data gaps across the evaluated humanitarian datasets are distinctly non-random and highly correlated. This structural missingness offers critical explainability regarding systemic data collection failures, demonstrating that outages occur in distinct functional blocks. Environmental sensor blackouts exhibit severe collinearity, highlighted by a 0.92 correlation between NDVI and CHIRPS, meaning that when one satellite metric fails, the other is almost guaranteed to be offline. Concurrently, the loss of conflict tracking data (ACLED) is critically linked to logistical blindness in the field; it correlates strongly with missing market vulnerability data (WFP, 0.65) and displacement metrics (IDP, 0.60). This indicates that kinetic events directly disrupt on-the-ground humanitarian reporting pipelines, resulting in compounded analytical blind spots during periods of acute crisis.</small></p>
</div>
 
### Clustering based on main drivers (quantitative)
To find the best imputation method for our missing data, we first needed to evaluate how geographic proximity and statistical patterns influence the data structure. We compared two scenarios — one based strictly on statistical profiles and another incorporating geographic coordinates — across different clustering approaches (such as Hierarchical and K-Means).
Ultimately, we selected KNN (K-Nearest Neighbors) because it achieved the highest silhouette score, proving to be the most effective at identifying coherent and well-separated neighbors. This ensures that missing values are imputed using truly similar data points, maintaining high data integrity, even though, imputation create high level of uncertanty. In the interview that we hade with Alice Giorgio, we discussed the matter. Alice highlight how, in a context, where data collection can not be always guaranteed, the output of the models accept the risks arising from high uncertenty.


-- also show how admin1s across countries are similar 


# Qualitative Profiles of Food Insecurity
### Text analysis
### Text-based clusters etc


# Predicting Food Insecurity through its drivers

Can the drivers predict hunger? We ask two questions, each with its own model.

<div style="background-color: #e8f4fa; border-left: 5px solid #0284c7; border-radius: 6px; padding: 1rem 1.25rem; margin-top: 1.5rem; margin-bottom: 1.25rem;">
<div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #0369a1;">Question 1 · Static inference</div>
<h4 style="font-weight: 700; margin: 0.25rem 0 0; color: #0369a1;">What explains where hunger is?</h4>
</div>

- Hunger is very context dependent: the same drop in rainfall or the same level of conflict means different things in the Sahel, the Horn of Africa, or Central America. One global rule has to fit all of them at once, so it does not even beat a simple baseline: the average level of each country.
- Localising fixes this. We train separate models for smaller groups of similar areas, for example one model per country, or one per geographic region. The grouping that works best is by what an area's IPC reports actually talk about, such as conflict and refugees, farming and water, or prices and inflation.
- Food prices and conflict are the strongest drivers.

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/static_scope_box.png" alt="Accuracy by grouping method" class="img-fluid rounded shadow-lg" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Accuracy by grouping method, scored per country. Boxes to the right of the dashed global line do better. Grouping by report text wins.</small></p>
</div>

> "Explainability is even more important than performance." —  WFP data scientist

In humanitarian work, decisions affect lives, so results have to be explainable before anyone acts on them.

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/nowcast/static_shap_beeswarm.png" alt="Which drivers explain hunger" class="img-fluid rounded shadow-sm hover-lift" style="max-width: 100%; border: 1px solid #e0e0e0;">
    <p class="text-muted mt-2"><small>Higher food prices and more conflict push the predicted level of hunger up.</small></p>
</div>

<div style="background-color: #fff8e1; border-left: 5px solid #e0a800; border-radius: 6px; padding: 1rem 1.25rem; margin-top: 2rem; margin-bottom: 1.25rem;">
<div style="text-transform: uppercase; letter-spacing: 0.5px; font-size: 0.75rem; font-weight: 700; color: #a16207;">Question 2 · Nowcasting</div>
<h4 style="font-weight: 700; margin: 0.25rem 0 0; color: #a16207;">What are hunger levels right now?</h4>
</div>

IPC assessments are slow, so a shock can go unseen for months. We developed a nowcasting model to accurately estimate the current level from the last assessment plus the latest drivers.

- About 18 percent lower error than carrying the last value forward, and it tracks the direction of change.
- One global model is enough here, the opposite of the static question. Once the model knows an area's own last value, a local model adds little.
- Rainfall is the strongest early signal among the drivers.

<div class="my-4">
    <iframe src="{{ site.baseurl }}/assets/charts/nowcast_map.html" width="100%" height="640px" style="border: 1px solid #e0e0e0; border-radius: 0.5rem;" loading="lazy" title="HERO live nowcast map"></iframe>
    <p class="text-muted mt-2"><small>Latest nowcast of the share of people in IPC Phase 3 or above. Hover for the trend, click to zoom.</small></p>
</div>

<div class="my-4 text-center">
    <a href="{{ site.baseurl }}/modelling.html" class="btn btn-premium-hero">Read the full modelling details</a>
</div>


# Conclusion + UI
