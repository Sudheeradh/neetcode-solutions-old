from collections import Counter, deque
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        unique = list(set(hand))
        unique.sort()
        unique = deque(unique)
        cnt = dict(Counter(hand))
        
        while unique:
            if cnt[unique[0]] == 0:
                del cnt[unique[0]]
                unique.popleft()
                continue
            
            for i in range(groupSize):
                if unique[0] + i not in cnt or cnt[unique[0] + i] <= 0:
                    return False
                cnt[unique[0] + i] -= 1
        
        for key in unique:
            return False
        
        return True
        