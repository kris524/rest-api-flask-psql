import os
from app import db
from models import DogOwner, Dog

db.create_all()

dogowner1 = DogOwner(name="joe", email="joe@gog.com")

dog1 = Dog(name="gosj", breed="rot", dogowner_id=1)


db.session.add_all([dogowner1])
db.session.add_all([dog1])

db.session.commit()
