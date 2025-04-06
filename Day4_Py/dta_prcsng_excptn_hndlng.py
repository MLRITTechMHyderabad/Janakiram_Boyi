def process_data(data, index):
    """
    Processes data with error handling.
    
    :param data: List of numbers (strings that should be converted to int)
    :param index: Index to divide with
    :return: Processed result or error message
    """
    try:
        # Convert elements to integers
        int_data = [int(item) for item in data]
        
        # Get divisor from index
        divisor = int_data[index]
        
        # Perform division
        result = sum(int_data) / divisor
        return result
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Data contains non-integer value."
    
    except IndexError:
        return "Error: Index out of range."
    
    except Exception as e:
        return f"Unexpected error: {e}"

# Example Usage:
data_list = ["10", "20", "0", "40"]
print(process_data(data_list, 2))  # Should handle division by zero

print(process_data(["10", "abc", "30"], 1))  # Should handle ValueError

print(process_data([10, 20], 5))  # Should handle IndexError
