# AI Resume Analyzer + Job Matcher

## Overview

This project analyzes a resume PDF and compares it with a job description. It gives a match score, extracts keywords, identifies missing skills, and provides improvement suggestions.

## Features

- Upload resume PDF
- Paste job description
- Extract resume text
- Compare resume with job description
- Show match percentage
- Show missing keywords
- Give resume improvement suggestions

## Tech Stack

- Python
- Streamlit
- PyPDF2
- Scikit-learn
- Pandas

## Resources

- Streamlit: https://streamlit.io/
- PyPDF2: https://pypi.org/project/PyPDF2/
- Scikit-learn: https://scikit-learn.org/
- Sample resumes: https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset
- Job descriptions: collect from LinkedIn, Indeed, Dice, or company career pages

## Folder Structure

```bash
ai-resume-analyzer/
├── app.py
├── resume_parser.py
├── job_matcher.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
└── screenshots/
```

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Future Improvements

- Add OpenAI/Gemini suggestions
- Add ATS keyword analysis
- Add downloadable PDF report
- Deploy on Streamlit Cloud

## Author

Govardhan Chowdary
