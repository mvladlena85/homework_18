from dao.director import DirectorDAO


class DirectorService:
    """
    Описание бизнес логики для объекта "режиссер"
    """
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self):
        """Получение полного списка режиссеров"""
        return self.director_dao.get_all()

    def get_director(self, did):
        """Получение режиссера по его id"""
        return self.director_dao.get_one(did)
