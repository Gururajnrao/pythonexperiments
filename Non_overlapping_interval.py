#Find least non-overlapping number from a given set of intervals
#Example 1:

#Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
#Output: 1
#Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
#Example 2:

#Input: intervals = [[1,2],[1,2],[1,2]]
#Output: 2
#Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
#Example 3:

#Input: intervals = [[1,2],[2,3]]
#Output: 0
#Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        print (intervals)
        output=0
        first_element=[intervals[0]]
        print(first_element)
        for i in range(1,len(intervals)):
            if (first_element[-1][1] > intervals[i][0]):
                 output+=1
        return output
