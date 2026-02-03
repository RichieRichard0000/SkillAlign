import pandas as pd

def load_skills(path="data/skills.csv"):
    return pd.read_csv(path)

def extract_skills(text: str, skills_df):
    found_skills = set()

    for _, row in skills_df.iterrows():
        skill = row["skill"].lower()
        if skill in text:
            found_skills.add(skill)

    return found_skills
