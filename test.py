import pdfplumber

with pdfplumber.open("resumes/CVs1/C1061.pdf") as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
print(text[:500])
