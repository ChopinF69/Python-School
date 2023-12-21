from domain.domainFilm import *
from domain.domainClient import *


class filmValidator:

    def validate_film(self, film):
        errors = []
        if film.get_titlu() == "":
            errors.append("Titulul nu poate fi valid")
        if film.get_gen() == "":
            errors.append("Genul nu poate fi gol")
        if film.get_descriere() == "":
            errors.append("Descrierea nu poate fi vida")
        if len(film.get_descriere()) > 100:
            errors.append("Descrierea este prea lunga")

        if(len(errors) > 0):
            error_string = '\n'.join(errors)
            raise ValueError(error_string)

class clientValidator:

    def validate_client(self, client):
        erorrs = []
        if client.get_cnp() == "":
            erorrs.append("CNP-ul nu poate fi vid")
        if client.get_nume() == "":
            erorrs.append("Numele nu poate fi vid")
        if len(client.get_nume()) > 10:
            erorrs.append("Numele nu poate fi mai lung de 10 caractere")
        if len(str(client.get_cnp())) > 10:  # Convert to string before checking length
            erorrs.append("CNP-ul nu poate avea mai mult de 10 cifre")

        if len(erorrs) > 0:
            error_string = '\n'.join(erorrs)
            raise ValueError(error_string)