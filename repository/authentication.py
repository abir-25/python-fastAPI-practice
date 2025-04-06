from datetime import timedelta

from sqlalchemy.orm import Session

from .. import models, schemas, token
from ..hashing import Hash
from fastapi import status, HTTPException

def login(request: schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect Password')

    access_token = token.create_access_token(data={"sub": request.username})
    return {"access_token": access_token, "token_type": "bearer"}
