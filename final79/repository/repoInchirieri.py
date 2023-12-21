from domain.domainInchirieri import Inchirieri

class repoInchirieri:
    def __init__(self):
        self.__listaInchirieri = []
        self.__id = 0

    def adauga_inchiriere(self, idClient, idFilm):
        '''
        Functia va adauga o inchiriere in repo
        :param idClient: INT
        :param idFilm: INT
        :return: VOID
        '''
        self.__id += 1
        inchiriere = Inchirieri(idClient, idFilm)
        self.__listaInchirieri.append(inchiriere)

    def sterge_inchiriere(self, idInchiriere):
        '''
        Functia va sterge o inchiriere din repo
        :param idInchiriere: INT
        :return: VOID
        '''
        new_inchiriere_list = []
        for inchiriere in self.__listaInchirieri:
            if inchiriere.get_idInchiriere() != idInchiriere:
                new_inchiriere_list.append(inchiriere)

        self.__listaInchirieri = new_inchiriere_list

    def get_all_inchirieri(self):
        '''
        Functia va returna toate inchirierile din repo
        :return: LIST INCHIRIERI
        '''
        return self.__listaInchirieri

    def search_inchiriere_by_id(self, idInchiriere):
        '''
        Functia va returna o INCHIRIERE pe baza id-ului
        :param idInchiriere: INT
        :return: INCHIRIERE
        '''
        for inchiriere in self.__listaInchirieri:
            if inchiriere.get_idInchiriere() == idInchiriere:
                return inchiriere
    def sterge_inchiriere(self , id1 , id2):

        listaNoua = []
        for inchiriere in self.__listaInchirieri:
            idClient = inchiriere.get_idClient()
            idFilm = inchiriere.get_idFilm()

            if(idClient != id1 and idFilm != id2):
                listaNoua.append(inchiriere)
        self.__listaInchirieri = listaNoua




