#from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import ollama

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # 384-dim


def extract_skills(jd_text):
    # Dummy skills extraction based on common terms
    keywords = ["python", "machine learning", "data analysis", "sql", "deep learning",
                "java", "c++", "excel", "communication", "problem-solving", "teamwork",
                "leadership", "cloud", "aws", "azure", "data science", "ai", "llm"]
    extracted = [kw for kw in keywords if kw.lower() in jd_text.lower()]
    return extracted

def get_embedding(text):
    return model.encode(text, convert_to_tensor=False)