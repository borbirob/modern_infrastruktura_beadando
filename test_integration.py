import pytest
from calculator import calculate_expression

class TestCalculatorIntegration:
    """
    Integrációs tesztek a magasabb szintű funkciókhoz,
    ahol több Calculator metódus működik együtt.
    """

    def test_calculate_expression_valid(self):
        """Teszteli az (a + b) / c kifejezés sikeres kiszámítását."""
        # Eredmény: (10 + 2) / 4 = 3.0
        assert calculate_expression(10, 2, 4) == 3.0

        # Eredmény: (-5 + 10) / 2.5 = 5 / 2.5 = 2.0
        assert calculate_expression(-5, 10, 2.5) == 2.0

    def test_calculate_expression_divide_by_zero(self):
        """Teszteli, hogy a calculate_expression megfelelően kezeli-e a nullával osztást (c=0)."""
        # A függvény a belső calc.divide metódus miatt ValueError-t dob
        with pytest.raises(ValueError, match="Osztás nullával nem megengedett."):
            calculate_expression(1, 1, 0)
