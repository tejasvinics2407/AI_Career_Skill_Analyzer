from backend.engine.skill_dependency_graph import (
    get_prerequisites
)


def calculate_minimum_skill_path(
    current_skills,
    required_skills
):
    """
    Calculate a dependency-aware learning path.

    Only skills required by the target role are considered.
    A prerequisite is included only when that prerequisite
    is also part of the target role's required skills.

    This prevents skills from unrelated domains from being
    added to the learning path.
    """

    # -----------------------------------------------------
    # NORMALIZE CURRENT SKILLS
    # -----------------------------------------------------

    current = {
        skill.lower()
        for skill in current_skills
    }


    # -----------------------------------------------------
    # ROLE-RELEVANT SKILL SET
    # -----------------------------------------------------

    required_lookup = {
        skill.lower(): skill
        for skill in required_skills
    }


    # -----------------------------------------------------
    # BUILD ALLOWED SKILL SET
    # -----------------------------------------------------

    allowed_skills = set()


    def collect_dependencies(skill):

        skill_lower = skill.lower()

        if skill_lower in allowed_skills:
            return

        allowed_skills.add(skill_lower)

        prerequisites = get_prerequisites(
            skill
        )

        for prerequisite in prerequisites:

            # Only include prerequisites that
            # belong to this target role.
            if prerequisite.lower() in required_lookup:

                collect_dependencies(
                    prerequisite
                )


    # Collect required skills and only
    # role-relevant dependencies.

    for skill in required_skills:

        collect_dependencies(
            skill
        )


    # -----------------------------------------------------
    # CREATE LEARNING PATH
    # -----------------------------------------------------

    learning_path = []

    added_skills = set()


    def add_skill(skill):

        skill_lower = skill.lower()


        # Already known
        if skill_lower in current:

            return


        # Already added
        if skill_lower in added_skills:

            return


        # Add role-relevant prerequisites first
        prerequisites = get_prerequisites(
            skill
        )

        for prerequisite in prerequisites:

            if (
                prerequisite.lower()
                in allowed_skills
            ):

                add_skill(
                    prerequisite
                )


        # Add actual skill
        if skill_lower not in current:

            learning_path.append(
                skill
            )

            added_skills.add(
                skill_lower
            )


    # -----------------------------------------------------
    # PROCESS REQUIRED SKILLS
    # -----------------------------------------------------

    for skill in required_skills:

        add_skill(
            skill
        )


    return learning_path