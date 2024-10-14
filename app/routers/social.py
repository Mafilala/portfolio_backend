from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models
from typing import List
# from .. import utils
router = APIRouter(
    prefix="/socials",
    tags=['Socials']
)


@router.get('/', response_model=List[schemas.SocialOut])
def getSocials(db: Session = Depends(get_db)):
    socials = db.query(models.Social).all()
    if not socials:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="social links not found!!!")
    return socials


@router.post('/')
def addSocial(social: schemas.SocialIn, db: Session = Depends(get_db)):
    new_social = models.Social(**social.model_dump())
    db.add(new_social)
    db.commit()
    db.refresh(new_social)
    return new_social
