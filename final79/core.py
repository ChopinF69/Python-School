from domain import *
from repository.repoClient import repoClient
from repository.repoFilm import repoFilm
from repository.repoInchirieri import repoInchirieri



from service.serviceClient import clientService
from service.serviceFilm import filmService
from service.serviceInchirieri import inchirieriService

from domain.domainInchirieri import Inchirieri
from domain.domainClient import Client
from domain.domainFilm import Film
from domain.validator import clientValidator , filmValidator
from domain.studentDTO import studentDTO


from ui.console import Console

def ISTVAN():
    print(f"||   _____    _______   ||           ||         || ||        ||||    ||")
    print(f"    / ____|  |__   __|   ||         ||         ||   ||       || ||   ||")
    print(f"||  | |         | |       ||       ||         ||     ||      ||  ||  ||")
    print(f"||  | |         | |        ||     ||         ||       ||     ||   || ||")
    print(f'||  \\\____      | |         ||   ||         ||---------||    ||    ||||')
    print(f"||      \\ |     | |          || ||         ||           ||   ||     |||")
    print(f"||  ____/ |     | |           |||         ||             ||  ||      ||")
    print()
    print()
ISTVAN()
#---------------------------------------------------------------
Consola = Console()

repoitoryClient = repoClient()
repositoryFilm = repoFilm()
repositoryInchirieri = repoInchirieri()


serviceClient = clientService()
serviceFilm = filmService()
serviceInchirieri = inchirieriService()

studentDTO = studentDTO()

#---------------------------------------------------------------
Consola.UI_afiseaza_meniu()
def main():
    print("Salut ! Proiectul meu , va urmea sa vezi optiunile")
    while True:
        optiune = Consola.UI_alege_optiune()
        if type(optiune) == str:
            print("Vous n'avez pas")

        if optiune == 1:
            exit()

        elif optiune == 2:
            ISTVAN()

        elif optiune == 3:
            Consola.UI_afiseaza_meniu()

        elif optiune == 4:
            clientNou = Consola.UI_get_client()
            nume = clientNou[0]
            cnp = clientNou[1]

            clientNou = serviceClient.service_adauga_client(nume , cnp)

        elif optiune == 5:
            filmNou = Consola.UI_get_film()
            titlu = filmNou[0]
            descriere = filmNou[1]
            gen = filmNou[2]

            filmNou = serviceFilm.service_adauga_film(titlu , descriere , gen)

        elif optiune == 6:
            listaClienti = serviceClient.service_get_all_clients()

            for client in listaClienti:
                print(str(client))

        elif optiune == 7:
            listaFilme = serviceFilm.service_get_all_films()

            for film in listaFilme:
                print(str(film))

        elif optiune == 8:
            #sterge un client
            nume = Consola.UI_get_client_nume()
            client = serviceClient.service_search_client_by_nume(nume)
            idClient = client.get_client_id()
            serviceClient.service_sterge_client(idClient)

        elif optiune == 9:
            #sterge un film
            titlu = Consola.UI_get_film_titlu()
            film = serviceFilm.service_search_film_by_titlu(titlu)
            idFilm = film.get_film_id()
            serviceFilm.service_sterge_film(idFilm)

        elif optiune == 10:
            #modifica un client
            nume = Consola.UI_get_client_nume()
            cnp = Consola.UI_get_client_cnp()
            client = serviceClient.service_search_client_by_nume(nume)
            idClient = client.get_client_id()

            clientNou = serviceClient.service_modifica_client(idClient , nume , cnp)

        elif optiune == 11:
            #modifica un film
            titlu = Consola.UI_get_film_titlu()
            descriere = Consola.UI_get_film_descriere()
            gen = Consola.UI_get_film_gen()

            film = serviceFilm.service_search_film_by_titlu(titlu)
            idFilm = film.get_film_id()

            filmNou = serviceFilm.service_modifica_film(idFilm , titlu , descriere , gen)

        elif optiune == 12:
            #afisam tot despre un client pe baza numelui dat
            nume = Consola.UI_get_client_nume()
            client = serviceClient.service_search_client_by_nume(nume)
            print(str(client))

        elif optiune == 13:
            #afisam tot despre un film pe baza titlului dat
            titlu = Consola.UI_get_film_titlu()
            film = serviceFilm.service_search_film_by_titlu(titlu)
            print(str(film))

        elif optiune == 14:
            #sa adaugam o inchirere
            numeClient = Consola.UI_get_client_nume()
            client = serviceClient.service_search_client_by_nume(numeClient)
            clientId = client.get_client_id()
            if clientId == 0:
                Consola.UI_nu_exista_client(numeClient)

            titluFilm = Consola.UI_get_film_titlu()
            film = serviceFilm.service_search_film_by_titlu(titluFilm)
            filmId = film.get_film_id()
            if filmId == 0:
                Consola.UI_nu_exista_client(titluFilm)

            if clientId != 0 and filmId != 0:
                inchiriereNoua = serviceInchirieri.service_adauga_inchiriere(clientId , filmId)

        elif optiune == 15:
            #afisam toate inchirierile

            listaInchireri = serviceInchirieri.service_get_all_inchirieri()
            if len(listaInchireri) > 0:
                for inchiriere in listaInchireri:
                    idClient = inchiriere.get_idClient()
                    idFilm = inchiriere.get_idFilm()

                    #client = repoClient.search_client_by_id(idClient)
                    client = serviceClient.service_search_client_by_id(idClient)
                    #film = repoFilm.search_film_by_id(idFilm)
                    film = serviceFilm.service_search_film_by_id(idFilm)

                    print(str(client) + " cu " + str(film))
            else:
                print("Nu exista inchirieri ! ")

        elif optiune == 16:
            #returnam un film , avem nevoie de nume client si titlu film

            numeClient = Consola.UI_get_client_nume()
            titluFilm = Consola.UI_get_film_titlu()

            client = serviceClient.service_search_client_by_nume(numeClient)
            film = serviceFilm.service_search_film_by_titlu(titluFilm)

            clientId = client.get_client_id()
            filmId = film.get_film_id()

            serviceInchirieri.service_sterge_inchiriere_idClient_idFilm(clientId, filmId)


        elif optiune == 17:

            listaClienti = serviceClient.service_get_all_clients()

            listaInchirieri = serviceInchirieri.service_get_all_inchirieri()

            result_dict = {}

            for client in listaClienti:

                id_client = client.get_client_id()

                nume = client.get_nume()

                cnt = 0

                for inchiriere in listaInchirieri:

                    id_client_inchiriere = inchiriere.get_idClient()

                    if id_client_inchiriere == id_client:
                        cnt += 1

                result_dict[nume] = cnt
            sorted_result = dict(sorted(result_dict.items(), key=lambda item: item[1], reverse=True))
            for nume_client, cnt in sorted_result.items():
                print(f"Clientul {nume_client} a efectuat {cnt} inchirieri.")

        elif optiune == 18:

            listaFilme = serviceFilm.service_get_all_films()

            listaInchirieri = serviceInchirieri.service_get_all_inchirieri()

            result_dict = {}

            for filme in listaFilme:

                id_film = filme.get_film_id()
                titlu = filme.get_titlu()
                cnt = 0
                for inchiriere in listaInchirieri:
                    id_inchiriere_film = inchiriere.get_idFilm()

                    if id_inchiriere_film == id_film:
                        cnt += 1

                result_dict[titlu] = cnt

            sorted_result = dict(sorted(result_dict.items() , key=lambda item : item[1] , reverse=True))

            for titlu_film , cnt in sorted_result.items():
                print(f"Filmul {titlu_film} a fost inchiriat de {cnt} ori")

        elif optiune == 19:
            #salveaza in fisier clientii
            #repoitoryClient.save__all_clients_to_file("clienti")

            serviceClient.service_aduga_lista_clienti_fisier("clienti")


        elif optiune == 20:
            serviceFilm.service_aduga_lista_filme_fisier("filme")


        elif optiune == 21:
            #obtinem lista de clienti din fisier si poate fi folosita mai departe
            lista_clienti_fisier = serviceClient.service_obtine_lista_clienti_fisier("clienti")
            serviceClient.service_set_clienti_din_fisier(lista_clienti_fisier)

        elif optiune == 22:
            lista_filme_fisier = serviceFilm.service_obtine_lista_clienti_fisier("filme")
            serviceFilm.service_set_filme_din_fisier(lista_filme_fisier)

        elif optiune == 23:
            '''
            Top 5 filme inchiriate de barbati , adica daca prima cifra a cnp-ului este impara
            '''
            dict_top5_filme = {}
            lista_clienti = serviceClient.service_get_all_clients() # lista clienti
            lista_inchirieri = serviceInchirieri.service_get_all_inchirieri() # lista inchirieri
            for inchiriere in lista_inchirieri:
                id_film = inchiriere.get_idFilm()
                dict_top5_filme[id_film] = 0

            for inchiriere in lista_inchirieri:
                id_client_inchiriere = inchiriere.get_idClient()
                client = serviceClient.service_search_client_by_id(id_client_inchiriere)
                cnp_client = client.get_cnp()
                id_film_inchiriere = inchiriere.get_idFilm()



                while cnp_client > 9:#ajungem la prima cifra
                    cnp_client = cnp_client / 10
                #print(id_client_inchiriere)
                cnp_client = (int)(cnp_client)
                print(cnp_client)
                if cnp_client % 2 == 1: # daca cnp-ul este la un barbat
                    dict_top5_filme[id_film_inchiriere] += 1

            print(dict_top5_filme)
            result_dict = dict(sorted(dict_top5_filme.items() , key=lambda item : item[1], reverse=True))
            index = 0
            for id_film , contor  in result_dict.items():
                film = serviceFilm.service_search_film_by_id(id_film)
                nume_film = film.get_titlu()
                if contor != 0 and index < 2:
                    index += 1
                    print(f"Id : {id_film} , nume film : {nume_film} , contor : {contor}")

if __name__ == "__main__":
    main()






