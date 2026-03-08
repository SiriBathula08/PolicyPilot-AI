from sentence_transformers import SentenceTransformer
import pandas as pd
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

df = pd.read_csv("data/policies.csv")

policy_texts = df["description"].tolist()

policy_embeddings = model.encode(policy_texts)

dimension = policy_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(policy_embeddings))


def search_policy(query, top_k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []

    for i in indices[0]:
        results.append({
            "scheme": df.iloc[i]["scheme"],
            "description": df.iloc[i]["description"],
            "target": df.iloc[i]["target"]
        })

    return results