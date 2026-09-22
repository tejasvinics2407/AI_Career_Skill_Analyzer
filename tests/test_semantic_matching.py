from backend.nlp.resume_parser import extract_resume_text
from backend.nlp.skill_extractor import extract_skills
from backend.nlp.semantic_matcher import SemanticSkillMatcher
from backend.engine.role_database import get_role_requirements


# --------------------------------------------------
# TEST RESUME TEXT
# --------------------------------------------------

resume_text = """
I am a Python developer with experience in PyTorch,
SQL and machine learning. I have worked on deep
learning projects and artificial intelligence applications.
"""


# --------------------------------------------------
# EXISTING SKILL EXTRACTION
# --------------------------------------------------

student_skills = extract_skills(resume_text)

print("\nSkills extracted by existing system:")
print(student_skills)


# --------------------------------------------------
# EXISTING ROLE DATABASE
# --------------------------------------------------

role = "Machine Learning Engineer"

required_skills = get_role_requirements(role)

print("\nRequired skills:")
print(required_skills)


# --------------------------------------------------
# NEW SEMANTIC NLP LAYER
# --------------------------------------------------

matcher = SemanticSkillMatcher()

results = matcher.match_skills(
    student_skills,
    required_skills
)


# --------------------------------------------------
# DISPLAY SEMANTIC RESULTS
# --------------------------------------------------

print("\n==============================")
print("     SEMANTIC MATCHING")
print("==============================\n")

for result in results:
    print(
        f"{result['candidate_skill']:<15}"
        f" → {result['required_skill']:<25}"
        f" Similarity: {result['similarity']}"
    )