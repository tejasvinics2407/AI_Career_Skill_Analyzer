import re


def find_skill_evidence(text, skill):
    """
    Find sentences or lines in a resume that contain a skill.
    """

    evidence = []

    lines = text.splitlines()

    skill_lower = skill.lower()

    for line in lines:

        line_clean = line.strip()

        if not line_clean:
            continue

        if skill_lower in line_clean.lower():

            evidence.append(line_clean)

    return evidence


def analyze_skill_evidence(text, skills):
    """
    Determine whether each detected skill has
    supporting evidence in the resume.
    """

    results = {}

    for skill in skills:

        evidence = find_skill_evidence(
            text,
            skill
        )

        if evidence:

            results[skill] = {
                "claimed": True,
                "demonstrated": True,
                "evidence": evidence
            }

        else:

            results[skill] = {
                "claimed": True,
                "demonstrated": False,
                "evidence": []
            }

    return results