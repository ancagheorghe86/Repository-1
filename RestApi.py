'''HTTP. Rest APIs. Requests
Folosim Simple Books API, descris aici : https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md
Toata rezolvarea se va face într-o clasa numita Books API Client. Pentru testare se va crea un obiect din aceasta clasa și se vor apela metodele implementate.
1. Folosind endpoint-ul de authentication, genereaza un access token (fa asta in constructor, client name si email ar trebui sa fie atribute).
2. Adaugă o metoda prin care poți vedea toate comenzile.
3. Adaugă o metoda prin care poți vedea toate cărțile.
4. Adaugă o metoda prin care poți posta o comanda.
5. Adaugă o metoda prin care poți șterge o comanda.
'''

import requests
import json

class BooksApiClient:
    base_url = "https://simple-books-api.glitch.me"

    def __init__(self, name, email, token=""):
        self.name = name
        self.email = email
        self.token = token
        if self.token == "":
            self.token = self.__authenticate()

    def __authenticate(self):
        url = f"{self.base_url}/api-clients"
        body = {
            "clientName": self.name,
            "clientEmail": self.email
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url=url, headers=headers, data=json.dumps(body))
        print(response.json())
        return response.json()['accessToken']

    def get_orders(self):
        # get request base_url + "orders"
        url = f"{self.base_url}/orders"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url=url, headers=headers)

        return response.json()

    def get_books(self):
        # get request catre base_url + "books
        pass

    def submit_order(self, book_id):
        pass

    def delete_order(self, order_id):
        pass


client = BooksApiClient(
    name ="dandan2",
    email ="dandan2@gmail.com",
    token = "74994aac6580358f5b7d71ca5972447f5b47b4c80ee5bfea91b52877e29171e7"
)


print(client.get_orders())