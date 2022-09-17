from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_room(db: Session, room_id: int):
    return db.query(models.Room).filter(models.Room.id == room_id).first()

def get_room_by_name(db: Session, name: str):
    return db.query(models.Room).filter(models.Room.name == name).first()

def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit).all()

def create_room(db: Session, room: schemas.RoomCreate):
    db_room = models.Room(name=room.name, status=room.status)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def get_achievement(db: Session, achiev_id: int):
    return db.query(models.Achievement).filter(models.Achievement.id == achiev_id).first()

def get_achievement_by_name(db: Session, name: str):
    return db.query(models.Achievement).filter(models.Achievement.name == name).first()

def get_achievements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Achievement).offset(skip).limit(limit).all()

def create_achievement(db: Session, achiev: schemas.AchievementCreate):
    db_achiev = models.Achievement(name=achiev.name, image=achiev.image)
    db.add(db_achiev)
    db.commit()
    db.refresh(db_achiev)
    return db_achiev

def get_schedule(db: Session, schedule_id: int):
    return db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()

def get_schedules(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Schedule).offset(skip).limit(limit).all()

def create_schedule(db: Session, schedule: schemas.ScheduleCreate):
    db_schedule = models.Schedule(schedulestart=schedule.schedulestart, schedulestop=schedule.schedulestop)
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule