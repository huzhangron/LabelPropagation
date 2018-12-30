import networkx as nx
from tqdm import tqdm

def normalized_overlap(g, node_1, node_2):
    """
    Calculating the normalized neighbourhood overlap.
    """
    inter = len(set(nx.neighbors(g, node_1)).intersection(set(nx.neighbors(g, node_2))))
    unio = len(set(nx.neighbors(g, node_1)).union(set(nx.neighbors(g, node_2))))
    return float(inter)/float(unio)

def overlap(g, node_1, node_2):
    inter = len(set(nx.neighbors(g, node_1)).intersection(set(nx.neighbors(g, node_2))))
    return float(inter)

def unit(g, node_1, node_2):
    return 1

def min_norm(g, node_1, node_2):
    inter = len(set(nx.neighbors(g, node_1)).intersection(set(nx.neighbors(g, node_2))))
    min_norm = min(len(set(nx.neighbors(g, node_1))), len(set(nx.neighbors(g, node_2))))
    return float(inter)/float(min_norm)

def overlap_generator(metric, graph):
    edges = nx.edges(graph)
    edges = edges + [(edge[1], edge[0]) for edge in edges]
    return {edge: metric(graph, edge[0], edge[1]) for edge in tqdm(edges)}
