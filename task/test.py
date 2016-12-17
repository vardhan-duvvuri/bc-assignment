from django.test import TestCase


class TestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_logout(self):
        resp = self.client.get('/logout/')
        self.assertEqual(resp.status_code, 302)

    def test_addcart(self):
        resp = self.client.get('/add/1')
        print(resp.status_code)
        self.assertEqual(resp.status_code, 200)

    def test_deletecart(self):
        resp = self.client.get('/delete/1')
        print(resp.status_code)
        self.assertEqual(resp.status_code, 200)

    def test_view(self):
        resp = self.client.get('/view/')
        print(resp.status_code)
        self.assertEqual(resp.status_code, 200)

    def test_order(self):
        resp = self.client.get('/order/')
        print(resp.status_code)
        self.assertEqual(resp.status_code, 200)

    def test_show_orders(self):
        resp = self.client.get('/show_orders/')
        print(resp.status_code)
        self.assertEqual(resp.status_code, 200)