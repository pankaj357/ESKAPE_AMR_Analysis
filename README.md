# ESKAPE_Project

## Title
**Comparative Genomic Analysis of Antibiotic Resistance Gene Neighborhoods in ESKAPE Pathogens Reveals High-Risk Clusters and Mobile Genetic Element Associations**

## Description
This repository contains the full analysis pipeline and results for a comparative genomic study of ESKAPE pathogens, focusing on antibiotic resistance gene (ARG) neighborhoods and their association with mobile genetic elements (MGEs). The study uses tools like Prokka, AMRFinderPlus, and Roary.

**Note:** The manuscript based on this work is currently being finalized and has not yet been submitted. This repository is made public for transparency and reproducibility.

## Repository Structure
```
ESKAPE_Project/
├── amr_full_results.csv           # Complete AMRFinderPlus output merged across all strains
├── amr_matrix.csv                 # Binary matrix (genes vs strains)
├── AMR_Results/                   # Intermediate AMRFinderPlus outputs
├── AMRF_input/                    # FASTA files and GFFs used for AMRFinderPlus
├── AMRF_output/                   # Parsed and post-processed AMRFinderPlus results
├── figures/                       # All figures used in the manuscript
├── genomes/                       # Raw genome FASTA files (.fna)
├── prokka_annotations/           # Prokka annotation output (.gff, .gbk, etc.)
├── roary_gffs/                   # GFF files prepared for Roary
├── roary_per_species/            # Roary results (pan-genome analysis)
├── script/                       # Python and shell scripts for processing and visualization
├── strain_specific_ARGs.csv      # Table listing unique ARGs for each strain
└── README.md                     # This file
```

## How to Use
1. Install dependencies (Python ≥3.8, AMRFinderPlus, Prokka, Roary)
2. Run scripts from the `script/` folder in order to replicate analysis.
3. Figures are available under `figures/` and can be reused with citation.

## Contact
**Author:** Pankaj  
**Affiliation:** Indian Agricultural Research Institute (IARI), New Delhi  
**Email:** ft.pank@gmail.com

## License
This project is made available under the MIT License.