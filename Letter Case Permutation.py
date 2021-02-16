class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return [""]
        self.res = []
        self.dfs(S,0,"")
        return self.res
    
    def dfs(self, S, i, temp):
        if i == len(S):
            self.res.append(temp)
            return 
        if S[i].isdigit():
            self.dfs(S, i+1, temp + S[i])
        else:
            self.dfs(S,i+1, temp + S[i].lower())
            self.dfs(S, i+1, temp + S[i].upper())
