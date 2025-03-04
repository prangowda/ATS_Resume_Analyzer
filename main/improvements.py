def suggest_improvements(ats_score):
    suggestions = []
    
    if ats_score < 50:
        suggestions.append("🔴 Add more job-relevant keywords from the job description.")
        suggestions.append("🔴 Ensure the resume format is ATS-friendly (No images, tables, or columns).")
    
    if ats_score < 70:
        suggestions.append("🟠 Use clear section headers (e.g., 'Experience', 'Education').")
        suggestions.append("🟠 Quantify achievements (e.g., 'Increased sales by 30%').")
    
    if ats_score >= 70:
        suggestions.append("✅ Your resume is well-optimized! Consider minor refinements for clarity.")
    
    return suggestions
