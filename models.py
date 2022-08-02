from app import db, ma
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields


class DogOwner(db.Model):
    __tablename__ = "dogowner"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String)
    email = db.Column("email", db.String)
    dog = db.relationship("Dog")

    def __repr__(self):
        return f'<name "{self.name}">'


class Dog(db.Model):
    __tablename__ = "dog"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String)
    breed = db.Column("breed", db.String)
    dogowner_id = db.Column(db.Integer, db.ForeignKey("dogowner.id"))

    def __repr__(self):
        return f'<breed "{self.breed}">'

    def __init__(self, name, breed, dogowner_id) -> None:
        self.name = name
        self.breed = breed
        self.dogowner_id = dogowner_id


class DogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dog


class DogOwnerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DogOwner
        include_relationships = True

    dog = fields.Nested(DogSchema(), many=True)
