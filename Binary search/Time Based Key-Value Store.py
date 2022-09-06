from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l, r = 0, len(self.data[key]) - 1
        while (l <= r):
            m = (l + r) // 2
            if (self.data[key][m][1] == timestamp):
                return self.data[key][m][0]
            if (timestamp >= self.data[key][m][1]):
                res = self.data[key][m][0]
                l = m + 1
            else:
                r = m - 1
        return(res)
        
        
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)