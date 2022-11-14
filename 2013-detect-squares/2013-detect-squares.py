class DetectSquares:

    def __init__(self):
        self.pt_count = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pt_count[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        for px, py in self.pts:
            if (abs(px - x) != abs(py - y) or px == x or py == y):
                continue
            res += self.pt_count[(x,py)] * self.pt_count[(px, y)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)