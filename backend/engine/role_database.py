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
    Return the required skills for a selected career role.
    """

    if role not in ROLE_DATABASE:
        raise ValueError(f"Unknown role: {role}")

    return ROLE_DATABASE[role]["required_skills"]