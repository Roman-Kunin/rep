# Multiply function
def multiply(x, y):
    output = 0
    for i in range(0, y):
        output += x
    return output


# Function checker
def check():
    passed_count = 0

    # Test#1
    if multiply(777, 666) == 777 * 666:
        print("Test#1: Status: passed")
        passed_count += 1
    elif multiply(777, 666) != 777 * 666:
        print("Test#1: Status: failed")

    # Test#2
    if multiply(123, 321) == 123 * 321:
        print("Test#2: Status: passed")
        passed_count += 1
    elif multiply(123, 321) != 123 * 321:
        print("Test#2: Status: failed")

    # Test#3
    if multiply(11, 22) == 11 * 22:
        print("Test#3: Status: passed")
        passed_count += 1
    elif multiply(11, 22) != 11 * 22:
        print("Test#3: Status: failed")

    # Test#4
    if multiply(1, 1) == 1 * 1:
        print("Test#4: Status: passed")
        passed_count += 1
    elif multiply(1, 1) != 1 * 1:
        print("Test#4: Status: failed")

    # Test#5
    if multiply(0, 0) == 0 * 0:
        print("Test#5: Status: passed")
        passed_count += 1
    elif multiply(0, 0) != 0 * 0:
        print("Test#5: Status: failed")

    # Conclusion
    if passed_count == 5:
        print("\n5 out of 5 tests passed.\nTask completed!")
    elif passed_count != 5:
        print(f"\n{passed_count} out of 5 tests passed.\nTask failed!")


check()
