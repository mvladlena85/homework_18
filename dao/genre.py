from dao.model.genre import Genre


class GenreDAO:
    """
    Класс доступа данным из таблицы БД genre
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, gid: str) -> Genre:
        """
        получение одной записи по ее id
        :param gid: str
            id
        :return: Genre
        """
        genre = self.session.query(Genre).get(gid)
        return genre

    def get_all(self) -> list[Genre]:
        """
        получение всех данных из таблицы
        :return: list[Genre]
        """
        genre = self.session.query(Genre).all()
        return genre
