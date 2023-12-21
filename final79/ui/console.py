
class Console:

    def __init__(self):
        pass
    #filme: <id>,<titlu>,<descriere>,<gen>
    @staticmethod
    def UI_get_film():
        '''
        :return: (titlu , descriere , gen)
        '''
        titlu = (input)("Ce nume va avea filmul ? ")
        descriere = (input)("Ce descriere are filmul ? ")
        gen = (input)("Ce gen are filmul ? ")

        return (titlu , descriere , gen)

    # clienți: <id>, <nume>, <CNP>
    @staticmethod
    def UI_get_client():
        '''
        Functia va returna atributele unui client
        :return: (nume , CNP)
        '''
        nume = (input)("Ce nume va avea clientul ? ")
        CNP = (input)("Ce cnp va avea clientul ? ")

        return (nume , CNP)

    @staticmethod
    def UI_alege_optiune():
        '''
        Functia va returna optiunea data de utilizator
        :return: STRING optiune
        '''
        optiune = (input)("Ce optiune alegi ? ")
        return (int)(optiune)

    @staticmethod
    def UI_afiseaza_meniu():
        print("1 . Iesi din program !")
        print("2 . ISTVAN")
        print("3 . Afiseaza optiuni")
        print("4 . Adauga client")
        print("5 . Adauga film")
        print("6 . Afiseaza toti clientii")
        print("7 . Afiseaza toate filmele")
        print("8 . Sterge un client")
        print("9 . Sterge un film")
        print("10 . Modifica un client")
        print("11 . Modifica un film")
        print("12 . Afiseaza tot despre clientul cu numele dat")
        print("13 . Afiseaza tot despre filmul cu titlul dat")
        print("14 . Realizeaza inchiriere")
        print("15 . Afiseaza toate inchirierile")
        print("16 . Returneaza un film")
        print("17 . Afiseaza nume client + numar filme")
        print("18 . Afiseaza nume film + de cate ori apare")
        print("19 . Updateaza fisierul cu clienti")
        print("20 . Updateaza fisierul cu filme")
        print("21 . Obtine lista clienti din fisierul --clienti")
        print("22 . Obtine lista filme din fisierul --filme")
        print("23 . Obtine top 5 filme inchiriate de barbati")
    @staticmethod
    def UI_get_client_id_ui() -> int:
        '''
        @no positional params taken
        @returns INT , the CLIENT s id
        '''
        id = (input)("La ce id vrei sa faci operatie la un client ? ")
        id = (int)(id)
        return id

    @staticmethod
    def UI_get_film_id_ui() -> int:
        '''
        @no positional params taken
        @returns INT , the FILM s id
        '''
        id = (input)("La ce id vrei sa faci operatie la un film ? ")
        id = (int)(id)
        return id

    @staticmethod
    def UI_get_client_nume():
        '''
        @no positional params taken
        @return STRING , the name of the CLIENT
        '''
        nume = input("Ce nume are clientul ? ")
        return nume

    @staticmethod
    def UI_get_client_cnp():
        '''
        @no positional arguments
        @return INT , the cnp of the CLIENT
        '''
        cnp = input("Ce cnp are clientul ? ")
        cnp = (int)(cnp)
        return cnp

    @staticmethod
    def UI_get_film_titlu():
        '''
        @no positional arguments
        @return STRING , the title of the FILM
        '''
        nume = input("Ce titlu are filmul ? ")
        return nume

    @staticmethod
    def UI_get_film_descriere():
        '''

        :return: descriere noua de film
        '''
        descriere = input("Ce descriere sa aiba filmul ? ")
        return descriere
    @staticmethod
    def UI_get_film_gen():
        '''

        :return: gen nou de film
        '''
        gen = input("Ce gen vrei sa aiba filmul ? ")
        return gen

    @staticmethod
    def UI_get_inchiriere():
        #vreau sa obtin la ce client sa adaug si ce film sa adaug
        numeClient = input("Ce nume are clientul care vrea sa inchirieze?")
        titluFilm = input("Ce titlu are filmul pe care clientul vrea sa il inchirieze ? ")

        return numeClient, titluFilm

    @staticmethod
    def UI_nu_exista_client(nume):
        '''
        In caz ca nu exista client functie de afisare a erorii
        :param nume: STRING
        :return: VOID print
        '''
        print(f"Nu existe clientul cu numele{nume}")

    @staticmethod
    def UI_nu_exista_film(titlu):
        '''
        In caz ca nu exista film functie de afisare a erorii
        :param titlu: STRING
        :return: VOID print
        '''
        print(f"Nu exista filmul {titlu}")

