from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)


app.config["SECRET_KEY"] = '55555'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:1310526879@localhost:5432/mypass_test'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
ma = Marshmallow(app)
db.init_app(app)
