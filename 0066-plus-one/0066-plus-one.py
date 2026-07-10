class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        into_int = int("".join(map(str, digits)))
        into_int += 1   
        print(into_int) 


        new_digits = []
        while into_int != 0:
            new_digits.append(into_int % 10)
            into_int //= 10   

        new_digits.reverse()
        return new_digits

        