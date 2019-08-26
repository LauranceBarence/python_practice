# 最后运行超时
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# 120ms 15MB
# def two_sum(nums, target):
#     dict1 = {}
#     for index in range(len(nums)):
#         complement = target - nums[index]
#         if complement in dict1.keys():
#             return [dict1[complement], index]
#         dict1[nums[index]] = index


def two_sum(nums, target):
    h = {}
    for i, num in enumerate(nums):
        if (target - num) in h:
            return [h[target-num], i]
        h[num] = i

