class Calculator:
    """Classe calculatrice avec opérations basiques."""
    
    def add(self, a: float, b: float) -> float:
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base: float, exponent: float) -> float:
        return base ** exponent
    
    def is_even(self, number: int) -> bool:
        return number % 2 == 0


class DatabaseService:
    """Service simulé avec dépendance externe."""
    
    def __init__(self):
        self.connected = False
    
    def connect(self):
        self.connected = True
        return True
    
    def get_data(self, query: str) -> list:
        if not self.connected:
            raise ConnectionError("Not connected to database")
        # Simulation d'accès BD
        return [{"id": 1, "value": "test"}]