from dao.movie import MovieDAO


class MovieService:
    """
    Описание бизнес логики для объекта "фильм"
    """
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movie(self, mid):
        """Получение фильма по его ID"""
        return self.movie_dao.get_one(mid)

    def get_movies(self):
        """Получение всех фильмов"""
        return self.movie_dao.get_all()

    def create_movie(self, data):
        """Создание нового фильма"""
        return self.movie_dao.create(data)

    def update_movie(self, data):
        """Изменение данных фильма"""
        movie = self.get_movie(data.get("id"))
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.director_id = data.get("director_id")
        movie.year = data.get("year")
        movie.genre_id = data.get("genre_id")
        movie.rating = data.get("rating")

        self.movie_dao.update(movie)

    def delete(self, mid):
        """Удаление фильма"""
        self.movie_dao.delete(mid)

    # def filter_movie(self, field, value):
    #     if field == "year":
    #         return self.movie_dao.get_by_year(value)
    #     if field == "genre":
    #         return self.movie_dao.get_by_genre(value)
    #     if field == "director":
    #         return self.movie_dao.get_by_director(value)

    def filter_movie(self, **kwargs):
        """Фильтрация фильмов по критериям"""
        return self.movie_dao.get_by_filter(**kwargs)
