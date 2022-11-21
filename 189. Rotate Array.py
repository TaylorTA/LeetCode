class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        changed = set()
        def change(i1, m, t):
            temp = nums[(i1+m)%len(nums)]
            nums[(i1+m)%len(nums)] = t
            changed.add(i1)
            if (i1+m)%len(nums) not in changed:
                change((i1+m)%len(nums), m, temp)

        m = k % len(nums)
        for i in range(len(nums)):
            if i not in changed:
                change(i, m, nums[i])
