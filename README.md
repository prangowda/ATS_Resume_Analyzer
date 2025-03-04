# **ATS Resume Analyzer**  
An AI-powered tool that evaluates resumes against job descriptions using **Natural Language Processing (NLP)** and provides an **ATS (Applicant Tracking System) score** along with **improvement suggestions**.

---

## **🌟 Features**  
✅ **Resume Parsing** – Extracts text from **PDF** and **DOCX** resumes.  
✅ **ATS Score Calculation** – Measures resume-job description relevance using **TF-IDF matching**.  
✅ **Improvement Suggestions** – AI-generated tips for **resume optimization**.  
✅ **Web UI (Flask)** – Upload resumes and get real-time feedback.  

---

## **🚀 Technologies Used**  
🔹 **Backend:** Python (Flask)  
🔹 **Natural Language Processing (NLP):** SpaCy, Scikit-learn, NLTK  
🔹 **File Handling:** PyPDF2, docx2txt  
🔹 **Web Framework:** Flask (for UI)  
🔹 **Machine Learning:** TF-IDF for text similarity  

---

## **📂 Project Structure**
```
📦 ATS_Resume_Analyzer
 ┣ 📜 app.py                   # Flask Web Application
 ┣ 📜 resume_parser.py          # Resume text extraction
 ┣ 📜 ats_scoring.py            # ATS scoring model
 ┣ 📜 improvements.py           # Resume optimization suggestions
 ┣ 📜 templates/                # HTML files for UI
 ┃ ┣ 📜 index.html              # Main web page
 ┣ 📜 static/                   # CSS, JavaScript (Optional)
 ┣ 📜 sample_resumes/           # Example resumes
 ┣ 📜 requirements.txt          # Required Python dependencies
 ┣ 📜 README.md                 # Documentation
 ┗ 📜 model/                    # NLP models (if used)
```

---

## **🔧 Installation & Setup**
### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/prangowda/ATS-Resume-Analyzer.git
cd ATS-Resume-Analyzer
```

### **Step 2: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **Step 3: Run the Flask App**  
```bash
python app.py
```

### **Step 4: Open the Web App**  
Go to **http://127.0.0.1:5000/** in your browser.

---

## **📝 Usage**
1️⃣ **Upload a Resume** (PDF or DOCX)  
2️⃣ **Paste the Job Description**  
3️⃣ **Click "Analyze Resume"**  
4️⃣ **View ATS Score & Suggested Improvements**  

---

## **🔍 Example Output**
### **ATS Score:** `75%`  
### **Suggestions:**  
✔️ **Use more job-relevant keywords.**  
✔️ **Format resume for ATS readability (avoid tables, images).**  
✔️ **Use proper headings (e.g., ‘Experience’, ‘Education’).**  

---

## **🛠️ Future Enhancements**  
✅ **Job Matching AI** – Suggests jobs based on resume analysis.  
✅ **Resume Formatting Checker** – Ensures **ATS-friendly formatting**.  
✅ **Real-Time Resume Builder** – Generates resume templates dynamically.  

---

## **🖥️ Technologies Used**
- **Python**
- **Flask**
- **scikit-learn**
- **spaCy**
- **PyPDF2**
- **docx2txt**
- **NLTK**
- **TF-IDF Vectorization**

