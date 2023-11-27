from typing import List

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
 element appears only once. The relative order of the elements should be kept the same.
  Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

1. Change the array nums such that the first k elements of nums contain the unique elements in the order they were
 present in nums initially. The remaining elements of nums are not important as well as the size of nums.
2. Return k.

Example 1:
Input: nums = [1, 1, 2]
Output: 2 and nums should be [1, 2, _]

Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Example 2:
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5 and nums should be [0, 1, 2, 3, 4, _, _, _, _, _]

Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 
respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""


def remove_duplicates(nums: List[int]) -> int:
    # write your code here
    return 0


# Don't modify below function. This function is used to test your code against example test cases. Please be aware that
# we will test your code against additional hidden test cases post submission.
def test_example_test_cases():
    # example test case 1
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    assert (k == 2 and [1, 2] == nums[:2])
    print("Example test case 1 successful")

    # example test case 2
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    assert (k == 5 and [0, 1, 2, 3, 4] == nums[:5])
    print("Example test case 2 successful")


# Feel free to test your code. The code you write after this line won't be marked.
if __name__ == "__main__":
    test_example_test_cases()
