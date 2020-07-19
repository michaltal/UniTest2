from unittest import TestCase
from unittest.mock import patch
from Package1.Worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        print('setup')
        self.bob = Worker('Bob', 'Marshall', 1970, 7, 30, '2 Dizengof, Tel Aviv', 'il')
        self.alice = Worker('Alice', 'Smith', 1995, 12, 1, '90 Yigal Alon, Tel Aviv', 'il')

    def tearDown(self):
        print('TearDown')

    def test_full_name(self):
        # bob = Worker('Bob', 'Marshall', 1970, 7, 5)
        # print(self.bob.full_name())
        self.assertTrue(self.bob.full_name() == 'Bob Marshall')
        self.assertTrue(self.alice.full_name() == 'Alice Smith')

    def test_age(self):
        # bob = Worker('Bob', 'Marshall', 1970, 7, 5)
        # print(self.bob.age())
        # print(datetime.datetime.now().year())
        self.assertTrue(self.bob.age() == "Bob is 50 years old")
        self.assertTrue(self.alice.age() == "Alice is 25 years old")

    def test_days_to_birthday(self):
        # bob = Worker('Bob', 'Marshall', 1970, 7, 30)
        # print(self.bob.days_to_birthday())
        # print(self.alice.days_to_birthday())
        self.assertIn("11", self.bob.days_to_birthday())
        self.assertIn("135", self.alice.days_to_birthday())

    def test_location(self):
        # bob = Worker('Bob', 'Marshall', 1970, 7, 30, '2 Dizengof, Tel Aviv', 'il')
        # print(bob.location())
        with patch('Worker.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            res = self.bob.location()
            mocked_get.assert_called_with('https://geocode.xyz/?locate=2 Dizengof, Tel Aviv,il &json=1')
            self.assertEqual(res, 'Success')

            mocked_get.return_value.ok = False

            res = self.bob.location()
            mocked_get.assert_called_with('https://geocode.xyz/?locate=2 Dizengof, Tel Aviv,il &json=1')
            self.assertEqual(res, 'Bad response!')
