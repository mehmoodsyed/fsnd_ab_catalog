#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    recordOwner = Column(String(500))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'owner': self.recordOwner,
            'id': self.id,
        }


class Audiobook(Base):
    __tablename__ = 'audiobook'

    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)
    duration = Column(String(8))
    price = Column(String(8))
    recordOwner = Column(String(500))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship(Genre)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'id': self.id,
            'duration': self.duration,
            'price': self.price,
            'owner': self.recordOwner,
        }


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    audiobook_id = Column(Integer, ForeignKey('audiobook.id'))
    audiobook = relationship(Audiobook, cascade="all, delete-orphan",
                             single_parent=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Narrator(Base):
    __tablename__ = 'narrator'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    audiobook_id = Column(Integer, ForeignKey('audiobook.id'))
    audiobook = relationship(Audiobook, cascade="all, delete-orphan",
                             single_parent=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Link(Base):
    __tablename__ = 'link'

    id = Column(Integer, primary_key=True)
    url = Column(Text, nullable=False)
    audiobook_id = Column(Integer, ForeignKey('audiobook.id'))
    audiobook = relationship(Audiobook, cascade="all, delete-orphan",
                             single_parent=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


engine = create_engine('sqlite:///audiobookcatalog.db')


Base.metadata.create_all(engine)
