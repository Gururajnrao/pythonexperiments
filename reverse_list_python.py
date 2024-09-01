# Input: list = [4, 5, 6, 7, 8, 9]
# Output: [9, 8, 7, 6, 5, 4] 
# Explanation: The list we are having in the output is reversed to the list we have in the input.

class Solution:
  def reverse_list(self,list1):
    return list1[::-1]
    
if __name__=="__main__":
   list1=[4,5,6,7,8,9]
   a=Solution()
   out=a.reverse_list(list1)
   print(out)


# Time and space complexity - O(n) - Slicing (i.e ::-1) creates a new list and does a linear copy