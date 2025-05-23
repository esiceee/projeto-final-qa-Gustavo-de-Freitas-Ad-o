import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = "https://jsonplaceholder.typicode.com"  # URL base da API de exemplo

    def test_get_posts(self):
        """Teste para verificar se a API retorna os posts corretamente."""
        response = requests.get(f"{self.BASE_URL}/posts")
        self.assertEqual(response.status_code, 200)  # Verifica se o status é 200 OK
        self.assertIsInstance(response.json(), list)  # Verifica se a resposta é uma lista
        self.assertGreater(len(response.json()), 0)  # Verifica se a lista não está vazia

    def test_get_post_by_id(self):
        """Teste para verificar se a API retorna um post específico."""
        post_id = 1
        response = requests.get(f"{self.BASE_URL}/posts/{post_id}")
        self.assertEqual(response.status_code, 200)  # Verifica se o status é 200 OK
        post = response.json()
        self.assertEqual(post['id'], post_id)  # Verifica se o ID do post é o esperado
        self.assertIn('title', post)  # Verifica se o post contém o campo 'title'

    def test_post_creation(self):
        """Teste para verificar se a API permite a criação de um novo post."""
        new_post = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = requests.post(f"{self.BASE_URL}/posts", json=new_post)
        self.assertEqual(response.status_code, 201)  # Verifica se o status é 201 Created
        created_post = response.json()
        self.assertEqual(created_post['title'], new_post['title'])  # Verifica se o título é o mesmo

if __name__ == '__main__':
    unittest.main()
