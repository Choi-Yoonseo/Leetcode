class Solution:
    def minimumSum(self, num: int) -> int:
        #정수의 자리를 그대로 가져다가 쓰는 방법이 없어서, 각각 문자로 바꾸고 리스트의 한 엘리먼트로 설정
        num=str(num)
        num=list(num)
        num.sort()
        a=num[0]+num[2]
        b=num[1]+num[3]
        
        return int(a) + int(b)
