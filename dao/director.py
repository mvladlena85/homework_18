from dao.model.director import Director


class DirectorDAO:
    """
    Класс доступа данным из таблицы БД director
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, did: str) -> Director:
        """
        получение режиссера по его id
        :param did: str
            id
        :return: Director
        """
        director = self.session.query(Director).get(did)
        return director

    def get_all(self) -> list[Director]:
        """
        получение всех данных из таблицы
        :return: list[Director]
        """
        director = self.session.query(Director).all()
        return director
