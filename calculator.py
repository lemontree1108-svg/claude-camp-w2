"""
Safe Calculator
Week 2 Project - Supports +, -, *, / with full error handling
"""


def calculate(num1, operator, num2):
    """Perform calculation and return (result, error_message)."""
    if operator == "+":
        return num1 + num2, None
    elif operator == "-":
        return num1 - num2, None
    elif operator in ("*", "x", "×"):
        return num1 * num2, None
    elif operator in ("/", "÷"):
        if num2 == 0:
            return None, "❌ Cannot divide by zero."
        return num1 / num2, None
    else:
        return None, f"❌ Unknown operator '{operator}'. Use +  -  *  /"


def get_number(prompt):
    """Prompt until a valid number is entered, or 'quit' is typed."""
    while True:
        value = input(prompt).strip()
        if value.lower() == "quit":
            return "quit"
        try:
            return float(value)
        except ValueError:
            print(f"❌ '{value}' is not a number. Please try again.")


def format_result(n):
    """Show as int if whole number, else as float."""
    return int(n) if isinstance(n, float) and n.is_integer() else n


def main():
    print("=" * 40)
    print("         Safe Calculator")
    print("=" * 40)
    print("Operators: +  -  *  /")
    print("Type 'quit' at any prompt to exit.\n")

    while True:
        # Get first number
        num1 = get_number("Enter first number: ")
        if num1 == "quit":
            break

        # Get operator
        operator = input("Enter operator (+  -  *  /): ").strip()
        if operator.lower() == "quit":
            break

        # Get second number
        num2 = get_number("Enter second number: ")
        if num2 == "quit":
            break

        # Calculate
        result, error = calculate(num1, operator, num2)

        if error:
            print(error)
        else:
            op_display = operator if operator not in ("x", "×") else "×"
            print(f"  {format_result(num1)} {op_display} {format_result(num2)} = {format_result(result)}")

        print()  # blank line between calculations

    print("Goodbye!")


if __name__ == "__main__":
    main()
