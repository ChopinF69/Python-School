
class Client:
    def __init__(self, client_id, nume, cnp):
        '''
        @param client_id : INT
        @param nume : STRING
        @param cnp : INT
        @returns : a new object CLIENT initialized
        '''
        
        self.__client_id = client_id
        self.__nume = nume
        self.__cnp = cnp
        
    def get_client_id(self):
        return self.__client_id

    def get_nume(self):
        return self.__nume
    def get_cnp(self):
        return self.__cnp
    
    def set_client_id(self, value):
        self.__client_id = value
    def set_nume(self, value):
        self.__nume = value
    def set_cnp(self, value):
        self.__cnp = value

    def __str__(self):
        return f'Numele clientului este {self.__nume} si CNP-ul este {self.__cnp}'

