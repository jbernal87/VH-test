import sys


def is_overlapped(line1, line2):
    line1_sort = sorted(line1)
    line2_sort = sorted(line2)
    return (line1_sort[1] >= line2_sort[0] and line2_sort[1] >= line1_sort[0])


def main():
    """Main entry point for the script."""
    try:
        line_1 = tuple(map(float, input("Please enter line 1: ").split()))
        line_2 = tuple(map(float, input("Please enter line 2: ").split()))
        print(line_1)
        print(line_2)
        print("_________")
        if is_overlapped(line_1, line_2):
            print("Overlapped")
        else:
            print("Not overlapped")

    except:
        print("Oops!", sys.exc_info()[0], "occurred.")


if __name__ == '__main__':
    sys.exit(main())
