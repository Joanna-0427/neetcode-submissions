class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''

        if key not in self.store:
            return res

        value = self.store[key]
        l, r = 0, len(value)-1
        while l <= r:
            mid = (l + r) // 2
            if value[mid][1] == timestamp:
                return value[mid][0]
            elif value[mid][1] < timestamp:
                res = value[mid][0]
                l = mid + 1
            elif value[mid][1] > timestamp:
                r = mid - 1
        return res
        
