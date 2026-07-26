---
layout: default
title: "Data collection"
permalink: /Data-Collection.html
show_sidetoc: true
header_type: hero
header_img: assets/images/folium_map.webp
header_title: "Data collection"
---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>

### Integrated Datasets and Architecture of HERO

A fundamental pillar of this effort lies in the collection and integration of diverse data sources (spanning socio-economic indicators, climate patterns, agricultural yields, and conflict metrics) into a unified analytical framework. By combining these fragmented datasets, it becomes possible to identify hidden correlations and early warning signals that would otherwise remain undetected.

#### HERO Dataset: Sources and Methodology
# ACLED (Armed Conflict Location & Event Data Project)
Powered by ACLED conflict logs matched with IPC hunger data, this pipeline measures how local violence directly drives food shortages. The method aggregates raw records of violent events and casualties, mapping them directly onto regional food security levels to create a single, unified dataset. The purpose is to reveal the exact link between armed conflict and rising hunger, giving AI models the conflict signals needed to catch emerging crisis hotspots early.
The purpose is to feed machine learning models with clear conflict signals, helping analysts measure how localized violence directly drives food crisis severity and population displacement.

# IPC (Integrated Food Security Phase Classification)
This pipeline collects official data from IPC (ipcinfo.org) on
Acute Food Insecurity analyses (2011–2026).
The method follows a two-stage automated process: first mapping and 
deduplicating report URLs, then extracting Key Results text and
downloading PDFs—automatically separating full reports from summary
snapshots. The purpose is to build a qualitative text corpus to
identify food crisis drivers and perform semantic comparisons across
different emergency contexts.

# WFP (World Food Programme)
Powered by global food price data from the World Food Programme (WFP) via HDX, this pipeline tracks local market economics to detect early signs of financial stress on food access. The method processes raw market logs, extracts core food price and inflation indices, and spatially joins physical markets to administrative regions before aligning them with IPC timelines. The purpose is to monitor market volatility and surging food costs, giving early-warning models clear economic signals to predict where price spikes will trigger severe hunger.

# IDP (Internally Displaced Persons)
Sourced from HDX HAPI (Humanitarian API), this pipeline gathers subnational displacement metrics to track internally displaced persons (IDPs) and population movements over time.
The method executes global API queries via ⁠fetch.py⁠, pulling pagination-managed displacement data in a single pass before filtering for target countries and saving it into Parquet files.
The purpose is to monitor demographic pressure and human displacement caused by conflict or disaster, supplying predictive models with key population signals to anticipate localized food shortages.

# RAINFALL 
This pipeline collects subnational dekadal rainfall data
from HDX/CHIRPS (data.humdata.org) via HDXRainfallLoader.
The method automatically fetches the full historical -subnat-full
csv resource for each country and organizes it into structured local
directories (data/raw_rainfall/).
The purpose is to supply quantitative precipitation metrics to
support food security risk analysis and early-warning modeling.

# NDVI (Normalized Difference Vegetation Index)
Driven by data from WFP via the HDX platform, this pipeline  gathers subnational NDVI (Normalized Difference Vegetation Index) metrics to gauge plant growth and biomass density.
The method leverages the hdx-python-api to pull and structure full historical vegetation series directly into a unified dataset.
The purpose is to provide clear environmental signals on drought, crop stress, and agricultural health—giving early-warning models the physical data needed to anticipate food shortages before they escalate.

# GDELT (Global Database of Events, Language, and Tone)
Sourced from the GDELT Project via Google BigQuery, this pipeline monitors global news coverage to capture real-time media signals on conflict, protests, and humanitarian responses. The method queries daily partitioned event tables and categorizes geopolitical actions using the CAMEO taxonomy to structure raw news data. The purpose is to provide early, near-real-time indicators of instability that often lead to food shortages, filling the time gap before official, structured field reports are published.




