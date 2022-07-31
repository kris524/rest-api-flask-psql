from flask import Flask
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)



from models import DogOwner

@app.route("/")
def index():
    dog_owners = DogOwner.query.all()
    return dog_owners


# from models import DogOwner, Dog, DogOwnerSchema, DogSchema


# @app.route("/dogowner", methods=["GET"])
# def all_owners():
#     owner = DogOwner.query.all()
#     result = DogOwnerSchema().dump(owner)
#     return {"dogowners": result}


if __name__ == "__main__":
    app.run(debug=True)
