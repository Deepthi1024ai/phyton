def safe division(): 
    """ 
    Demonstrates error handling for division by zero. 
    """ 
    try: 
        numerator = float(input("Enter numerator: ")) 
        denominator = float(input("Enter denominator: ")) 
        result = numerator / denominator 
        print(f"Result: {result:.2f}") 
    except ZeroDivisionError: 
        print("Error: Division by zero is not allowed.") 
    except ValueError: 
        print("Invalid input. Please enter numerical values only.") 
 
# Run the function 
safe_division()
