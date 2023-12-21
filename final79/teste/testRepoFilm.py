import unittest
from domain.domainFilm import Film
from repository.repoFilm import repoFilm

class TestFilm(unittest.TestCase):

    def test_film_initialization(self):
        film_id = 1
        titlu = "Inception"
        descriere = "A mind-bending movie"
        gen = "Sci-Fi"

        film = Film(film_id, titlu, descriere, gen)

        self.assertEqual(film.get_film_id(), film_id)
        self.assertEqual(film.get_titlu(), titlu)
        self.assertEqual(film.get_descriere(), descriere)
        self.assertEqual(film.get_gen(), gen)

    def test_setters(self):
        film = Film(1, "Inception", "A mind-bending movie", "Sci-Fi")

        new_id = 2
        new_titlu = "Interstellar"
        new_descriere = "Exploring space and time"
        new_gen = "Sci-Fi"

        film.set_film_id(new_id)
        film.set_titlu(new_titlu)
        film.set_descriere(new_descriere)
        film.set_gen(new_gen)

        self.assertEqual(film.get_film_id(), new_id)
        self.assertEqual(film.get_titlu(), new_titlu)
        self.assertEqual(film.get_descriere(), new_descriere)
        self.assertEqual(film.get_gen(), new_gen)

    def test_str_method(self):
        film = Film(1, "Inception", "A mind-bending movie", "Sci-Fi")
        expected_str = 'Filmul este Inception , genul este Sci-Fi , descrierea este : A mind-bending movie'

        self.assertEqual(str(film), expected_str)

class TestRepoFilm(unittest.TestCase):

    def test_adauga_film(self):
        repo = repoFilm()

        titlu = "Inception"
        descriere = "A mind-bending movie"
        gen = "Sci-Fi"

        repo.adauga_film(titlu, descriere, gen)

        films = repo.get_all_films()
        self.assertEqual(len(films), 1)

        added_film = films[0]
        self.assertEqual(added_film.get_titlu(), titlu)
        self.assertEqual(added_film.get_descriere(), descriere)
        self.assertEqual(added_film.get_gen(), gen)

    def test_sterge_film(self):
        repo = repoFilm()

        repo.adauga_film("Inception", "A mind-bending movie", "Sci-Fi")
        repo.adauga_film("Interstellar", "Exploring space and time", "Sci-Fi")

        repo.sterge_film(1)

        films = repo.get_all_films()
        self.assertEqual(len(films), 1)

        remaining_film = films[0]
        self.assertEqual(remaining_film.get_titlu(), "Interstellar")
        self.assertEqual(remaining_film.get_descriere(), "Exploring space and time")
        self.assertEqual(remaining_film.get_gen(), "Sci-Fi")

    def test_modifica_film(self):
        repo = repoFilm()

        repo.adauga_film("Inception", "A mind-bending movie", "Sci-Fi")
        repo.adauga_film("Interstellar", "Exploring space and time", "Sci-Fi")

        repo.modifica_film(1, "Memento", "A psychological thriller", "Thriller")

        films = repo.get_all_films()
        modified_film = films[0]

        self.assertEqual(modified_film.get_titlu(), "Memento")
        self.assertEqual(modified_film.get_descriere(), "A psychological thriller")
        self.assertEqual(modified_film.get_gen(), "Thriller")

    def test_search_film_by_id(self):
        repo = repoFilm()

        repo.adauga_film("Inception", "A mind-bending movie", "Sci-Fi")
        repo.adauga_film("Interstellar", "Exploring space and time", "Sci-Fi")

        film = repo.search_film_by_id(2)

        self.assertEqual(film.get_titlu(), "Interstellar")
        self.assertEqual(film.get_descriere(), "Exploring space and time")
        self.assertEqual(film.get_gen(), "Sci-Fi")

    def test_search_film_by_titlu(self):
        repo = repoFilm()

        repo.adauga_film("Inception", "A mind-bending movie", "Sci-Fi")
        repo.adauga_film("Interstellar", "Exploring space and time", "Sci-Fi")

        film = repo.search_film_by_titlu("Inception")

        self.assertEqual(film.get_film_id(), 1)
        self.assertEqual(film.get_descriere(), "A mind-bending movie")
        self.assertEqual(film.get_gen(), "Sci-Fi")

if __name__ == '__main__':
    unittest.main()
