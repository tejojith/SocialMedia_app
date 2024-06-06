from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import model, schemas, util, oauth2
from .. import database 


router = APIRouter(
    prefix = "/users",
    tags = ['User'] )

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    
    hashed_password = util.pwd_context.hash(user.password)
    user.password = hashed_password

    new_user = model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/{id}', response_model = schemas.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
                            , detail= f"user with id: {id} does not exist" )
    return user