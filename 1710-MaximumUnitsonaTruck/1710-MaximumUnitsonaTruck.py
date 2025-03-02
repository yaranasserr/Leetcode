from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Step 1: Sort boxes in descending order of units per box
        boxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        
        res = 0  # Stores the total number of units
        resbox = 0  # Tracks the number of boxes loaded
        
        # Step 2: Iterate over sorted boxes
        for num, units in boxes:
            if truckSize == 0:  # Stop if truck is full
                break

            # Step 3: Take as many boxes as we can (either all or what's left of truckSize)
            take = min(num, truckSize)  
            res += take * units  # Add units from these boxes
            truckSize -= take  # Reduce truck space

        return res  # Return the max units that can be loaded
