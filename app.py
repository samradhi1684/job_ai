import streamlit as st
import pandas as pd
import os
from io import BytesIO
from agents import jd_parser, resume_parser, skill_matcher

# --- CONFIG ---
st.set_page_config(page_title="AI Job Screening System", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# --- TITLE ---
st.title("🧠 AI Job Screening System")

# --- LOAD JD CSV ---
jd_df = pd.read_csv("resumes/job_description.csv", encoding="ISO-8859-1")
jd_df.columns = jd_df.columns.str.strip()

# --- SIDEBAR ---
with st.sidebar:
    st.header("📋 Controls")
    jd_options = jd_df['Job Title'].unique().tolist()
    selected_jd = st.selectbox("Choose Job Role", jd_options)
    min_score = st.slider("Minimum Match Score", 0.0, 1.0, 0.55)
    screen_now = st.button("🔍 Screen Candidates")

# --- JD PREVIEW ---
jd_text = jd_df[jd_df['Job Title'] == selected_jd]['Description'].values[0]
st.subheader(f"📌 Job Description: {selected_jd}")
st.text_area("Job Description Preview", jd_text, height=200, disabled=True)

# --- RESUME SCAN ---
st.subheader("📂 Resumes in Dataset")
cv_folder = "resumes/CVs1/"
cv_files = [os.path.join(cv_folder, f) for f in os.listdir(cv_folder) if f.endswith(".pdf")]
st.write(f"📄 Found `{len(cv_files)}` resumes.")

# --- PROCESS BUTTON ---
if screen_now:
    if not jd_text or len(cv_files) == 0:
        st.error("❗ Make sure a JD is selected and resumes exist.")
    else:
        with st.spinner("⚙️ Analyzing resumes and calculating match scores..."):

            # JD EMBEDDING
            jd_skills = jd_parser.extract_skills(jd_text)
            jd_embedding = jd_parser.get_embedding(", ".join(jd_skills))

            # RESUME EMBEDDING
            resume_embeddings = {}
            resume_texts = {}
            for path in cv_files:
                try:
                    with open(path, 'rb') as f:
                        file_data = BytesIO(f.read())
                        text = resume_parser.extract_text(path)
                        skills = resume_parser.extract_skills(text)
                        emb = resume_parser.get_embedding(", ".join(skills))
                        fname = os.path.basename(path)
                        resume_embeddings[fname] = emb
                        resume_texts[fname] = text
                except Exception as e:
                    st.warning(f"⚠️ Error processing {os.path.basename(path)}: {str(e)}")

            # RANKING
            ranked = skill_matcher.rank_candidates(jd_embedding, resume_embeddings)
            filtered = [r for r in ranked if r[1] >= min_score]

        # --- DISPLAY RESULTS ---
        st.success(f"🏆 Top {min(10, len(filtered))} Candidates (Min Score ≥ {min_score}):")
        for i, (name, score) in enumerate(filtered[:10], 1):
            with st.expander(f"{i}. {name} — 🔹 Score: {score:.2f}"):
                st.write(resume_texts.get(name, "Preview not available."))
