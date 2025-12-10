import pytest
from src.calculator import Calculator, DatabaseService


class TestFixtures:
    """Démonstration des fixtures pytest."""
    
    @pytest.fixture
    def calculator(self):
        """Fixture de base qui retourne une nouvelle instance."""
        return Calculator()
    
    @pytest.fixture
    def calculator_with_cleanup(self):
        """Fixture avec cleanup."""
        calc = Calculator()
        yield calc
        # Cleanup après le test
        print("\nCleanup after test")
    
    @pytest.fixture(scope="class")
    def shared_calculator(self):
        """Fixture partagée pour toute la classe."""
        return Calculator()
    
    @pytest.fixture
    def db_service(self):
        """Fixture pour le service de base de données."""
        service = DatabaseService()
        service.connect()
        return service
    
    # Tests utilisant les fixtures
    def test_with_basic_fixture(self, calculator):
        assert calculator.add(1, 1) == 2
    
    def test_with_cleanup_fixture(self, calculator_with_cleanup):
        assert calculator_with_cleanup.multiply(3, 4) == 12
    
    def test_shared_fixture_1(self, shared_calculator):
        shared_calculator.result = 10
    
    def test_shared_fixture_2(self, shared_calculator):
        # Accède à l'attribut défini dans le test précédent
        assert hasattr(shared_calculator, 'result')
    
    def test_database_service(self, db_service):
        data = db_service.get_data("SELECT * FROM test")
        assert len(data) == 1
        assert data[0]["id"] == 1