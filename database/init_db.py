# =========================================================
# DATABASE INITIALIZATION
# =========================================================

from database.database import engine, Base

# Import models so SQLAlchemy knows about the tables
from database.models import (
    Student,
    SkillRecord,
    AssessmentResult,
    LearningProgress
)


# =========================================================
# CREATE TABLES
# =========================================================

Base.metadata.create_all(
    bind=engine
)


print("===================================")
print("DATABASE INITIALIZED SUCCESSFULLY")
print("===================================")
print("Tables created:")
print("- students")
print("- skill_records")
print("- assessment_results")
print("- learning_progress")