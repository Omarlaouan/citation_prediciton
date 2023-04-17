# Citation Prediction between Research Papers

## Overview
The goal of this project is to apply machine learning/artificial intelligence techniques to the link prediction problem of whether a research paper cites another research paper. The citation network consists of several thousands of research papers, along with their abstracts and their lists of authors. The dataset was taken from machine learning, artificial intelligence, data mining, and natural language processing conferences and journals. The project aims to use edge information to learn the parameters of a classifier and then to use the classifier to predict whether two nodes are linked by an edge or not.
[Here is the detailled presentation of the project](Project presentation - citation prediction.pdf)

## Repo Structure
The project has the following structure:

```bash
.
├── README.md
├── Project presentation - citation prediction.pdf
├── code_clean.ipynb
├── data
│   ├── processed
│   │   ├── X_test.csv
│   │   ├── X_train.csv
│   │   ├── X_valid.csv
│   │   ├── y_test.csv
│   │   ├── y_train.csv
│   │   └── y_valid.csv
│   └── raw
│       ├── abstracts.txt
│       ├── authors.txt
│       ├── edgelist.txt
│       └── test.txt
├── doc2vec
│   ├── doc2vec_model_abstracts
│   └── doc2vec_model_authors
├── embed
│   └── abstracts_emb.json
└── viz
    └── tableau viz.twb
```

## Dataset

The dataset used in this project is available in the `data` folder, which contains two sub-folders:
- `raw`: containing the original data files:
    - `edgelist.txt`: a citation network created from papers published at machine learning, artificial intelligence, data mining, and natural language processing venues. Nodes correspond to papers, while edges represent citation relationships. The graph is undirected.
    - `abstracts.txt`: it contains the abstracts of the papers.
    - `authors.txt`: this file contains the authors of the papers.
    - `test.txt`: this file contains 106,692 unordered node pairs. The goal is to predict if there is an edge between the two elements of each pair or not.
- `processed`: containing the processed data files:
    - `X_train.csv`: training set features
    - `y_train.csv`: training set labels
    - `X_valid.csv`: validation set features
    - `y_valid.csv`: validation set labels
    - `X_test.csv`: test set features
    - `y_test.csv`: test set labels

In addition, the `doc2vec` folder contains two trained Doc2Vec models for the abstracts and authors data, and the `embed` folder contains the abstracts data in embedded format.

## Code

The `code_clean.ipynb` notebook contains cleaned and commented code for the machine learning models used in the project, including Logistic Regression, XgBoost, and MLP. 

## Visualization

The `viz` folder contains a Tableau visualization with interesting insights about the citation network.

## Methods Used
The following machine learning methods are used for this project:
- Logistic Regression
- XGBoost
- MLP (Multi-Layer Perceptron)

## Future Work

To further enhance the prediction model, additional techniques such as Node2vec, Tf-Idf, and Scibert could be explored to improve feature extraction and representation.
