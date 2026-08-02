def filterVowel(letter):
    vowels=['a','e','i','o','u']
    if(letter in vowels):
        return True
    else:
        return False
letters=['a','f','b','e','c']
filtered_vowels=filter(filterVowel,letters)
for vowel in filtered_vowels:
    print(vowel)


