import pytest
from src.calculator import Calculator, DatabaseService


class TestExceptions:
    """Tests des exceptions."""
    
    def test_divide_by_zero_exception(self):
        calc = Calculator()
        
        with pytest.raises(ValueError) as exc_info:
            calc.divide(10, 0)
        
        assert str(exc_info.value) == "Cannot divide by zero"
        assert isinstance(exc_info.value, ValueError)
    
    def test_database_not_connected(self):
        service = DatabaseService()
        
        with pytest.raises(ConnectionError) as exc_info:
            service.get_data("SELECT * FROM table")
        
        assert "Not connected to database" in str(exc_info.value)
    
    def test_multiple_exceptions(self):
        calc = Calculator()
        
        # Test qu'une exception spécifique est levée
        with pytest.raises((ValueError, TypeError)):
            # Cette partie devrait lever ValueError
            calc.divide(10, 0)