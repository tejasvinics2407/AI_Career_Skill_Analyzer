from backend.nlp.resume_parser import extract_resume_text


resume_path = "uploads/sample_resume.pdf"

text = extract_resume_text(resume_path)

print("\n========== RESUME TEXT ==========\n")
print(text)
print("\n=================================\n")