from backend.engine.skill_dependency_graph import (
    get_prerequisites
)


def calculate_minimum_skill_path(
    current_skills,
    required_skills
):
    """
    Calculate a dependency-aware learning path.

    Only skills that are required by the target role
    or are prerequisites of those required skills
    are considered.
    """

    # -----------------------------------------------------
    # NORMALIZE CURRENT SKILLS
    # -----------------------------------------------------

    current = {
        skill.lower()
        for skill in current_skills
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

            collect_dependencies(
                prerequisite
            )


    # Collect required skills and
    # everything they depend on.

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


        # Add prerequisites first
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


        # Add the actual skill
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