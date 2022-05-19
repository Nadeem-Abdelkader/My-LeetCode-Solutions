class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = [int(i) for i in str(x)]
        if res == res[::-1]:
            return True
        else:
            return False

        