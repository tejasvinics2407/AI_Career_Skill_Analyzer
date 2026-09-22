from backend.engine.domain_database import DOMAIN_DATABASE
ROLE_DATABASE = {

    "Machine Learning Engineer": {
        "required_skills": [
            "Python",
            "SQL",
            "NumPy",
            "Pandas",
            "Machine Learning",
            "Statistics",
            "Scikit-learn",
            "TensorFlow",
            "PyTorch",
            "Deep Learning"
        ]
    },

    "AI Engineer": {
        "required_skills": [
            "Python",
            "Machine Learning",
            "Artificial Intelligence",
            "Natural Language Processing",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "SQL",
            "Git"
        ]
    },

    "Data Scientist": {
        "required_skills": [
            "Python",
            "SQL",
            "NumPy",
            "Pandas",
            "Statistics",
            "Machine Learning",
            "Data Visualization",
            "Scikit-learn"
        ]
    },

    "Software Developer": {
        "required_skills": [
            "Python",
            "Java",
            "C++",
            "SQL",
            "Git",
            "GitHub",
            "HTML",
            "CSS",
            "JavaScript"
        ]
    },

    "Data Analyst": {
        "required_skills": [
            "Python",
            "SQL",
            "Pandas",
            "NumPy",
            "Statistics",
            "Data Visualization",
            "Excel"
        ]
    },

    "Robotics Engineer": {
        "required_skills": [
            "Python",
            "C++",
            "C",
            "ROS",
            "SLAM",
            "LiDAR",
            "Motion Planning",
            "Computer Vision",
            "Robotic Autonomy",
            "Control Systems",
            "Mechatronics",
            "Path Planning"
        ]
    }

}


def get_role_requirements(role):
    """
    Return required skills for any role across all domains.
    Falls back to the original role database.
    """

    # Check the new multi-domain database first
    for domain in DOMAIN_DATABASE.values():
        if role in domain:
            return domain[role]

    # Fall back to the original database
    if role in ROLE_DATABASE:
        return ROLE_DATABASE[role]["required_skills"]

    raise ValueError(f"Unknown role: {role}")