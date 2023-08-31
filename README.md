# ma-dissertation

This repository contains the code used in my MA dissertation, "Aggression, Anger, Family: Semantic Shift and Race in Mental Healthcare Settings".

The `notebooks/` folder contains the Jupyter notebooks used to write the initial code for the Reddit dataset (`med-transcriptions-test.ipynb`), find embeddings and concordances from the CRIS data (`embeddings_and_concordances.ipynb`), and calculate synonym pairs for evaluating embedding models (`find_synonym_pairs_corpus.ipynb`). An old notebook with a rougher version of the embedding calculation is also present (`join_data_OLD.ipynb`).

The `embedding_vectors/` folder contains a zipped file of all the embedding vectors output by the chosen models, as well as JSON-formatted files containing all the embedding vectors output by CBOW and skip-gram methodologies for every keyword and ethnicity.

