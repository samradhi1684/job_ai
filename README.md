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

📁 agents/                            # Python modules for parsing and matching logic
│   ├── jd_parser.py                 # Extracts and embeds job description skills
│   ├── resume_parser.py            # Extracts and embeds skills from resumes
│   └── skill_matcher.py            # Ranks candidates based on skill similarity

📁 resumes/                           # Data folder for JD and resumes
│   ├── job_description.csv         # Contains job roles and their descriptions
│   └── CVs1/                       # Folder with uploaded candidate resumes (PDFs)

📁 venv/                              # Virtual environment (excluded from Git)
│   └── ...                         # All venv-related files (in .gitignore)

📄 app.py                            # Main Streamlit app — UI + logic
📄 requirements.txt                 # List of all project dependencies
📄 test.py                          # Script to test individual modules or functions

##  How to run

1. **Clone the repository**
   git clone https://github.com/yourusername/job_ai.git
   cd job_ai
2. **Create and activate a virtual environment**
   python -m venv venv
   venv\Scripts\activate  # For Windows
   source venv/bin/activate  # For macOS/Linux
3. **Install dependencies**
   pip install -r requirements.txt
4. **Run the app**
   streamlit run app.py

## Dependencies
streamlit
pandas
pdfplumber
openai (or your embedding generator)
scikit-learn
langchain (for upcoming multi-agent support)

## Upcoming features

>Email-based Interview Scheduling
>SQLite integration for persistent storage
>Advanced candidate analytics dashboard
>Role-based authentication for recruiters

## Author
samradhi.s4@gmail.com


