---
title: "Research"
layout: default
excerpt: "RT2 Lab -- Research"
sitemap: false
permalink: /research/
---

# Overview

Our lab investigates how molecular interactions govern gene expression, with a central focus on post-transcriptional regulation. We integrate multi-omics approaches—including transcriptomics, ribosome profiling, and proteomics—to study expression dynamics across development, differentiation, and aging. By combining these datasets, we uncover regulatory mechanisms that control gene output beyond transcription. A major area of our work involves mapping expression changes during dynamic biological processes like yeast meiosis and embryonic stem cell differentiation, allowing us to pinpoint both regulated targets and their upstream RNA-binding protein (RBP) regulators.

To study how RBPs interact with both RNAs and other proteins, we have developed innovative methods such as SPIDR and SEC-MX. These technologies allow us to examine protein-RNA and protein-protein interactions (PPIs) at high resolution and scale. We apply these methods to explore how RBPs shape processes such as alternative polyadenylation and translational regulation, and how co-translational folding and chaperone assistance influence PPI formation. Together, our research covers quantitative protein dynamics and molecular interactions, offering a comprehensive view of gene regulation in dynamic cellular contexts.


# Quantitative Expression Dynamics

Our lab integrates multi-omics approaches such as transcriptomics, ribosome profiling, global proteomics, and dynamic SILAC to investigate how gene expression is modulated over time and across cellular states. These strategies allow us to build quantitative models that link RNA production, translational efficiency, and protein stability, revealing how cells coordinate these layers to drive processes like differentiation, immune activation, and aging.

To measure protein turnover at scale, we developed dynamic Stable-Isotope Labeling of Organoids (dSILO)—a novel approach to quantify proteome-wide degradation rates in 3D organoid systems. Applying dSILO to pancreatic ductal adenocarcinoma (PDA) organoids, we found that metastatic organoids exhibit accelerated global protein turnover compared to primary tumor counterparts. We observed that proteins functioning within macromolecular complexes show significantly more coordinated turnover rates than expected by chance, suggesting that complex membership imposes constraints on protein lifetime.

We also explore how transcriptional and translational regulation interact to shape expression dynamics. In collaboration with the Brar Lab, we discovered that in meiotic yeast, nearly 10% of genes switch between producing a canonical, translatable mRNA and a longer isoform known as a Long Undecoded Transcript Isoform (LUTI). These LUTIs include upstream open reading frames (uORFs) in their extended 5′ UTRs, which reduce translational efficiency and suppress protein production. This regulated isoform switching acts as a gene-specific mechanism to temporally repress translation, offering a new layer of control over expression that is distinct from transcript abundance.

<div style="text-align: center">
![LUTI]({{ site.url }}{{ site.baseurl }}/images/other/LUTI_mechanism_25_percent.png)
</div>

Building on these findings, we are now applying similar principles to multicellular systems. We have collected a time-course dataset of embryonic stem cell (ESC) differentiation, with matched measurements of RNA levels, translation rates, and protein abundances. This rich dataset allows us to dissect how regulation at the 5′ and 3′ untranslated regions (UTRs) influence translation and protein output. 

<div style="text-align: center">
![ESC Differentiation]({{ site.url }}{{ site.baseurl }}/images/other/fullDifferentiation_w_sampleCollection_25_percent.png)
</div>



# Molecular Interactions

We aim to understand how molecular interactions form and remodel as cells respond to dynamic biological processes. Building on our work in expression dynamics and protein turnover, our lab develops scalable approaches to study interaction networks across the proteome and transcriptome. By investigating how protein complexes assemble and reconfigure, and how protein-RNA interactions control gene expression, we seek to uncover mechanistic principles that drive cellular dynamics during development, stress, and aging.

## Protein-RNA Interactions
Our lab is advancing the study of protein–RNA interactions through the development of SPIDR (Split and Pool Identification of RBP targets), a highly multiplexed method that enables the simultaneous profiling of RNA binding sites for dozens to hundreds of RNA-binding proteins (RBPs) in a single experiment. Traditional techniques like CLIP-seq are limited to one protein at a time, but SPIDR overcomes this to link proteins with their RNA targets in a multiplexed way at single-nucleotide resolution. This technology represents a two-orders-of-magnitude improvement in throughput, while retaining the precision and reliability of existing methods.
SPIDR offers not just large-scale data, but also immediate molecular insights into RNA regulation, enabling the systematic discovery of RBP binding sites, interaction dynamics, and regulatory mechanisms across different cellular states. This platform opens new avenues for exploring both transcriptional and post-transcriptional gene regulation with unmatched resolution and throughput.

Using SPIDR, we have begun to uncover the dynamic and combinatorial nature of protein-RNA interactions at scale. For example, in studying the response of HEK293 cells to mTOR inhibition, SPIDR revealed that the RBP LARP1 binds specifically to the mRNA entry channel of the 40S ribosome—showing how SPIDR can give structural insight into protein-RNA interactions. We also observed condition-dependent changes in ribonucleoprotein composition, such as increased LARP1 binding and decreased eIF4A association under mTOR inhibition. These results highlight how SPIDR can resolve dynamic changes in RNA-protein complexes that underlie gene regulatory responses, even in pathways that have been studied for decades.

<div style="text-align: center">
![SPIDR Method Overview]({{ site.url }}{{ site.baseurl }}/images/other/spidr_protocol_diagram_50_percent.png)
</div>

## Protein-Protein Interactions
Our lab is developing and applying innovative methods to study the dynamic protein-protein interaction (PPI) networks that regulate RNA-binding protein (RBP) function throughout the RNA life cycle. RBPs work together in diverse ribonucleoprotein complexes (RNPs), which continually rearrange during RNA processing, localization, translation, and decay. In collaboration with Gene Yeo’s lab, we constructed an RNA-aware, RBP-centric PPI map across these stages using immunoprecipitation-mass spectrometry (IP-MS) of ~100 endogenous RBPs, with and without RNA digestion. This large-scale study revealed thousands of RNA-dependent and -independent interactions among over 1,100 proteins and highlighted hub proteins like ERH and SNRNP200 that play multifaceted roles across subcellular compartments and stress conditions. These results provide a valuable resource for understanding the modular organization and functional transitions of RNA-regulatory networks.

To enable dynamic PPI measurements at scale, we developed SEC-MX, a mass spectrometry-based method that combines size exclusion chromatography (SEC) with tandem mass tag (TMT) multiplexing. SEC-MX reduces the number of required LC-MS/MS runs by tenfold while maintaining resolution and sensitivity, making it practical to study PPI changes over time or between conditions. SEC-MX also supports efficient enrichment of post-translational modifications (PTMs), such as phosphorylation, allowing us to examine how PTMs influence protein complex assembly. Using this approach, we found that most cellular proteins exist in multiple assembly states and that phosphorylation is often specific to certain assemblies. These data offer mechanistic hypotheses about PTM-regulated interactions.

<div style="text-align: center">
![SEC-MX]({{ site.url }}{{ site.baseurl }}/images/other/protein_centric_hypothetical_wide_20_percent.png)
</div>

<!-- [put mRNA life cycle figure here] -->

