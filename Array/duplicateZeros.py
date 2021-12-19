class Solution(object):
    def duplicateZeros(arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        len_=len(arr)
        i=0
        while i<len_:
            if arr[i]==0:
                arr.insert(i+1, 0)
                i+=2
                arr.pop()
            else:
                i+=1
        print arr
                
    input = [1,0,2,3,0,4,5,0,8,6,5,1,0,6]
    duplicateZeros(input)