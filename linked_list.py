#!/usr/bin/python3
#Input: a: 5->10->15, b: 2->3->20
#Output: 2->3->5->10->15->20

#Input: a: 1->1, b: 2->4
#Output: 1->1->2->4

class Node:
   def __init__(self,key):
      self.key=key
      self.next=None


if __name__=='__main__':
   a=Node(5)
   a.next=Node(10)
   a.next.next=Node(15)

   b=Node(2)
   b.next=Node(3)
   b.next.next=Node(20)

   v=[]
   while (a is not None):
      v.append(a.key)
      a=a.next
   
   while (b is not None):
      v.append(b.key)
      b=b.next
   
   v.sort()
   print(v)
### The above makes a new list which is sorted
## Time complexity is O(n+m log(n+m)) and the space complexity is O(n+m) . 
# The log is coming into picture here because the sorting algorithms use a logarthmic approach to sort the contents
result = Node(-1)
temp = result
print(temp)
for i in range(len(v)):
    print(Node(v[i]))
    result.next = Node(v[i])
    result = result.next
    print(result)
 
temp = temp.next
print(temp)
print("Resultant Merge Linked List is : ")
while(temp is not None):
    print(temp.key, end=" ")
    temp = temp.next


      

   

