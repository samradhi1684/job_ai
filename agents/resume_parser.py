import os
import pdfplumber
from sentence_transformers import SentenceTransformer


# Load model globally
model = SentenceTransformer('all-MiniLM-L6-v2')  # You can pick other models


def get_embedding(text):
    return model.encode(text, convert_to_tensor=False).tolist()

def extract_text(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
            return text.strip()
    except Exception as e:
        print(f"❌ Error reading {pdf_path}: {e}")
        return ""

def get_all_resumes_text(cv_folder_path):
    resumes_data = []
    for file in os.listdir(cv_folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(cv_folder_path, file)
            text = extract_text(path)  # ✅ FIXED
            resumes_data.append({"filename": file, "text": text})
    return resumes_data

def extract_skills(text):  # ✅ NEW FUNCTION
    keywords = ["Python", "Java", "SQL", "Machine Learning", "Data Analysis", "Excel", "C++", "AWS"]
    found = [kw for kw in keywords if kw.lower() in text.lower()]
    return found
