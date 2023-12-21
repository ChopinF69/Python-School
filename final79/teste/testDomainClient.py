import unittest
from domain.domainClient import Client

class TestClient(unittest.TestCase):

    def test_client_initialization(self):
        client_id = 1
        nume = "John Doe"
        cnp = 1234567890

        client = Client(client_id, nume, cnp)

        self.assertEqual(client.get_client_id(), client_id)
        self.assertEqual(client.get_nume(), nume)
        self.assertEqual(client.get_cnp(), cnp)
        #mai adauga teste pentru setteri
        client_id = 2
        nume = "Jane Doe"
        cnp = 9876543210
        client = Client(client_id, nume, cnp)
        self.assertEqual(client.get_client_id(), client_id)
        self.assertEqual(client.get_nume(), nume)
        self.assertEqual(client.get_cnp(), cnp)

        #generate another test like the last one
        client_id = 3
        nume = "John Doe"
        cnp = 1234567890
        client = Client(client_id, nume, cnp)
        self.assertEqual(client.get_client_id(), client_id)
        self.assertEqual(client.get_nume(), nume)

        client_id = 4
        nume = "Jane Doe"
        cnp = 9876543210
        client = Client(client_id, nume, cnp)
        self.assertEqual(client.get_client_id(), client_id)
        self.assertEqual(client.get_nume(), nume)


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

if __name__ == '__main__':
    unittest.main()
