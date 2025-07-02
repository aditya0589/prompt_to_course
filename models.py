from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import os
import tempfile


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(200))
    plans = relationship("Plan", back_populates="user")

class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True)
    subject = Column(String(100))
    timeframe = Column(String(100))
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="plans")

# DB setup

db_path = os.path.join(tempfile.gettempdir(), "local.db")
engine = create_engine(f"sqlite:///{db_path}")
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
