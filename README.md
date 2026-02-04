# SkillAlign – Resume & Job Description Matcher 🚀

🔗 **Live Demo:** https://skillalign.streamlit.app/

SkillAlign is an end-to-end NLP-powered web application that analyzes how well a resume aligns with a given job description and highlights **actionable skill gaps**.  
It is designed to help students and early professionals apply **strategically**, not blindly.

---

## ✨ Key Features

- 📄 Upload **Resume PDF**
- 🧾 Upload **Job Description PDF**
- 🧠 Automatic text extraction from PDFs
- 📊 Resume–JD **match score (0–100)**
- ✅ Clearly identified **matched skills**
- ❌ Clearly identified **missing skills**
- 🧩 Powered by a **670+ skill taxonomy**
- ⚡ Clean, fast, and interactive **Streamlit UI**

---

## 🧠 How It Works

1. **PDF Parsing**  
   Resume and JD PDFs are uploaded and converted into clean text.

2. **Text Preprocessing**  
   - Lowercasing  
   - Noise removal  
   - Stopword removal  
   - Lemmatization (NLTK)

3. **Skill Extraction**  
   - Skills are matched against a curated taxonomy of **670+ technical skills**
   - Skills are categorized and compared between resume and JD

4. **Semantic Similarity**  
   - TF-IDF + Cosine Similarity is used to measure contextual alignment

5. **Final Scoring Logic**
   ```
   Final Score =
   70% → Skill Match Coverage
   30% → Semantic Similarity
   ```

6. **Result Visualization**
   - Match score
   - Matched skills
   - Missing skills

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Frontend & Hosting
- **NLTK** – Text preprocessing
- **Scikit-learn** – TF-IDF & similarity
- **Pandas / NumPy** – Data handling
- **PDFMiner** – PDF text extraction

---

## 📂 Project Structure

```
SkillAlign/
│
├── app.py                 # Streamlit app entry point
├── requirements.txt       # Dependencies
│
├── data/
│   └── skills.csv         # 670+ skill taxonomy
│
├── src/
│   ├── preprocess.py      # Text cleaning & NLP
│   ├── skill_extractor.py # Skill matching logic
│   ├── similarity.py      # Semantic similarity
│   ├── matcher.py         # Scoring logic
│   └── pdf_reader.py      # PDF text extraction
│
└── README.md
```

---

## 🚀 Run Locally

```bash
git clone https://github.com/RichieRichard000/SkillAlign.git
cd SkillAlign

pip install -r requirements.txt
streamlit run app.py
```

---

## ⚠️ Limitations

- Scanned PDFs (images) are not supported (OCR not included)
- Skill matching is rule-based (can be extended with embeddings)
- Soft skills coverage is limited (future scope)

---

## 🔮 Future Improvements

- 🔍 OCR support for scanned resumes
- 🧠 Embedding-based skill matching
- 📈 Skill importance weighting
- 👥 Resume comparison across multiple roles
- 🏢 Company-specific JD optimization

---

## 🎯 Why This Project Matters

Students often receive rejections without feedback.  
SkillAlign converts vague job descriptions into **clear, data-backed insights**, enabling focused preparation and smarter applications.

---

## 👤 Author

**Devansh Baranwal**  
B.Tech Student | Aspiring Data & ML Engineer  

🌐 Live App: https://skillalign.streamlit.app/

---

⭐ If you found this project useful, consider starring the repository!
