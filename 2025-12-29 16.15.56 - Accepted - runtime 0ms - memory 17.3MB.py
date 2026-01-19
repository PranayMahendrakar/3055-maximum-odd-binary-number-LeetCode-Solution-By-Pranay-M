class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeros = s.count('0')
        # Put ones-1 at the beginning, then all zeros, then 1 at the end
        return '1' * (ones - 1) + '0' * zeros + '1'