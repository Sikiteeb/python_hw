import subprocess
import sys


def install_square_shann():
    try:
        import square_shann
    except ImportError:
        print("Installing square_shann module from Test PyPI...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-i", "https://test.pypi.org/simple/", "square-shann==0.0.1"])


def main():
    install_square_shann()

    from square_shann import square_formula

    a = float(input("Enter the value for 'a': "))
    b = float(input("Enter the value for 'b': "))

    result = square_formula(a, b)
    print(f"({a}+{b})² = {result}")


if __name__ == "__main__":
    main()
