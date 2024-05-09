class Solution:
    def countDigits(self, num: int) -> int:
        num_str = str(num)  # 숫자를 문자열로 변환
        total = 0

        for digit_char in num_str:
            digit = int(digit_char)  # 문자열을 다시 숫자로 변환
            if digit != 0 and num % digit == 0:  # 0으로 나누는 것은 불가능하므로 0은 제외
                total += 1

        return total