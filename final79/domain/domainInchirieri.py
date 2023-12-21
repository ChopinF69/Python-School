class Inchirieri:
    def __init__(self , idClient , idFilm) -> None:
        self.__idClient = idClient
        self.__idFilm = idFilm

    def get_idClient(self):
        return self.__idClient
    def get_idFilm(self):
        return self.__idFilm
    
    def set_idClient(self , value):
        self.__idClient = value
    def set_idFilm(self, value):
        self.__idFilm = value