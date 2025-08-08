import pandas as pd
import networkx as nx

def load_graph(edge_file: str) -> nx.Graph:
    df = pd.read_csv(edge_file)
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['source'], row['target'], weight=row['weight'])
    print(f"Graph Loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G

if __name__ == "__main__":
    G = load_graph("data/sample_edges.csv")
