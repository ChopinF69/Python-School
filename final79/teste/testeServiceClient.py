import unittest
from domain.domainClient import Client
from service.serviceClient import clientService

class TestClientService(unittest.TestCase):

    def setUp(self):
        self.client_service = clientService()

    def test_service_adauga_client(self):
        nume = "John Doe"
        cnp = 1234567890

        added_client = self.client_service.service_adauga_client(nume, cnp)

        self.assertEqual(added_client.get_nume(), nume)
        self.assertEqual(added_client.get_cnp(), cnp)

        all_clients = self.client_service.service_get_all_clients()
        self.assertIn(added_client, all_clients)

    def test_service_sterge_client(self):
        nume = "John Doe"
        cnp = 1234567890

        added_client = self.client_service.service_adauga_client(nume, cnp)
        client_id = added_client.get_client_id()

        self.client_service.service_sterge_client(client_id)

        all_clients = self.client_service.service_get_all_clients()
        self.assertNotIn(added_client, all_clients)

    def test_service_modifica_client(self):
        nume = "John Doe"
        cnp = 1234567890

        added_client = self.client_service.service_adauga_client(nume, cnp)
        client_id = added_client.get_client_id()

        new_nume = "Jane Doe"
        new_cnp = 9876543210

        modified_client = self.client_service.service_modifica_client(client_id, new_nume, new_cnp)

        self.assertEqual(modified_client.get_nume(), new_nume)
        self.assertEqual(modified_client.get_cnp(), new_cnp)

    def test_service_search_client_by_id(self):
        nume = "John Doe"
        cnp = 1234567890

        added_client = self.client_service.service_adauga_client(nume, cnp)
        client_id = added_client.get_client_id()

        found_client = self.client_service.service_search_client_by_id(client_id)

        self.assertEqual(found_client, added_client)

    def test_service_search_client_by_nume(self):
        nume = "John Doe"
        cnp = 1234567890

        added_client = self.client_service.service_adauga_client(nume, cnp)

        found_client = self.client_service.service_search_client_by_nume(nume)

        self.assertEqual(found_client, added_client)

    def test_service_search_client_by_cnp(self):
        nume = "John Doe"
        cnp = 1234567890

        added_client = self.client_service.service_adauga_client(nume, cnp)

        found_client = self.client_service.service_search_client_by_cnp(cnp)

        self.assertEqual(found_client, added_client)

    def test_service_get_all_clients(self):
        nume1 = "John Doe"
        cnp1 = 1234567890
        nume2 = "Jane Doe"
        cnp2 = 9876543210

        self.client_service.service_adauga_client(nume1, cnp1)
        self.client_service.service_adauga_client(nume2, cnp2)

        all_clients = self.client_service.service_get_all_clients()

        self.assertEqual(len(all_clients), 2)

if __name__ == '__main__':
    unittest.main()
