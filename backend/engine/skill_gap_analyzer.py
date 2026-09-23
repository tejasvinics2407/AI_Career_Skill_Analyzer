from backend.nlp.semantic_matcher import SemanticSkillMatcher


semantic_matcher = SemanticSkillMatcher()


def analyze_skill_gap(
    student_skills,
    required_skills,
    semantic_threshold=0.65
):
    """
    Compare the skills found in a resume
    with the skills required for a career role.

    Uses:
    1. Exact skill matching
    2. Semantic similarity matching
    3. True skill-gap detection
    """

    student_skills_lower = {
        skill.lower() for skill in student_skills
    }

    skills_you_have = []
    skills_semantically_related = []
    skills_missing = []

    for skill in required_skills:

        # -------------------------------------------------
        # 1. EXACT MATCH
        # -------------------------------------------------

        if skill.lower() in student_skills_lower:

            skills_you_have.append(skill)

            continue

        # -------------------------------------------------
        # 2. SEMANTIC MATCH
        # -------------------------------------------------

        best_candidate = None
        best_score = 0.0

        for candidate in student_skills:

            score = semantic_matcher.similarity(
                candidate,
                skill
            )

            if score > best_score:
                best_score = score
                best_candidate = candidate

        if best_score >= semantic_threshold:

            skills_semantically_related.append({
                "required_skill": skill,
                "related_skill": best_candidate,
                "similarity": round(best_score, 3)
            })

        # -------------------------------------------------
        # 3. TRUE SKILL GAP
        # -------------------------------------------------

        else:

            skills_missing.append(skill)

    return {
        "skills_you_have": skills_you_have,
        "skills_semantically_related": skills_semantically_related,
        "skills_missing": skills_missing
    }