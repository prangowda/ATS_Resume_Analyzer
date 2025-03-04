from flask import Flask, render_template, request
from resume_parser import extract_resume_text
from ats_scoring import calculate_ats_score
from improvements import suggest_improvements

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume = request.files["resume"]
        job_desc = request.form["job_desc"]
        
        resume_text = extract_resume_text(resume.filename)
        ats_score = calculate_ats_score(resume_text, job_desc)
        suggestions = suggest_improvements(ats_score)
        
        return render_template("index.html", ats_score=ats_score, suggestions=suggestions)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
