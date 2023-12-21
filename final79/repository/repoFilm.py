from domain import *

class repoFilm():
    def __init__(self):
        self.__lista_filme = []
        self.__id = 0

    def set_lista_filme(self , lista_filme):
        self.__lista_filme = lista_filme
    def adauga_film(self , titlu , descriere ,gen):
        '''
        Adaugam un nou film
        @param : new_film FILM
        @return : VOID type function
        '''
        self.__id += 1
        filmNou = Film(self.__id , titlu , descriere , gen)

        self.__lista_filme.append(filmNou)

    def sterge_film(self , id):
        '''
        Functia va sterge un film in repo
        :param id: INT
        :return: VOID
        '''
        new_film_list = []
        for film in self.__lista_filme:
            if film.get_film_id() != id:
                new_film_list.append(film)

        self.__lista_filme = new_film_list

    def modifica_film(self , id , titlu_nou , descriere_noua , gen_nou):
        '''

        @param id: INT
        @param titlu_nou: STRING
        @param descriere_noua: STRING
        @param gen_nou: STRING
        @return: VOID
        '''

        new_movie_list = []
        for film in self.__lista_filme:
            if id == film.get_film_id():
                film.set_titlu(titlu_nou)
                film.set_gen(gen_nou)
                film.set_titlu(titlu_nou)
                film.set_descriere(descriere_noua)

            new_movie_list.append(film)

        self.__lista_filme = new_movie_list

    def search_film_by_id(self , id):
        '''
        Functia va returna un FILM pe baza id-ului
        :param id: INT
        :return: FILM
        '''
        for film in self.__lista_filme:
            if(film.get_film_id() == id):
                return film
        return 0

    def search_film_by_titlu(self , titlu):
        '''
        Functia va returna un film pe baza titlului
        :param titlu: STRING
        :return: VOID
        '''
        for film in self.__lista_filme:
            if(film.get_titlu() == titlu):
                return film
        return 0

    def get_all_films(self):
        '''
        Functia va returna toate filmele din repo
        :return: LIST FILME
        '''
        return self.__lista_filme

    def __save_all_films_to_file(self , filename):
        '''
        Salveaza toate filmele intr-un fisier
        :param filename: numele fisierului
        :return: VOID
        '''
        with open(filename , "w") as f:
            for film in self.__lista_filme:
                value = f"{film.get_film_id()};{film.get_titlu()};{film.get_descriere()};{film.get_gen()}\n"
                f.write(value)

    def save__all_films_to_file(self , filename):
        '''
        Salveaza toate filmele intr-un fisier public
        :param filename: numele fisierului
        :return: VOID
        '''

        self.__save_all_films_to_file(filename)