class Solution(object):
    def sortedSquares(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        sortedArray = [0] * len(nums)
        for i in range(right, left-1 , -1) :
            if(abs(nums[left]) < abs(nums[right])):
                square = nums[right] ** 2
                right -= 1
            else:
                square = nums[left] ** 2
                left += 1
            sortedArray[i] = square
        print(sortedArray)

    nums = [-7,-3,2,3,11]
    sortedSquares(nums)   
