import streamlit as st
from resume_parser import extract_text_from_pdf
from job_matcher import calculate_match_score, find_missing_skills

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("AI Resume Analyzer + Job Matcher")
st.write("Upload your resume and paste a job description to check your match score.")

resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=250)

if st.button("Analyze Resume"):
    if resume_file is None or not job_description.strip():
        st.error("Please upload a resume and paste a job description.")
    else:
        resume_text = extract_text_from_pdf(resume_file)
        score = calculate_match_score(resume_text, job_description)
        present, missing = find_missing_skills(resume_text, job_description)

        st.subheader("Results")
        st.metric("Resume Match Score", f"{score}%")

        st.subheader("Matched Skills")
        st.write(", ".join(present) if present else "No common skills found.")

        st.subheader("Missing Skills")
        st.write(", ".join(missing) if missing else "No major missing skills found.")

        st.subheader("Suggestions")
        if missing:
            st.write("Add these skills naturally into your resume if you have experience with them:")
            for skill in missing:
                st.write(f"- {skill}")
        else:
            st.success("Your resume matches the job description well.")
