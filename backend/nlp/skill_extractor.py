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
    "Perception": ["perception"],"Mechatronics": ["mechatronics"],
"Perception": ["perception"],

# Finance & Business
"Excel": ["excel", "microsoft excel"],
"Financial Modeling": ["financial modeling", "financial modelling"],
"Accounting": ["accounting"],
"Financial Analysis": ["financial analysis"],
"Power BI": ["power bi"],
"Data Visualization": ["data visualization", "data visualisation"],
"Data Analysis": ["data analysis"],
"Business Analysis": ["business analysis"],
"Requirements Analysis": ["requirements analysis"],

# Mechanical & Manufacturing
"CAD": ["cad", "computer aided design"],
"SolidWorks": ["solidworks", "solid works"],
"Mechanical Design": ["mechanical design"],
"Thermodynamics": ["thermodynamics"],
"Materials Science": ["materials science"],
"Manufacturing": ["manufacturing"],
"Engineering Drawing": ["engineering drawing"],
"CNC": ["cnc", "computer numerical control"],
"Production Planning": ["production planning"],
"Quality Control": ["quality control"],
"Lean Manufacturing": ["lean manufacturing"],

# Civil & Infrastructure
"AutoCAD": ["autocad", "auto cad"],
"Structural Analysis": ["structural analysis"],
"Construction": ["construction"],
"Surveying": ["surveying"],
"Concrete Technology": ["concrete technology"],
"Geotechnical Engineering": ["geotechnical engineering"],
"STAAD.Pro": ["staad.pro", "staad pro"],
"Revit": ["revit"],
"Structural Design": ["structural design"],

# Marketing & UX
"SEO": ["seo", "search engine optimization"],
"Content Marketing": ["content marketing"],
"Social Media Marketing": ["social media marketing"],
"Google Analytics": ["google analytics"],
"Digital Advertising": ["digital advertising"],
"Email Marketing": ["email marketing"],
"Marketing Analytics": ["marketing analytics"],
"Figma": ["figma"],
"UI Design": ["ui design", "user interface design"],
"UX Design": ["ux design", "user experience design"],
"User Research": ["user research"],
"Wireframing": ["wireframing", "wireframes"],
"Prototyping": ["prototyping", "prototype"],
"Usability Testing": ["usability testing"]

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