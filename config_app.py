import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
#'sqlite:////' + os.path.join(basedir, 'site.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_rep')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '234iujvec984c839mji'
#app.config['SECRET_KEY'] = '234iujvec984c839mji'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

