from flask_restx import Namespace, Resource

from dao.model.genre import GenreSchema
from implemented import genre_service

"""
Представления для обработки запросов к /genres/
"""
genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_genres()
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_genre(gid)
        if not genre:
            return "Wrong genre id", 404
        return genre_schema.dump(genre), 200
