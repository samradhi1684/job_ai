# 🧠 AI Job Screening System

An AI-powered web application that automates the candidate screening process by analyzing resumes and matching them with job descriptions using intelligent embedding-based comparison. Built using **Streamlit**, this tool streamlines recruitment by shortlisting candidates based on skill relevance and match score.

---

## 🚀 Features

- **Job Description Summarizer**  
  Extracts required skills, qualifications, and responsibilities from uploaded job descriptions.

- **Resume Parser**  
  Automatically parses candidate resumes in PDF format and extracts key details like education, work experience, and skills.

- **Skill Matcher**  
  Compares extracted resume data with the job description using vector embeddings to compute a similarity score.

- **Candidate Shortlisting**  
  Ranks and displays top candidates based on a customizable threshold score.

- **Interview Scheduler** *(Coming Soon)*  
  Sends personalized interview invitation emails to shortlisted candidates with options for time, date, and format.

## Folder Structure

 resumes/ ├── job_description.csv # Job titles and corresponding JDs └── CVs1/ # PDF resumes to be screened  agents/ ├── jd_parser.py # JD skill extraction + embedding ├── resume_parser.py # Resume parsing logic └── skill_matcher.py # Candidate ranking logic app.py # Main Streamlit frontend requirements.txt # Python dependencies README.md # Project documentation

##  How to run

1. **Clone the repository** : 
   git clone https://github.com/yourusername/job_ai.git, 
   cd job_ai
2. **Create and activate a virtual environment** : 
   python -m venv venv, 
   venv\Scripts\activate  # For Windows, 
   source venv/bin/activate  # For macOS/Linux
3. **Install dependencies** : 
   pip install -r requirements.txt
4. **Run the app** :
   streamlit run app.py

## Dependencies
streamlit,
pandas,
pdfplumber,
openai (or your embedding generator),
scikit-learn,
langchain (for upcoming multi-agent support)

## Upcoming features

>Email-based Interview Scheduling,
>SQLite integration for persistent storage,
>Advanced candidate analytics dashboard,
>Role-based authentication for recruiters

## Author
samradhi.s4@gmail.com


