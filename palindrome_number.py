#! /usr/bin/python3
#Input1: test_number = 12321 
#Output1: True 
#Input2: test_number = 1234 
#Output2: False

def test_number_palindrome(number):
   palinstr=str(number)
   #revpalinstr=palinstr[::-1]
   #print (revpalinstr)
   if palinstr == palinstr[::-1]:
      print ("Integer is a palindrome")
   else:
      print ("Integer not a palindrome")
   

if __name__=='__main__':
   test_number_palindrome(input())
   


#Reference: https://www.geeksforgeeks.org/python-program-to-check-if-number-is-palindrome-one-liner/
#Time complexity O(n) and Space complexity O(1)