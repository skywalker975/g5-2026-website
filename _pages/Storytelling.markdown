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
<iframe src="assets/toADD/sito/HTI_vs_SSD_SDN_modificato.html" width="100%" height="600" style="border:none;"></iframe>
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
<iframe src="assets/toADD/sito/SDN_3_modificato_v2.html" width="100%" height="600" style="border:none;"></iframe>
  .descrizione guerra in sudan:
  testo: From mid-2019 to early 2023, the share of Sudan's population facing severe food insecurity (IPC Phase 3+)
  remained relatively low and stable, staying between 13% and 25%.
  That changed in April 2023, when civil war broke out between the Sudanese Armed Forces (SAF) and
  the Rapid Support Forces (RSF) after the 2021 coup.
  Food insecurity then rose sharply. Within a year, it more than doubled — climbing from around 35% to a 
  peak of over 53% by mid-2024.
  Levels have stayed high ever since, remaining between 40% and 50% through 2025. The impact goes far
  beyond this chart: the war has forced more than 14 million people from their homes, left around 25
  million facing severe hunger, and caused an estimated 400,000 deaths — making it one of the worst
  humanitarian crises in the world today.
 
 testo: Before the conflict's began, the percentage of the aggregated population
 experiencing IPC Phase 3+ acute food insecurity stayed within a relatively stable range, though still concerning — moving between roughly 13% and 25% from July 2019 through early 2023.
 Once the the conflict began in early 2023, the data takes a dramatic turn upward. By
 July 2023, the insecurity metric passes the 40% mark, demonstrating an immediate and severe degradation of
 logistical and agricultural stability. The numbers kept rising, reaching a devastating peak of nearly 55%
 by mid-2024. Although levels have eased slightly since that peak they haven't gone back down. 
 The metric remains structurally elevated well above 40% through January 2026, showing that this isn't a
 temporary spike, but a lasting crisis with no sign of returning to pre-war conditions.

-grafico Afghanistan 
<iframe src="assets/toADD/sito/AFG_IPC3+_modificata.html" width="100%" height="600" style="border:none;"></iframe>
 .trend stabile basso
 .shock 5/2021 ritiro truppe USA e poi diminuzione trend
testo:The graph presented tracks the aggregated percentage of the population facing IPC Phase 3+ acute food insecurity. Initially, the metric fluctuates around a relatively stable, low baseline. This stability is violently disrupted by a massive structural shock beginning in May 2021, coinciding with the withdrawal of US troops. This geopolitical event acts as a catalyst for a sharp escalation in acute food insecurity, driving the population percentage to a peak of nearly 55%. Following this acute crisis phase, the data demonstrates a steady, though volatile, downward trajectory, with food insecurity levels progressively declining through 2026 to settle back near 20%.

 - Stagionalità Sud Sudan (assets/toADD/sito/01_Statistical_Decomposition_STL.png)
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
<iframe src="assets/toADD/sito/datiMancanti.html" width="100%" height="600" style="border:none;"></iframe>
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


<h1 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">From Words to Data: Mapping Famine Drivers Through Term Frequency</h1>





<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">

In IPC reports, words are never neutral: their recurrence forms the digital footprint of a real-world emergency. Textual analysis reveals that the bigram <b>'food insecurity'</b> dominates the dataset with 1,068 occurrences, frequently paired with critical terms like <b>'acute'</b> (658) and <b>'malnutrition'</b> (154). However, it is the underlying drivers that shape this semantic map. The frequency of words like <b>'price'</b> (524) highlights economic shocks and barriers to food access, while the agricultural production cluster (<i>'production'</i>, <i>'harvest'</i>, <i>'crop'</i>) captures the immediate impact of climate factors on the ground. In this context, counting words means mapping the boundaries of hunger.

</p>



<div class="row my-5 justify-content-center text-center">

    <div class="col-md-12 mb-4">

        <h5 class="mb-3 fw-bold text-secondary fade-in-up" style="animation-delay: 0.5s;">Top 50 Words (Bubble Chart)</h5>

        <img src="{{ site.baseurl }}/assets/images/packed_bubble_mixed.png" alt="Packed Bubble Chart of Unigrams and Bigrams" class="img-fluid rounded shadow-sm hover-lift fade-in-up" style="max-width: 100%; border: 1px solid #e0e0e0; animation-delay: 0.6s;">

    </div>

</div>



<hr class="section-divider">



## <span class="text-gradient">The Crisis Algorithm: Drivers of Food Insecurity</span>



Behind the IPC data architecture lies the convergence of macroeconomic, climatic, and social forces. By analyzing the semantic patterns within the reports, the primary catalysts of hunger emerge clearly across three interconnected macro-drivers:



<div class="comparison-table-wrapper glass-card hover-lift">

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



<h3 class="mt-5 mb-4 text-gradient">Mapping the Geography of Crisis Drivers</h3>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">

While the macroeconomic, climatic, and structural drivers of hunger are universal, their impact is intensely localized. By normalizing the frequency of these critical terms, we can generate a focused heatmap highlighting a selected group of highly vulnerable nations. The visualization below reveals the unique crisis signature of these specific regions: some nations are predominantly scarred by conflict and displacement, while others suffer primarily from the collapse of agricultural production due to climate extremes. This heatmap translates semantic prevalence into a stark geographic reality.

</p>



<div class="my-5 text-center">

    <img src="{{ site.baseurl }}/assets/images/heatmap_driver.png" alt="Heatmap of Food Insecurity Drivers by Country" class="img-fluid rounded shadow-lg" style="max-width: 100%; border: 1px solid #e0e0e0;">

</div>



<hr class="section-divider">


<style>
/* Modern Interactive Tooltip */
.history-tooltip {
    position: relative;
    display: inline-block;
    cursor: help;
    border-bottom: 2px dotted #007bff;
    color: inherit;
    font-weight: 600;
}

.history-tooltip .tooltip-text {
    visibility: hidden;
    width: 280px;
    background-color: #2c3e50;
    color: #ecf0f1;
    text-align: left;
    border-radius: 8px;
    padding: 12px;
    position: absolute;
    z-index: 1000;
    bottom: 125%;
    left: 50%;
    margin-left: -140px;
    opacity: 0;
    transition: opacity 0.3s;
    font-size: 0.85rem;
    font-weight: normal;
    line-height: 1.4;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    font-family: var(--font-sans);
}

.history-tooltip .tooltip-text::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    margin-left: -8px;
    border-width: 8px;
    border-style: solid;
    border-color: #2c3e50 transparent transparent transparent;
}

.history-tooltip:hover .tooltip-text {
    visibility: visible;
    opacity: 1;
}

.history-tooltip i {
    margin-right: 5px;
    color: #4ade80;
}
</style>

## <span class="text-gradient">Decoding the Narrative: The NLP Pipeline</span>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
To move beyond simple word counts and uncover the hidden semantic structures of food crises, we utilized an advanced Natural Language Processing (NLP) pipeline. Since we were operating on a highly specialized dataset of only a few hundred reports, training an AI from scratch was impossible. Instead, we leveraged powerful pretrained models to read the reports and let the data organize itself into coherent thematic clusters. <i>(For a deep dive into the technical details and architectures of the models cited below, please refer to our <a href="{{ site.baseurl }}/Text-analysis.html">Technical Text Analysis</a> page).</i>
</p>

<div class="row mt-4">
    <div class="col-md-12 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-user-secret"></i> 1. Anonymization: Hiding the Map</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        Before diving into the vocabulary, it was crucial to anonymize the texts using <b>GLiNER</b>, a pretrained model for <a href="{{ site.baseurl }}/Text-analysis.html">Named Entity Recognition (NER)</a>. We explicitly masked dates and geopolitical entities (like country and region names). The goal was to prevent the algorithm from grouping reports simply because they mentioned the same country, forcing it instead to find the <i>true</i> underlying causes of the crisis.
        </p>

        <div class="example-box mt-4 p-3 rounded" style="background-color: #f8f9fa; border-left: 4px solid #007bff;">
            <h5 style="font-size: 1rem; font-weight: bold; color: #495057;"><i class="fas fa-file-alt"></i> Original Text</h5>
            <p style="font-family: monospace; font-size: 0.85rem; color: #6c757d; margin-bottom: 15px;">
                "The 8th analysis cycle on the Integrated Food Security Classification Framework (IPC) of <span style="background-color: #ffcccc; padding: 2px 4px; border-radius: 3px;">DRC</span> held in <span style="background-color: #ffffcc; padding: 2px 4px; border-radius: 3px;">December 2012</span> identified 6.4 million people affected by a situation of food and livelihood crises, <span style="background-color: #ffcccc; padding: 2px 4px; border-radius: 3px;">77 regions</span> have been classified in phase 3 and <span style="background-color: #ffcccc; padding: 2px 4px; border-radius: 3px;">8 regions</span> in Phase 4 throughout <span style="background-color: #ffcccc; padding: 2px 4px; border-radius: 3px;">DRC</span>."
            </p>
            <h5 style="font-size: 1rem; font-weight: bold; color: #495057;"><i class="fas fa-user-secret"></i> GLiNER Anonymized Text</h5>
            <p style="font-family: monospace; font-size: 0.85rem; color: #28a745; margin-bottom: 0;">
                "The 8th analysis cycle on the Integrated Food Security Classification Framework (IPC) of <span style="background-color: #e2f0d9; padding: 2px 4px; border-radius: 3px; font-weight: bold;">[AFFECTED_AREA]</span> held in <span style="background-color: #e2f0d9; padding: 2px 4px; border-radius: 3px; font-weight: bold;">[DATE]</span> identified 6.4 million people affected by a situation of food and livelihood crises, <span style="background-color: #e2f0d9; padding: 2px 4px; border-radius: 3px; font-weight: bold;">[AFFECTED_AREA]</span> have been classified in phase 3 and <span style="background-color: #e2f0d9; padding: 2px 4px; border-radius: 3px; font-weight: bold;">[AFFECTED_AREA]</span> in Phase 4 throughout <span style="background-color: #e2f0d9; padding: 2px 4px; border-radius: 3px; font-weight: bold;">[AFFECTED_AREA]</span>."
            </p>
        </div>
    </div>
</div>

<div class="row">
    <div class="col-md-12 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-filter"></i> 2. The Power and Limits of Keywords (TF-IDF)</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        Initially, we used <b>TF-IDF</b> (Term Frequency-Inverse Document Frequency) to cluster the reports. This method groups texts based on the statistical frequency of identical words. Below, we can see two reports that were grouped together because they share the exact same vocabulary (highlighted in <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">yellow</span>) to describe a complex agricultural and economic shock. 
        </p>

        <div class="example-box mt-3 p-3 rounded" style="background-color: #f8f9fa; border-left: 4px solid #17a2b8;">
            <h5 style="font-size: 1rem; font-weight: bold; color: #495057;"><i class="fas fa-map-marker-alt"></i> Zimbabwe <span style="font-size: 0.85rem; color: #6c757d; font-weight: normal;">(Apr 2013 - Apr 2014)</span></h5>
            <p style="font-family: monospace; font-size: 0.85rem; color: #6c757d; margin-bottom: 15px; line-height: 1.5; text-align: justify;">
                "Agriculture is a key livelihoods activity for the majority of Zimbabwe's rural population. Mainly because of the <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">poor</span> rainfall <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">season</span> quality, <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">production</span> of major <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">crops</span> in 2012/13 fell compared to last <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">season</span>'s harvest. Livestock were in a fair to <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">good</span> condition in April 2013. Grazing and water for livestock were generally adequate in most parts of the country save for the communal <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">areas</span>... Currently, staple cereals are generally available throughout the country from both own <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">production</span> and the market, but low incomes and higher than normal <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">prices</span> of staple cereals are limiting household <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">access</span>. There is continued limited diversity of <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">food</span> consumed by rural <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">households</span>..."
            </p>
            <h5 style="font-size: 1rem; font-weight: bold; color: #495057;"><i class="fas fa-map-marker-alt"></i> Uganda <span style="font-size: 0.85rem; color: #6c757d; font-weight: normal;">(Jan 2017 - Feb 2018)</span></h5>
            <p style="font-family: monospace; font-size: 0.85rem; color: #6c757d; margin-bottom: 0; line-height: 1.5; text-align: justify;">
                "<span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">Food</span> in markets is easily accessed and affordable because <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">prices</span> have declined and the <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">households</span> have adequate purchasing power. They have <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">good</span> nutrition levels because they are able to eat two or more time a day with a <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">good</span> dietary diversity. Currently <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">access</span> to livestock products is <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">good</span> because of the available pasture and water... The <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">households</span> in these regions all suffered the effects of prolonged dry spells that stressed most of the <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">crops</span> and reduced yields... However, as the <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">production</span> in the second <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">season</span> is anticipated to be normal and above normal for some <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">areas</span>... They have <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">poor</span> purchasing power as their incomes are low..."
            </p>
        </div>
        
        <br>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        While TF-IDF is highly effective when authors use the exact same terminology, it has a fatal flaw: <b>it relies entirely on exact keyword matches</b>. This makes it vulnerable to <b>False Positives</b>. Because many reports use the same standard humanitarian boilerplate language, TF-IDF will often cluster them together, completely ignoring the underlying cause of the crisis. 
        <br><br>
        Take a look at the two reports below. TF-IDF confidently clustered them together because they both heavily use words like <i>"malnutrition"</i>, <i>"child"</i>, <i>"production"</i>, and <i>"season"</i> (highlighted in <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">yellow</span>). However, look at the actual climatic shock that triggered the crisis (highlighted in <span style="color: #dc3545; font-weight: bold;">red</span>): Angola is suffering from the worst <b>drought</b> in 40 years, while Bangladesh is submerged by severe river <b>flooding</b>. TF-IDF grouped a crisis of "no water" with a crisis of "too much water" just because the humanitarian jargon matched!
        </p>

        <div class="example-box mt-3 p-3 rounded" style="background-color: #f8f9fa; border-left: 4px solid #dc3545;">
            <h5 style="font-size: 1rem; font-weight: bold; color: #495057;"><i class="fas fa-map-marker-alt"></i> Angola <span style="font-size: 0.85rem; color: #6c757d; font-weight: normal;">(Apr 2021 - Mar 2022) - <span style="color: #dc3545; font-weight: bold;">Drought Shock</span></span></h5>
            <p style="font-family: monospace; font-size: 0.85rem; color: #6c757d; margin-bottom: 15px; line-height: 1.5; text-align: justify;">
                "The worst <span style="color: #dc3545; font-weight: bold; text-decoration: underline;">drought in the last 40 years</span> and rising food prices have resulted in high acute food insecurity... The high acute food insecurity in this region can mainly be attributed to the recurrent effects of <span style="color: #dc3545; font-weight: bold; text-decoration: underline;">drought</span> which has reduced both agricultural and livestock <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">production</span>... An IPC Acute <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">Malnutrition</span> analysis of 10 municipalities in Southern Angola has revealed that around 114,000 <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">children</span> under the age of five are suffering or are likely to suffer from acute <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">malnutrition</span>... For the period of October 2021 to February 2022, a projection analysis of the situation suggests that the rainy <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">season</span>, characterized by food shortages and high incidence of acute <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">malnutrition</span>, may lead to a deterioration..."
            </p>
            <h5 style="font-size: 1rem; font-weight: bold; color: #495057;"><i class="fas fa-map-marker-alt"></i> Bangladesh <span style="font-size: 0.85rem; color: #6c757d; font-weight: normal;">(Sep 2014 - Dec 2014) - <span style="color: #007bff; font-weight: bold;">Flooding Shock</span></span></h5>
            <p style="font-family: monospace; font-size: 0.85rem; color: #6c757d; margin-bottom: 0; line-height: 1.5; text-align: justify;">
                "During the <span style="color: #007bff; font-weight: bold; text-decoration: underline;">flooding</span>, crop land and homesteads <span style="color: #007bff; font-weight: bold; text-decoration: underline;">deluged with water</span> and cause severe damage to standing crops... <span style="color: #007bff; font-weight: bold; text-decoration: underline;">Flood water</span> brings huge silt and sands and cultivable lands lose its productivity... Analysis revealed that income opportunities may be greatly hampered due to the 2014 <span style="color: #007bff; font-weight: bold; text-decoration: underline;">flooding and consequent river erosion</span>. Fish <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">production</span> is also negatively affected... <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">Child Malnutrition</span>: The districts and upazilas analyzed structurally suffer from the alarming <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">level</span> of acute <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">malnutrition</span>... shocks due to <span style="color: #007bff; font-weight: bold; text-decoration: underline;">flooding</span> and consequent river erosion... alarming <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">level</span> of acute <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">child malnutrition</span>."
            </p>
        </div>
    </div>
</div>


<div class="row">
    <div class="col-md-12 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-brain"></i> 3. Dense Embeddings: Finding the Meaning</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        To solve the keyword limitation, we advanced to <b>Dense Semantic Embeddings</b> using the pretrained <b>BGE-M3</b> model. Instead of counting words, this model maps entire paragraphs into a high-dimensional mathematical space where texts are grouped purely by their <i>meaning</i>. This allowed us to discover profound, previously invisible connections, successfully linking reports that described the exact same structural crisis using entirely different vocabularies.
        </p>
    </div>
</div>

<div class="row mt-4">
    <div class="col-md-12 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-search-plus"></i> Discovery: Connecting Different Words to the Same Crisis</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        To demonstrate what we gained by moving to dense embeddings, look at how the model connected a report from <b>El Salvador</b> with one from <b>Zambia</b>. 
        <br><br>
        Because they use completely different phrasing—"mobility restrictions" versus "reduced livelihood opportunities"—TF-IDF would struggle to link them. But the dense embedding model recognized they were describing the exact same underlying tragedy: families plunged into food insecurity by the economic paralysis of the COVID-19 lockdown.
        </p>
        <div class="example-box mt-3 p-3 rounded" style="background-color: #f8f9fa; border-left: 4px solid #17a2b8;">
            <h5 style="font-size: 1rem; font-weight: bold; color: #495057;"><i class="fas fa-map-marker-alt"></i> El Salvador <span style="font-size: 0.85rem; color: #6c757d; font-weight: normal;">(October 2020 - February 2021)</span></h5>
            <p style="font-family: monospace; font-size: 0.85rem; color: #6c757d; margin-bottom: 15px; line-height: 1.5; text-align: justify;">
                "These groups have experienced <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">income losses</span> due to <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">mobility and transportation restrictions</span> due to the <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">COVID-19 pandemic</span>... This <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">reduction of income</span> limits affected households' access to basic services and food."
            </p>
            <h5 style="font-size: 1rem; font-weight: bold; color: #495057;"><i class="fas fa-map-marker-alt"></i> Zambia <span style="font-size: 0.85rem; color: #6c757d; font-weight: normal;">(July - September 2022)</span></h5>
            <p style="font-family: monospace; font-size: 0.85rem; color: #6c757d; margin-bottom: 0; line-height: 1.5; text-align: justify;">
                "The current vulnerability in Zambia has been driven by a high incidence of poverty, the impact of the <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">COVID-19 pandemic</span>, macroeconomic instability... primarily driven by shocks such as prolonged dry spells, flooding, <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">reduced livelihood opportunities</span> due to <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">restrictions</span> linked to <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">COVID-19</span>."
            </p>
        </div>
    </div>
</div>

<hr class="section-divider">

## <span class="text-gradient">The Interactive Timeline: A History of Crisis</span>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Food insecurity is rarely a static condition; it evolves. By mapping out the dominant crisis type (using our semantic clusters) for each country year by year, we built the interactive timeline below. You can explore how nations shift from agricultural shocks to economic inflation, or how conflict suddenly hijacks a country's entire food system. 
<br><br><i>Select a country from the sidebar to isolate its unique journey through the crisis landscape.</i>
</p>

<div class="iframe-container my-5" style="width: 90vw; position: relative; left: 50%; right: 50%; margin-left: -45vw; margin-right: -45vw; height: 650px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
    <iframe src="{{ site.baseurl }}/assets/data/Cluster_evolution_global.html" width="100%" height="100%" frameborder="0" style="border:none;"></iframe>
</div>

<hr class="section-divider">

### <span class="text-gradient">Crisis Profiles: Shared Destinies</span>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The most startling revelation from the dense clustering was the discovery of <b>Crisis Profiles</b>—nations that share identical evolutionary paths despite being thousands of miles apart. By removing borders, the data showed us that risk follows specific, recurring patterns. <i>(Hover over the highlighted text to reveal the historical context).</i>
</p>

#### Profile 1: The Agro-Pastoral Climate Trap (Kenya & Uganda)

<p style="font-size: 1rem; line-height: 1.6; text-align: justify;">
Kenya and Uganda are bound by a shared geographical vulnerability. Their evolutionary trajectory perfectly mirrors the unpredictable swings of the climate. We see both nations plunge into <b>Agro-pastoral Water Vulnerability</b> during the devastating <span class="history-tooltip">El Niño-induced floods<span class="tooltip-text"><i class="fas fa-info-circle"></i> In 2015-2016, a super El Niño triggered torrential rains across East Africa, washing away harvests and decimating livestock herds before they could recover.</span></span>, and then suffer immense <b>Rainfall Impact on Crops</b> during the punishing <span class="history-tooltip">La Niña droughts<span class="tooltip-text"><i class="fas fa-info-circle"></i> Between 2020 and 2023, the Horn of Africa experienced an unprecedented five consecutive failed rainy seasons, pushing millions to the brink of famine.</span></span>. This is a classic climate-driven trap, where communities have no time to recover before the next environmental shock hits.
</p>

<div class="iframe-container my-5" style="width: 90vw; position: relative; left: 50%; right: 50%; margin-left: -45vw; margin-right: -45vw; height: 650px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
    <iframe src="{{ site.baseurl }}/assets/data/df_cluster_embedding_densi_ok_pair_fullscreen.html" width="100%" height="100%" frameborder="0" style="border:none;"></iframe>
</div>

#### Profile 2: The Multidimensional Collapse (Sudan & Haiti)

<p style="font-size: 1rem; line-height: 1.6; text-align: justify;">
At first glance, a North African nation and a Caribbean island have nothing in common. Yet, the model recognized their shared tragedy. Both nations are enduring a profound structural collapse, overwhelmed by <span class="history-tooltip">severe political crises<span class="tooltip-text"><i class="fas fa-info-circle"></i> Haiti was plunged into chaos following the 2021 assassination of President Jovenel Moïse, while Sudan's fragile transition shattered into civil war in April 2023.</span></span> and escalating <span class="history-tooltip">violent internal conflicts<span class="tooltip-text"><i class="fas fa-info-circle"></i> Armed factions in Sudan have displaced millions, while heavily armed gangs in Haiti have effectively blockaded Port-au-Prince, cutting off vital food supplies.</span></span>. Their trajectories are not driven by the weather, but by <b>Conflict-Induced Refugee Emergency</b> and <b>Agricultural Price Inflation</b>. This profile shows us the darkest side of food insecurity: hunger weaponized by systemic failure and violence.
</p>

<div class="iframe-container my-5" style="width: 90vw; position: relative; left: 50%; right: 50%; margin-left: -45vw; margin-right: -45vw; height: 650px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
    <iframe src="{{ site.baseurl }}/assets/data/df_cluster_embedding_densi_ok_pair4_fullscreen.html" width="100%" height="100%" frameborder="0" style="border:none;"></iframe>
</div>



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
