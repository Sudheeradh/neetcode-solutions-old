class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        trip1, trip2, trip3 = False, False, False
        for i in range(len(triplets)):
            if triplets[i][0] == target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                trip1 = True
            if triplets[i][1] == target[1] and triplets[i][0] <= target[0] and triplets[i][2] <= target[2]:
                trip2 = True
            if triplets[i][2] == target[2] and triplets[i][1] <= target[1] and triplets[i][0] <= target[0]:
                trip3 = True
        return trip1 and trip2 and trip3
        