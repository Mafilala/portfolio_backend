from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models

router = APIRouter(
    prefix="/about",
    tags=['About']
)

# Get the current 'About' information
@router.get('/', response_model=schemas.AboutIn)
def get_about(db: Session = Depends(get_db)):
    about = db.query(models.About).first()
    if not about:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="About section not found!")
    return about

# Add or update the 'About' section
@router.post('/', response_model=schemas.AboutIn)
def add_or_update_about(about: schemas.AboutIn, db: Session = Depends(get_db)):
    current_about = db.query(models.About).first()

    if current_about:
        current_about.image_url = about.image_url
        current_about.intro = about.intro
        current_about.experience = about.experience
        db.commit()
        db.refresh(current_about)
        return current_about
    else:
        # Create a new 'About' entry
        new_about = models.About(**about.model_dump())
        db.add(new_about)
        db.commit()
        db.refresh(new_about)
        return new_about
