---
layout: default
title: "Text analysis"
permalink: /Text-analysis.html
show_sidetoc: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Text analysis"

---

<div class="full-width-wrapper">
    <img src="{{ site.baseurl }}/assets/images/header.svg" alt="sbd-pattern" class="full-width-image">
</div>



<h1 class="text-gradient font-weight-bold mb-4 fade-in-up" style="animation-delay: 0.1s;">From Words to Data: Mapping Famine Drivers Through Term Frequency</h1>


<p class="lead fade-in-up" style="font-size: 1.1rem; line-height: 1.7; text-align: justify; animation-delay: 0.2s;">
In IPC reports, words are never neutral: their recurrence forms the digital footprint of a real-world emergency. Textual analysis reveals that the bigram <b>'food insecurity'</b> dominates the dataset with 1,068 occurrences, frequently paired with critical terms like <b>'acute'</b> (658) and <b>'malnutrition'</b> (154). However, it is the underlying drivers that shape this semantic map. The frequency of words like <b>'price'</b> (524) highlights economic shocks and barriers to food access, while the agricultural production cluster (<i>'production'</i>, <i>'harvest'</i>, <i>'crop'</i>) captures the immediate impact of climate factors on the ground. In this context, counting words means mapping the boundaries of hunger.
</p>

<div class="row my-5 text-center">
    <div class="col-md-6 mb-4">
        <h5 class="mb-3 fw-bold text-secondary fade-in-up" style="animation-delay: 0.3s;">Top 50 Words (Treemap)</h5>
        <img src="{{ site.baseurl }}/assets/images/treemap_mixed.png" alt="Treemap of Unigrams and Bigrams" class="img-fluid rounded shadow-sm hover-lift fade-in-up" style="max-width: 100%; border: 1px solid #e0e0e0; animation-delay: 0.4s;">
    </div>
    <div class="col-md-6 mb-4">
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
While the macroeconomic, climatic, and structural drivers of hunger are universal, their impact is intensely localized. By normalizing the frequency of these critical terms for each country, we can generate a global heatmap of vulnerability. The visualization below reveals the unique crisis signature of each region: some nations are predominantly scarred by conflict and displacement, while others suffer primarily from the collapse of agricultural production due to climate extremes. This heatmap translates semantic prevalence into a stark geographic reality.
</p>

<div class="my-5 text-center">
    <img src="{{ site.baseurl }}/assets/images/heatmap_driver.png" alt="Heatmap of Food Insecurity Drivers by Country" class="img-fluid rounded shadow-lg" style="max-width: 100%; border: 1px solid #e0e0e0;">
</div>

<hr class="section-divider">


## <span class="text-gradient">Decoding the Narrative: The NLP Pipeline</span>

To move beyond simple word counts and uncover the hidden semantic structures of food crises, we implemented an advanced Natural Language Processing (NLP) pipeline. The goal was not just to read the reports, but to let the data organize itself into coherent thematic clusters.

<div class="row mt-4">
    <div class="col-md-12 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-user-secret"></i> 1. Anonymization & Tag Removal (GLiNER)</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        Before diving into the vocabulary, it was crucial to anonymize the texts to prevent a specific type of bias. By utilizing <b>GLiNER</b> (<a href="https://arxiv.org/abs/2311.08526" target="_blank">Generalist Model for Named Entity Recognition using Bidirectional Transformer</a>), we identified and masked named entities such as specific locations, organizations, and individuals. Rooted in the <b>BERT</b> family of bidirectional transformers, GLiNER was chosen because, as demonstrated in its founding paper, it can significantly outperform massive Large Language Models (LLMs) on zero-shot Named Entity Recognition tasks, while remaining highly efficient. The primary goal of this anonymization was to prevent the clustering algorithm from grouping reports based on geopolitical similarity (e.g., countries located in the same region), forcing it instead to cluster documents based on the similarity of the underlying drivers inherent to food insecurity. Since this phase focused on a statistical analysis of word frequency and co-occurrence (TF-IDF), the entity tags generated by GLiNER were completely removed.
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
    <div class="col-md-6 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-filter"></i> 2. Noise Reduction & Vectorization</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        The first challenge was cleaning the data. We removed standard English stopwords along with specific geographical entities (country names) to ensure the algorithms focused strictly on the <i>nature</i> of the crisis rather than the location. Using <b>TF-IDF</b> (Term Frequency-Inverse Document Frequency), we transformed the raw text of the reports into a high-dimensional mathematical space, capturing both unigrams and bigrams to preserve context (e.g., "food insecurity" instead of just "food").
        </p>
    </div>
    <div class="col-md-6 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-compress-arrows-alt"></i> 3. Dimensionality Reduction</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        Since the TF-IDF matrix contained thousands of features, we applied <b>LSA (Latent Semantic Analysis)</b> via TruncatedSVD to extract the most important underlying concepts. However, to combat the "curse of dimensionality" before clustering, we utilized <b>UMAP (Uniform Manifold Approximation and Projection)</b> to further compress the semantic space into <b>5 dimensions</b>. UMAP acts as a topological lens, pulling semantically similar reports close together while pushing unrelated ones apart.
        </p>
    </div>
</div>
<div class="row">
    <div class="col-md-12 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-project-diagram"></i> 4. Clustering Strategies</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        To categorize the reports into distinct crisis typologies, we tested two different clustering algorithms. First, <b>K-Means</b>, an approach that partitions the space into a predefined number of clusters, perfect for segmenting broad macro-trends. Second, <b>HDBSCAN</b>, a density-based algorithm capable of discovering clusters of varying shapes and sizes while isolating "noise" (reports that don't fit into any clear pattern). 
        </p>
    </div>
</div>

<div class="row mt-4">
    <div class="col-md-12 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-search-plus"></i> Example: HDBSCAN Cluster 7 (Agricultural Shocks & Dry Spells)</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        To understand the power of the clustering pipeline combined with <b>c-TF-IDF</b>, let's look at two completely different reports that the algorithm grouped into the same cluster (HDBSCAN Cluster 7). Despite originating from different countries (Zimbabwe and Uganda) and different periods, they describe an identical chain of events: a climate shock (prolonged <b>dry spells</b>) that destroys <b>crop production</b> and stresses <b>livestock</b>, forcing rural <b>households</b> to rely entirely on local <b>markets</b>. However, because of soaring <b>prices</b> and low <b>incomes</b>, these families face restricted <b>access</b> to food, resulting in a severe drop in dietary <b>diversity</b>.
        <br><br>
        To maximize visual clarity, we have highlighted in <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">blue</span> the top cluster keywords extracted by c-TF-IDF (<i>livestock, market, income, dry spell, normal, adequate, water, diversity</i>). We have also highlighted in <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">yellow</span> other highly significant words that both texts share despite referring to different crises, showing how structurally identical these situations are.
        </p>
        <div class="example-box mt-3 p-3 rounded" style="background-color: #f8f9fa; border-left: 4px solid #17a2b8;">
            <h5 style="font-size: 1rem; font-weight: bold; color: #495057;"><i class="fas fa-map-marker-alt"></i> Zimbabwe <span style="font-size: 0.85rem; color: #6c757d; font-weight: normal;">(Apr 2013 - Apr 2014)</span></h5>
            <p style="font-family: monospace; font-size: 0.85rem; color: #6c757d; margin-bottom: 15px; line-height: 1.5; text-align: justify;">
                "Agriculture is a key livelihoods activity for the majority of Zimbabwe's rural population. Mainly because of the <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">poor</span> rainfall <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">season</span> quality, <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">production</span> of major <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">crops</span> in 2012/13 fell compared to last <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">season</span>'s harvest. <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">Livestock</span> (cattle, sheep and goats) were in a fair to <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">good</span> condition in April 2013. Grazing and <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">water</span> for <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">livestock</span> were generally <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">adequate</span> in most parts of the country save for the communal <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">areas</span>, where it was, as is <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">normal</span>, generally inadequate. Currently, staple cereals are generally available throughout the country from both own <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">production</span> and the <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">market</span>, but low <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">income</span>s and higher than <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">normal</span> <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">prices</span> of staple cereals are limiting household <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">access</span>. There is continued limited <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">diversity</span> of <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">food</span> consumed by rural <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">households</span>... Rainfall distribution was erratic... The first effective rains were followed by a long <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">dry spell</span> which was coupled by very high temperatures... Most of the <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">households</span> in the affected <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">areas</span> will still depend on the <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">market</span> for their basic <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">food</span> needs."
            </p>
            <h5 style="font-size: 1rem; font-weight: bold; color: #495057;"><i class="fas fa-map-marker-alt"></i> Uganda <span style="font-size: 0.85rem; color: #6c757d; font-weight: normal;">(Jan 2017 - Feb 2018)</span></h5>
            <p style="font-family: monospace; font-size: 0.85rem; color: #6c757d; margin-bottom: 0; line-height: 1.5; text-align: justify;">
                "<span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">Food</span> in <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">market</span>s is easily accessed and affordable because <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">prices</span> have declined and the <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">households</span> have <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">adequate</span> purchasing power. They have <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">good</span> nutrition levels because they are able to eat two or more time a day with a <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">good</span> dietary <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">diversity</span>. Currently <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">access</span> to <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">livestock</span> products is <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">good</span> because of the available pasture and <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">water</span>. However, <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">livestock</span> <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">production</span> is expected to decline due to expected dry conditions... The <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">households</span> in these regions all suffered the effects of prolonged <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">dry spell</span>s that stressed most of the <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">crops</span> and reduced yields... However, as the <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">production</span> in the second <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">season</span> is anticipated to be <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">normal</span> and above <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">normal</span> for some <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">areas</span>... For those whose livelihood depends mainly on <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">livestock</span>, the situation may not improve due to the expected <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">dry spell</span> in January and February, which is likely to reduce the availability of <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">water</span> and pasture... They have <span style="background-color: #fff3cd; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #856404;">poor</span> purchasing power as their <span style="background-color: #d1ecf1; padding: 2px 4px; border-radius: 3px; font-weight: bold; color: #0c5460;">income</span>s are low..."
            </p>
        </div>
    </div>
</div>

<hr class="section-divider">

<hr class="section-divider">

## Interactive Timeline & Semantic Clusters

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>

<div id="vis" style="width: 100%; overflow-x: auto;"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    const spec = "{{ site.baseurl }}/assets/data/grafico_altair.json";
    vegaEmbed('#vis', spec, {actions: false}).catch(console.error);
});
</script>

<hr class="section-divider">

## <span class="text-gradient">Phase 2: Deep Semantic Embeddings</span>

While TF-IDF effectively captures statistical word frequencies, it can struggle with the nuanced context of complex narratives. To address this, we advanced the pipeline to a purely semantic approach.

<div class="row mt-4">
    <div class="col-md-6 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-brain"></i> 1. Dense Semantic Embeddings (BGE-M3)</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        Using the state-of-the-art <b>BAAI/bge-m3</b> model, we transformed the anonymized reports into dense, high-dimensional vectors (1024 dimensions). Rooted in the powerful <b>XLM-RoBERTa</b> architecture (part of the BERT family of encoder-only transformers), this model was chosen for its massive 8192-token context window—allowing it to ingest entire reports without fragmenting the text—and its exceptional ability to map technical synonyms (e.g., "prolonged water stress" and "rainfall deficit") into the exact same semantic space across multiple languages.
        </p>
    </div>
    <div class="col-md-6 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-globe"></i> 2. Geographic Entropy & Validation</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        After applying UMAP (reducing to 5 dimensions) and clustering with K-Means and HDBSCAN, we needed to rigorously validate the semantic purity of the clusters. We calculated the <b>Geographic Entropy</b> of each cluster to prove that the algorithm wasn't simply grouping reports by country. High entropy scores confirmed that our clusters successfully aggregated reports across different continents based strictly on their underlying food insecurity drivers.
        </p>
    </div>
</div>
<div class="row">
    <div class="col-md-12 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-robot"></i> 3. Topic Extraction (c-TF-IDF) & LLM-as-a-Judge</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        Once the clusters were formed in both Phase 1 and Phase 2, the final step was understanding what they represented. We used <b>class-based TF-IDF (c-TF-IDF)</b>, a technique popularized by the paper <i>"BERTopic: Neural topic modeling with a class-based TF-IDF procedure"</i>. This methodology represents a paradigm shift in topic modeling because it <b>decouples</b> the semantic clustering of documents from the extraction of their topic representations. By treating all documents within a single cluster as one massive "super-document", c-TF-IDF generates highly coherent and distinctive keywords, empirically outperforming traditional generative probabilistic models like Latent Dirichlet Allocation (LDA). Rather than struggling to balance word frequencies and semantic meaning simultaneously, this approach guarantees high topic diversity and human-readable accuracy. Finally, we employed an <b>LLM-as-a-Judge</b> approach, leveraging a Large Language Model to interpret these c-TF-IDF keywords, evaluate the semantic coherence of the clusters, and translate mathematical groupings into clear, actionable narratives of conflict, drought, and economic collapse.
        </p>
    </div>
</div>
