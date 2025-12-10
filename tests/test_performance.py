# tests/test_performance.py
import pytest
import time

@pytest.mark.slow  # 🏷️ Ce test est marqué comme "slow"
def test_long_running_operation():
    """Test qui prend du temps (simulation)"""
    time.sleep(5)  # ⏱️ Simulation d'une opération lente
    assert 1 + 1 == 2

def test_quick_operation():
    """Test rapide - pas de marqueur"""
    assert 2 * 2 == 4

@pytest.mark.slow
def test_api_call():
    """Test avec appel API externe"""
    # Simulation d'appel API lent
    time.sleep(3)
    assert True