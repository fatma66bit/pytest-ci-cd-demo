import pytest
from unittest.mock import Mock, patch, MagicMock
from src.calculator import Calculator, DatabaseService


class TestMocking:
    """Tests avec mocking."""
    
    def test_mock_basique(self):
        # Création d'un mock simple
        mock_obj = Mock()
        mock_obj.method.return_value = 42
        
        assert mock_obj.method() == 42
        mock_obj.method.assert_called_once()
    
    def test_mock_with_side_effect(self):
        mock_obj = Mock()
        mock_obj.calculate.side_effect = [1, 2, 3]
        
        assert mock_obj.calculate() == 1
        assert mock_obj.calculate() == 2
        assert mock_obj.calculate() == 3
    
    def test_patch_function(self):
        with patch('src.calculator.Calculator.add') as mock_add:
            mock_add.return_value = 100
            calc = Calculator()
            
            result = calc.add(2, 3)
            
            assert result == 100
            mock_add.assert_called_once_with(2, 3)
    
    def test_patch_class(self):
        with patch('src.calculator.DatabaseService') as MockDB:
            service = MockDB()  # ← CORRECTION !
            service.get_data.return_value = [{"id": 999}]
            data = service.get_data("query")
            assert data[0]["id"] == 999
    
    @patch('src.calculator.DatabaseService.connect')
    def test_decorator_patch(self, mock_connect):
        mock_connect.return_value = False
        
        service = DatabaseService()
        result = service.connect()
        
        assert result is False
        mock_connect.assert_called_once()
    
    def test_mock_exception(self):
        mock_obj = Mock()
        mock_obj.process.side_effect = ValueError("Error occurred")
        
        with pytest.raises(ValueError, match="Error occurred"):
            mock_obj.process()