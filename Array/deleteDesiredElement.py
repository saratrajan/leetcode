class Solution(object):
    def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lastpos = len(nums)-1
        pos = 0
        valcount = 0
        while (pos <=  lastpos):
            if(nums[pos] == val):
                valcount += 1
                nums[pos] = nums[lastpos]
                lastpos -= 1
            else:
                pos += 1
        if(valcount > 0):
            del nums[-valcount:] 
        print(nums)
        print(valcount)

    nums = [2,1,9,13,27,1,7,9,6]
    val = 9
    removeElement(nums,val)