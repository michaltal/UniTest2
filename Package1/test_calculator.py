from unittest import TestCase, mock
from Package1.Calculator import Calculator

class TestCalculator(TestCase):
    @mock.patch('Package1.Calculator.Calculator.sum_numbers', return_value=9)

    def test_sum_numbers(self, mock_sum_numbers):
        calc = Calculator(4, 4)
        print(calc.sum_numbers())
        self.assertEqual(calc.sum_numbers(), 9)
