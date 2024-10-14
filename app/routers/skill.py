from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models
from typing import List
# from .. import utils
router = APIRouter(
    prefix="/skills",
    tags=['Skill']
)


@router.get('/', response_model=List[schemas.SkillIn])
def getSkills(db: Session = Depends(get_db)):
    skills = db.query(models.Skill).all()
    if not skills:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="skill links not found!!!")
    return skills


@router.post('/')
def addSkill(skill: schemas.SkillIn, db: Session = Depends(get_db)):
    new_skill = models.Skill(**skill.model_dump())
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill
