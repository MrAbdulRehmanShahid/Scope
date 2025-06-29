"""Iterating Over Strings and Counting Vowels"""
"""
word = "Python"
for letter in word:
    print(letter)
# Getting Index and Value:
for index, letter in  enumerate(word):
    print(f"Character {index} is {letter}")
# Modifying During Iteration:
for letter in word:
    print(letter.upper())
# Conditional Inside Loop
for letter in word:
    if letter == "h":
        print("Found h")
# Practice Challenge:
word1 = "Hello"
for index, letter in enumerate(word1):
    if letter == "l":
        continue
    print(f"{index} {letter}")

word = "Education"
vowel_count = 0
# Your code here
for char in word.lower():
    if char in "aeiou":
        vowel_count+= 1     
print(f"Total vowels: {vowel_count}") 


vowel_count = sum(1 for char in word.lower() if char in "aeiou")
vowel_counts = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
for char in word.lower():
    if char in vowel_counts:
        vowel_counts[char] += 1
print(f"Total vowels: {vowel_count}") 
"""

"""# Counting Vowels and Consonants
This code counts the number of vowels and consonants in a given text."""
text = "Hello World!"
vowels = 0
consonants = 0
for char in text.lower():
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
print(f"Total vowels: {vowels}")
print(f"Total consonants: {consonants}")
    








vowel_count = sum(1 for char in text.lower() if char in "aeiou")
vowel_counts = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
for char in text.lower():
    if char in vowel_counts:
        vowel_counts[char] += 1
consonants_count = sum(1 for char in text.lower()if char.isalpha() and char not in "aeiou")
consonants_counts = {'b':0, 'c':0, 'd':0, 'f':0, 'g':0, 'h':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
for char in text.lower():
    if char in consonants_counts:
        consonants_counts[char] += 1
print(f"Total vowels: {vowel_count}")
print(f"Total consonants: {consonants_count}")
from collections import defaultdict

counts = defaultdict(int)
for char in text.lower():
    if char.isalpha():
        counts[char] += 1
print("Vowel counts:", {k:v for k,v in counts.items() if k in "aeiou"})
print("Consonant counts:", {k:v for k,v in counts.items() if k not in "aeiou"})
