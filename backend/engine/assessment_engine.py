# ---------------------------------------------------------
# ADAPTIVE SKILL ASSESSMENT ENGINE
# ---------------------------------------------------------

QUESTION_BANK = {

    "Python": [
        {
            "question": "Which data type is used to store a sequence of values in Python?",
            "options": [
                "List",
                "Integer",
                "Boolean",
                "Float"
            ],
            "answer": "List"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": [
                "function",
                "def",
                "fun",
                "define"
            ],
            "answer": "def"
        },
        {
            "question": "Which library is commonly used for numerical array operations in Python?",
            "options": [
                "NumPy",
                "Flask",
                "FastAPI",
                "Git"
            ],
            "answer": "NumPy"
        },
        {
            "question": "What does len() return when used on a list?",
            "options": [
                "The last element",
                "The number of elements",
                "The data type",
                "The memory address"
            ],
            "answer": "The number of elements"
        },
        {
            "question": "Which symbol is used to start a comment in Python?",
            "options": [
                "//",
                "#",
                "/*",
                "--"
            ],
            "answer": "#"
        }
    ],


    "Machine Learning": [
        {
            "question": "What is the main purpose of a machine learning model?",
            "options": [
                "To learn patterns from data",
                "To replace the operating system",
                "To create hardware",
                "To increase internet speed"
            ],
            "answer": "To learn patterns from data"
        },
        {
            "question": "Which of the following is a supervised learning task?",
            "options": [
                "Classification",
                "Clustering",
                "Dimensionality reduction",
                "Association rule mining"
            ],
            "answer": "Classification"
        },
        {
            "question": "What is overfitting?",
            "options": [
                "Model performs well on training data but poorly on unseen data",
                "Model has no training data",
                "Model always predicts the same value",
                "Model uses too little memory"
            ],
            "answer": "Model performs well on training data but poorly on unseen data"
        },
        {
            "question": "Which dataset is commonly used to evaluate a model on unseen data?",
            "options": [
                "Test dataset",
                "Training dataset",
                "Source code",
                "Database schema"
            ],
            "answer": "Test dataset"
        },
        {
            "question": "Which metric is commonly used for classification problems?",
            "options": [
                "Accuracy",
                "Mean Squared Error",
                "CPU frequency",
                "File size"
            ],
            "answer": "Accuracy"
        }
    ],


    "SQL": [
        {
            "question": "Which SQL command is used to retrieve data?",
            "options": [
                "SELECT",
                "GET",
                "FETCHDATA",
                "READ"
            ],
            "answer": "SELECT"
        },
        {
            "question": "Which clause is used to filter rows?",
            "options": [
                "WHERE",
                "FILTER",
                "SORT",
                "CHECK"
            ],
            "answer": "WHERE"
        },
        {
            "question": "Which command is used to add a new row?",
            "options": [
                "INSERT",
                "ADD",
                "CREATE ROW",
                "APPEND"
            ],
            "answer": "INSERT"
        },
        {
            "question": "Which clause is used to sort query results?",
            "options": [
                "ORDER BY",
                "SORT BY",
                "GROUP BY",
                "ARRANGE"
            ],
            "answer": "ORDER BY"
        },
        {
            "question": "Which SQL command modifies existing records?",
            "options": [
                "UPDATE",
                "MODIFY",
                "CHANGE",
                "EDIT"
            ],
            "answer": "UPDATE"
        }
    ],


    "ROS": [
        {
            "question": "What does ROS stand for?",
            "options": [
                "Robot Operating System",
                "Robotic Operating Software",
                "Robot Optimization System",
                "Remote Operating System"
            ],
            "answer": "Robot Operating System"
        },
        {
            "question": "What is a ROS node?",
            "options": [
                "A process that performs a specific computation",
                "A physical robot wheel",
                "A database table",
                "A programming language"
            ],
            "answer": "A process that performs a specific computation"
        },
        {
            "question": "Which ROS concept is commonly used for publish/subscribe communication?",
            "options": [
                "Topic",
                "Variable",
                "Class",
                "Loop"
            ],
            "answer": "Topic"
        },
        {
            "question": "What does a ROS publisher do?",
            "options": [
                "Sends messages to a topic",
                "Deletes nodes",
                "Creates hardware",
                "Compiles Python"
            ],
            "answer": "Sends messages to a topic"
        },
        {
            "question": "What does a ROS subscriber do?",
            "options": [
                "Receives messages from a topic",
                "Creates a database",
                "Controls the CPU",
                "Compiles C++"
            ],
            "answer": "Receives messages from a topic"
        }
    ],


    "Computer Vision": [
        {
            "question": "What is computer vision primarily concerned with?",
            "options": [
                "Understanding information from images or videos",
                "Managing databases",
                "Designing processors",
                "Writing operating systems"
            ],
            "answer": "Understanding information from images or videos"
        },
        {
            "question": "Which type of data is commonly processed in computer vision?",
            "options": [
                "Images",
                "Only text",
                "Only audio",
                "Only SQL tables"
            ],
            "answer": "Images"
        },
        {
            "question": "What is image classification?",
            "options": [
                "Assigning an image to a category",
                "Compressing a file",
                "Deleting an image",
                "Changing a database"
            ],
            "answer": "Assigning an image to a category"
        },
        {
            "question": "What does image resolution describe?",
            "options": [
                "The number of pixels in an image",
                "The file name",
                "The programming language",
                "The image's database ID"
            ],
            "answer": "The number of pixels in an image"
        },
        {
            "question": "Which Python library is commonly used for computer vision?",
            "options": [
                "OpenCV",
                "SQLAlchemy",
                "FastAPI",
                "Uvicorn"
            ],
            "answer": "OpenCV"
        }
    ]

}


# ---------------------------------------------------------
# GET QUESTIONS FOR A SKILL
# ---------------------------------------------------------

def get_questions(skill):
    """
    Return assessment questions for the selected skill.
    """

    return QUESTION_BANK.get(skill, [])


# ---------------------------------------------------------
# CALCULATE SCORE
# ---------------------------------------------------------

def calculate_score(skill, user_answers):
    """
    Calculate the assessment score.

    user_answers should be a list containing
    the answers selected by the user.
    """

    questions = get_questions(skill)

    if not questions:
        return {
            "skill": skill,
            "score": 0,
            "total_questions": 0,
            "correct_answers": 0,
            "level": "Not Assessed"
        }

    correct_answers = 0

    for question, user_answer in zip(
        questions,
        user_answers
    ):

        if user_answer == question["answer"]:
            correct_answers += 1

    total_questions = len(questions)

    score = (
        correct_answers / total_questions
    ) * 100


    # -----------------------------------------
    # DETERMINE PROFICIENCY
    # -----------------------------------------

    if score >= 80:

        level = "Advanced"

    elif score >= 60:

        level = "Intermediate"

    elif score >= 40:

        level = "Beginner"

    else:

        level = "Needs Improvement"


    return {
        "skill": skill,
        "score": score,
        "total_questions": total_questions,
        "correct_answers": correct_answers,
        "level": level
    }