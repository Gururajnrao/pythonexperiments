#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned)

#Example 1:

#Input: x = 123
#Output: 321

#Example 2:
#Input: x = -123
#Output: -321

#Example 3:
#Input: x = 120
#Output: 21

#Constraints:
#-231 <= x <= 231 - 1

def reverse_int(n):
  r=0
  sign=-1 if n<0 else 1
  n=abs(n)  
  while (n!=0):
      
    a=n%10
    #print(a,r)
    if r > 2**31//10 or (r == 2**31//10 and a > 7):
       return 0
 
        # Check if the reverse number will underflow 32-bit integer
    if r < -2**31//10 or (r == -2**31//10 and a < -8):
       return 0
    r=r*10+a
    n=n//10

  return sign*r

if __name__=='__main__':
    reverse=reverse_int(int(input()))
    
    print(reverse)


# Time complexity = O(log n)
# Space complexity = O(1)