words = ["race", "ecar", "meet", "em"]
anagrams = {}
for word in words:
   reverse_word=word[::-1]
   if reverse_word in words:
       anagrams[word] = (words.pop(words.index(reverse_word)))
print(anagrams)