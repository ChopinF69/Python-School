class Film:
    def __init__(self, film_id, titlu, descriere, gen):
        '''
        @param film_id : INT
        @param titlu : STRING
        @param descriere : STRING
        @param gen : STRING
        @returns a new object FILM initialized 
        '''
        self.__film_id = film_id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen
    
    def get_film_id(self):
        return self.__film_id
    
    def get_titlu(self):
        return self.__titlu
    def get_descriere(self):
        return self.__descriere
    def get_gen(self):
        return self.__gen
    
    def set_film_id(self , value):
        self.__film_id = value
    def set_titlu(self, value):
        self.__titlu = value
    def set_descriere(self, value):
        self.__descriere = value
    def set_gen(self, value):
        self.__gen = value

    def __str__(self):
        return f'Filmul este {self.__titlu} , genul este {self.__gen} , descrierea este : {self.__descriere}'
