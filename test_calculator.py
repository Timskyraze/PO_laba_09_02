import pytest
from calculator import Calculator

class TestCalculator:
    
    @pytest.fixture
    def calc(self):
        return Calculator()
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (-2, 3, 1),
        (0, 5, 5),
        (2.5, 3.5, 6.0),
        (-5, -3, -8),
    ])
    def test_add(self, calc, a, b, expected):
        result = calc.add(a, b)
        assert result == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (10, 2, 5),
        (9, 3, 3),
        (5, 2, 2.5),
        (-10, 2, -5),
        (0, 5, 0),
    ])
    def test_divide_normal(self, calc, a, b, expected):
        result = calc.divide(a, b)
        assert result == expected
    
    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError) as exc_info:
            calc.divide(10, 0)
        assert str(exc_info.value) == "Деление на ноль невозможно"
    
    @pytest.mark.parametrize("number,expected", [
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (13, True),
        (17, True),
        (1, False),
        (4, False),
        (9, False),
        (15, False),
        (0, False),
        (-5, False),
        (97, True),
        (100, False),
    ])
    def test_is_prime_number(self, calc, number, expected):
        result = calc.is_prime_number(number)
        assert result == expected