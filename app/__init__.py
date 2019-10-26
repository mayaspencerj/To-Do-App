#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#app = Flask(__name__)
#app.config.from_object('config_app')
#db = SQLAlchemy(app)
#from app import views, models

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object('config_app')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import views, models
