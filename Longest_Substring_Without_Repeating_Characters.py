class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word=''
        result =0
        for char in s:
            if char not in word:
                word += char
            else:
                if len(word)>result:
                    result=len(word)
                word = word[1::]
                if char in word:
                    while True:
                        if word[0]==char:
                            word = word[1::]
                            break
                        word = word[1::]
                word += char
        if len(word)>result:
            result=len(word)
        return result

