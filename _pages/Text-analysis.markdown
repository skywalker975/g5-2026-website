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
        Before diving into the vocabulary, it was crucial to anonymize the texts to prevent a specific type of bias. By utilizing <b>GLiNER</b> (<a href="https://arxiv.org/abs/2311.08526" target="_blank">Generalist Model for Named Entity Recognition using Bidirectional Transformer</a>)—a state-of-the-art model that delivered excellent performance—we identified and masked named entities such as specific locations, organizations, and individuals. The primary goal of this anonymization was to prevent the clustering algorithm from grouping reports based on geopolitical similarity (e.g., countries located in the same region), forcing it instead to cluster documents based on the similarity of the underlying drivers inherent to food insecurity. Since this phase focused on a statistical analysis of word frequency and co-occurrence (TF-IDF), the entity tags generated by GLiNER were completely removed.
        </p>
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
    <div class="col-md-6 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-project-diagram"></i> 4. Clustering Strategies</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        To categorize the reports into distinct crisis typologies, we tested two different clustering algorithms. First, <b>K-Means</b>, an approach that partitions the space into a predefined number of clusters, perfect for segmenting broad macro-trends. Second, <b>HDBSCAN</b>, a density-based algorithm capable of discovering clusters of varying shapes and sizes while isolating "noise" (reports that don't fit into any clear pattern). 
        </p>
    </div>
    <div class="col-md-6 mb-4 glass-card p-4 hover-lift">
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-tags"></i> 5. Topic Extraction (c-TF-IDF)</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        Once the clusters were formed, the final step was understanding what they represented. Using a technique derived from BERTopic called <b>class-based TF-IDF (c-TF-IDF)</b>, we extracted the most distinctive keywords for each cluster. This allowed us to automatically generate semantic labels, translating mathematical groupings back into human-readable narratives of conflict, drought, and economic collapse.
        </p>
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
        Using the state-of-the-art <b>BAAI/bge-m3</b> model, we transformed the anonymized reports into dense, high-dimensional vectors (1024 dimensions). This transformer model was chosen for its massive 8192-token context window—allowing it to ingest entire reports without fragmenting the text—and its ability to group technical synonyms (e.g., "prolonged water stress" and "rainfall deficit") into the exact same semantic space.
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
        <h4 style="color: #007bff; font-weight: bold;"><i class="fas fa-robot"></i> 3. Advanced Topic Modeling & LLM-as-a-Judge</h4>
        <p class="lead" style="font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        To interpret the clusters, we integrated a lemmatization pipeline (NLTK) with c-TF-IDF to extract clean, root-level keywords. Finally, we employed an <b>LLM-as-a-Judge</b> approach, leveraging a Large Language Model to describe the clusters and evaluate their semantic coherence, translating mathematical groupings into clear, actionable narratives.
        </p>
    </div>
</div>
