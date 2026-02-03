import streamlit as st
from src.matcher import analyze_resume
from src.pdf_reader import extract_text_from_pdf

st.set_page_config(
    page_title="Resume–JD Skill Matcher",
    layout="centered"
)

st.title("📄 Resume–Job Description Matcher")
st.write(
    "Upload your resume and job description PDFs to analyze skill match "
    "and identify missing skills."
)

# --- File Upload Section ---
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

jd_file = st.file_uploader(
    "Upload Job Description (PDF)",
    type=["pdf"]
)

# --- Analyze Button ---
if st.button("🔍 Analyze Match"):
    if resume_file is None or jd_file is None:
        st.warning("Please upload both Resume and Job Description PDFs.")
    else:
        with st.spinner("Extracting text and analyzing..."):
            resume_text = extract_text_from_pdf(resume_file)
            jd_text = extract_text_from_pdf(jd_file)

            if not resume_text or not jd_text:
                st.error("Failed to extract text from one or both PDFs.")
            else:
                result = analyze_resume(resume_text, jd_text)

                st.subheader("📊 Match Results")

                st.metric(
                    label="Match Score",
                    value=f"{result['match_score']} / 100"
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.success("✅ Matched Skills")
                    if result["matched_skills"]:
                        for skill in result["matched_skills"]:
                            st.write(f"- {skill}")
                    else:
                        st.write("No matched skills found.")

                with col2:
                    st.error("❌ Missing Skills")
                    if result["missing_skills"]:
                        for skill in result["missing_skills"]:
                            st.write(f"- {skill}")
                    else:
                        st.write("No missing skills 🎉")

                st.caption(
                    "Score is calculated using skill overlap (70%) and "
                    "semantic similarity (30%)."
                )
