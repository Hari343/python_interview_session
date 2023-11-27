from typing import List
from heapq import heapify, nlargest

"""
    Given a list of integers, write a function to return the third-largest distinct integer from the list.
    You SHOULDN'T use any built-in sorting function. It is guaranteed that the input list will contain at
    least 3 distinct integers.

    Examples 1:
    Input: [4, 1, 6, 4, 8, 12]
    Output: 6
    Explanation: There are 5 distinct numbers. They are (in sorted ascending order): [1, 4, 6, 8, 12].
     So the third-largest is 6

    Example 2:
    Input: [94, 95, 96]
    Output: 94
    Explanation: The list has 3 distinct integers. Third-largest one is 94
"""


def third_largest(nums: List[int]):
    return nlargest(3, set(nums))[-1]


# Don't modify this function. This function is used to test your code against example test cases. Please be aware that
# we will test your code against additional hidden test cases post submission.
def test_example_test_cases():
    # test case 1
    assert (6 == third_largest([4, 1, 6, 4, 8, 12]))
    print("Example test case 1 successful")

    # test case 2
    assert (94 == third_largest([94, 95, 96]))
    print("Example test case 2 successful")


# Feel free to test your code. The code you write after this line won't be marked.
if __name__ == "__main__":
    test_example_test_cases()

