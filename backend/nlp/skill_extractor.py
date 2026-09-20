import re


SKILL_DATABASE = {
    "Python": ["python"],
    "C": ["c programming", "c language", " c "],
    "C++": ["c++"],
    "Java": ["java"],
    "JavaScript": ["javascript", "js"],
    "SQL": ["sql", "mysql"],
    "NumPy": ["numpy"],
    "Pandas": ["pandas"],
    "Machine Learning": ["machine learning", "ml"],
    "Artificial Intelligence": ["artificial intelligence", "ai"],
    "Natural Language Processing": ["natural language processing", "nlp"],
    "Git": ["git"],
    "GitHub": ["github"],
    "VS Code": ["vs code", "visual studio code"],
    "HTML": ["html"],
    "CSS": ["css"],
    "React": ["react"],
    "FastAPI": ["fastapi"],
    "Flask": ["flask"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "ROS": ["ros", "robot operating system"],
    "SLAM": ["slam","simultaneous localization and mapping"],
    "LiDAR": ["lidar","light detection and ranging"],
    "Motion Planning": ["motion planning"],
    "Path Planning": ["path planning"],
    "Computer Vision": ["computer vision"],
    "Robotic Autonomy": ["robotic autonomy","autonomous robot","autonomous robotics"],
    "Control Systems": ["control systems","control system","controllers"],
    "Mechatronics": ["mechatronics"],
    "Perception": ["perception"]
}

def extract_skills(text):
    """
    Extract known technical skills from resume text.
    """

    text_lower = text.lower()

    found_skills = []

    for skill, keywords in SKILL_DATABASE.items():

        for keyword in keywords:

            if keyword == "c++":
                if "c++" in text_lower:
                    found_skills.append(skill)
                    break

            elif keyword == "c programming" or keyword == "c language":
                pattern = r"\b" + re.escape(keyword) + r"\b"

                if re.search(pattern, text_lower):
                    found_skills.append(skill)
                    break

            else:
                pattern = r"\b" + re.escape(keyword) + r"\b"

                if re.search(pattern, text_lower):
                    found_skills.append(skill)
                    break

    return sorted(found_skills)