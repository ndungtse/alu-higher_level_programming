#!/usr/bin/python3
word = "object-oriented programming with Python"
# rebuild the sentence using slices of word only
word = word[:15] + word[15:31] + word[31:]
print(word)
