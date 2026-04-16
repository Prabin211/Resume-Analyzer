# AI Resume Analyzer

A full-stack AI-powered web application that analyzes resumes, extracts skills, calculates ATS scores, and matches resumes with job descriptions.

🔗 **Live Demo**: https://resume-analyzer-8kw6.onrender.com  
💻 **GitHub Repo**: https://github.com/Prabin211/Resume-Analyzer  

---

## ✨ Features

- 📄 Upload Resume (PDF)
- 🧠 Extract Skills using NLP
- 📊 Calculate ATS Score
- 🎯 Match Resume with Job Description
- ❌ Identify Missing Skills
- 📈 Visualize Results using Charts
- 🌐 Live Deployed Application

---

## 🛠 Tech Stack

- **Backend**: Django, Django REST Framework  
- **Frontend**: HTML, CSS  
- **Machine Learning**: Scikit-learn, NLP  
- **Libraries**: PyMuPDF, NumPy  
- **Deployment**: Render  

---

## 🖥️ How It Works

1. Upload your resume (PDF)
2. Enter a job description
3. System extracts text & skills
4. Calculates ATS score
5. Matches resume with job description
6. Displays results visually

---
## 📌 Future Improvements

- 🔐 User authentication
- 📊 Dashboard for resume history
- 📄 Resume preview
- ⚡ Faster ML models
- 🎨 Advanced UI

## 📸 Screenshots

### 🏠 Home Page
![Home](https://github.com/Prabin211/Resume-Analyzer/blob/main/screenshot.png?raw=true)

---

## 🚀 Installation (Local Setup)

```bash
git clone https://github.com/Prabin211/Resume-Analyzer.git
cd Resume-Analyzer

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver