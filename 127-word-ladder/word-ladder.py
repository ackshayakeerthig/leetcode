class Solution:
    def ladderLength(self, beginWord: str, endWord: str, words: List[str]) -> int:
        words=set(words)
        if endWord not in words:
            return 0
        q=deque()
        q.append((beginWord,1))
        
        n=len(words)
        k=len(beginWord)
        # if k==1:
        #     return 2 if endWord in words else 0
        visited=set()
        visited.add(beginWord)

        while ( q):
            current,trans=q.popleft()
            visited.add(current)
            if current==endWord:
                return trans
            for i in range(len(current)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newword=current[:i]+ch+current[i+1:]
                    if newword in words and newword not in visited:
                        q.append((newword,trans+1))
        return 0

