import networkx as nx
import community as community_louvain  # pip install python-louvain
from graph_build import load_graph

def detect_communities(graph_path: str):
    G = load_graph(graph_path)
    partition = community_louvain.best_partition(G, weight='weight')
    nx.set_node_attributes(G, partition, 'community')
    
    communities = {}
    for node, comm in partition.items():
        communities.setdefault(comm, []).append(node)
    
    print(f"Detected {len(communities)} communities")
    for c, nodes in communities.items():
        print(f"Community {c}: {nodes}")
    
    return G, partition

if __name__ == "__main__":
    G, partition = detect_communities("data/sample_edges.csv")
