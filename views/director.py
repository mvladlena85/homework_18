from flask_restx import Namespace, Resource

from dao.model.director import DirectorSchema
from implemented import director_service


"""
Представления для обработки запросов к /directors/
"""
director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_directors()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_director(did)
        if not director:
            return "Wrong director id", 404
        return director_schema.dump(director), 200
