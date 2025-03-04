import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = spacy.load("en_core_web_sm")

def calculate_ats_score(resume_text, job_desc):
    documents = [resume_text, job_desc]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    similarity_score = (tfidf_matrix[0] @ tfidf_matrix[1].T).toarray()[0][0]
    ats_score = round(similarity_score * 100, 2)
    
    return ats_score
