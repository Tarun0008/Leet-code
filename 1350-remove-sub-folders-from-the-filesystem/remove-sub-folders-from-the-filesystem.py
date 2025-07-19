class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res=[]

        folder.sort()

        for s in folder:
            if not res or not s.startswith(res[-1] + '/'):
                res.append(s)
        return res
