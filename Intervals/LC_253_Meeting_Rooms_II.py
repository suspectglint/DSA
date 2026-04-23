"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #Approach 1 - Using Min Heap here we are trying to store the minimum 
        #number of meetings required at any point in time using their end times.
        """
        min_heap=[]
        intervals.sort(key=lambda i : i.start)
        for intr in intervals:
            if min_heap and intr.start>=min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,intr.end)
        return len(min_heap)
        """
        #Approach 2 - Using Sweep Line Algorithm - Here we are trying to store the
        #start times and end times in the timeline using a map and signify
        #start by increasing 1 and end by decreasing 1. And we traverse this map
        #in sorted order of times and add the map value to a variable curr - to track
        #the number of meetings required at any point of time.
        #And res is used to capture the maximum meetings required at any point of time.
        #Finally we return the res which signifies the maximum number of meetings needed
        #at any point of time.
        """
        map_time=defaultdict(int)
        for i in intervals:
            map_time[i.start]+=1
            map_time[i.end]-=1
        res=curr=0
        for t in sorted(map_time):
            curr+=map_time[t]
            res=max(res,curr)
        return res
        """
        #Approach 3 - Using two pointer approach where we use two lists
        #to store start and end times in sorted order and process them using
        #two pointers.
        """
        start=[i.start for i in intervals]
        end=[i.end for i in intervals]
        start.sort()
        end.sort()
        s=e=curr=res=0
        while s<len(start):
            if start[s]>=end[e]:
                e+=1
            else:
                curr+=1
            s+=1
            res=max(res,curr)
        return res
        """