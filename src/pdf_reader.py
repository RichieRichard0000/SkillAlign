from pdfminer.high_level import extract_text
import tempfile
import os

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from a Streamlit uploaded PDF file.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    text = extract_text(tmp_path)
    os.remove(tmp_path)

    return text.strip()
