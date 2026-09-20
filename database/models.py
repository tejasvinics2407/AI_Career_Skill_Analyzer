# =========================================================
# DATABASE MODELS
# =========================================================

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Text

from database.database import Base


# =========================================================
# STUDENT PROFILE
# =========================================================

class Student(Base):

    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=True
    )

    email = Column(
        String,
        nullable=True
    )

    target_role = Column(
        String,
        nullable=True
    )


# =========================================================
# SKILL RECORD
# =========================================================

class SkillRecord(Base):

    __tablename__ = "skill_records"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        nullable=False
    )

    skill = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )

    source = Column(
        String,
        nullable=True
    )


# =========================================================
# ASSESSMENT RESULT
# =========================================================

class AssessmentResult(Base):

    __tablename__ = "assessment_results"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        nullable=False
    )

    skill = Column(
        String,
        nullable=False
    )

    score = Column(
        Float,
        nullable=False
    )

    correct_answers = Column(
        Integer,
        nullable=False
    )

    total_questions = Column(
        Integer,
        nullable=False
    )

    proficiency = Column(
        String,
        nullable=False
    )


# =========================================================
# LEARNING PROGRESS
# =========================================================

class LearningProgress(Base):

    __tablename__ = "learning_progress"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        nullable=False
    )

    skill = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )

    progress_percentage = Column(
        Float,
        default=0
    )

    notes = Column(
        Text,
        nullable=True
    )