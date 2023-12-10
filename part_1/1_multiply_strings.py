from typing import List

"""
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
     also represented as a string.

    Note: You MUST NOT use any built in string to integer conversion functions 

    Examples 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"
    Explanation: 2 * 3 == 6

    Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"
    Explanation: 123 * 456 == 56088
"""


def multiply_strings(str1: str, str2: str) -> str:
    # write your code here
    return "0"


# Don't modify below function. This function is used to test your code against example test cases. Please be aware that
# we will test your code against additional hidden test cases post submission.
def test_example_test_cases():
    # test case 1
    assert("6" == multiply_strings("2", "3"))
    print("Example test case 1 successful")

    # test case 2
    assert("56088" == multiply_strings("123", "456"))
    print("Example test case 2 successful")


# Feel free to test your code. The code you write after this line won't be marked.
if __name__ == "__main__":
    test_example_test_cases()
