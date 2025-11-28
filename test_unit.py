# test_calculator.py

import pytest
from calculator import Calculator, calculate_expression

class TestCalculatorUnit:
    """
    Unit tesztek a Calculator osztály alapvető műveleteihez.
    """

    # Minden teszt előtt inicializálja a Calculator objektumot
    @pytest.fixture
    def calculator(self):
        return Calculator()

    def test_add(self, calculator):
        """Teszteli az összeadást pozitív és negatív számokkal."""
        assert calculator.add(1, 2) == 3
        assert calculator.add(-1, 5) == 4
        assert calculator.add(0, 0) == 0
        assert calculator.add(1.5, 2.5) == 4.0

    def test_subtract(self, calculator):
        """Teszteli a kivonást."""
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(3, 5) == -2
        assert calculator.subtract(10, 0) == 10

    def test_multiply(self, calculator):
        """Teszteli a szorzást."""
        assert calculator.multiply(2, 4) == 8
        assert calculator.multiply(-2, 3) == -6
        assert calculator.multiply(5, 0) == 0

    def test_divide_success(self, calculator):
        """Teszteli az érvényes osztást."""
        assert calculator.divide(10, 2) == 5
        assert calculator.divide(5, 2) == 2.5
        assert calculator.divide(-6, 3) == -2

    def test_divide_by_zero(self, calculator):
        """Teszteli a nullával való osztás hibakezelését (ValueError)."""
        with pytest.raises(ValueError, match="Osztás nullával nem megengedett."):
            calculator.divide(10, 0)
