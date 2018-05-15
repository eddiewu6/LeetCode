#Solution1: brutal force
#O(n ** 2) in time, O(1) in space
#76/77 cases passed, time exceed limit error

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if intervals[j].start < intervals[i].start and intervals[j].end > intervals[i].start:
                    return False
                if intervals[j].start <= intervals[i].start and intervals[j].end >= intervals[i].end:
                    return False
                if intervals[j].start >= intervals[i].start and intervals[j].end <= intervals[i].end:
                    return False
                if intervals[j].start < intervals[i].end and intervals[j].end > intervals[i].end:
                    return False
        return True

#Solution1: sort the intervals according to the starting time
#O(nlogn) in time, O(1) in space
#AC in 56ms

def canAttendMeetings(self, intervals):

    intervals.sort(key=lambda x: x.start)
    
    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i-1].end:
            return False
        
    return True
