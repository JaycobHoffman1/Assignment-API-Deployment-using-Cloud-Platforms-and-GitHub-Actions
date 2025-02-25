import unittest
from app import app
import json

class TestSum(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_negative_sum(self):
        payload = { 'num1': -1, 'num2': -5 }
        response = self.app.post('/sum', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], -6)

    def test_all_results(self, id):
        response = self.app.get(f'/sum/results/{id}')
        self.assertEqual(response.status_code, 404) # Invalid test result

if __name__ == '__main__':
    unittest.main()