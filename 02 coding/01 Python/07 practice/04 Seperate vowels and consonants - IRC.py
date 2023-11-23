# Seperate Vowels and Consonants

word = "aabcceeeddffggiiijkllopo"
print(word)

print("---------")

vowels = "aeiou"

separated_list = []
vowel_part = ""
consonant_part = ""
for each_char in word:
    # print(each_char)
    if each_char in vowels:
        if len(consonant_part) > 0:
            separated_list.append(consonant_part)
        consonant_part = ""
        vowel_part += each_char
    else:
        if len(vowel_part) > 0:
            separated_list.append(vowel_part)
        vowel_part = ""
        consonant_part += each_char
    
# Add the remaining parts after the loop
if len(consonant_part) > 0:
    separated_list.append(consonant_part)
elif len(vowel_part) > 0:
    separated_list.append(vowel_part)
    
print(separated_list)