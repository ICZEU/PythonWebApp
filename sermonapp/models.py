#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111
from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy import  Integer, String, LargeBinary, DateTime
from sqlalchemy.orm import relationship
from sermonapp import db


class Speaker(db.Model):
    __tablename__ = 'Speakers'

    id = Column('Id', Integer, primary_key=True)
    lastname = Column('LastName', String(200), nullable=False)
    firstname = Column('FirstName', String(200), nullable=False)
    position = Column('Position', String(200))
    description = Column('Description', String(1000))
    image_id = Column('ImageId', Integer, ForeignKey('Files.Id'))
    image = relationship('File')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Speaker %r, %r>' % (self.lastname, self.firstname)


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
    image_id = Column('ImageId', Integer, ForeignKey('Files.Id'))
    image = relationship('File')
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
    file_data = relationship('FileData', lazy='noload')

    def __init__(self, name=None, content_type=None, data=None):
        """Initialize a File.

        name         -- file name
        content_type -- mime type of the file
        data         -- binary data file content
        """
        self.name = name
        self.content_type = content_type
        self.file_data = FileData(data)

    def __repr__(self):
        return '<File %r>' % self.name


class FileData(db.Model):
    """Represents a pure binary file data."""

    __tablename__ = 'FileData'

    id = Column('Id', Integer, primary_key=True)
    data = Column('Data', LargeBinary(), nullable=False)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<FileData %r>' % self.id


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
