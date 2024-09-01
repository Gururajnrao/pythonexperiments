#!/usr/bin/python3
# Merge intervals

def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals based on the starting point
    #print(intervals)
    intervals.sort(key=lambda x: x[0])
    #print (intervals)
    merged = [intervals[0]]

    #print(merged)
    #print(len(intervals))
    for i in range(1, len(intervals)):
        # If the current interval overlaps with the last merged interval, merge them
        #print(merged[-1][1])
        print (merged[-1][1])
        print (intervals[i][0])
        if merged[0][1] >= intervals[i][0]:
            merged[0][1] = max(merged[0][1], intervals[i][1])
            print(merged)
            print("Entered here")
        else:
            merged.append(intervals[i])
    
    return merged

# Example 2
intervals = [[1,3],[2,6],[8,10],[15,18]]
output = merge_intervals(intervals)
print(output)  # Output: [[1, 5]]