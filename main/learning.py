from typing import List



class Solution  :  
    def maxSubArray(self , nums: List[slice]  ) -> slice :
        cur_sum = 0
        max_sum = float('-inf')
        

        for i in nums:
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0 :
                cur_sum = 0
        return max_sum        

solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4 , -1, 2,2, -5 ,4]))




username = input("Enter a username : ")

if " " in username  :
    print("your username can't contain spaces")
else : 
    print(f"hello {username}")
