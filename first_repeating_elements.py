#!/usr/bin/python3
# Input: arr[] = {10, 5, 3, 4, 3, 5, 6}
#Output: 5 
#Explanation: 5 is the first element that repeats

#Input: arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
#Output: 6 
#Explanation: 6 is the first element that repeats

class Solution:
   def find_repeating(self,arr):
      Min=-1 #Initialize the index
      myset={}
      length=len(arr)
      for i in range(length-1,-1,-1):
         if arr[i] in myset.keys():
            Min=i
            #print("Entered 1")
            #print(myset[arr[i]])
            #print(Min)
            #print(arr[Min])
         else:
            myset[arr[i]]=1
            #print("Entered 2")
            #print(i)
            #print(myset[arr[i]])
      if (Min!=-1):
         print ("Repeating elements are:",arr[Min])
      else:
         print("No repeating elements in the list")
        
                    

if __name__=='__main__':
    arr=[10,5,3,4,3,5,3,6]
    a=Solution()
    a.find_repeating(arr)
    

