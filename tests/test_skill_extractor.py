from backend.nlp.resume_parser import extract_resume_text
from backend.nlp.skill_extractor import extract_skills


resume_path = "uploads/sample_resume.pdf"

# Step 1: Extract text from resume
resume_text = extract_resume_text(resume_path)

# Step 2: Extract skills from resume text
skills = extract_skills(resume_text)

print("\n========== EXTRACTED SKILLS ==========\n")

for skill in skills:
    print("✓", skill)

print("\n=======================================\n")