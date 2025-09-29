class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        neg = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)

        int_part = numerator//denominator
        remainder = numerator % denominator

        if remainder == 0:
            return ("-" if neg else "") + str(int_part)
        
        char = []
        seen = {}
        while remainder != 0:
            if remainder in seen:
                idx = seen[remainder]
                char.insert(idx,"(")
                char.append(")")
                break
            seen[remainder] = len(char)
            remainder *= 10
            digit = remainder // denominator
            char.append(str(digit))
            remainder = remainder % denominator

        out = str(int_part) + "." + "".join(char)
        if neg: out = "-" + out
        return out

print(Solution().fractionToDecimal(1, 2))
print(Solution().fractionToDecimal(2, 1))
print(Solution().fractionToDecimal(4, 333))