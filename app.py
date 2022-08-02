from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

import models



@app.route("/getall")
def get_all():
    dog_owners_schema = models.DogOwnerSchema(many=True)
    dog_schema = models.DogSchema(many=True)
    all_dogowners = models.DogOwner.query.all()

    return jsonify(dog_owners_schema.dump(all_dogowners))

if __name__ == "__main__":
    app.run(debug=True)
