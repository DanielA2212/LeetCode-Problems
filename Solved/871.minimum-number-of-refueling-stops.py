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

        # A list to keep track of available fuel from passed stations
        available_fuel = []
        
        # The target is added as a station with 0 fuel to handle the final distance
        stations.append([target, 0])
        

        stops = 0
        current_fuel = startFuel
        prev_location = 0
        
        # Going through each station
        for location, fuel in stations:

            # Calculate distance to current station
            distance = location - prev_location

            # Deduct fuel for the distance traveled
            current_fuel -= distance
            
            # If we run out of fuel, use fuel from previous stations
            while current_fuel < 0 and available_fuel:

                # Sort and take the largest available fuel amount
                available_fuel.sort()
                current_fuel += available_fuel.pop()
                stops += 1  # Stop count
            
            # If we still don't have enough fuel after using all available fuel
            if current_fuel < 0:
                return -1
            
            # Current station's fuel is added to available fuel
            available_fuel.append(fuel)

            # Previous location is updated to current station
            prev_location = location
        
        return stops
        
# @lc code=end

