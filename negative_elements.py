#!/usr/bin/python3
class Solution:
    def segregateElements(self, arr):
        arr.sort(key=lambda x: x < 0)
        return(arr)


if __name__=='__main__':
    arr=[1,-2,3,4,5,-1,-2]
    a=Solution()
    n=a.segregateElements(arr)
    print(n)
    

# Time: O(n log n)
# Space: O(1) but worst case O(n) due to sort function