from flask import Flask

from flask_restplus import Api
from marshmallow import ValidationError

from app import models, schemas, resources

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

models.db.init_app(app)
schemas.ma.init_app(app)
resources.api.init_app(app)

@app.before_first_request
def create_tables():
    models.db.create_all()


if __name__ == "__main__":
    app.run(port=5000, debug=True)
