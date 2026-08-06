class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        end = len(nums)

        while i < end:
            if nums[i] == val:
                end -= 1
                nums[i] = nums[end]
            else:
                i += 1

        return end
        

