#!/usr/bin/python3
from typing import List

class Solution:
   def twosum(self, nums: List[int], target: int)->List[int]:
       condition=lambda x: x<target
       filtered_list=[x for x in nums if condition (x) ]
       hashmap={}
       for i,j in enumerate(filtered_list):
           complement=target-j
           print("Complement,Hashmap",complement,hashmap)
           if complement in hashmap :
               print("Entered")
               return(hashmap[complement],i)
           hashmap[j]=i
       return []

       

if __name__=="__main__":
    a=Solution()
    output=[]
    output=a.twosum([2,1,11,15],9)
    print(output)


#Time complexity: O(n) since you iterate through the list only once
#Space complexity: O(n) since all the variables could be stored if none of them maps to the two sum.