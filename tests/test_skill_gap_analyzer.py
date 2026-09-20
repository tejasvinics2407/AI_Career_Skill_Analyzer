from backend.engine.role_database import get_role_requirements
from backend.engine.skill_gap_analyzer import analyze_skill_gap


# Skills extracted from our sample resume
student_skills = [
    "Artificial Intelligence",
    "C++",
    "Git",
    "GitHub",
    "Machine Learning",
    "Natural Language Processing",
    "NumPy",
    "Pandas",
    "Python",
    "SQL",
    "VS Code"
]


# Target career
role = "Machine Learning Engineer"

# Get skills required for the role
required_skills = get_role_requirements(role)

# Analyze the skill gap
result = analyze_skill_gap(
    student_skills,
    required_skills
)


print("\n========== SKILL GAP ANALYSIS ==========\n")

print("Career Role:", role)

print("\nSKILLS YOU HAVE:")

for skill in result["skills_you_have"]:
    print("✓", skill)


print("\nSKILLS YOU ARE MISSING:")

for skill in result["skills_missing"]:
    print("✗", skill)


print("\n========================================\n")