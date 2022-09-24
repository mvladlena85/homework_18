from flask import Flask
from flask_restx import Api

from config import Config
from constants import DATA
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from setup_db import db

from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns


# функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    app.app_context().push()
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


# функция заливки данных в БД
def create_data(app, db):
    with app.app_context():
        db.drop_all()
        db.create_all()
        movie_list = []
        genre_list = []
        director_list = []

        for movie in DATA["movies"]:
            m = Movie(
                id=movie["pk"],
                title=movie["title"],
                description=movie["description"],
                trailer=movie["trailer"],
                year=movie["year"],
                rating=movie["rating"],
                genre_id=movie["genre_id"],
                director_id=movie["director_id"],
            )
            movie_list.append(m)

        for director in DATA["directors"]:
            d = Director(
                id=director["pk"],
                name=director["name"],
            )
            director_list.append(d)

        for genre in DATA["genres"]:
            g = Genre(
                id=genre["pk"],
                name=genre["name"],
            )
            genre_list.append(g)

        with db.session.begin():
            db.session.add_all(genre_list)
            db.session.add_all(director_list)
            db.session.add_all(movie_list)


config = Config()
app = create_app(config)

if __name__ == '__main__':
    app.run(host="localhost", port=10001)
