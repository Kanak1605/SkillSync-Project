from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from typing import List, Dict
import numpy as np
def build_resume_corpus(resumes: List[Dict]) -> List[str]:
    return [r.raw_text or "" for r in resumes]
def rank_resumes_for_job(job_text: str, resumes: List[Dict], top_k=10):
    corpus = build_resume_corpus(resumes)
    if not any(corpus):
        return []
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform([job_text] + corpus)
    job_vec = tfidf_matrix[0]
    resume_vecs = tfidf_matrix[1:]
    cosine_similarities = linear_kernel(job_vec, resume_vecs).flatten()
    ranked_idx = np.argsort(-cosine_similarities)[:top_k]
    results = []
    for idx in ranked_idx:
        results.append({
            "resume_id": resumes[idx].id,
            "score": float(cosine_similarities[idx])
        })
    return results
