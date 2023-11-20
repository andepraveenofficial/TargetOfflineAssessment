# Print a to z

my_dictionary = dict()

for counter in range(ord("a"), ord("z")+1):
    my_dictionary[chr(counter)] = counter

print(my_dictionary)    