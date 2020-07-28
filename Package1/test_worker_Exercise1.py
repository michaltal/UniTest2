from unittest import TestCase
from Package1.Worker import Worker


class TestWorker(TestCase):
    def test_full_name(self):
        bob = Worker('bob', 'Cohen', 1980, 1, 1, '1 Yigal Alon, Tel Aviv', 'il')
        self.assertTrue(bob.full_name() == 'bob Cohen')
        self.assertIn('bob', bob.full_name())

    def test_age_past(self):
        bob = Worker('bob', 'Cohen', 1980, 1, 1, '1 Yigal Alon, Tel Aviv', 'il')
        print(bob.age())
        self.assertIn('is', bob.age())

    def test_age_future(self):
        mati = Worker('Mati', 'Levi', 2021, 1,1,'1 Yigal Alon, Tel Aviv', 'il')
        self.assertIn('-1', mati.age())

    def test_age_current_year(self):
        mati = Worker('Mati', 'Levi', 2020, 1, 1, '1 Yigal Alon, Tel Aviv', 'il')
        self.assertIn('0', mati.age())

    def test_days_to_birthday_future(self):
        mati = Worker('Mati', 'Levi', 1980, 7, 30, '1 Yigal Alon, Tel Aviv', 'il')
        print(mati.days_to_birthday())
        self.assertIn('2 days', mati.days_to_birthday())

    def test_days_to_birthday_past(self):
        mati = Worker('Mati', 'Levi', 1980, 7, 1, '1 Yigal Alon, Tel Aviv', 'il')
        print(mati.days_to_birthday())
        self.assertIn('-27 days', mati.days_to_birthday())

    def test_days_to_birthday_today(self):
        mati = Worker('Mati', 'Levi', 1980, 7, 28, '1 Yigal Alon, Tel Aviv', 'il')
        print(mati.days_to_birthday())
        self.assertIn('', mati.days_to_birthday())


    def test_greet(self):
        pass

    def test_location(self):
        pass
