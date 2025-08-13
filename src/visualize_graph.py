import matplotlib.pyplot as plt
import networkx as nx
from graph_build import load_graph
import community as community_louvain

def visualize_communities(graph_path: str, save_path: str = "results/sample_communities.png"):
    G = load_graph(graph_path)
    partition = community_louvain.best_partition(G, weight='weight')
    
    pos = nx.spring_layout(G, seed=42)
    colors = [partition[node] for node in G.nodes()]
    
    plt.figure(figsize=(8, 6))
    nx.draw_networkx(G, pos, node_color=colors, cmap=plt.cm.Set3, with_labels=True)
    plt.title("Detected Communities")
    plt.savefig(save_path)
    plt.show()

if __name__ == "__main__":
    visualize_communities("data/sample_edges.csv")
