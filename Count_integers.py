#Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
#Output: 3 
#Explanation: 10 appears three times in given list.
#Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16
#Output: 0
#Explanation: 16 appears zero times in given list.

class Solution:
    def count_integers(self,val,lst):
      self.left=0
      self.right=len(lst)-1
      count=0
      while (self.left != self.right):
         if lst[self.left] == val or lst[self.right]==val:
            count+=1
         self.left+=1
         self.right-=1
      if lst[self.left]==val:
         count+=1
      return count
            

       


if __name__=='__main__':
    val=16
    lst=[8, 6, 8, 10, 8, 20, 10, 8, 8]
    a=Solution()
    output=a.count_integers(val,lst)
    print(output)


# Time complexity = O(n)
# Space complexity = O(1)