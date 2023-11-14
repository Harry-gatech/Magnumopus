# Magnumopus
A versatile Python package developed for advanced bioinformatics analysis. 


Overview:

Welcome to MagnumOpus, a versatile Python package developed for advanced bioinformatics analysis. This toolkit combines the functionality of isPCR and the Needleman-Wunsch algorithm, providing a unified solution for in-silico PCR and global sequence alignment.

Features:

isPCR Functionality:

The isPCR module within MagnumOpus allows users to predict amplicons from primer and assembly files seamlessly.
Unified into a single function "ispcr," users can input primer and assembly file paths along with a maximum amplicon size.
Needleman-Wunsch Algorithm:

The Needleman-Wunsch algorithm has been implemented in Python and integrated into the MagnumOpus toolkit.
The function "needleman_wunsch" aligns two sequences based on user-defined match, mismatch, and gap scores.
amplicon_align.py Script:

The amplicon_align script provides a command-line interface for easy utilization of MagnumOpus functionalities.
Users can input assembly files, primer file, maximum amplicon size, match, mismatch, and gap scores.
The script performs isPCR on both assembly files, aligns amplicons, and prints the best alignment and alignment score.

Directory Structure:

└── magnumopus
   ├── __init__.py
   ├── ispcr.py
   ├── nw.py
   └── more_module_files_if_you_like.py

└── amplicon_align.py


