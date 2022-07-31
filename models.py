# from flask_sqlalchemy import SQLAlchemy
from app import db
from app import ma


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


# class DogOwnerSchema(ma.SQLAlchemySchema):
#     # class Meta:
#     #     mode = DogOwner
#     #     load_instance= True
#     id = ma.auto_field()
#     name = ma.auto_field()
#     email = ma.auto_field()


# class DogSchema(ma.Schema):
#     id = ma.fields.Integer()
#     name = ma.fields.String()
#     breed = ma.fields.String()
#     dogowner_id = ma.fields.Integer()
