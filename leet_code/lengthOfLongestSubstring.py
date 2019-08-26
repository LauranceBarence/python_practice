import time


# 70ms
class Solution:
    def lengthOfLongestSubstring(self, s):
        hash_dict = {}
        max = 0
        start = 0
        for index, str_ in enumerate(s):
            if (str_ in hash_dict) and (hash_dict[str_] >= start):
                lth = index - start
                max = lth if lth > max else max
                start = hash_dict[str_] + 1
            hash_dict[str_] = index
        lth = len(s) - start
        max = lth if lth > max else max
        end = time.process_time()
        return max


solution = Solution()
print(solution.lengthOfLongestSubstring('pwwkew'))

# 140ms
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         hash_dict = {}
#         max = 0
#         i = 0
#         j = 0
#         while j < len(s):
#             if s[j] in hash_dict.keys():
#                 i = hash_dict[s[j]] if hash_dict[s[j]] > i else i
#             max = max if max > (j - i + 1) else (j - i + 1)
#             hash_dict[s[j]] = j + 1
#             j += 1
#         return max
