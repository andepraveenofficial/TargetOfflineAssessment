# Seperate Vowels and Consonants

word = "aabcceeeddffggiiijkllop"
print(word)

print("-------------")

vowels = "aeiou"

separated_list = []
add_word = ""
for counter in range(len(word)):
    each_char = word[counter]
    # print(each_char)

    if each_char in vowels:
        # print(each_char)
        add_word += each_char
        if counter < len(word)-1:
            next_letter = word[counter+1]
            if next_letter in vowels:
                pass
            else:
                separated_list.append(add_word)
                add_word = ""
        else:
            separated_list.append(add_word)

    else:
        # print(each_char)
        add_word += each_char
        if counter < len(word)-1:
            next_letter = word[counter+1]
            if next_letter not in vowels:
                pass
            else:
                separated_list.append(add_word)
                add_word = ""
        else:
            separated_list.append(add_word)

print(separated_list)

