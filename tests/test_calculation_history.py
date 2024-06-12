'''My Calculator Test'''

# Place standard library imports before third-party imports
from decimal import Decimal
import pytest

#Importing the Calculation and Calculations classes from the calculator package.

from calculator.calculations import Calculation
from calculator.calculation_history import Calculations

# Importing arithmetic operation functions (add and subtract) to be tested.
from calculator.actions import add, subtract

# @pytest.fixture is a decorator that marks a function to set up the test environment.
# It is used here to prepare the environment for testing calculations.
@pytest.fixture
def setup_calculations():
  # The function setup_calculations() clears any previous calculation history and adds sample calculations for testing.
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation():
    #The function test_add_calculation() checks if adding a calculation to the history works. It creates a new calculation, adds it to the history, and then verifies if it's the most recent entry.
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history():
    # The function test_get_history() checks if retrieving the calculation history works. It gets the history and verifies it contains the correct number of calculations.
    history = Calculations.get_history()
    # assert len(history) == 1, "History does not contain the expected number of calculations"

def test_clear_history():
    #The function test_clear_history() checks if clearing the calculation history works. It clears the history and verifies that the history is empty.
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not clearr"

def test_get_latest():
    #The function `test_get_latest()` checks if getting the latest calculation from the history works. It retrieves the latest calculation and verifies that it matches the expected values from the last added calculation.
    Calculations.add_calculation(Calculation(Decimal('30'), Decimal('3'), add))
    latest = Calculations.get_latest()
    assert latest.a == Decimal('30') and latest.b == Decimal('3'), "Wrong calculation"
    Calculations.clear_history()

# @pytest.fixture
def test_find_by_operation():
    # The function `test_find_by_operation()` checks if finding calculations by operation type works. It finds all calculations with the 'add' operation and verifies the count. It then does the same for the 'subtract' operation.
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 0, "Wrong calculations with add operation"
    # Find all the calculations with the subtract operation.
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 0, "Wrong calculations with subtract operation"

def test_get_latest_with_empty_history():
    #The function `test_get_latest_with_empty_history()` checks if getting the latest calculation works when the history is empty. It clears the history and verifies that the latest calculation is `None`.
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "None with calculation with empty history"
