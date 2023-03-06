# coding=utf-8
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .entity import Entity, Base

from marshmallow import Schema, fields

class Score(Entity, Base):
    __tablename__ = 'scores'

    user_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    score = Column(Integer)
    user = relationship("User", backref="score")
    game = relationship("Game", backref="score")

    def __init__(self, user_id, game_id, score, created_by):
        Entity.__init__(self, created_by)
        self.user_id = user_id
        self.game_id = game_id
        self.score = score

class ScoreSchema(Schema):
    id = fields.Number()
    user_id = fields.Number()
    game_id = fields.Number()
    score = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
