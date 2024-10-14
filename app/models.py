from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Skill(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True, nullable=False)
    icon = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, nullable=False)
    image_url = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    live_url = Column(String, nullable=False)


class About(Base):
    __tablename__ = 'about'
    id = Column(Integer, primary_key=True, nullable=False)
    image_url = Column(String, nullable=False)
    intro = Column(String, nullable=False)
    experience = Column(String, nullable=False)


class Social(Base):
    __tablename__ = 'socials'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    link = Column(String, nullable=False)
    icon = Column(String, nullable=False)


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("now()"), nullable=False)