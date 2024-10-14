from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models
from typing import List
# from .. import utils
router = APIRouter(
    prefix="/projects",
    tags=['Projects']
)


@router.get('/', response_model=List[schemas.ProjectIn])
def getProjects(db: Session = Depends(get_db)):
    project = db.query(models.Project).all()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="project links not found!!!")
    return project


@router.post('/')
def addProject(project: schemas.ProjectIn, db: Session = Depends(get_db)):
    new_project = models.Project(**project.model_dump())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project
