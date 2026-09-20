def analyze_skill_gap(student_skills, required_skills):
    """
    Compare the skills found in a resume
    with the skills required for a career role.
    """

    student_skills_lower = {
        skill.lower() for skill in student_skills
    }

    skills_you_have = []
    skills_missing = []

    for skill in required_skills:

        if skill.lower() in student_skills_lower:
            skills_you_have.append(skill)

        else:
            skills_missing.append(skill)

    return {
        "skills_you_have": skills_you_have,
        "skills_missing": skills_missing
    }