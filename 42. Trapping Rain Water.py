


"""Cannot deal with [2,2,2,0,2,2,2] situation"""    
    def findLocalPeak(self,height):
        peaks = []
        if height[0] > height[1]:
            peaks.append(0)
        i = 1
        while i < len(height):
            if height[i] > height[i-1]:
                #print("i:",i)
                temppeak = height[i]
                if i == len(height)-1:
                    peaks.append(i)
                #print("org temppeak"+str(temppeak))
                for j in range(i+1,len(height)):
                    #print("j:",j)
                    if temppeak < height[j]:
                        temppeak = height[j]
                        #print("temppeak"+str(temppeak))
                        i = j
                        
                    if temppeak > height[j]:
                        peaks.append(i)
                        #print("append:"+str(i))
                        i = j
                        break
                    if temppeak == height[j]:
                        i = j+1
            i += 1
        return peaks
"""

"""
##Partial solution1, find all local peak and calculate the area,did not concider [5,3,1,4,2,5] situation, where 5,4,5 is considered as local peak
##O(n) in time, O(n) in space
##152/315 cases passed
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height) < 3:
            return 0
        peak = self.findLocalPeak(height)
        print(peak)
        if len(peak) < 2:
            return 0
        totalArea = 0
        
        for i in range(len(peak)-1):
            temp = min(height[peak[i]],height[peak[i+1]])
            removeparts = 0
            for j in range(peak[i]+1,peak[i+1]):
                if height[j] > temp:
                    removeparts += temp
                else:
                    removeparts += height[j]
            area = (peak[i+1]-peak[i]-1)*temp - removeparts
            totalArea += area
        return totalArea
        
            
    def findLocalPeak(self,height):
        peaks = [0]
        i = 1
        lastMax = height[0]
        while i < len(height):
            
            if height[i] > height[peaks[-1]]:
                lastMax = height[i]
                peaks = peaks[:len(peaks)-1]
                peaks.append(i)
            if height[i] < height[peaks[-1]]:
                if height[peaks[-1]] == lastMax:
                    peaks.append(i)
                else:
                    peaks = peaks[:len(peaks)-1]
                    peaks.append(i)
            i += 1
        return peaks