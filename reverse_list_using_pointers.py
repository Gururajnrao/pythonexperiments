# Input: list = [4, 5, 6, 7, 8, 9]
# Output: [9, 8, 7, 6, 5, 4] 
# Explanation: The list we are having in the output is reversed to the list we have in the input.

class Solution:
  def reverse_list(self,list1):
    left=0
    right=len(list1)-1
    while (left < right):
      temp=list1[left]
      list1[left]=list1[right]
      list1[right]=temp
      left+=1
      right-=1
    return list1

    
if __name__=="__main__":
   list1=[4,5,6,7,8,9]
   a=Solution()
   out=a.reverse_list(list1)
   print(out)


# Time complexity - O(n) since you have to still traverse through the entire array
# Space complexity - O(1) since you are not creating a new list and swapping elements in the existing list