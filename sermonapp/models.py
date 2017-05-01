#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111
from sqlalchemy import Column, ForeignKey
from sqlalchemy import  Integer, String, LargeBinary, DateTime
from sqlalchemy.orm import relationship
from sermonapp import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'Users'

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String(50), unique=True)
    email = Column('Email', String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class Category(db.Model):
    __tablename__ = 'Categories'

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String(100), unique=True, nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % (self.name)


class Series(db.Model):
    __tablename__ = 'Series'

    id = Column('Id', Integer, primary_key=True)
    title = Column('Title', String(100), unique=True, nullable=False)
    description = Column('Description', String(1000))
    file_id = Column('FileId', Integer, ForeignKey('Files.Id'))
    file = relationship("File")
    created_at = Column('CreatedAt', DateTime, default=datetime.now)

    def __init__(self, title=None, description=None):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<Series %r>' % self.title


class File(db.Model):
    __tablename__ = 'Files'

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String(100), nullable=False)
    content_type = Column('ContentType', String(100))
    file_data_id = Column('FileDataId', Integer, ForeignKey('FileData.Id'))

    def __init__(self, name=None, content_type=None, file_data=None):
        self.name = name
        self.content_type = content_type
        self.file_data_id = file_data.id

    def __repr__(self):
        return '<File %r>' % self.name


class FileData(db.Model):
    __tablename__ = 'FileData'

    id = Column('Id', Integer, primary_key=True)
    data = Column('Data', LargeBinary(), nullable=False)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<FileData %r>' % self.id
