---
layout: default
title: "Data collection"
permalink: /Data-Collection.html
show_sidetoc: true
header_type: hero
header_img: assets/images/header_data_coll.jpg
header_title: "Data collection"
---


## Integrated Datasets and Architecture of HERO

A fundamental pillar of this effort lies in the collection and integration of diverse data sources (spanning socio-economic indicators, climate patterns, agricultural yields, and conflict metrics) into a unified analytical framework. The backbone (*spine*) of this entire data architecture is established by the **Integrated Food Security Phase Classification (IPC)** assessments. All secondary, high-frequency signals—such as ACLED conflict records, IDP displacement data, WFP market prices, CHIRPS rainfall metrics, WFP NDVI vegetation indices, and GDELT media monitoring—are integrated into the IPC base structure via **Left Join** operations across the spatial and temporal dimensions. 

This architectural choice ensures that the final dataset preserves the exact row hierarchy of official IPC evaluations, representing missing values from secondary pipelines as `NaN` without dropping any primary IPC observation. The integrated data is consolidated into standardized wide-format Parquet layers:
* **`merged_adm1_wide.parquet`** (~10,024 rows): Structured at the Admin Level 1 (province) per IPC validity period, used for regional clustering, global analysis, and GDELT integration.
* **`merged_adm1_wide_con_coordinate.parquet`**: Augments the ADM1 wide dataset with geographic centroid coordinates (`latitude`, `longitude`) to force spatial cohesion during spatially constrained clustering.
* **`merged_adm1_wide_knn.parquet`**: Provides a complete feature matrix with missing secondary values imputed via the KNN Imputer algorithm.
* **`merged_adm2_wide.parquet`** (~42,957 rows): Structured at the Admin Level 2 (district/department) per IPC validity period, designed for high-resolution localized predictions.


For Time Series Analysis (TSA) and Machine Learning (ML) modeling, irregular IPC validity windows (`From` – `To`) are expanded into a uniform monthly time axis (`MS` - Month Start). Overlapping months are aggregated via mean values, and intermediate gaps are filled using linear interpolation alongside edge carrying (`ffill`/`bfill`). This transformation extracts 9 static structural descriptors per time series, including statistical moments (mean, variance, skewness, kurtosis), long-term memory (Hurst exponent $H$), regularity (Approximate Entropy ApEn), and short-term memory through standardized AR(1)–AR(3) autoregressive coefficients.

---
### HERO Dataset: Sources and Methodology
#### ACLED (Armed Conflict Location & Event Data Project)
The ACLED pipeline processes raw conflict logs partitioned across multiple files (`violent_events_1-3.csv`) and matches them with IPC hunger data, yielding a consolidated dataset of 56,414 rows and 15 columns. Designed to feed machine learning models with clear conflict signals, it measures how localized violence directly drives food crisis severity and population displacement.

The pipeline filters for 48 target baseline countries monitored by IPC and enforces a temporal floor starting on January 1, 2017. Raw point-based violent event records and casualties are aggregated at the ADM1 level per month/year. To enable relational integration, ACLED's textual month and year values are formatted into `Mmm-YY` (e.g., `Apr-19`) to match the IPC `Date of analysis` key. 

Integration relies on three core join keys: ISO3 country code (`Country`), temporal window (`Date of analysis`), and standardized level-1 region code (`adm1_pcode`), supported by descriptive qualitative attributes (`Level 1`, `Area`, `Validity period`, `From`, `To`, `Phase`). Geographic harmonization includes regular expression patches for non-standard P-codes (e.g., converting `TD` prefixes to `TCD` and `NER` to `NE`), as well as explicit dictionary overrides for Nigerian and Cameroonian anomalies (e.g., `NG00` -> `NG001`).

Key output metrics include:
* **`Events`**: Total count of violent incidents in the ADM1 region during the month.
* **`Fatalities`**: Aggregated death count from violent incidents.
* **`violence_ratio`**: A calculated lethality ratio defined as Fatalities / Events (zero-corrected when events equal zero).
* **`Percentage`**: Analytically recalculated as (Number / Total country population) * 100 to prevent numerical drift caused by averaging pre-existing percentages across heterogeneous populations.

Unmatched records during the `m:1` Left Join result in `NaN` values for ACLED metrics across 22,981 rows, highlighting structural key gaps in certain territories (e.g., PAK, GIN, MDG).

---

#### IPC (Integrated Food Security Phase Classification)
The IPC dataset captures spatial and socio-economic structures to monitor acute food insecurity mapped across the 2024–2025 analysis cycle and historical runs. The extraction is driven by APIs from the HDX platform and IPC platforms, structuring food insecurity metrics across both **wide** (`ipc_global_area_wide_pcoded.csv`, 72,213 rows) and **long** (`ipc_global_area_long_pcoded.csv`, 64,214 rows) schemas. The data is also serialized into columnar Parquet formats using `fastparquet-python`.

The architecture follows a strict geographical hierarchy spanning national levels (ISO-3) down to micro-administrative units (Admin Levels 1–3, communes) and displacement camps (e.g., *Markazi Camp*, *Ali Addeh*), uniquely referenced via standardized OCHA P-Codes. Analysis units are classified by demographic group (rural, urban, host, or refugee populations) and primary Livelihood Zones.

The dataset tracks target population counts (`Number`) and prevalence rates (`Percentage` / `population_fraction_in_phase`) across five core IPC phases:
* **Phase 1**: Minimal
* **Phase 2**: Stressed
* **Phase 3**: Crisis
* **Phase 4**: Emergency
* **Phase 5**: Catastrophe/Famine
* **Phase 3+ (`phase_3plus_...`)**: The primary target variable used in ML predictive models and clustering, representing the aggregated population in Phase 3, 4, and 5.

Temporal observations are categorized via `Validity period` / `ipc_type` into `current` assessments, `first projection` (short-to-medium term), and `second projection` (medium-to-long term).

---

#### WFP (World Food Programme)
Powered by global food price data from the World Food Programme (WFP) via HDX, this pipeline tracks local market economics to detect early financial stress on food access. The extraction accesses the *Global Real-Time Food Prices* repository via a vertical metadata map (`metadata-global-real-time-food-prices.csv`), which dynamically supplies resource URLs for bulk processing.

The raw market dataset is denormalized in a **wide format** where each row captures the complete state of a physical market in a given month across 52 target countries. The time series spans from January 1, 2017, to June 2026 (truncated from historical records dating back to 2002), generating 7,225,344 rows during raw extraction. 

The schema is structured into five core functional areas:
1. **Spatial Identification**: `ISO3`, `country`, `adm1_name`, `adm2_name`, `mkt_name`, and exact point coordinates (`lat`, `lon`).
2. **Temporal Keys**: `year`, `month`, and combined timestamp string `DATES`.
3. **Data Quality Flags**: `currency`, `components`, `data_coverage` (ratio of real vs. imputed historical records), `index_confidence_score`, and `spatially_interpolated` indicators.
4. **Commodity Tracking**: Individual items (e.g., wheat, rice, maize) expanded into 6 distinct attributes covering standard average price, open (`o_`), high (`h_`), low (`l_`), close (`c_`), item-specific inflation (`inflation_`), and item confidence (`trust_`).
5. **Macro Economic Targets**: Integrated composite metrics including `food_price_index` (Food Basket Index) and `inflation_food_price_index` (general food inflation rate).

Physical market coordinates are spatially mapped to administrative boundaries using strict point-in-polygon (`strict_pip`) or elastic buffer (`elastic_buffer`) joins before temporal alignment with IPC analysis windows.

---

#### IDP (Internally Displaced Persons)
Sourced from the HDX HAPI (Humanitarian API), this pipeline gathers subnational displacement stock metrics to monitor internally displaced persons (IDPs) and population movements over time. The dataset is serialized into Parquet format using Apache Arrow structures.

Structurally organized around 14 core attributes, the dataset establishes spatial context through standardized location codes (`location_code`, `location_name`) and administrative classifications spanning primary (`admin1_code`, `admin1_name`) and secondary (`admin2_code`, `admin2_name`) levels. 

The automated pipeline (`fetch.py`) queries global API endpoints, executing pagination-managed passes to download displacement records for target countries. Operational tracking and source lineage are maintained through:
* **`resource_hdx_id`**: Source identifier on HDX.
* **`reporting_round`**: Reporting cycle identifier.
* **`idp_assessment_type`**: Methodological approach used for population tracking.
* **`operation`**: Associated humanitarian emergency operation.
* **`idp_population`**: Quantifiable displaced population count, extracted using the latest available report prior to the IPC end date (`To`).
* **`idp_staleness_days`**: Quality control metric recording elapsed days between IDP data collection and IPC analysis; records exceeding a 400-day staleness threshold are discarded.

---

#### Rainfall
This pipeline collects subnational dekadal rainfall data from HDX/CHIRPS (Climate Hazards group InfraRed Precipitation with Stations) via the `HDXRainfallLoader` module, downloading raw files formatted as `{iso2}-rainfall-subnat-full.csv` under `data/raw_rainfall/{iso3}/`.

The dataset provides continuous time-series coverage starting January 1, 1981, through the present, plus short-term forecast horizons. Observations are structured at a **dekad** granularity (10-day intervals, 3 per month starting on the 1st, 11th, and 21st, yielding ~36 dekads per year) across Admin 1 and Admin 2 levels. 

The 15-column schema comprises:
* **Spatial/Temporal Metadata**: `date` (dekad start date), `adm_level` (1 or 2), `adm_id` (HDX numeric ID), `PCODE` (official administrative P-code), and `n_pixels` (count of contained CHIRPS pixels, serving as an area proxy).
* **Direct Precipitation**: `rfh` (actual dekad rainfall in mm) and `rfh_avg` (long-term historical mean for the dekad).
* **Rolling Accumulations**: `r1h` (1-month rolling sum across 3 dekads) and `r3h` (3-month rolling sum across 9 dekads), along with their historical averages (`r1h_avg`, `r3h_avg`).
* **Anomalies & Relative Performance**: `rfq` (dekad percentage of normal, calculated as approx. rfh / rfh_avg * 100), `r1q` (1-month percentage of normal), and `r3q` (3-month percentage of normal). Initial dekads naturally contain `NaN` in rolling fields until the temporal window fills.
* **Status Flags**: `version` column categorizing data stability as `final` (historical), `prelim` (recent observations), or `forecast` (upcoming estimates).

---

#### NDVI (Normalized Difference Vegetation Index)
Driven by data from WFP via HDX (`organization:wfp`, query `ndvi`), this pipeline gathers subnational Normalized Difference Vegetation Index metrics to track crop health, biomass density, and drought anomalies.

The pipeline utilizes `hdx-python-api` with a custom user agent (`NDVI_WFP_Consolidator`) to query, download, and parse subnational vegetation series. The extraction covers 52 target countries (e.g., AFG, ETH, YEM, ZAF, MWI, PSE) from January 1, 2017, to June 2026, truncated from historical raw data dating back to July 2002. Prior to final filtering, extraction processes generate 7,225,344 rows, saved in dual `.parquet` (`wfp_ndvi.parquet`) and `.csv` formats.

Key identifying variables include `country_iso3`, `hdx_dataset_name`, and observation `date`. The consolidated metrics include:
* **`ndvi_vim`**: Mean vegetation vigor index, weighted over agricultural pixels to measure greenness.
* **`ndvi_viq`**: Vegetation quality index (anomaly relative to historical normal levels), serving as a direct physical proxy for agricultural drought detection.

*Note on Data Processing:* The raw parsing pipeline ingests both full historical resources (`*-ndvi-subnat-full.csv`) and 5-year trend resources (`*-ndvi-subnat-5ytd.csv`). Because the `full` resource already contains the recent 5-year window, concatenation without explicit deduplication introduces redundant records that require post-hoc `drop_duplicates()` filtering prior to modeling.

---

#### GDELT (Global Database of Events, Language, and Tone)
Sourced from the GDELT Project via Google BigQuery (`gdelt-bq.gdeltv2.events_partitioned`), this pipeline monitors global news coverage to capture real-time media signals on conflict, geopolitical tension, and food crisis drivers.

The raw extraction queries BigQuery for 48 FIPS country codes matching IPC coverage from 2017 to 2026, retrieving 65,814,898 raw event logs. Spatial assignment maps GDELT text coordinates (extracted via GNS gazetteer) to official OCHA ADM1 and ADM2 shapefiles using spatial joins (`gpd.sjoin`, predicate `within`). To resolve geocoding artifacts (e.g., coordinates placed on country centroids), a Nearest Neighbor fallback join within a 20 km radius in EPSG:3857 projection recovers 768,770 out of 1,038,338 unmapped events. The remaining 269,568 events (0.41%) exceeding 20 km are discarded as spatial orphans.

At ADM1 level, events are categorized using CAMEO taxonomy into 4 QuadClasses:
* **QuadClass 1**: Verbal Cooperation (statements, commitments).
* **QuadClass 2**: Material Cooperation (aid delivery, support).
* **QuadClass 3**: Verbal Conflict (threats, sanctions).
* **QuadClass 4**: Material Conflict (military force, physical violence).

The final wide-format dataset (`gdelt_adm1_final.parquet` and `gdelt_adm2_final.parquet`, serialized via `pyarrow` v24.0.0) contains monthly aggregated features:
* **`n_events_qc1` – `n_events_qc4`**: Total distinct recorded event counts per QuadClass.
* **`total_mentions_qc1` – `total_mentions_qc4`**: Total global media mentions per QuadClass.
* **`avg_tone_qc1` – `avg_tone_qc4`**: Average media tone weighted by total mentions, ranging from negative values (panic, crisis) to positive values (peaceful resolution).

---

#### IPC Reports (via Web Scraping)
This pipeline systematically collects official narrative reports from the IPC portal (`https://www.ipcinfo.org/ipc-country-analysis/en/`) covering Acute Food Insecurity Classification analyses published between 2011 and 2026. 

The automated collection pipeline covers 36 target countries, discovering 502 unique report links through a two-stage architecture:
1. **Stage 1: URL Mapping and Deduplication**: Iterates through country and year selection filters to harvest analysis URLs. Cross-year duplicate URLs are removed. Web automation utilizes `undetected_chromedriver` to bypass Cloudflare bot detection mechanisms.
2. **Stage 2: Text Extraction and PDF Download**: Extracts the raw "Key Results" textual body from each analysis page, achieving a 99.8% extraction success rate (501 texts successfully parsed out of 502 targets). Full PDF reports and summary snapshots are downloaded, with the automated browser session restarting every 50 pages to prevent IP rate-limiting and server bans.


