class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counts=Counter(arr).values()
        if len(counts)==len(set(counts)):
            return True
        else:
            return False