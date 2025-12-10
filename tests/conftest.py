import pytest
from src.calculator import Calculator


# Fixtures disponibles pour tous les tests
@pytest.fixture(scope="session")
def session_calculator():
    """Fixture de session partagée entre tous les tests."""
    calc = Calculator()
    print("\nSession fixture created")
    yield calc
    print("\nSession fixture cleaned up")


@pytest.fixture
def calculator_factory():
    """Factory fixture."""
    def _create_calculator(initial_value=0):
        calc = Calculator()
        calc.memory = initial_value
        return calc
    return _create_calculator


# Hook pour ajouter des informations aux rapports
def pytest_html_report_title(report):
    report.title = "Rapport de Tests CI/CD"


# Optionnel: Marqueurs personnalisés
def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "slow: marque les tests lents (ex: tests d'intégration)"
    )