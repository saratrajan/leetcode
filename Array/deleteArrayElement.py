class Solution(object):
    def deleteFirstElem(arr):
        """
        :type arr: List[int]
        """
        for i in range(len(arr)-1):
            arr[i] = arr[i + 1]
        print(arr)

    arr = [1,2,3,4,5,6,7,8,9,0]
    deleteFirstElem(arr)        
