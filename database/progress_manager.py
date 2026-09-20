# =========================================================
# LEARNING PROGRESS MANAGER
# =========================================================

from sqlalchemy.orm import Session

from database.models import LearningProgress


# =========================================================
# CREATE OR UPDATE PROGRESS
# =========================================================

def save_progress(
    db: Session,
    student_id: int,
    skill: str,
    status: str,
    progress_percentage: float = 0,
    notes: str = None
):
    """
    Create a new learning-progress record or update
    an existing record for the same student and skill.
    """

    # -----------------------------------------------------
    # CHECK IF RECORD ALREADY EXISTS
    # -----------------------------------------------------

    progress = (
        db.query(LearningProgress)
        .filter(
            LearningProgress.student_id == student_id,
            LearningProgress.skill == skill
        )
        .first()
    )


    # -----------------------------------------------------
    # CREATE NEW RECORD
    # -----------------------------------------------------

    if progress is None:

        progress = LearningProgress(
            student_id=student_id,
            skill=skill,
            status=status,
            progress_percentage=progress_percentage,
            notes=notes
        )

        db.add(progress)


    # -----------------------------------------------------
    # UPDATE EXISTING RECORD
    # -----------------------------------------------------

    else:

        progress.status = status

        progress.progress_percentage = (
            progress_percentage
        )

        progress.notes = notes


    # -----------------------------------------------------
    # SAVE TO DATABASE
    # -----------------------------------------------------

    db.commit()

    db.refresh(progress)


    return progress


# =========================================================
# GET STUDENT PROGRESS
# =========================================================

def get_student_progress(
    db: Session,
    student_id: int
):
    """
    Return all learning-progress records
    belonging to a student.
    """

    return (
        db.query(LearningProgress)
        .filter(
            LearningProgress.student_id == student_id
        )
        .all()
    )