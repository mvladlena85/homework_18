from flask import request
from flask_restx import Namespace, Resource

from dao.model.movie import MovieSchema
from implemented import movie_service

"""
Представления для обработки запросов к /movies/
"""
movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        # genre_id = request.args.get("genre_id")
        # director_id = request.args.get("director_id")
        # year = request.args.get("year")
        # if genre_id is not None:
        #     movies = movie_service.filter_movie("genre", genre_id)
        # elif director_id is not None:
        #     movies = movie_service.filter_movie("director", director_id)
        # elif year is not None:
        #     movies = movie_service.filter_movie("year", year)
        # else:
        #     movies = movie_service.get_movies()
        # return movies_schema.dump(movies), 200
        args = request.args
        if len(args):
            movies = movie_service.filter_movie(**args)
        else:
            movies = movie_service.get_movies()
        return movies_schema.dump(movies), 200

    def post(self):
        data = request.json
        movie = movie_service.create_movie(data)
        return movie.id, 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_movie(mid)
        if not movie:
            return "Wrong movie id", 404
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data["id"] = mid
        movie_service.update_movie(data)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204
