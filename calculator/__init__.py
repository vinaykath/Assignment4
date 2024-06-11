'''

This Python code defines a  Calculator  class that provides an interface for arithmetic operations (addition, subtraction, multiplication, division) on  Decimal  numbers using static methods. Each method creates a  Calculation  object, performs the calculation, stores it in a history, and returns the result.

Design Principles Highlighted

Single Responsibility Principle (SRP): The  Calculator  class is dedicated to performing calculations, while the  Calculations  class manages the history, ensuring each class has one clear purpose.

Don't Repeat Yourself (DRY): The  _perform_operation  method consolidates common tasks, minimizing redundancy in the  add ,  subtract ,  multiply , and  divide  methods by abstracting the repetitive processes.

Separation of Concerns**: The  Calculator  handles the calculation logic, and the  Calculations  class manages the history. This clear division of tasks enhances maintainability and scalability.

Encapsulation: The  Calculator  class encapsulates the behavior of performing calculations and managing their results, demonstrating functional encapsulation.

Polymorphism: The use of a  Callable  type hint for the  operation  parameter in  _perform_operation  allows for any matching function to be passed and executed, providing flexibility and promoting reuse.

'''

# Import necessary modules and classes
from calculator.calculation_history import Calculations  # Manages history of calculations
from calculator.actions import add, subtract, multiply, divide  # Arithmetic operations
from calculator.calculations import Calculation  # Represents a single calculation
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

# Definition of the Calculator class
class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        # Create a Calculation object using the static create method, passing in operands and the operation
        calculation = Calculation.create(a, b, operation)
        # Add the calculation to the history managed by the Calculations class
        Calculations.add_calculation(calculation)
        # Perform the calculation and return the result
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        # Perform addition by delegating to the _perform_operation method with the add operation
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        # Perform subtraction by delegating to the _perform_operation method with the subtract operation
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        # Perform multiplication by delegating to the _perform_operation method with the multiply operation
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        # Perform division by delegating to the _perform_operation method with the divide operation
        return Calculator._perform_operation(a, b, divide)