# =========================================================
# SKILL DEPENDENCY GRAPH
# =========================================================

import networkx as nx


# =========================================================
# SKILL DEPENDENCIES
# =========================================================

SKILL_DEPENDENCIES = {

    # -----------------------------------------------------
    # AI / MACHINE LEARNING
    # -----------------------------------------------------

    "Machine Learning": [
        "Python",
        "Statistics"
    ],

    "Scikit-learn": [
        "Python",
        "Machine Learning"
    ],

    "Deep Learning": [
        "Python",
        "Machine Learning",
        "Statistics"
    ],

    "TensorFlow": [
        "Python",
        "Deep Learning"
    ],

    "PyTorch": [
        "Python",
        "Deep Learning"
    ],

    "Artificial Intelligence": [
        "Python"
    ],

    "Natural Language Processing": [
        "Python",
        "Machine Learning"
    ],


    # -----------------------------------------------------
    # DATA SCIENCE
    # -----------------------------------------------------

    "NumPy": [
        "Python"
    ],

    "Pandas": [
        "Python",
        "NumPy"
    ],

    "Data Visualization": [
        "Python",
        "Pandas"
    ],


    # -----------------------------------------------------
    # ROBOTICS
    # -----------------------------------------------------

    "ROS": [
        "Python",
        "C++"
    ],

    "SLAM": [
        "ROS",
        "LiDAR"
    ],

    "Motion Planning": [
        "Python",
        "C++",
        "ROS"
    ],

    "Path Planning": [
        "Motion Planning"
    ],

    "Computer Vision": [
        "Python"
    ],

    "Perception": [
        "Computer Vision",
        "Python"
    ],

    "Control Systems": [
        "C++",
        "Mathematics"
    ],

    "Robotic Autonomy": [
        "ROS",
        "SLAM",
        "Motion Planning",
        "Perception",
        "Control Systems"
    ],

    "Mechatronics": [
        "C",
        "Control Systems"
    ],

    "LiDAR": [
        "Robotics"
    ]
}


# =========================================================
# GET DIRECT PREREQUISITES
# =========================================================

def get_prerequisites(skill):
    """
    Return the direct prerequisites of a skill.
    """

    return SKILL_DEPENDENCIES.get(
        skill,
        []
    )


# =========================================================
# GET ALL RECURSIVE DEPENDENCIES
# =========================================================

def get_all_dependencies(
    skill,
    visited=None
):
    """
    Return all prerequisite skills required
    to learn a particular skill.
    """

    if visited is None:
        visited = set()

    if skill in visited:
        return []

    visited.add(skill)

    dependencies = []

    for prerequisite in get_prerequisites(skill):

        dependencies.append(
            prerequisite
        )

        dependencies.extend(
            get_all_dependencies(
                prerequisite,
                visited
            )
        )

    return dependencies


# =========================================================
# BUILD NETWORKX GRAPH
# =========================================================

def build_skill_graph(required_skills):
    """
    Build a directed NetworkX graph containing
    the required skills and only role-relevant
    prerequisites.

    Edge direction:

        prerequisite → skill

    Example:

        Python → Machine Learning
    """

    graph = nx.DiGraph()


    # -----------------------------------------------------
    # CREATE ROLE SKILL LOOKUP
    # -----------------------------------------------------

    required_lookup = {
        skill.lower(): skill
        for skill in required_skills
    }


    # -----------------------------------------------------
    # ADD ROLE-RELEVANT SKILLS AND DEPENDENCIES
    # -----------------------------------------------------

    def add_skill_with_dependencies(skill):

        # Add the required skill itself
        graph.add_node(
            skill
        )

        prerequisites = get_prerequisites(
            skill
        )

        for prerequisite in prerequisites:

            # -------------------------------------------------
            # IMPORTANT:
            # Only include a prerequisite if it is also
            # required by the selected career role.
            # -------------------------------------------------

            if (
                prerequisite.lower()
                not in required_lookup
            ):

                continue


            # Add prerequisite node
            graph.add_node(
                prerequisite
            )


            # prerequisite → skill
            graph.add_edge(
                prerequisite,
                skill
            )


            # Recursively add only role-relevant
            # prerequisites.
            add_skill_with_dependencies(
                prerequisite
            )


    # -----------------------------------------------------
    # BUILD GRAPH FROM ROLE REQUIREMENTS
    # -----------------------------------------------------

    for skill in required_skills:

        add_skill_with_dependencies(
            skill
        )


    return graph


# =========================================================
# GET GRAPH DATA
# =========================================================

def get_graph_data(required_skills):
    """
    Convert the NetworkX graph into simple
    node and edge lists that can be used
    by the frontend.
    """

    graph = build_skill_graph(
        required_skills
    )


    nodes = []

    for node in graph.nodes:

        nodes.append(
            node
        )


    edges = []

    for source, target in graph.edges:

        edges.append(
            {
                "source": source,
                "target": target
            }
        )


    return {
        "nodes": nodes,
        "edges": edges
    }