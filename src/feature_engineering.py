import networkx as nx
import numpy as np
from numpy import dot
from numpy.linalg import norm

class GraphMetrics:
    def __init__(self, G, abstracts_emb, authors_emb):
        """
        Initialize the GraphMetrics class with a graph and embeddings.

        Args:
            G (networkx.Graph): The input graph.
            abstracts_emb (dict): Dictionary containing abstract embeddings for nodes.
            authors_emb (dict): Dictionary containing authors embeddings for nodes.
        """
        self.G = G
        self.abstracts_emb = abstracts_emb
        self.authors_emb = authors_emb

    def get_jaccard_coefficient(self, node1, node2):
        """Calculate the Jaccard Coefficient for two nodes."""
        jac = nx.jaccard_coefficient(self.G, [(node1, node2)])
        return list(jac)[-1][-1]

    def get_adamic_adar_index(self, node1, node2):
        """Calculate the Adamic-Adar Index for two nodes."""
        preds = nx.adamic_adar_index(self.G, [(node1, node2)])
        try:
            for u, v, p in preds:
                return p
        except:
            return 0

    def get_clustering(self, node1, node2):
        """Calculate the clustering coefficient for two nodes."""
        res = list(nx.clustering(self.G, [node1, node2]).values())
        if len(res) == 1:
            res = [res[0], res[0]]
        return res

    def get_common_neighbor_centrality(self, node1, node2):
        """Calculate the Common Neighbor Centrality for two nodes."""
        preds = nx.common_neighbor_centrality(self.G, [(node1, node2)])
        for u, v, p in preds:
            return p

    def get_cn_soundarajan_hopcroft(self, node1, node2):
        """Calculate the CN Soundarajan-Hopcroft score for two nodes."""
        preds = nx.cn_soundarajan_hopcroft(self.G, [(node1, node2)])
        try:
            for u, v, p in preds:
                return p
        except:
            return 0

    def get_ra_index_soundarajan_hopcroft(self, node1, node2):
        """Calculate the RA Soundarajan-Hopcroft score for two nodes."""
        preds = nx.ra_index_soundarajan_hopcroft(self.G, [(node1, node2)])
        try:
            for u, v, p in preds:
                return p
        except:
            return 0

    def get_degree(self, node):
        """Calculate the degree of a node."""
        return self.G.degree(node)

    def get_degree_centrality(self, node):
        """Calculate the degree centrality of a node."""
        return nx.degree_centrality(self.G)[node]

    def get_resource_allocation(self, node1, node2):
        """Calculate the Resource Allocation Index for two nodes."""
        preds = nx.resource_allocation_index(self.G, [(node1, node2)])
        for u, v, p in preds:
            return p

    def get_abstract_embedding(self, node):
        """Get the abstract embedding of a node."""
        return self.abstracts_emb.get(node, None)

    def get_authors_embedding(self, node):
        """Get the authors embedding of a node."""
        return self.authors_emb.get(node, None)

    def get_cosine_similarity(self, list_1, list_2):
        """Calculate the cosine similarity between two vectors."""
        cos_sim = dot(list_1, list_2) / (norm(list_1) * norm(list_2))
        return cos_sim

# Usage:
# G = nx.Graph()  # Your graph initialization here
# abstracts_emb = {}  # Your abstract embeddings initialization here
# authors_emb = {}  # Your authors embeddings initialization here
# metrics = GraphMetrics(G, abstracts_emb, authors_emb)
# Example usage: jac_coeff = metrics.get_jaccard_coefficient(node1, node2)
