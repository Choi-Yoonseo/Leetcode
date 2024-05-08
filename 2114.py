class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(i.count(" ") for i in sentences)+1

        #i는 sentences를 순회하며 공백의 개수를 새는 역할을 해줌