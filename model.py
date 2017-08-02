from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__  = 'user'
    id             = Column(Integer, primary_key=True)
    username       = Column(String)
    password       = Column(String)
    age			   = Column(Integer)
    interests      = Column(String)
    bio			   = Column(String)
    picture        = Column(String) #link to the picture

class Video(Base):
    __tablename__  = 'video'
    id             = Column(Integer, primary_key=True)
    video          = Column(String)
    username       = Column(String)
    date           = Column(String)
    # ADD YOUR FIELD BELOW ID

# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel