import unittest
from calculator import Calculator

class TestCalculatorUnit(unittest.TestCase):
    """
    Egységtesztek a Calculator osztály metódusaihoz.
    """

    def setUp(self):
        """Beállítás minden teszt előtt: létrehozzuk a Calculator példányt."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Teszteli két pozitív szám összeadását."""
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtract_negative_result(self):
        """Teszteli a kivonást negatív eredménnyel."""
        self.assertEqual(self.calc.subtract(10, 15), -5)

    def test_multiply_by_zero(self):
        """Teszteli a nullával való szorzást."""
        self.assertEqual(self.calc.multiply(100, 0), 0)

    def test_divide_standard(self):
        """Teszteli a standard osztást."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_by_zero_exception(self):
        """
        Teszteli, hogy az osztás nullával kivételt dob-e (ValueError).
        """
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        # Ellenőrizzük a kivétel üzenetét is
        self.assertTrue('Osztás nullával nem megengedett.' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
