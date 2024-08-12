import networkx as nx
import random
from random import randint

class TestEdgeExtractor:
    def __init__(self, G, split_rate):
        """
        Initialize the TestEdgeExtractor with a graph and a split rate.

        Args:
            G (networkx.Graph): The input graph.
            split_rate (float): The proportion of edges to be removed for validation.
        """
        self.G = G
        self.split_rate = split_rate
        self.val_edges = []
        self.y_val = []

    def extract_test_edges(self):
        """
        Randomly select a portion of the edges from the graph, remove them from the graph,
        and create a validation dataset with an equal number of positive and negative samples.

        Returns:
            networkx.Graph: The modified graph with selected edges removed.
            list: A list of validation edges (positive and negative samples).
            list: The corresponding labels for the validation edges (1 for positive samples, 0 for negative samples).
        """
        edges = list(self.G.edges())
        nodes = list(self.G.nodes())
        n = self.G.number_of_nodes()

        # Select edges randomly based on split_rate and add them to val_edges
        for edge in edges:
            if random.random() < self.split_rate:
                self.val_edges.append(edge)
                self.y_val.append(1)

        # Generate negative samples and add them to the list
        negative_samples = []
        for i in range(len(self.val_edges)):
            n1 = nodes[randint(0, n - 1)]
            n2 = nodes[randint(0, n - 1)]
            negative_samples.append((n1, n2))
            self.y_val.append(0)

        # Remove selected edges from the graph
        for edge in self.val_edges:
            self.G.remove_edge(edge[0], edge[1])

        # Combine positive and negative samples in val_edges
        self.val_edges = [*self.val_edges, *negative_samples]

        return self.G, self.val_edges, self.y_val

# Usage:
# G = nx.Graph()  # Your graph initialization here
# extractor = TestEdgeExtractor(G, 0.2)
# G, val_edges, y_val = extractor.extract_test_edges()
