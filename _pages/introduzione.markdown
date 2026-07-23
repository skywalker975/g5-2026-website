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


<img src="percorso/della-tua-immagine.jpg" class="img-fluid" alt="Descrizione immagine">


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


---





## 🚀 HERO platfrom

Explore all the data, Cartesian graphs, geospatial maps, and test the interactive scenario simulator directly on our dashboard:

<div class="text-center my-5">
    <a href="https://github.com/skywalker975/g5-2026-website" class="btn btn-premium-hero btn-lg px-5 py-3 shadow"><i class="fas fa-chart-line mr-2"></i> Explore Dashboard HERO</a>
</div>
