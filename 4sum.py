def sum3(nums,target = 0):
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n ):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate i
            for j in range(i + 1, n ):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicate j
                k, l = j + 1, n - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        # Skip duplicates for k
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        # Skip duplicates for l
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif total < target:
                        k += 1
                    else:
                        l -= 1
        return res
out = sum3([-2, -2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2, 2])
print(out)
