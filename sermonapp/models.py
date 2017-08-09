#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111
import uuid
from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, LargeBinary
from sqlalchemy import DateTime, Boolean, BigInteger
from sqlalchemy.orm import relationship
from sermonapp import db


def new_uuid():
    """Create a new uuid in hex format."""
    return uuid.uuid4().hex


class Sermon(db.Model):
    __tablename__ = 'Sermons'

    id = Column('Id', Integer, primary_key=True)
    title = Column('Title', String(250), nullable=False)
    date = Column('Date', DateTime, default=datetime.today, nullable=False)
    speaker_id = Column('SpeakerId', Integer, ForeignKey('Speakers.Id'))
    speaker = relationship('Speaker')
    series_id = Column('SeriesId', Integer, ForeignKey('Series.Id'))
    series = relationship('Series')
    category_id = Column('CategoryId', Integer, ForeignKey('Categories.Id'))
    category = relationship('Category')
    bible_references = Column('BibleReferences', String(1000))
    audio_file_id = Column('AudioFileId', Integer, ForeignKey('Files.Id'))
    audio_file = relationship('File')
    video_id = Column('VideoId', Integer, ForeignKey('Videos.Id'))
    video = relationship('Video')
    published_from = Column('PublishedFrom', DateTime)
    published_until = Column('PublishedUntil', DateTime)
    hidden = Column('Hidden', Boolean, nullable=False, default=False)
    created_at = Column('CreatedAt', DateTime, default=datetime.now, nullable=False)

    def is_public(self):
        """Decides whether a sermon can be published or not."""
        return self.audio_file or (self.video.provider and self.video.embed_id)

    def __repr__(self):
        return '<Sermon %r>' % (self.id)


class Video(db.Model):
    __tablename__ = 'Videos'

    id = Column('Id', Integer, primary_key=True)
    provider = Column('Provider', String(100), nullable=False)
    embed_id = Column('EmbedId', String(100), nullable=False)

    def __init__(self, provider=None, embed_id=None):
        self.provider = provider
        self.embed_id = embed_id

    def __repr__(self):
        return '<Video %r>' % (self.id)


class Speaker(db.Model):
    __tablename__ = 'Speakers'

    id = Column('Id', Integer, primary_key=True)
    lastname = Column('LastName', String(200), nullable=False)
    firstname = Column('FirstName', String(200), nullable=False)
    position = Column('Position', String(200))
    description = Column('Description', String(1000))
    image_id = Column('ImageId', Integer, ForeignKey('Files.Id'))
    image = relationship('File')
    created_at = Column('CreatedAt', DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return '<Speaker %r, %r>' % (self.lastname, self.firstname)


class Category(db.Model):
    __tablename__ = 'Categories'

    id = Column('Id', Integer, primary_key=True)
    name = Column('Name', String(100), unique=True, nullable=False)
    created_at = Column('CreatedAt', DateTime, default=datetime.now, nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % (self.name)


class Series(db.Model):
    __tablename__ = 'Series'

    id = Column('Id', Integer, primary_key=True)
    title = Column('Title', String(100), unique=True, nullable=False)
    description = Column('Description', String(1000))
    image_id = Column('ImageId', String(32), ForeignKey('Files.Id'))
    image = relationship('File')
    created_at = Column('CreatedAt', DateTime, default=datetime.now, nullable=False)

    def __init__(self, title=None, description=None):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<Series %r>' % self.title



class File(db.Model):
    __tablename__ = 'Files'

    id = Column('Id', String(32), primary_key=True, default=new_uuid)
    name = Column('Name', String(100), nullable=False)
    content_type = Column('ContentType', String(100))
    file_size = Column('FileSize', BigInteger)
    file_data_id = Column('FileDataId', Integer, ForeignKey('FileData.Id'), nullable=False)
    file_data = relationship('FileData', lazy='noload')
    created_at = Column('CreatedAt', DateTime, default=datetime.now, nullable=False)

    def __init__(self, name=None, content_type=None, data=None):
        """Initialize a File.

        name         -- file name
        content_type -- mime type of the file
        data         -- binary data file content
        """
        self.name = name
        self.content_type = content_type
        self.file_size = data and len(data)
        self.file_data = FileData(data)

    def __repr__(self):
        return '<File %r>' % self.name


class FileData(db.Model):
    """Represents a large binary object (BLOB)."""

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
    name = Column('Name', String(50), unique=True, nullable=False)
    email = Column('Email', String(120), unique=True, nullable=False)
    created_at = Column('CreatedAt', DateTime, default=datetime.now, nullable=False)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class UploadChunk():
    """Metadata of file upload chunk"""
    def __init__(self, chunk_index=None, content_type=None, file_name=None,
                 total_file_size=None, total_chunks=None, upload_uid=None):
        self.chunk_index = chunk_index
        self.content_type = content_type
        self.file_name = file_name
        self.total_file_size = total_file_size
        self.total_chunks = total_chunks
        self.upload_uid = upload_uid
