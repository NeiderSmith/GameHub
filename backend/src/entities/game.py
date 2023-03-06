# coding=utf-8
from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .entity import Entity, Base
from .gamecategory import GameCategorySchema

from marshmallow import Schema, fields

class Game(Entity, Base):
    __tablename__ = 'games'

    title = Column(String)
    description = Column(String)
    release_date = Column(Date)
    cover_image = Column(String)
    category_id = Column(Integer, ForeignKey("game_category.id"))
    active = Column(Boolean)
    category = relationship("GameCategory")

    def __init__(self, title, description, release_date, cover_image, category_id, active, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
        self.release_date = release_date
        self.cover_image = cover_image
        self.category_id = category_id
        self.active = active

class GameSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    cover_image = fields.Str()
    release_date = fields.Date()
    category_id = fields.Number()
    category = fields.Nested(GameCategorySchema(only=("name",)))
    active = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
