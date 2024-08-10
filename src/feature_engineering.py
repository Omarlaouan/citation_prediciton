def get_jaccard_coefficient(current_node1, current_node2):
    """Calculate the Jaccard Coefficient for two nodes."""
    jac = nx.jaccard_coefficient(G, [(current_node1, current_node2)])
    return list(jac)[-1][-1]


def get_adamic_adar_index(e1, e2):
    """Calculate the Adamic-Adar Index for two nodes."""
    preds = nx.adamic_adar_index(G, [(e1, e2)])
    try:
        for u, v, p in preds:
            return p
    except:
        return 0


def get_clustering(e1, e2):
    """Calculate the clustering coefficient for two nodes."""
    res = list(nx.clustering(G, [e1, e2]).values())
    if len(res) == 1:
        res = [res[0], res[0]]
    return res


def get_common_neighbor_centrality(e1, e2):
    """Calculate the Common Neighbor Centrality for two nodes."""
    preds = nx.common_neighbor_centrality(G, [(e1, e2)])
    for u, v, p in preds:
        return p


def get_cn_soundarajan_hopcroft(e1, e2):
    """Calculate the CN Soundarajan-Hopcroft score for two nodes."""
    preds = nx.cn_soundarajan_hopcroft(G, [(e1, e2)])
    try:
        for u, v, p in preds:
            return p
    except:
        return 0


def get_ra_index_soundarajan_hopcroft(e1, e2):
    """Calculate the RA Soundarajan-Hopcroft score for two nodes."""
    preds = nx.ra_index_soundarajan_hopcroft(G, [(e1, e2)])
    try:
        for u, v, p in preds:
            return p
    except:
        return 0


def get_degree(node):
    """Calculate the degree of a node."""
    res = G.degree(node)
    return res


def get_degree_centrality(node):
    """Calculate the degree centrality of a node."""
    res = nx.degree_centrality(G)[0]
    return res


def get_resource_allocation(e1, e2):
    """Calculate the Resource Allocation Index for two nodes."""
    preds = nx.resource_allocation_index(G, [(e1, e2)])
    for u, v, p in preds:
        return p


def get_abstract_embedding(node):
    """Get the abstract embedding of a node."""
    res = abstracts_emb[node]
    return res


def get_authors_embedding(node):
    """Get the authors embedding of a node."""
    res = authors_emb[node]
    return res


def get_cosine_similarity(list_1, list_2):
    """Calculate the cosine similarity between two vectors."""
    cos_sim = dot(list_1, list_2) / (norm(list_1) * norm(list_2))
    return cos_sim