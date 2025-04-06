from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import status, HTTPException


def all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, description=request.description, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog is not found of ID: {id}')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': f'Blog is not found of ID: {id}'}
    return blog

def update(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog not found with ID: {id}')

    db.query(models.Blog).filter(models.Blog.id == id).update(request.dict(), synchronize_session=False)
    db.commit()

    return {'message': 'Blog is updated successfully'}

def destroy(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog not found with ID: {id}')

    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()

    return {'message': 'Blog is deleted successfully'}