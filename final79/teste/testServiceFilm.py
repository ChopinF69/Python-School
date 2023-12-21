import unittest
from domain.domainFilm import Film
from service.serviceFilm import filmService
from domain.studentDTO import studentDTO
class TestFilmService(unittest.TestCase):

    def setUp(self):
        self.film_service = filmService()

    def test_service_adauga_film(self):
        titlu = "Inception"
        gen = "Sci-Fi"
        descriere = "A mind-bending journey into the world of dreams."

        added_film = self.film_service.service_adauga_film(titlu, gen, descriere)

        self.assertEqual(added_film.get_titlu(), titlu)
        self.assertEqual(added_film.get_gen(), gen)
        self.assertEqual(added_film.get_descriere(), descriere)

        all_films = self.film_service.service_get_all_films()
        self.assertIn(added_film, all_films)

    def test_service_sterge_film(self):
        titlu = "Inception"
        gen = "Sci-Fi"
        descriere = "A mind-bending journey into the world of dreams."

        added_film = self.film_service.service_adauga_film(titlu, gen, descriere)
        film_id = added_film.get_film_id()

        self.film_service.service_sterge_film(film_id)

        all_films = self.film_service.service_get_all_films()
        self.assertNotIn(added_film, all_films)

    def test_service_modifica_film(self):
        titlu = "Inception"
        gen = "Sci-Fi"
        descriere = "A mind-bending journey into the world of dreams."

        added_film = self.film_service.service_adauga_film(titlu, gen, descriere)
        film_id = added_film.get_film_id()

        new_titlu = "Interstellar"
        new_gen = "Sci-Fi"
        new_descriere = "Exploring space and time."

        modified_film = self.film_service.service_modifica_film(film_id, new_titlu, new_descriere, new_gen)

        self.assertEqual(modified_film.get_titlu(), new_titlu)
        self.assertEqual(modified_film.get_gen(), new_gen)
        self.assertEqual(modified_film.get_descriere(), new_descriere)

    def test_service_search_film_by_id(self):
        titlu = "Inception"
        gen = "Sci-Fi"
        descriere = "A mind-bending journey into the world of dreams."

        added_film = self.film_service.service_adauga_film(titlu, gen, descriere)
        film_id = added_film.get_film_id()

        found_film = self.film_service.service_search_film_by_id(film_id)

        self.assertEqual(found_film, added_film)

    def test_service_search_film_by_titlu(self):
        titlu = "Inception"
        gen = "Sci-Fi"
        descriere = "A mind-bending journey into the world of dreams."

        added_film = self.film_service.service_adauga_film(titlu, gen, descriere)

        found_film = self.film_service.service_search_film_by_titlu(titlu)

        self.assertEqual(found_film, added_film)

    def test_service_get_all_films(self):
        titlu1 = "Inception"
        gen1 = "Sci-Fi"
        descriere1 = "A mind-bending journey into the world of dreams."

        titlu2 = "Interstellar"
        gen2 = "Sci-Fi"
        descriere2 = "Exploring space and time."

        self.film_service.service_adauga_film(titlu1, gen1, descriere1)
        self.film_service.service_adauga_film(titlu2, gen2, descriere2)

        all_films = self.film_service.service_get_all_films()

        self.assertEqual(len(all_films), 2)

if __name__ == '__main__':
    unittest.main()
