from fastapi import FastAPI, Depends, HTTPException, status  # Importar status desde fastapi
from sqlalchemy.orm import Session
from typing import List  # Importar List desde typing
from fastapi.security import OAuth2PasswordRequestForm  # Importar OAuth2PasswordRequestForm
from datetime import timedelta  # Importar timedelta desde datetime
from . import models, schemas, crud, database, auth

app = FastAPI()

models.SQLModel.metadata.create_all(bind=database.engine)

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/roles/", response_model=schemas.Role)
def create_role(role: schemas.RoleCreate, db: Session = Depends(database.get_db)):
    return crud.create_role(db=db, role=role)

@app.get("/roles/", response_model=List[schemas.Role])
def get_roles(db: Session = Depends(database.get_db)):
    return crud.get_roles(db=db)

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(auth.get_current_user)):
    return current_user