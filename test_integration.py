import unittest
from calculator import calculate_expression

class TestCalculatorIntegration(unittest.TestCase):
    """
    Integrációs tesztek, amelyek több metódus vagy komponens együttműködését tesztelik.
    Itt a (a + b) / c kifejezés kiszámítását teszteljük.
    """

    def test_simple_expression(self):
        """Teszteli az (10 + 2) / 3 kifejezést, ami 4-et kell, hogy eredményezzen."""
        a, b, c = 10, 2, 3
        expected = 4.0
        result = calculate_expression(a, b, c)
        self.assertEqual(result, expected)

    def test_expression_with_negative_result(self):
        """Teszteli a (-5 + 1) / 2 kifejezést, ami -2-t kell, hogy eredményezzen."""
        a, b, c = -5, 1, 2
        expected = -2.0
        result = calculate_expression(a, b, c)
        self.assertEqual(result, expected)

    def test_divide_by_zero_in_expression(self):
        """
        Teszteli, hogy a kifejezés nullával való osztása is hibát dob-e.
        Itt az integrált hívási lánc ellenőrzi a hiba terjedését.
        """
        a, b, c = 5, 5, 0 # (5 + 5) / 0
        with self.assertRaises(ValueError):
            calculate_expression(a, b, c)

if __name__ == '__main__':
    unittest.main()
