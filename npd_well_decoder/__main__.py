import sys
from .npd import parse_wellbore_name


def main():
    if len(sys.argv) == 2:
        print(parse_wellbore_name(sys.argv[1]))
    else:
        print("npd '<well-name>'")


if __name__ == "__main__":
    main()
