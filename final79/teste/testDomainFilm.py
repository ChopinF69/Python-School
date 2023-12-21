import unittest
from domain.domainFilm import Film

class TestFilm(unittest.TestCase):

    def test_film_initialization(self):
        film_id = 1
        titlu = "Inception"
        descriere = "A mind-bending thriller"
        gen = "Sci-Fi"

        film = Film(film_id, titlu, descriere, gen)

        self.assertEqual(film.get_film_id(), film_id)
        self.assertEqual(film.get_titlu(), titlu)
        self.assertEqual(film.get_descriere(), descriere)
        self.assertEqual(film.get_gen(), gen)

    def test_setters(self):
        film = Film(1, "Inception", "A mind-bending thriller", "Sci-Fi")

        new_id = 2
        new_titlu = "Interstellar"
        new_descriere = "A space epic"
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
        film = Film(1, "Inception", "A mind-bending thriller", "Sci-Fi")
        expected_str = 'Filmul este Inception , genul este Sci-Fi , descrierea este : A mind-bending thriller'

        self.assertEqual(str(film), expected_str)

if __name__ == '__main__':
    unittest.main()
