import os
import pandas as pd
import urllib.request

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
SNAP_URL = "https://snap.stanford.edu/data/soc-redditHyperlinks-title.tsv"

def download_snap():
    file_path = os.path.join(DATA_DIR, "soc-redditHyperlinks-title.tsv")
    if not os.path.exists(file_path):
        print("Downloading Reddit Hyperlinks dataset...")
        urllib.request.urlretrieve(SNAP_URL, file_path)
        print("Download complete.")
    else:
        print("Dataset already downloaded.")
    return file_path

def preprocess():
    file_path = download_snap()
    print("Processing dataset...")
    df = pd.read_csv(file_path, sep="\t", header=None, names=["source", "target", "post_id", "timestamp"])

    # Remove self-loops (optional)
    df = df[df["source"] != df["target"]]

    # Aggregate into weighted edge list
    edge_weights = df.groupby(["source", "target"]).size().reset_index(name="weight")

    # Save to CSV
    output_path = os.path.join(DATA_DIR, "reddit_edges.csv")
    edge_weights.to_csv(output_path, index=False)
    print(f"Saved preprocessed edge list to {output_path}")

if __name__ == "__main__":
    preprocess()
