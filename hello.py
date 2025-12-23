#!/usr/bin/env python3
def aadit(name: str = "aadit", times: int = 3) -> None:
    """Print that <name> is cool `times` times."""
    for _ in range(times):
        print(f"{name} is cool")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        name = sys.argv[1]
        count = int(float(sys.argv[2])) if len(sys.argv) > 2 else 3
        aadit(name, count)
    else:
        name = input("Enter a name (or press enter for 'aadit'): ").strip() or "aadit"
        count_input = input("How many times do you want to print it? (default 3): ").strip()
        count = int(float(count_input)) if count_input else 3
        aadit(name, count)
