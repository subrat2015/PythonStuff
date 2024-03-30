from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in map:
                return map[diff], i
            map[n] = i
obj = TwoSum()
myList = [2,7,11,15]
obj.twoSum(myList,9)
