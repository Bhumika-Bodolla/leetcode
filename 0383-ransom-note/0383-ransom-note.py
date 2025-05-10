from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_count=Counter(ransomNote)
        mag_count=Counter(magazine)

        for char in ransomNote:
            if ran_count [char]> mag_count.get(char,0):
                return False

        return True
        