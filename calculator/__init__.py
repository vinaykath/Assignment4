from calculator.user_input import UserInput
from calculator.actions import add, subtract, multiply, divide
from calculator.calculation_history import CalculationsHistory, Calc

class Calculator:
    @staticmethod
    def addition(a,b):
        result = UserInput(a, b, add)  
        # adding function from calculator.actions
        CalculationsHistory.create_history(result)
        return result.result()
    @staticmethod
    def subtraction(a,b):
        result = UserInput(a, b, subtract)  
        # Subtracting function from calculator.actions
        CalculationsHistory.create_history(result)
        return result.result()
    @staticmethod
    def multiplication(a,b):
        result = UserInput(a, b, multiply)
         # Multiply function from calculator.actions
        CalculationsHistory.create_history(result)
        return result.result()
    @staticmethod
    def divison(a,b):
        try:
            result = UserInput(a, b, divide)  
         # Dividing function from calculator.actions
            CalculationsHistory.create_history(result)
            return result.result()
        except ZeroDivisionError:
            print("Cannot divided by Zero.")
        
