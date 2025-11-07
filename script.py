"""
Template CLI Script
-------------------
Example usage:
    python script.py hello 4 -v
"""

# Imports
import argparse


def echo_and_square(echo: str, square: int, verbose: bool) -> None:
    """
    Prints an echoed string and the square of an integer.
    """
    if verbose:
        print("Verbose mode is ON")
        print(f"Echoed string: {echo}")
        print(f"{square}^2 = {square ** 2}")
    else:
        print(echo)
        print(square ** 2)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A simple CLI template demonstrating positional and optional arguments."
    )
    
    # Positional arguments
    parser.add_argument("echo", help="Echo the string you use here")
    parser.add_argument("square", type=int, help="Display a square of a given number")

    # Optional (keyword) arguments
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")

    # Argument for getting version number
    parser.add_argument("-V", "--version", action="version", version="%(prog)s 1.0")

    # Retrieve arguments from parser
    args = parser.parse_args()  # returns a namespace with all the args
    echo_and_square(args.echo, args.square, args.verbose)


if __name__ == "__main__":
    main()