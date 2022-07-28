from flask import Flask

app = Flask(__name__)

# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = f"postgresql://{username}:{password}@{host}:{port}/{database}"


if __name__ == "__main__":
    app.run(debug=True)
