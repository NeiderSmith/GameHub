# coding=utf-8
from sqlalchemy import Column, String, Integer, DateTime, Date

from .entity import Entity, Base

from marshmallow import Schema, fields

class User(Entity, Base):
    __tablename__ = 'users'

    name = Column(String)
    birthdate = Column(Date)

    def __init__(self, name, birthdate, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.birthdate = birthdate

class UserSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    birthdate = fields.Date()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
