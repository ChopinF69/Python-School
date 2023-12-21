from domain.domainClient import Client
from domain.validator import clientValidator
from repository.repoClient import repoClient
from utils.utils import *

class clientService:
    def __init__(self):
        '''
        Initializam service-ul cu obiectul REPO si Validator
        '''
        self.__repo = repoClient()
        self.__validator = clientValidator()

    def service_adauga_client(self , nume , cnp):
        '''
        Insereaza un client in repo
        :param nume: STRING
        :param cnp: INT
        :return: film nou adaugat
        :raises ValueError pentru date invalida
        '''

        clientNou = Client(1 , nume , cnp)
        self.__validator.validate_client(clientNou)
        self.__repo.adauga_client(nume , cnp)

        return clientNou
     
    def service_sterge_client(self , id):
        '''
        Functi sterge din repo un client pe baza id-ului
        :param id: INT
        :return: VOID clientul va fi sters
        '''
        self.__repo.sterge_client(id)

    def service_modifica_client(self , id , nume , cnp):
        '''
        Functia modifica un client din repo pe baza id-ului
        :param id: INT
        :param nume: STRING
        :param cnp: INT
        :return: VOID
        '''

        clientNou = Client(1 , nume , cnp)
        self.__validator.validate_client(clientNou)
        self.__repo.modifica_client(id , nume , cnp)

        return clientNou

    def service_search_client_by_id(self , id):
        '''
        Functia va returna Clientul pe baza id-ului
        :param id: INT
        :return: CLIENT
        '''
        clientNou = self.__repo.search_client_by_id(id)
        return clientNou

    def service_search_client_by_nume(self , nume):
        '''
        Functia va returna din repo un client pe baza numelui
        :param nume: STRING
        :return: CLIENT
        '''
        clientNou = self.__repo.search_client_by_nume(nume)
        return clientNou

    def service_search_client_by_cnp(self , cnp):
        '''
        Functia va returna din repo un client pe baza cnp-ului
        :param cnp: INT
        :return: CLIENT
        '''
        clientNou = self.service_search_client_by_cnp(cnp)
        return clientNou

    def service_get_all_clients(self):
        '''
        Functia va returna din repo o lista cu toti clientii
        :return: LIST CLIENTi
        '''
        #return self.__repo.get_all_clients()
        l = self.__repo.get_all_clients()
        listaClienti = self.__repo.get_all_clients()
        return l

    def service_add_random_clients(self , number):
        '''
        Functia va adauga in repo un numar random de clienti
        :param nr: INT
        :return: VOID
        '''

        for _ in range(number):
            clientNou = Client(1 , generateRandomString(3) , generateRandomCnp(3))
            self.__validator.validate_client(clientNou)
            self.__repo.adauga_client(clientNou)

    def service_aduga_lista_clienti_fisier(self , path):
        '''
        Functia va adauga in repo lista de clienti din path
        :param path: FILE
        :return:
        '''
        listaClienti = self.__repo.get_all_clients()
        with open(path, "w") as f:
            for client in listaClienti:
                id = client.get_client_id()
                nume = client.get_nume()
                cnp = client.get_cnp()
                # Scrie detaliile clientului în fișier
                f.write(f"{id};{nume};{cnp}\n")
    def service_obtine_lista_clienti_fisier(self , path):
        '''
        Functia va obtine in repo lista de filme
        :param path: FILE
        :return:
        '''
        listaClienti = []
        with open(path, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() != "":
                    client_data = line.strip().split(';')
                    client_id = (int)(client_data[0])
                    nume = client_data[1]
                    cnp = (int)(client_data[2])
                    #client_id , nume , cnp = (client_data[0] , client_data[1] , client_data[2])
                    client = Client(client_id , nume , cnp)
                    listaClienti.append(client)
        return listaClienti

    def service_set_clienti_din_fisier(self , lista_clienti):
        '''
        Functia va seta lista de clienti obtinuta din fisier
        :param lista_clienti: LISTA DE CLIENTI DIN FISIER
        :return:
        '''
        self.__repo.set_lista_clienti(lista_clienti)