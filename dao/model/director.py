from marshmallow import Schema, fields

from setup_db import db


class Director(db.Model):
    """
    Модель SQLAlchemy для объекта "режиссер".
    """
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    """
    Схема для сериализации объекта "режиссер"
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
