from domain.domainFilm import Film
from domain.validator import filmValidator
from repository.repoFilm import repoFilm

class filmService:
    def __init__(self):
        '''
        Intializam service-ul de filme cu REPO si VALIDATOR
        '''
        self.__repo = repoFilm()
        self.__validator = filmValidator()

    def service_adauga_film(self , titlu , gen , descriere):
        '''
        Functia va adauga un film in repo
        :param titlu: STRING
        :param gen: STRING
        :param descriere: STRING
        :return: VOID
        :raises : ValueErrors daca produsul e invalid
        '''

        film = Film(1 , titlu ,descriere , gen)

        self.__validator.validate_film(film)
        self.__repo.adauga_film(titlu , descriere , gen)

        return film

    def service_sterge_film(self , id):
        '''
        Functia va sterge din repo un Film
        :param id: INT
        :return:
        '''

        self.__repo.sterge_film(id)

    def service_modifica_film(self , id , titlu , descriere, gen):
        '''
        Functia va modifica in repo un film
        :param id: INT
        :param titlu: STRING
        :param descriere: STRING
        :param gen: STRING
        :return: filmul modificat
        :raises : Value error daca filmul este invalid
        '''

        filmNou = Film(id , titlu , descriere , gen)
        self.__validator.validate_film(filmNou)
        self.__repo.modifica_film(id , titlu , descriere , gen)

        return filmNou

    def service_search_film_by_id(self , id):
        '''
        Functia va returna un Film pe baza id-ului
        :param id: INT
        :return: FILM
        '''

        film = self.__repo.search_film_by_id(id)
        return film

    def service_search_film_by_titlu(self, titlu):
        '''
        Functia va returna un Film pe baza titlului
        :param titlu: STRING
        :return: FILM
        '''

        film = self.__repo.search_film_by_titlu(titlu)
        return film

    def service_add_random_number_filme(self , number):
        pass

    def service_get_all_films(self):
        '''
        Getter pentru fime
        :return: LIST
        '''
        return self.__repo.get_all_films()

    def service_aduga_lista_filme_fisier(self, path):
        '''
        Functia va adauga in fisier de la lista de filme
        :param path: FILE
        :return: VOID
        '''
        #listaFilme = self.__repo.get_all_clients()
        listaFilme = self.__repo.get_all_films()
        with open(path, "w") as f:
            for film in listaFilme:
                id = film.get_film_id()
                titlu = film.get_titlu()
                descriere = film.get_descriere()
                gen = film.get_gen()
                # Scrie detaliile filmului în fișier
                f.write(f"{id};{titlu};{descriere};{gen}\n")

    def service_obtine_lista_clienti_fisier(self , path):
        '''
        Functia va obtine lista de clienti din fisier
        :param path: FILE
        :return: LIST
        '''
        listaFilme = []
        with open(path, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() != "":
                    film_data = line.strip().split(';')
                    film_id = (int)(film_data[0])
                    titlu = film_data[1]
                    descriere = film_data[2]
                    gen = film_data[3]
                    #film_id , titlu , descriere , gen = map(int , client_data[0] , client_data[1] , client_data[2] , client_data[3])
                    film = Film(film_id , titlu , descriere , gen)
                    listaFilme.append(film)
        return listaFilme




    def service_set_filme_din_fisier(self , lista_filme):
        self.__repo.set_lista_filme(lista_filme)