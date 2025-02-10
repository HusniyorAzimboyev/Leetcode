def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):  # Exclude last index
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:  # Need to jump
                jumps += 1
                current_end = farthest
                
        return jumps