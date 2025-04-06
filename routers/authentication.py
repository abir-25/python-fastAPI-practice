from fastapi import APIRouter, Depends, status
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import authentication

router = APIRouter(
    tags=['authentication']
)
get_db = database.get_db


@router.post('/login', status_code=status.HTTP_201_CREATED)
def login(request: schemas.Login, db: Session = Depends(get_db)):
    return authentication.login(request, db)