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
The ACLED dataset contains 56,414 rows and 15 columns, designed to integrate food insecurity metrics with armed conflict intensities. Powered by ACLED conflict logs matched with IPC hunger data, this pipeline measures how local violence directly drives food shortages.

It relies on three core join and identification variables: the ISO 3166-1 alpha-3 country code (Country), the analysis time frame formatted as Mmm-YY (Date of analysis), and the standardized level-1 region code (adm1_pcode).
Additional qualitative descriptors include Level 1, Area, Validity period, From, To, and the specific IPC Phase.
The method aggregates raw records of violent events and casualties, mapping them directly onto regional food security levels to create a single, unified dataset. The ultimate purpose is to feed machine learning models with clear conflict signals, helping analysts measure how localized violence directly drives food crisis severity and population displacement, thereby catching emerging crisis hotspots early.

# IPC (Integrated Food Security Phase Classification)

The IPC Data dataset captures spatial and socio-economic structures to monitor food security based on the Integrated Food Security Phase Classification framework, mapped to the 2024–2025 analysis cycle. It follows a strict geographic hierarchy spanning from national levels (ISO-3) down to micro-administrative and local units—including Admin Levels 1–3, communes, and displacement camps—each uniquely referenced using standardized P-Codes.

Alongside geographic boundaries, the dataset classifies analysis units by demographic group (rural, urban, host, or displaced and refugee populations) and primary Livelihood Zones, such as agro-pastoral or coastal systems. Ultimately, the purpose of this architecture is to build a robust qualitative text corpus to identify food crisis drivers and perform semantic comparisons across different emergency contexts.

# WFP (World Food Programme)
Powered by global food price data from the World Food Programme (WFP) via HDX, this pipeline tracks local market economics to detect early signs of financial stress on food access.

The WFP dataset provides subnational spatio-temporal observations (typically ADM1 or ADM2 levels) across 52 countries—such as AFG, ETH, YEM, and ZAF—based on HDX metadata. Covering continuous time-series data at a decadal or monthly resolution from January 1, 2017, to June 2026 (truncated from historical data dating back to 2002), the extracted raw dataset encompasses 7,225,344 rows prior to final filtering.

The method processes raw market logs, extracts core food price and inflation indices, and spatially joins physical markets to administrative regions before aligning them with IPC timelines. Its core identification structure is defined by three key variables: country_iso3 (the ISO 3166-1 alpha-3 country code), hdx_dataset_name (the source dataset title on HDX), and date (the observation timestamp).
The ultimate purpose is to monitor market volatility and surging food costs, giving early-warning models clear economic signals to predict where price spikes will trigger severe hunger.

# IDP (Internally Displaced Persons)
Sourced from HDX HAPI (Humanitarian API), this pipeline gathers subnational displacement metrics to track internally displaced persons (IDPs) and population movements over time.

The IDP dataset contains georeferenced humanitarian and demographic monitoring data primarily focused on population mobility, displacement, and crisis tracking. Structurally, the dataset is organized around 14 core attributes that capture detailed spatial, operational, and demographic information. Geographic and administrative context is established through location codes and names (location_code, location_name), as well as administrative level classifications (admin_level) ranging from primary (admin1_code, admin1_name) to secondary subdivisions (admin2_code, admin2_name).

The method executes global API queries via fetch.py, pulling pagination-managed displacement data in a single pass before filtering for target countries and saving it into Parquet files. Operational tracking and source metadata are maintained via Humanitarian Data Exchange identifiers (resource_hdx_id), reporting cycles (reporting_round), assessment types (assessment_type), and specific humanitarian emergency operations (operation). Finally, the dataset provides key quantifiable metrics by recording affected population counts (population) alongside precise temporal boundaries defined by start and end reference dates (reference_period_start, reference_period_end).
The ultimate purpose is to monitor demographic pressure and human displacement caused by conflict or disaster, supplying predictive models with key population signals to anticipate localized food shortages.

# RAINFALL 
This pipeline collects subnational dekadal rainfall data from HDX/CHIRPS (data.humdata.org) via HDXRainfallLoader.

The dataset is a time series running from January 1, 1981, through the present (plus a short forecast horizon), structured at a dekad granularity—three 10-day intervals per month for each administrative unit. Its 15-column schema brings together spatial-temporal metadata, precipitation metrics, and data status flags. On the spatial and temporal front, each row records the dekad start date (date), the administrative level (adm_level, where 1 represents regions/states and 2 represents districts/LGAs), unique spatial identifiers (adm_id and the official PCODE), and the area extent proxied by the count of contained CHIRPS pixels (n_pixels).

The method automatically fetches the full historical -subnat-full CSV resource for each country and organizes it into structured local directories (data/raw_rainfall/). The core of the dataset tracks rainfall performance, capturing single-dekad precipitation in millimeters (rfh), its long-term average (rfh_avg), and the percentage of normal rainfall (rfq). To account for broader seasonal trends, these are complemented by rolling 1-month sum windows (r1h, over 3 dekads) and 3-month sum windows (r3h, over 9 dekads), alongside their respective long-term means (r1h_avg, r3h_avg) and percentage-of-normal anomalies (r1q, r3q). Due to the length of these rolling windows, the earliest dekads for each admin unit naturally contain NaN values across these aggregated fields. Finally, the version column classifies the data status, distinguishing between consolidated historical records (final), recent preliminary observations (prelim), and upcoming estimates (forecast).

# NDVI (Normalized Difference Vegetation Index)
Driven by data from WFP via the HDX platform, this pipeline gathers subnational NDVI (Normalized Difference Vegetation Index) metrics to gauge plant growth and biomass density.

The NDVI dataset captures satellite-derived vegetation indices for monitoring environmental conditions. Prior to final filtering, the raw extraction yields 7,225,344 rows, relying on three core identification variables: country_iso3 (the ISO 3166-1 alpha-3 country code), hdx_dataset_name (the originating dataset name on HDX), and date (the timestamp of the satellite observation).

The method leverages the hdx-python-api to pull and structure full historical vegetation series directly into a unified dataset.
The ultimate purpose is to provide clear environmental signals on drought, crop stress, and agricultural health—giving early-warning models the physical data needed to anticipate food shortages before they escalate.

# GDELT (Global Database of Events, Language, and Tone)
Sourced from the GDELT Project via Google BigQuery, this pipeline monitors global news coverage to capture real-time media signals on conflict, protests, and humanitarian responses.

The GDELT dataset provides fine-grained spatial and temporal media-monitoring coverage across 48 IPC-tracked countries and 5,769 unique ADM2 regions (districts/municipalities), mapped via spatial joins between GDELT event coordinates and official OCHA/HDX shapefiles. Spanning from January 2017 to June 2026 at a monthly resolution, the unpivoted long-format dataset comprises 2,695,764 rows and 10 columns derived from GDELT 2.0 (events_partitioned). Its identification features include country ISO codes (iso3), regional and district boundary identifiers (adm1_pcode, adm2_pcode), temporal trackers (year, month), and conflict classification variables using CAMEO taxonomy (EventRootCode for root actions 01–20 and QuadClass for macro-groupings 1–4). Numeric outcomes are measured through three key metrics: n_events (total distinct recorded events), total_mentions (sum of media mentions across events), and avg_tone (average media coverage tone weighted by number of mentions).

The method queries daily partitioned event tables and categorizes geopolitical actions using the CAMEO taxonomy to structure raw news data.
The ultimate purpose is to provide early, near-real-time indicators of instability that often lead to food shortages, filling the time gap before official, structured field reports are published.

# IPC reports (via web scraping from https://www.ipcinfo.org/ipc-country-analysis/en/)

This pipeline collects official report from IPC on Acute Food Insecurity analyses spanning from 2011 to 2026.
The method follows a two-stage automated process: first mapping and deduplicating report URLs, then extracting Key Results text and downloading PDFs—automatically separating full reports from summary snapshots.


