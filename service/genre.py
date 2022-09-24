from dao.genre import GenreDAO


class GenreService:
    """
    Описание бизнес логики для объекта "жанр"
    """
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self):
        """Получение полного списка жанров"""
        return self.genre_dao.get_all()

    def get_genre(self, gid):
        """Получение жанра по его id"""
        return self.genre_dao.get_one(gid)

