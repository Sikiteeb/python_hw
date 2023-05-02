import sys


def square_formula(a, b):
    result = (a + b) ** 2
    return result


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python square_formula.py <a> <b>")
        sys.exit(1)

    a = sys.argv[1]
    b = sys.argv[2]

    if not (is_number(a) and is_number(b)):
        print("Error: Both inputs must be valid numbers.")
        sys.exit(1)

    a = float(a)
    b = float(b)

    result = square_formula(a, b)
    print(f"({a}+{b})² = {result}")
