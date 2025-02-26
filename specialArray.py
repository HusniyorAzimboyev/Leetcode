def isArraySpecial(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ntype = ""
        for num in nums:
            if num%2==0:
                if ntype=="even":
                    return False
                ntype = "even"
            else:
                if ntype=="odd":
                    return False
                ntype = "odd"
        return True
print(isArraySpecial([1,4,3,8]))