#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#
# https://leetcode.com/problems/encode-and-decode-strings/description/
# (Premium; solved on NeetCode's free mirror:
#  https://neetcode.io/problems/string-encode-and-decode)
#
# Design an algorithm to encode a list of strings to a single string. The
# encoded string is then decoded back to the original list of strings.
#
# Example 1: strs = ["neet","code","love","you"] -> ["neet","code","love","you"]
# Example 2: strs = ["we","say",":","yes"]       -> ["we","say",":","yes"]
#
# Constraints:
#   0 <= strs.length < 100
#   0 <= strs[i].length < 200
#   strs[i] contains only UTF-8 characters.
#
# @lc code=start

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        # header: where each word ends in the payload, e.g. "4,8,12,15#"
        endOffsets = []
        offset = 0
        for word in strs:
            offset += len(word)
            endOffsets.append(str(offset))

        return ",".join(endOffsets) + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        # the header is only digits and commas, so the first '#' ends it
        headerEnd = s.index("#")
        header = s[:headerEnd]
        payload = s[headerEnd + 1:]

        words = []
        start = 0
        if header:
            for end in header.split(","):
                words.append(payload[start:int(end)])
                start = int(end)

        return words

# @lc code=end
