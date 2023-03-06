# coding=utf-8
from sqlalchemy import Column, String

from .entity import Entity, Base

from marshmallow import Schema, fields

class GameCategory(Entity, Base):
    __tablename__ = 'game_category'

    name = Column(String)
    description = Column(String)

    def __init__(self, name, description, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.description = description

class GameCategorySchema(Schema):
    id = fields.Number()
    name = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
