from domain.domainClient import Client

class repoClient():
    def __init__(self):
        self.__listaClienti = []
        self.__id = 0

    def set_lista_clienti(self , lista_clienti):
        self.__listaClienti = lista_clienti
    def adauga_client(self, nume , cnp):
        '''
        Functia va adauga un client in repo
        :param nume: STRING
        :param cnp: INT
        :return:
        '''
        self.__id += 1
        client = Client(self.__id , nume , cnp)
        self.__listaClienti.append(client)

    def sterge_client(self , clientId):
        '''
        @param clientId: INT and it represents the clientId
        @return: VOID type function
        '''
        clientId -= 1
        self.__listaClienti.pop(clientId)

    def modifica_client(self, id , new_name , new_cnp ):
        """
        Modifica datele unui client pe baza id-ului
        @param id: INT id-ul clientului de modificat
        @param new_name: STRING noul nume
        @param new_cnp:  INT noul cnp
        """
        new_clients_list=[]
        for customer in self.__listaClienti:
            if customer.get_client_id()== id:
                customer.set_nume(new_name)
                customer.set_cnp(new_cnp)
            new_clients_list.append(customer)
        self.__listaClienti = new_clients_list

    def search_client_by_id(self , id):
        '''
        Functia va returna un CLIENT pe baza id-ului
        :param id: INT
        :return: CLIENT
        '''
        for client in self.__listaClienti:
            if(client.get_client_id() == id):
                return client
        return 0

    def search_client_by_nume(self , nume):
        '''
        Functia va returna un CLIENT pe baza numelui
        :param nume: STRING
        :return: CLIENT
        '''
        for client in self.__listaClienti:
            if(client.get_nume() == nume):
                return client
        return 0

    def search_client_by_cnp(self , cnp):
        '''
        Functia va returna un CLIENT pe baza id-ului
        :param cnp: INT
        :return: CLIENT
        '''
        for client in self.__listaClienti:
            if(client.get_cnp() == cnp):
                return client
        return 0

    def get_all_clients(self):
        '''
        Functia va returna toti clientii
        :return: CLIENT LIST
        '''
        return self.__listaClienti

    def __save_all_clients_to_file(self , filename):
        '''
        Salveaza toti clientii intr-un fisier
        :param filename: numele fisierului
        :return: VOID
        '''
        with open(filename , "w") as f:
            for client in self.__listaClienti:
                value = f"{client.get_client_id()};{client.get_nume()};{client.get_cnp()}\n"
                f.write(value)

    def save__all_clients_to_file(self , filename):
        '''
        Salveaza toti clientii intr-un fisier public
        :param filename: numele fisierului
        :return: VOID
        '''

        self.__save_all_clients_to_file(filename)