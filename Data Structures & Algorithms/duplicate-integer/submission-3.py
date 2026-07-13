class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for number in nums:
            if number in vistos:
                return True
            vistos.add(number)
        return False