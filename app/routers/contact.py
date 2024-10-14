from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models
from typing import List
router = APIRouter(
    prefix="/contacts",
    tags=['Contacts']
)


@router.post('/', response_model=schemas.ContactIn)
def addContact(contact: schemas.ContactIn, db: Session = Depends(get_db)):
    new_contact = models.Contact(**contact.model_dump())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact


@router.get('/', response_model=List[schemas.ContactIn])
def getContacts(db: Session = Depends(get_db)):
    contacts = db.query(models.Contact).all()
    if not contacts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="contact information not found!!!")
    return contacts
