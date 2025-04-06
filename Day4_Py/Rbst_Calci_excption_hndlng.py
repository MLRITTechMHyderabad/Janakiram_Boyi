def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.
    
    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """

    try:
        # TODO: Implement operation handling and raise exceptions for invalid cases
        if operator == '+':
            return a+b
        elif operator == "-":
            return a-b
        elif operator == "*":
            return a*b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Error: Division by zero ")
            return a / b
        elif operator == "%":
            if b == 0:
                raise ZeroDivisionError("Error: Modulo by zero is not allowed.")
            return a % b
        elif operator == "**":
            return a ** b
        else:
            raise ValueError("Error: Unsupported operator")
        pass  
    except ZeroDivisionError as e:
        return str(e)
        pass  # TODO: Handle division by zero
    except ValueError as e:
        return str(e)
        pass  # TODO: Handle invalid numbers
    except TypeError as e:
        return f"Error : Invalid Input"
        pass  # TODO: Handle non-numeric input
    except Exception as e:
       return f"Error: Unexpected error: {e}"
    pass  # TODO: Handle any unexpected exceptions

# Example Usage:
print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type"
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"
