"""
394.Decode String
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = '1234567890'
        # stack for nums, stack for letters
        stack_nums, stack_words, result, num = [], [], '', ''
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack_words.append(result)
                stack_nums.append(int(num))
                result, num = '', ''
            elif ch == ']':
                result = stack_words.pop() + stack_nums.pop() * result
            else:
                result += ch
        return result
