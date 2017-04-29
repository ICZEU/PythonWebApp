#!/usr/bin/python
# -*- coding: utf-8 -*-
from sermonapp import db
from sermonapp.models import User
from sermonapp.models import Category

def ensure_database():
    """Initialize the database if it has not tables yet."""
    if not db.engine.dialect.has_table(db.engine, User.__tablename__):
        db.create_all()
        seed()


def seed():
    """Add default data to the database."""
    db.session.add(Category('Jugendgottesdienst'))
    db.session.add(Category('Sonntagsgottesdienst'))
    db.session.add(Category('Veranstaltung'))
    db.session.commit()