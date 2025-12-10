import pytest
from src.calculator import Calculator


class TestParametrized:
    """Tests avec paramétrisation."""
    
    @pytest.fixture
    def calc(self):
        return Calculator()
    
    # Test paramétré simple
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
        (100, 200, 300),
    ])
    def test_add_parametrized(self, calc, a, b, expected):
        assert calc.add(a, b) == expected
    
    # Test paramétré avec IDs explicites
    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (10, 2, 5),
            (9, 3, 3),
            (1, 1, 1),
        ],
        ids=["division entière", "division exacte", "division par un"]
    )
    def test_divide_parametrized(self, calc, a, b, expected):
        assert calc.divide(a, b) == expected
    
    # Test paramétré avec marks
    @pytest.mark.parametrize("number,expected", [
        pytest.param(2, True, id="pair petit"),
        pytest.param(100, True, id="pair grand"),
        pytest.param(3, False, id="impair petit"),
        pytest.param(101, False, id="impair grand"),
    ])
    def test_is_even_parametrized(self, calc, number, expected):
        assert calc.is_even(number) == expected