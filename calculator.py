class Calculator:
    """
    Egy egyszerű számológép osztály alapvető matematikai műveletekhez.
    """
    def add(self, a: float, b: float) -> float:
        """Két szám összeadása."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Két szám kivonása."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Két szám szorzása."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Két szám osztása. Zérus osztó esetén kivételt dob.
        """
        if b == 0:
            raise ValueError("Osztás nullával nem megengedett.")
        return a / b

# Egy példa egy magasabb szintű funkcióra, ami integrálja a műveleteket
def calculate_expression(a: float, b: float, c: float) -> float:
    """
    Kiszámítja az (a + b) / c kifejezést a Calculator osztály használatával.
    Ezt a funkciót teszteljük az integrációs tesztben.
    """
    calc = Calculator()
    # Integráció: az 'add' és 'divide' metódusok együttműködésének tesztelése
    sum_result = calc.add(a, b)
    return calc.divide(sum_result, c)
