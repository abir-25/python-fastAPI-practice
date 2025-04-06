from fastapi import APIRouter, Depends, status
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(id, db: Session = Depends(get_db)):
    return user.show(id, db)