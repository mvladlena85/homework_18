from dao.model.movie import Movie, MovieSchema


class MovieDAO:
    """
    Класс доступа данным из таблицы БД movie
    """
    movie_schema = MovieSchema()
    movies_schema = MovieSchema(many=True)

    def __init__(self, session):
        self.session = session

    def get_one(self, mid: str) -> Movie:
        """
        получение одной записи по ее id
        :param mid: id
        :return: Movie
        """
        movie = self.session.query(Movie).get(mid)
        return movie

    def get_all(self) -> list[Movie]:
        """
        получение всех данных из таблицы
        :return: list[Movie]
        """
        movies = self.session.query(Movie).all()
        return movies

    # def get_by_director(self, did):
    #     movies = self.session.query(Movie).filter_by(Movie.director_id == did)
    #     return movies
    #
    # def get_by_genre(self, gid):
    #     movies = self.session.query(Movie).filter(Movie.genre_id == gid).all()
    #     return movies
    #
    # def get_by_year(self, year):
    #     movies = self.session.query(Movie).filter(Movie.year == year).all()
    #     return movies

    def get_by_filter(self, **kwargs) -> list[Movie]:
        """
        получение списка фильмов, в соответствии с критериями фильтрации
        :param kwargs:
            список с параметрами фильтров
        :return: list[Movie]
        """
        movies = self.session.query(Movie).filter_by(**kwargs)
        return movies

    def create(self, data: dict) -> Movie:
        """
        создание новой записи в таблице
        :param data: dict
        :return: Movie
        """
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie: Movie) -> Movie:
        """
        обновление данных по фильму
        :param movie:
        :return:
        """
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid: str):
        """
        удаление записи по ее Id
        :param mid: str
            id
        :return: None
        """
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
