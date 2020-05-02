# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for w in words:
            temp = chars
            hasWord = True
            for c in w:
                if c not in temp:
                    hasWord = False
                    break
                i = temp.index(c)
                temp = temp.replace(c, '', 1)
            if hasWord:
                result += len(w)
        return result


if __name__ == "__main__":
    print(Solution().countCharacters(["hello", "world", "leetcode"],
                                     "welldonehoneyr"))
