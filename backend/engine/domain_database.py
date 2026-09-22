# =========================================================
# MULTI-DOMAIN CAREER DATABASE
# =========================================================

DOMAIN_DATABASE = {

    "Computer Science & AI": {

        "Machine Learning Engineer": [
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
        ],

        "AI Engineer": [
            "Python",
            "Machine Learning",
            "Artificial Intelligence",
            "Natural Language Processing",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "SQL",
            "Git"
        ],

        "Software Developer": [
            "Python",
            "Java",
            "C++",
            "SQL",
            "Git",
            "GitHub",
            "HTML",
            "CSS",
            "JavaScript"
        ],

        "Data Scientist": [
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


    "Finance & Business": {

        "Financial Analyst": [
            "Excel",
            "Financial Modeling",
            "Accounting",
            "Financial Analysis",
            "Statistics",
            "SQL",
            "Power BI",
            "Data Visualization"
        ],

        "Business Analyst": [
            "Excel",
            "SQL",
            "Power BI",
            "Data Analysis",
            "Statistics",
            "Business Analysis",
            "Requirements Analysis",
            "Data Visualization"
        ]
    },


    "Mechanical & Manufacturing": {

        "Mechanical Engineer": [
            "CAD",
            "SolidWorks",
            "Mechanical Design",
            "Thermodynamics",
            "Materials Science",
            "Manufacturing",
            "Engineering Drawing"
        ],

        "Manufacturing Engineer": [
            "CAD",
            "SolidWorks",
            "Manufacturing",
            "CNC",
            "Production Planning",
            "Quality Control",
            "Materials Science",
            "Lean Manufacturing"
        ]
    },


    "Civil & Infrastructure": {

        "Civil Engineer": [
            "AutoCAD",
            "Structural Analysis",
            "Construction",
            "Surveying",
            "Concrete Technology",
            "Geotechnical Engineering",
            "Engineering Drawing"
        ],

        "Structural Engineer": [
            "AutoCAD",
            "Structural Analysis",
            "STAAD.Pro",
            "Revit",
            "Concrete Technology",
            "Structural Design",
            "Engineering Drawing"
        ]
    },


    "Marketing & UX": {

        "Digital Marketing Specialist": [
            "SEO",
            "Content Marketing",
            "Social Media Marketing",
            "Google Analytics",
            "Digital Advertising",
            "Email Marketing",
            "Marketing Analytics"
        ],

        "UX Designer": [
            "Figma",
            "UI Design",
            "UX Design",
            "User Research",
            "Wireframing",
            "Prototyping",
            "Usability Testing"
        ]
    }
}


def get_domains():
    return list(DOMAIN_DATABASE.keys())


def get_roles(domain):
    if domain not in DOMAIN_DATABASE:
        raise ValueError(f"Unknown domain: {domain}")

    return list(DOMAIN_DATABASE[domain].keys())


def get_domain_role_requirements(domain, role):
    if domain not in DOMAIN_DATABASE:
        raise ValueError(f"Unknown domain: {domain}")

    if role not in DOMAIN_DATABASE[domain]:
        raise ValueError(
            f"Unknown role '{role}' in domain '{domain}'"
        )

    return DOMAIN_DATABASE[domain][role]