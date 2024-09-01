#! /usr/bin/python3
#Input: arr[] = {1, 2, 4, 6, 3, 7, 8} , N = 8
#Output: 5
#Explanation: Here the size of the array is 8, so the range will be [1, 8]. The missing number between 1 to 8 is 5

#Input: arr[] = {1, 2, 3, 5}, N = 5
#Output: 4
#Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4

class Solution:
    def missing_number(self, n, arr):
        self.real_sum=sum(arr)
        self.expected_sum=(n*(n+1))//2
        self.missing_number=self.expected_sum - self.real_sum
        return self.missing_number
    
if __name__ == "__main__":
    a=Solution()
    arr1=[1, 2, 3, 5]
    length=len(arr1)+1
    val=a.missing_number(length,arr1)
    print(val)


# TIme complexity = O(n)
# Space complexity = O(1)