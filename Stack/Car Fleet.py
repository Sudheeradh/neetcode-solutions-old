class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashMap = {}
        for i in range(len(position)):
            hashMap[position[i]] = speed[i]
        fin = []
        position.sort()
        fin.append(position[len(position) - 1])
        for i in range(len(position) - 2, -1, -1):
            t1 = (target - position[i])/hashMap[position[i]]
            t2 = (target - fin[-1])/hashMap[fin[-1]]
            
            if t1 > t2:
                fin.append(position[i])
        return len(fin)