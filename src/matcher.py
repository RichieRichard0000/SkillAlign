from .preprocess import preprocess_text
from .skill_extractor import load_skills, extract_skills
from .similarity import calculate_similarity


def analyze_resume(resume_text: str, jd_text: str):
    skills_df = load_skills()

    resume_clean = preprocess_text(resume_text)
    jd_clean = preprocess_text(jd_text)

    resume_skills = extract_skills(resume_clean, skills_df)
    jd_skills = extract_skills(jd_clean, skills_df)

    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills - resume_skills

    if len(jd_skills) == 0:
        skill_score = 0
    else:
        skill_score = (len(matched_skills) / len(jd_skills)) * 70

    semantic_score = calculate_similarity(resume_clean, jd_clean) * 30

    final_score = float(round(skill_score + semantic_score, 2))


    return {
        "match_score": final_score,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }
