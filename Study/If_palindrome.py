# Function
def if_palindrome(word):
    word_lower = word.lower()
    word_reverse = "".lower()
    word_len = len(word_lower)
    while word_len != 0:
        word_reverse += word_lower[word_len - 1]
        word_len -= 1

    if word_lower == word_reverse:
        return "True"
    elif word_lower != word_reverse:
        return "False"


def check():
    pass_count = 0
    # Test#1
    if if_palindrome("Nigger") == "False":
        print("Test#1: Status: Passed")
        pass_count += 1
    elif if_palindrome("Nigger") == "True":
        print("Test#1: Status: Failed")

    # Test#2
    if if_palindrome("NiggiN") == "True":
        print("Test#2: Status: Passed")
        pass_count += 1
    elif if_palindrome("NiggiN") == "False":
        print("Test#2: Status: Failed")

    # Test#3
    if if_palindrome("rar") == "True":
        print("Test#3: Status: Passed")
        pass_count += 1
    elif if_palindrome("rar") == "False":
        print("Test#3: Status: Failed")

    # Test#4
    if if_palindrome("Notepad") == "False":
        print("Test#4: Status: Passed")
        pass_count += 1
    elif if_palindrome("Notepad") == "True":
        print("Test#4: Status: Failed")

    # Test#5
    if if_palindrome("Reser") == "True":
        print("Test#5: Status: Passed")
        pass_count += 1
    elif if_palindrome("Reser") == "False":
        print("Test#5: Status: Failed")


check()
