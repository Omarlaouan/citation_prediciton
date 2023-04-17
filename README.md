# Citation Prediction between Research Papers

## Overview
The goal of this project is to apply machine learning/artificial intelligence techniques to the link prediction problem of whether a research paper cites another research paper. The citation network consists of several thousands of research papers, along with their abstracts and their lists of authors. The dataset was taken from machine learning, artificial intelligence, data mining, and natural language processing conferences and journals. The project aims to use edge information to learn the parameters of a classifier and then to use the classifier to predict whether two nodes are linked by an edge or not.

## Dataset Description
The dataset contains the following files:

1. `edgelist.txt`: a citation network created from papers published at machine learning, artificial intelligence, data mining, and natural language processing venues. Nodes correspond to papers, while edges represent citation relationships. The graph is undirected.
2. abstracts.txt: it contains the abstracts of the papers.
3. authors.txt: this file contains the authors of the papers.
4. test.txt: this file contains 106,692 unordered node pairs. The goal is to predict if there is an edge between the two elements of each pair or not.

## Methods Used
The following machine learning methods are used for this project:
- Logistic Regression
- XGBoost
- MLP (Multi-Layer Perceptron)

## Results
The performance of the models is evaluated using the log loss metric. The best-performing model will be used to predict the edges in the test dataset.

## Conclusion
This project aims to explore the application of machine learning techniques to the problem of citation prediction between research papers. The main goal is to use edge information to predict whether two nodes are linked by an edge or not. By comparing the performance of different machine learning methods, we hope to identify the best model for this task.
