---
layout: default
title: "Data collection"
permalink: /Data-Collection.html
show_sidetoc: true
header_type: hero
header_img: assets/copertine_pagine/data_collection_and_processing.png
header_title: "Data collection"
---

<h1 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">Integrated Datasets and Architecture of HERO</h1>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
A fundamental pillar of this effort lies in the collection and integration of diverse data sources (spanning socio-economic indicators, climate patterns, agricultural yields, and conflict metrics) into a unified analytical framework. The backbone (<em>spine</em>) of this entire data architecture is established by the <strong>Integrated Food Security Phase Classification (IPC)</strong> assessments. All secondary, high-frequency signals—such as ACLED conflict records, IDP displacement data, WFP market prices, CHIRPS rainfall metrics, WFP NDVI vegetation indices, and GDELT media monitoring—are integrated into the IPC base structure via <strong>Left Join</strong> operations across the spatial and temporal dimensions.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
This architectural choice ensures that the final dataset preserves the exact row hierarchy of official IPC evaluations, representing missing values from secondary pipelines as <code>NaN</code> without dropping any primary IPC observation. The integrated data is consolidated into standardized wide-format Parquet layers:
</p>

<ul class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
  <li><code>merged_adm1_wide.parquet</code> (~10,024 rows): Structured at the Admin Level 1 (province) per IPC validity period, used for regional clustering, global analysis, and GDELT integration.</li>
  <li><code>merged_adm1_wide_con_coordinate.parquet</code>: Augments the ADM1 wide dataset with geographic centroid coordinates (<code>latitude</code>, <code>longitude</code>) to force spatial cohesion during spatially constrained clustering.</li>
  <li><code>merged_adm1_wide_knn.parquet</code>: Provides a complete feature matrix with missing secondary values imputed via the KNN Imputer algorithm.</li>
  <li><code>merged_adm2_wide.parquet</code> (~42,957 rows): Structured at the Admin Level 2 (district/department) per IPC validity period, designed for high-resolution localized predictions.</li>
</ul>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
For Time Series Analysis (TSA) and Machine Learning (ML) modeling, irregular IPC validity windows (<code>From</code> – <code>To</code>) are expanded into a uniform monthly time axis (<code>MS</code> - Month Start). Overlapping months are aggregated via mean values, and intermediate gaps are filled using linear interpolation alongside edge carrying (<code>ffill</code>/<code>bfill</code>). This transformation extracts 9 static structural descriptors per time series, including statistical moments (mean, variance, skewness, kurtosis), long-term memory (Hurst exponent H), regularity (Approximate Entropy ApEn), and short-term memory through standardized AR(1)–AR(3) autoregressive coefficients.
</p>

<hr>

<h2 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">HERO Dataset: Sources and Methodology</h2>

<h3 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">ACLED (Armed Conflict Location & Event Data Project)</h3>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The ACLED pipeline processes raw conflict logs partitioned across multiple files (<code>violent_events_1-3.csv</code>) and matches them with IPC hunger data, yielding a consolidated dataset of 56,414 rows and 15 columns. Designed to feed machine learning models with clear conflict signals, it measures how localized violence directly drives food crisis severity and population displacement.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The pipeline filters for 48 target baseline countries monitored by IPC and enforces a temporal floor starting on January 1, 2017. Raw point-based violent event records and casualties are aggregated at the ADM1 level per month/year. To enable relational integration, ACLED's textual month and year values are formatted into <code>Mmm-YY</code> (e.g., <code>Apr-19</code>) to match the IPC <code>Date of analysis</code> key.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Integration relies on three core join keys: ISO3 country code (<code>Country</code>), temporal window (<code>Date of analysis</code>), and standardized level-1 region code (<code>adm1_pcode</code>), supported by descriptive qualitative attributes (<code>Level 1</code>, <code>Area</code>, <code>Validity period</code>, <code>From</code>, <code>To</code>, <code>Phase</code>). Geographic harmonization includes regular expression patches for non-standard P-codes (e.g., converting <code>TD</code> prefixes to <code>TCD</code> and <code>NER</code> to <code>NE</code>), as well as explicit dictionary overrides for Nigerian and Cameroonian anomalies (e.g., <code>NG00</code> -> <code>NG001</code>).
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Key output metrics include:
</p>

<ul class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
  <li><code>Events</code>: Total count of violent incidents in the ADM1 region during the month.</li>
  <li><code>Fatalities</code>: Aggregated death count from violent incidents.</li>
  <li><code>violence_ratio</code>: A calculated lethality ratio defined as Fatalities / Events (zero-corrected when events equal zero).</li>
  <li><code>Percentage</code>: Analytically recalculated as (Number / Total country population) * 100 to prevent numerical drift caused by averaging pre-existing percentages across heterogeneous populations.</li>
</ul>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Unmatched records during the <code>m:1</code> Left Join result in <code>NaN</code> values for ACLED metrics across 22,981 rows, highlighting structural key gaps in certain territories (e.g., PAK, GIN, MDG).
</p>

<hr>

<h3 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">IPC (Integrated Food Security Phase Classification)</h3>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The IPC dataset captures spatial and socio-economic structures to monitor acute food insecurity mapped across the 2024–2025 analysis cycle and historical runs. The extraction is driven by APIs from the HDX platform and IPC platforms, structuring food insecurity metrics across both <strong>wide</strong> (<code>ipc_global_area_wide_pcoded.csv</code>, 72,213 rows) and <strong>long</strong> (<code>ipc_global_area_long_pcoded.csv</code>, 64,214 rows) schemas. The data is also serialized into columnar Parquet formats using <code>fastparquet-python</code>.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The architecture follows a strict geographical hierarchy spanning national levels (ISO-3) down to micro-administrative units (Admin Levels 1–3, communes) and displacement camps (e.g., <em>Markazi Camp</em>, <em>Ali Addeh</em>), uniquely referenced via standardized OCHA P-Codes. Analysis units are classified by demographic group (rural, urban, host, or refugee populations) and primary Livelihood Zones.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The dataset tracks target population counts (<code>Number</code>) and prevalence rates (<code>Percentage</code> / <code>population_fraction_in_phase</code>) across five core IPC phases:
</p>

<ul class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
  <li><strong>Phase 1</strong>: Minimal</li>
  <li><strong>Phase 2</strong>: Stressed</li>
  <li><strong>Phase 3</strong>: Crisis</li>
  <li><strong>Phase 4</strong>: Emergency</li>
  <li><strong>Phase 5</strong>: Catastrophe/Famine</li>
  <li><strong>Phase 3+ (<code>phase_3plus_...</code>)</strong>: The primary target variable used in ML predictive models and clustering, representing the aggregated population in Phase 3, 4, and 5.</li>
</ul>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Temporal observations are categorized via <code>Validity period</code> / <code>ipc_type</code> into <code>current</code> assessments, <code>first projection</code> (short-to-medium term), and <code>second projection</code> (medium-to-long term).
</p>

<hr>

<h3 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">WFP (World Food Prices)</h3>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Powered by global food price data from the World Food Programme (WFP) via HDX, this pipeline tracks local market economics to detect early financial stress on food access. The extraction accesses the <em>Global Real-Time Food Prices</em> repository via a vertical metadata map (<code>metadata-global-real-time-food-prices.csv</code>), which dynamically supplies resource URLs for bulk processing.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The raw market dataset is denormalized in a <strong>wide format</strong> where each row captures the complete state of a physical market in a given month across 52 target countries. The time series spans from January 1, 2017, to June 2026 (truncated from historical records dating back to 2002), generating 7,225,344 rows during raw extraction.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The schema is structured into five core functional areas:
</p>

<ul class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
  <li><strong>Spatial Identification</strong>: <code>ISO3</code>, <code>country</code>, <code>adm1_name</code>, <code>adm2_name</code>, <code>mkt_name</code>, and exact point coordinates (<code>lat</code>, <code>lon</code>).</li>
  <li><strong>Temporal Keys</strong>: <code>year</code>, <code>month</code>, and combined timestamp string <code>DATES</code>.</li>
  <li><strong>Data Quality Flags</strong>: <code>currency</code>, <code>components</code>, <code>data_coverage</code> (ratio of real vs. imputed historical records), <code>index_confidence_score</code>, and <code>spatially_interpolated</code> indicators.</li>
  <li><strong>Commodity Tracking</strong>: Individual items (e.g., wheat, rice, maize) expanded into 6 distinct attributes covering standard average price, open (<code>o_</code>), high (<code>h_</code>), low (<code>l_</code>), close (<code>c_</code>), item-specific inflation (<code>inflation_</code>), and item confidence (<code>trust_</code>).</li>
  <li><strong>Macro Economic Targets</strong>: Integrated composite metrics including <code>food_price_index</code> (Food Basket Index) and <code>inflation_food_price_index</code> (general food inflation rate).</li>
</ul>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Physical market coordinates are spatially mapped to administrative boundaries using strict point-in-polygon (<code>strict_pip</code>) or elastic buffer (<code>elastic_buffer</code>) joins before temporal alignment with IPC analysis windows.
</p>

<hr>

<h3 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">IDP (Internally Displaced Persons)</h3>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Sourced from the HDX HAPI (Humanitarian API), this pipeline gathers subnational displacement stock metrics to monitor internally displaced persons (IDPs) and population movements over time. The dataset is serialized into Parquet format using Apache Arrow structures.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Structurally organized around 14 core attributes, the dataset establishes spatial context through standardized location codes (<code>location_code</code>, <code>location_name</code>) and administrative classifications spanning primary (<code>admin1_code</code>, <code>admin1_name</code>) and secondary (<code>admin2_code</code>, <code>admin2_name</code>) levels.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The automated pipeline (<code>fetch.py</code>) queries global API endpoints, executing pagination-managed passes to download displacement records for target countries. Operational tracking and source lineage are maintained through:
</p>

<ul class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
  <li><strong><code>resource_hdx_id</code></strong>: Source identifier on HDX.</li>
  <li><strong><code>reporting_round</code></strong>: Reporting cycle identifier.</li>
  <li><strong><code>idp_assessment_type</code></strong>: Methodological approach used for population tracking.</li>
  <li><strong><code>operation</code></strong>: Associated humanitarian emergency operation.</li>
  <li><strong><code>idp_population</code></strong>: Quantifiable displaced population count, extracted using the latest available report prior to the IPC end date (<code>To</code>).</li>
  <li><strong><code>idp_staleness_days</code></strong>: Quality control metric recording elapsed days between IDP data collection and IPC analysis; records exceeding a 400-day staleness threshold are discarded.</li>
</ul>

<hr>

<h3 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">Rainfall</h3>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
This pipeline collects subnational dekadal rainfall data from HDX/CHIRPS (Climate Hazards group InfraRed Precipitation with Stations) via the <code>HDXRainfallLoader</code> module, downloading raw files formatted as <code>{iso2}-rainfall-subnat-full.csv</code> under <code>data/raw_rainfall/{iso3}/</code>.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The dataset provides continuous time-series coverage starting January 1, 1981, through the present, plus short-term forecast horizons. Observations are structured at a <strong>dekad</strong> granularity (10-day intervals, 3 per month starting on the 1st, 11th, and 21st, yielding ~36 dekads per year) across Admin 1 and Admin 2 levels.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The 15-column schema comprises:
</p>

<ul class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
  <li><strong>Spatial/Temporal Metadata</strong>: <code>date</code> (dekad start date), <code>adm_level</code> (1 or 2), <code>adm_id</code> (HDX numeric ID), <code>PCODE</code> (official administrative P-code), and <code>n_pixels</code> (count of contained CHIRPS pixels, serving as an area proxy).</li>
  <li><strong>Direct Precipitation</strong>: <code>rfh</code> (actual dekad rainfall in mm) and <code>rfh_avg</code> (long-term historical mean for the dekad).</li>
  <li><strong>Rolling Accumulations</strong>: <code>r1h</code> (1-month rolling sum across 3 dekads) and <code>r3h</code> (3-month rolling sum across 9 dekads), along with their historical averages (<code>r1h_avg</code>, <code>r3h_avg</code>).</li>
  <li><strong>Anomalies & Relative Performance</strong>: <code>rfq</code> (dekad percentage of normal, calculated as approx. rfh / rfh_avg * 100), <code>r1q</code> (1-month percentage of normal), and <code>r3q</code> (3-month percentage of normal). Initial dekads naturally contain <code>NaN</code> in rolling fields until the temporal window fills.</li>
  <li><strong>Status Flags</strong>: <code>version</code> column categorizing data stability as <code>final</code> (historical), <code>prelim</code> (recent observations), or <code>forecast</code> (upcoming estimates).</li>
</ul>

<hr>

<h3 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">NDVI (Normalized Difference Vegetation Index)</h3>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Driven by data from WFP via HDX (<code>organization:wfp</code>, query <code>ndvi</code>), this pipeline gathers subnational Normalized Difference Vegetation Index metrics to track crop health, biomass density, and drought anomalies.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The pipeline utilizes <code>hdx-python-api</code> with a custom user agent (<code>NDVI_WFP_Consolidator</code>) to query, download, and parse subnational vegetation series. The extraction covers 52 target countries (e.g., AFG, ETH, YEM, ZAF, MWI, PSE) from January 1, 2017, to June 2026, truncated from historical raw data dating back to July 2002. Prior to final filtering, extraction processes generate 7,225,344 rows, saved in dual <code>.parquet</code> (<code>wfp_ndvi.parquet</code>) and <code>.csv</code> formats.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Key identifying variables include <code>country_iso3</code>, <code>hdx_dataset_name</code>, and observation <code>date</code>. The consolidated metrics include:
</p>

<ul class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
  <li><strong><code>ndvi_vim</code></strong>: Mean vegetation vigor index, weighted over agricultural pixels to measure greenness.</li>
  <li><strong><code>ndvi_viq</code></strong>: Vegetation quality index (anomaly relative to historical normal levels), serving as a direct physical proxy for agricultural drought detection.</li>
</ul>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
<em>Note on Data Processing:</em> The raw parsing pipeline ingests both full historical resources (<code>*-ndvi-subnat-full.csv</code>) and 5-year trend resources (<code>*-ndvi-subnat-5ytd.csv</code>). Because the <code>full</code> resource already contains the recent 5-year window, concatenation without explicit deduplication introduces redundant records that require post-hoc <code>drop_duplicates()</code> filtering prior to modeling.
</p>

<hr>

<h3 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">GDELT (Global Database of Events, Language, and Tone)</h3>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
Sourced from the GDELT Project via Google BigQuery (<code>gdelt-bq.gdeltv2.events_partitioned</code>), this pipeline monitors global news coverage to capture real-time media signals on conflict, geopolitical tension, and food crisis drivers.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The raw extraction queries BigQuery for 48 FIPS country codes matching IPC coverage from 2017 to 2026, retrieving 65,814,898 raw event logs. Spatial assignment maps GDELT text coordinates (extracted via GNS gazetteer) to official OCHA ADM1 and ADM2 shapefiles using spatial joins (<code>gpd.sjoin</code>, predicate <code>within</code>). To resolve geocoding artifacts (e.g., coordinates placed on country centroids), a Nearest Neighbor fallback join within a 20 km radius in EPSG:3857 projection recovers 768,770 out of 1,038,338 unmapped events. The remaining 269,568 events (0.41%) exceeding 20 km are discarded as spatial orphans.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
At ADM1 level, events are categorized using CAMEO taxonomy into 4 QuadClasses:
</p>

<ul class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
  <li><strong>QuadClass 1</strong>: Verbal Cooperation (statements, commitments).</li>
  <li><strong>QuadClass 2</strong>: Material Cooperation (aid delivery, support).</li>
  <li><strong>QuadClass 3</strong>: Verbal Conflict (threats, sanctions).</li>
  <li><strong>QuadClass 4</strong>: Material Conflict (military force, physical violence).</li>
</ul>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The final wide-format dataset (<code>gdelt_adm1_final.parquet</code> and <code>gdelt_adm2_final.parquet</code>, serialized via <code>pyarrow</code> v24.0.0) contains monthly aggregated features:
</p>

<ul class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
  <li><strong><code>n_events_qc1</code> – <code>n_events_qc4</code></strong>: Total distinct recorded event counts per QuadClass.</li>
  <li><strong><code>total_mentions_qc1</code> – <code>total_mentions_qc4</code></strong>: Total global media mentions per QuadClass.</li>
  <li><strong><code>avg_tone_qc1</code> – <code>avg_tone_qc4</code></strong>: Average media tone weighted by total mentions, ranging from negative values (panic, crisis) to positive values (peaceful resolution).</li>
</ul>

<hr>

<h3 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">IPC Reports (via Web Scraping)</h3>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
This pipeline systematically collects official narrative reports from the IPC portal (<code>https://www.ipcinfo.org/ipc-country-analysis/en/</code>) covering Acute Food Insecurity Classification analyses published between 2011 and 2026.
</p>

<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
The automated collection pipeline covers 36 target countries, discovering 502 unique report links through a two-stage architecture:
</p>

<ul class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
  <li><strong>Stage 1: URL Mapping and Deduplication</strong>: Iterates through country and year selection filters to harvest analysis URLs. Cross-year duplicate URLs are removed. Web automation utilizes <code>undetected_chromedriver</code> to bypass Cloudflare bot detection mechanisms.</li>
  <li><strong>Stage 2: Text Extraction and PDF Download</strong>: Extracts the raw "Key Results" textual body from each analysis page, achieving a 99.8% extraction success rate (501 texts successfully parsed out of 502 targets). Full PDF reports and summary snapshots are downloaded, with the automated browser session restarting every 50 pages to prevent IP rate-limiting and server bans.</li>
</ul>
