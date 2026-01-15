import pyperclip
from utils.git import get_staged_diff


def main():
    diff = get_staged_diff()

    if not diff:
        print("No changes.")
        return

    pyperclip.copy(diff)

    print("Successfully.")


if __name__ == "__main__":
    main()
