import unittest
from main import create_app, db
from models.Menu import Menu

class TestMenu(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_menu_index(self):
        response = self.client.get("/menu/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_menu_create(self):
        response = self.client.post("/menu/", json={"title": "noodles", "price": 20, "vegetarian": True})
        
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertTrue(bool("id" in data.keys()))
        
        menu = Menu.query.get(data["id"])
        self.assertIsNotNone(menu)

    def test_menu_show(self):
        menu = Menu.query.first()

        response = self.client.get(f"/menu/{menu.id}", )
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    # def test_menu_update(self):
    #     menu = Menu.query.first()
    #     print(menu.title)

    #     response = self.client.post(f"/menu/{menu.id}", json={"title": "apple"})
    #     print(menu.title)
    #     data = response.get_json()

    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsInstance(data, dict)
    
    def test_menu_delete(self):
        menu = Menu.query.first()
        
        response = self.client.delete(f"/menu/{menu.id}")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        menu = Menu.query.get(menu.id)
        self.assertIsNone(menu)