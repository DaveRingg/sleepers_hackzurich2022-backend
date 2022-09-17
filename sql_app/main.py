from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert, update, delete

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Users
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/update", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    update(db.get_users).where(db.get_users.c.id == user_id).value(email = user.email, hashed_password = user.password, is_active = user.is_active, address = user.address, overallenergyhistory = overallenergyhistory, moneysaved = user.moneysaved, co2saved = user.co2saved, achievements = user.achievements, rooms = user.rooms)
    return db_user

#Rooms
@app.post("/users/{user_id}/rooms/", response_model=schemas.Room)
def create_room(room: schemas.Room, db: Session = Depends(get_db)):
    db_room = crud.get_room_by_name(db, name=room.name)
    if db_room:
        raise HTTPException(status_code=400, detail="Room already registered")
    return crud.create_room(db=db, room=room)


@app.get("/users/{user_id}/rooms/", response_model=List[schemas.Room])
def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return rooms


@app.get("/users/{user_id}/rooms/{room_id}", response_model=schemas.Room)
def read_room(room_id: int, db: Session = Depends(get_db)):
    db_room = crud.get_room(db, room_id=room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

#Schedules
@app.post("/users/{user_id}/rooms/{room_id}/schedules", response_model=schemas.Schedule)
def create_schedule(schedule: schemas.Schedule, db: Session = Depends(get_db)):
    return crud.create_schedule(db=db, schedule=schedule)


@app.get("/users/{user_id}/rooms/{room_id}/schedules", response_model=List[schemas.Schedule])
def read_schedules(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    schedules = crud.get_schedules(db, skip=skip, limit=limit)
    return schedules


@app.get("/users/{user_id}/rooms/{room_id}/schedules", response_model=schemas.Room)
def read_room(room_id: int, db: Session = Depends(get_db)):
    db_room = crud.get_room(db, room_id=room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

#Achievements
@app.post("/users/{user_id}/achievements/", response_model=schemas.Achievement)
def create_achievement(achievement: schemas.Achievement, db: Session = Depends(get_db)):
    db_achiev = crud.get_achievement_by_name(db, name=achievement.name)
    if db_achiev:
        raise HTTPException(status_code=400, detail="Achievement already registered")
    return crud.create_achievement(db=db, achiev=achievement)


@app.get("/users/{user_id}/achievements/", response_model=List[schemas.Achievement])
def read_achievements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    achievements = crud.get_achievements(db, skip=skip, limit=limit)
    return achievements


@app.get("/users/{user_id}/achievements/{achiev_id}", response_model=schemas.Achievement)
def read_achievement(achiev_id: int, db: Session = Depends(get_db)):
    db_achiev = crud.get_achievement(db, achiev_id=achiev_id)
    if db_achiev is None:
        raise HTTPException(status_code=404, detail="Achievement not found")
    return db_achiev

#Blackout
@app.get("/blackout/")
def get_blackout():
    return 1000