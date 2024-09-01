#!/usr/bin/python3
# Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
#Output: 3 
#Explanation: 10 appears three times in given list.
#Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16
#Output: 0
#Explanation: 16 appears zero times in given list.

class Solution:
    def count_integers(self,val,lst):
      y=lambda x:x==val
      filtered_list=[x for x in lst if y(x) ]
      print(filtered_list)
      return len(filtered_list)

            

       


if __name__=='__main__':
    val=8
    lst=[8, 6, 8, 10, 8, 20, 10, 8, 8]
    a=Solution()
    output=a.count_integers(val,lst)
    print(output)


# Time complexity = O(n)
# Space complexity = O(n)