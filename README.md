# Reddit Community Detection (Louvain + Node2Vec)

This project detects communities in a subreddit network using:
- **Classical Graph Algorithms**: Louvain/Leiden community detection
- **Machine Learning**: Node2Vec + KMeans clustering
- **Visualization**: NetworkX + TSNE

## 📂 Project Structure

- `src/` → Python scripts for graph processing, clustering, and visualization
- `notebooks/` → Jupyter notebook for full workflow demo
- `results/` → Graph visualizations and cluster outputs
- `data/` → Sample edge list (replace with Reddit Hyperlinks SNAP dataset)

## 📊 Sample Result

Louvain detected 3 communities in the sample graph:

![Community Graph](results/sample_communities.png)

## ⚡ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run community detection:
```bash
python src/community_detect.py
```

3. Run Node2Vec clustering:
```bash
python src/node2vec_cluster.py
```

4. Explore full workflow in the notebook:
```bash
jupyter notebook notebooks/reddit_community_detection.ipynb
```
