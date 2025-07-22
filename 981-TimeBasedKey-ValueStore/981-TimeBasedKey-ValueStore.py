# Last updated: 7/22/2025, 2:48:24 PM
class TimeMap:
    def __init__(self):
        self.store = {}       # key -> {timestamp: value}
        self.timestamps = {}  # key -> list of timestamps (in sorted order)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
            self.timestamps[key] = []
        self.store[key][timestamp] = value
        self.timestamps[key].append(timestamp)  # Assumes timestamps are added in order

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        times = self.timestamps[key]

      
        left, right = 0, len(times) - 1
        res_time = -1

        while left <= right:
            mid = (left + right) // 2
            if times[mid] <= timestamp:
                res_time = times[mid]
                left = mid + 1
            else:
                right = mid - 1

        if res_time == -1:
            return ""
        return self.store[key][res_time]
