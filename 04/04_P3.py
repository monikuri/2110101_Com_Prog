vowel = 0
consonant = 0
s = input()
for c in s:
    if c.isalpha():
        if c.lower() in ['a','e','i','o','u']:
            vowel += 1
        else:
            consonant += 1
print(vowel, consonant)