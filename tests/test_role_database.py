from backend.engine.role_database import get_role_requirements


role = "Machine Learning Engineer"

skills = get_role_requirements(role)

print("\n========== ROLE REQUIREMENTS ==========\n")

print("Career Role:", role)

print("\nRequired Skills:")

for skill in skills:
    print("✓", skill)

print("\n=======================================\n")