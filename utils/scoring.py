REQUIRED_SKILLS = [
    "python", "django", "machine learning",
    "sql", "react", "java", "c++"
]

def calculate_ats_score(found_skills):
    matched = len(found_skills)
    total = len(REQUIRED_SKILLS)

    score = (matched / total) * 100

    missing_skills = [
        skill for skill in REQUIRED_SKILLS if skill not in found_skills
    ]

    return round(score, 2), missing_skills