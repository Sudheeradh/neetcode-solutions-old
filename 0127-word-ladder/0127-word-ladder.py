from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        hmap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                hmap[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighbour in hmap[pattern]:
                        if neighbour not in visited:
                            q.append(neighbour)
                            visited.add(neighbour)
            res += 1
        return 0