def largest(numlist):
    output = 0
    for largest_number in numlist:
        if largest_number > output:
            output = largest_number
    return output


def check():
    pass_count = 0
    # Test#1
    if largest([1, 2, 3, 4, 5]) == 5:
        print("\nTest#1: Status: passed")
        pass_count += 1
    elif largest([1, 2, 3, 4, 5]) != 5:
        print("\nTest#1: Status: failed")

    # Test#2
    if largest([23, 8934, 9999]) == 9999:
        print("Test#2: Status: passed")
        pass_count += 1
    elif largest([23, 8934, 9999]) != 9999:
        print("Test#2: Status: failed")

    # Test#3
    if largest([2, 34, 434]) == 434:
        print("Test#3: Status: passed")
        pass_count += 1
    elif largest([2, 34, 434]) != 434:
        print("Test#3: Status: failed")

    # Test#4
    if largest([43, 65, 7689867]) == 7689867:
        print("Test#4: Status: passed")
        pass_count += 1
    elif largest([43, 65, 7689867]) != 7689867:
        print("Test#4: Status: failed")

    # Test#5
    if largest([5, 0, 89]) == 89:
        print("Test#5: Status: passed")
        pass_count += 1
    elif largest([5, 0, 89]) != 89:
        print("Test#5: Status: failed")

    # Conclusion
    if pass_count == 5:
        print("\n5 out of 5 tests passed.\nTask complete!")
    elif pass_count != 5:
        print(f"\n{pass_count} of 5 tests passed.\nTask failed!")


check()
