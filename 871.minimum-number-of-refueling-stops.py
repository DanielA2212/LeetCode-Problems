#
# @lc app=leetcode id=871 lang=python
#
# [871] Minimum Number of Refueling Stops
#

# @lc code=start
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        available_fuel = []
        stations.append([target, 0])
        stops = 0
        current_fuel = startFuel
        prev_location = 0
        
        for location, fuel in stations:
            distance = location - prev_location
            current_fuel -= distance
            
            while current_fuel < 0 and available_fuel:
                # Get the station with most fuel
                available_fuel.sort()
                current_fuel += available_fuel.pop()
                stops += 1
            
            if current_fuel < 0:
                return -1
            
            available_fuel.append(fuel)
            prev_location = location
        
        return stops
        
# @lc code=end

