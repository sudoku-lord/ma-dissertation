# ma-dissertation

This repository contains the code used in my MA dissertation, "Aggression, Anger, Family: Semantic Shift and Race in Mental Healthcare Settings".

The `notebooks/` folder contains the Jupyter notebooks used to write the initial code for the Reddit dataset (`med-transcriptions-test.ipynb`), find embeddings and concordances from the CRIS data (`embeddings_and_concordances.ipynb`), and calculate synonym pairs for evaluating embedding models (`find_synonym_pairs_corpus.ipynb`). An old notebook with a rougher version of the embedding calculation is also present (`join_data_OLD.ipynb`).

The `embedding_vectors/` folder contains a zipped file of all the embedding vectors output by the chosen models, as well as JSON-formatted files containing all the embedding vectors output by CBOW and skip-gram methodologies for every keyword and ethnicity.

The `results/` folder contains `top_words.py`, a short piece of code which displays the length of each concordance file, and which I used to determine which concordance files were longest for each ethnic group. It also has three sub-folders: `concordances/`, which contains files of concordance excerpts for each keyword, gender, and ethnic group combination; `cosine_sim_comparisons/`, which contains the cosine similarity measures of keywords for each pair of ethnicities/genders; and `path_comparison_results/`, which has files of both Wu-Palmer and Leacock-Chodorow measures for every keyword for each pair of ethncities/genders.
