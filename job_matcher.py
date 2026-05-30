import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

COMMON_SKILLS = [
    "python", "sql", "machine learning", "deep learning", "nlp",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "aws", "azure", "gcp", "docker", "fastapi", "streamlit",
    "mlflow", "git", "github", "data analysis", "statistics"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def calculate_match_score(resume_text, job_description):
    documents = [clean_text(resume_text), clean_text(job_description)]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)

def find_missing_skills(resume_text, job_description):
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(job_description)

    jd_skills = [skill for skill in COMMON_SKILLS if skill in jd_clean]
    missing = [skill for skill in jd_skills if skill not in resume_clean]
    present = [skill for skill in jd_skills if skill in resume_clean]

    return present, missing
