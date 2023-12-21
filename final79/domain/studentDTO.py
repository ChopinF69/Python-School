from domain.domainClient import Client
from repository.repoClient import repoClient
from repository.repoInchirieri import repoInchirieri

class studentDTO(repoClient , repoInchirieri):
    def __init__(self):
        self.__numarFilme = []

    def get_lista_numar_filme(self):
        return self.__numarFilme

    #ar trebui sa avem aici ceva de genu : nume - numar de filme

    def obtine_numar_filme_dupa_nume(self):

        dict = []
        #listaInchirieri = self.__repoInchirieri.get_all_inchirieri()
        listaInchirieri = self.get_all_inchirieri()
        #listaClienti = self.__repoClient.get_all_clients()
        listaClienti = self.get_all_clients()
        print(listaClienti)
        for client in listaClienti:
            id_client = client.get_client_id()
            nume_client = client.get_nume()
            print(nume_client)
            dict[nume_client] = 0
            #ne voim uita in lista de inchirieri si vom vedea cate inchirieri sunt cu id_client
            for inchirieri in listaInchirieri:
                id_client_inchiriere = inchirieri.get_idClient()
                if id_client == id_client_inchiriere:
                    #
                    dict[nume_client] += 1
        self.__numarFilme = dict
        return dict


