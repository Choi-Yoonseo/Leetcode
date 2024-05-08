class Solution:
    def scoreOfString(self, s: str) -> int:
        res=0
        for i in range(1,len(s)):
            res+=abs(ord(s[i]) - ord(s[i-1]))
            
            #아스키코드, abs, #i번째와 i-1번째의 아스키코드의 값을 빼서 절댓값처리
        return res