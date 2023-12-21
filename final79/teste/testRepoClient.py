import unittest
from domain.domainClient import Client
from repository.repoClient import repoClient

class TestClient(unittest.TestCase):

    def test_client_initialization(self):
        client_id = 1
        nume = "John Doe"
        cnp = 1234567890

        client = Client(client_id, nume, cnp)

        self.assertEqual(client.get_client_id(), client_id)
        self.assertEqual(client.get_nume(), nume)
        self.assertEqual(client.get_cnp(), cnp)

    def test_setters(self):
        client = Client(1, "John Doe", 1234567890)

        new_id = 2
        new_nume = "Jane Doe"
        new_cnp = 9876543210

        client.set_client_id(new_id)
        client.set_nume(new_nume)
        client.set_cnp(new_cnp)

        self.assertEqual(client.get_client_id(), new_id)
        self.assertEqual(client.get_nume(), new_nume)
        self.assertEqual(client.get_cnp(), new_cnp)

    def test_str_method(self):
        client = Client(1, "John Doe", 1234567890)
        expected_str = 'Numele clientului este John Doe si CNP-ul este 1234567890'

        self.assertEqual(str(client), expected_str)

class TestRepoClient(unittest.TestCase):

    def test_adauga_client(self):
        repo = repoClient()

        nume = "John Doe"
        cnp = 1234567890

        repo.adauga_client(nume, cnp)

        clients = repo.get_all_clients()
        self.assertEqual(len(clients), 1)

        added_client = clients[0]
        self.assertEqual(added_client.get_nume(), nume)
        self.assertEqual(added_client.get_cnp(), cnp)

    def test_sterge_client(self):
        repo = repoClient()

        repo.adauga_client("John Doe", 1234567890)
        repo.adauga_client("Jane Doe", 9876543210)

        repo.sterge_client(1)

        clients = repo.get_all_clients()
        self.assertEqual(len(clients), 1)

        remaining_client = clients[0]
        self.assertEqual(remaining_client.get_nume(), "Jane Doe")
        self.assertEqual(remaining_client.get_cnp(), 9876543210)

    def test_modifica_client(self):
        repo = repoClient()

        repo.adauga_client("John Doe", 1234567890)
        repo.adauga_client("Jane Doe", 9876543210)

        repo.modifica_client(1, "Jack Doe", 5555555555)

        clients = repo.get_all_clients()
        modified_client = clients[0]

        self.assertEqual(modified_client.get_nume(), "Jack Doe")
        self.assertEqual(modified_client.get_cnp(), 5555555555)

    def test_search_client_by_id(self):
        repo = repoClient()

        repo.adauga_client("John Doe", 1234567890)
        repo.adauga_client("Jane Doe", 9876543210)

        client = repo.search_client_by_id(2)

        self.assertEqual(client.get_nume(), "Jane Doe")
        self.assertEqual(client.get_cnp(), 9876543210)

    def test_search_client_by_nume(self):
        repo = repoClient()

        repo.adauga_client("John Doe", 1234567890)
        repo.adauga_client("Jane Doe", 9876543210)

        client = repo.search_client_by_nume("John Doe")

        self.assertEqual(client.get_client_id(), 1)
        self.assertEqual(client.get_cnp(), 1234567890)

    def test_search_client_by_cnp(self):
        repo = repoClient()

        repo.adauga_client("John Doe", 1234567890)
        repo.adauga_client("Jane Doe", 9876543210)

        client = repo.search_client_by_cnp(9876543210)

        self.assertEqual(client.get_client_id(), 2)
        self.assertEqual(client.get_nume(), "Jane Doe")

if __name__ == '__main__':
    unittest.main()
