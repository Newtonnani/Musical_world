from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

POSTGRES = {
    'user': 'postgres',
    'pw': '1234',
    'db': 'songs',
    'host': 'localhost',
    'port': '5432',
}

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    db.init_app(app)
    with app.app_context():
        from . import routes
        db.create_all()
        return app