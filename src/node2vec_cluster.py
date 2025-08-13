import networkx as nx
from node2vec import Node2Vec
from sklearn.cluster import KMeans
from graph_build import load_graph

def node2vec_clustering(graph_path: str, n_clusters: int = 3):
    G = load_graph(graph_path)
    node2vec = Node2Vec(G, dimensions=16, walk_length=10, num_walks=50, workers=2)
    model = node2vec.fit(window=5, min_count=1)
    
    embeddings = [model.wv[node] for node in G.nodes()]
    nodes = list(G.nodes())
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(embeddings)
    labels = kmeans.labels_
    
    for cluster_id in range(n_clusters):
        cluster_nodes = [nodes[i] for i, lbl in enumerate(labels) if lbl == cluster_id]
        print(f"Cluster {cluster_id}: {cluster_nodes}")
    
    return nodes, labels

if __name__ == "__main__":
    node2vec_clustering("data/sample_edges.csv", n_clusters=3)
