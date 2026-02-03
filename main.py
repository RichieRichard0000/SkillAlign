from src.matcher import analyze_resume

resume_text = """
I have experience in Python, SQL, data analysis and Git.
"""

jd_text = """
Looking for skills in Python, SQL, Power BI, communication.
"""

result = analyze_resume(resume_text, jd_text)

print(result)
