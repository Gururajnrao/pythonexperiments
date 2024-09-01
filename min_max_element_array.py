#!/usr/bin/python3
#Input: arr[] = {3, 5, 4, 1, 9}
#Output: Minimum element is: 1
#        Maximum element is: 9

#Input: arr[] = {22, 14, 8, 17, 35, 3}
#Output:  Minimum element is: 3
#         Maximum element is: 35

class Solution:
    def min_max_array(self,arr):
       arr.sort()
       length=len(arr)
       return arr[0],arr[length-1]

if __name__=='__main__':
   arr=[22, 14, 8, 17, 35, 3]
   s=Solution()
   min,max=s.min_max_array(arr) 
   print ("Minimum element is:",min)
   print ("Maximum element is:",max)
   

# Time complexity : O nlog(n)
# Space complexity: O(1)
