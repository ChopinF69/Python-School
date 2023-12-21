from domain.domainInchirieri import Inchirieri
from repository.repoInchirieri import repoInchirieri

class inchirieriService:
    def __init__(self):
        self.__repo = repoInchirieri()

    def service_adauga_inchiriere(self , idClient , idFilm):

        inchiriereNoua = Inchirieri(idClient , idFilm)
        self.__repo.adauga_inchiriere(idClient , idFilm)
        return inchiriereNoua

    def service_sterge_inchiriere(self , idInchiriere):

        self.__repo.sterge_inchiriere(idInchiriere)

    def service_get_all_inchirieri(self):

        return self.__repo.get_all_inchirieri()
    #write a function that tests the service_get_all_inchirieri

    def service_search_inchiriere_by_id(self , idInchiriere):

        inchiriere = self.__repo.search_inchiriere_by_id(idInchiriere)
        return inchiriere

    def service_get_inchiriere_ids(self , id1 , id2):
        listaInchirieri = self.__repo.get_all_inchirieri()

        for inchiriere in listaInchirieri:
            idClient = inchiriere.get_id_client()
            idFilm = inchiriere.get_id_film()

            if(idClient == id1 and idFilm == id2):
                return inchiriere

    def service_sterge_inchiriere_idClient_idFilm(self , idClient, idFilm):

        self.__repo.sterge_inchiriere(idClient, idFilm)


