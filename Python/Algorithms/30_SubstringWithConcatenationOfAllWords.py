# Sliding window, utilizing collections.Counter
# Time:  O(n*m), where n is the length of string s and m is the word length
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_counts = Counter(words)
        l_word = len(words[0])
        l_words = len(words)
        l_comb = l_word * l_words
        indices = []
        for i in range(len(s)-l_comb+1):
            cnt = copy.copy(word_counts)
            for j in range(i, i+l_comb, l_word):
                sub = s[j:j+l_word]
                if sub in cnt and cnt[sub]:
                    cnt[sub] -= 1
                else:
                    break
            else:
                indices.append(i)
        return indices