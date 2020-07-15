from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch
from Package1.Worker import Worker

mock = Mock()
# Mock -  You can do this by passing it as an argument to a function or by redefining another object
# function_name(mock)
# The return value of mock is also a Mock.

class TestWorker(TestCase):


    # @mock.patch('datetime.datetime.now().year', return_value=2019)

    def test_full_name(self):
        bob = Worker('Bob', 'Marshall', 1970, 7, 5)
        self.assertTrue(bob.full_name() == 'Bob Marshall')
        print('hi hi')

    def test_age(self):
        #datetime = Mock()
        #with mock.patch('datetime.datetime.now().year',return_value = 2019)
          bob = Worker('Bob', 'Marshall', 1970, 7, 5)
          print(bob.age())
          print(datetime.datetime.now().year())
          self.assertTrue(bob.age() == 49)

    def test_days_to_birthday(self):
        bob = Worker('Bob', 'Marshall', 1970, 7, 5)
        self.assertTrue(bob.days_to_birthday() == 4)
