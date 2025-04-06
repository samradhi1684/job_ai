import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def rank_candidates(jd_embedding, resume_embeddings):
    scores = []
    for name, emb in resume_embeddings.items():
        similarity = cosine_similarity([jd_embedding], [emb])[0][0]
        scores.append((name, similarity))
    return sorted(scores, key=lambda x: x[1], reverse=True)
