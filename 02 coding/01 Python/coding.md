
##### Important Topics
* Concatenation
* Repetition
* Indexing
* Membership Check
* String Format
* Slicing
* Iteration

##### Core Topics
* Conditional Control Statements
    - `if`
    - `elif`
    - `else` 
* Looping Control Statements
    - `for`
    - `while`
       * Flow control statements
          - `continue` 
          - `break`   
* Functions
   - `def`  => Named Function
   - `lambda` => Anonymous Function
* `pass` 
    - When it is executed, nothing happens.   
    - we can create empty functions, empty conditional statements, empty looping statements.

##### String Methods
* Verification
   - `isdigit()`
   - `islower()`
   - `isupper()`
   - `isalpha()`
   - `isalnum()`
   - `startswith()`
   - `endswith()` 
* Conversion
   - `lower()`
   - `upper()`
   - `swapcase()`
* Updation
   - `strip()`
   - `replace()` 
   - `split()`
* Counting
  - `count()`
* Finding
  - `index()`  

##### Float Methods
* `round(number, digits)`


##### List Methods
* `append()` => adds an element to the end of the list.
* `extend()` => adds all the elements of the sequence to the end of the list.
* `insert(index, value)` => element inserted to the list at specified index.
* `pop()` => removes last element
* `remove()` => removes the first matching element from the list
* `clear()` => removes all the items from the list & it gives Empty List
* `count()` => returns the number of elements with the specified value
* `index()` => returns the index of first matching element from the list
* `sort()` => arrange in ascending order
* `join()` => The `join()` takes all the items in a sequence of strings and joins them into one string.
   - `sentence = "joiner".join(sequence)` 


##### Tuple Methods
Tuple Doesn't have any methods.

##### Set Methods
* `add()` => adds the item to the set, if  the item is not present already.
* `update()` => add multiple items to the set.
* `discard()` => takes a single value and removes if present.
* Set Operations
  -  `union`  => `|`
     -  union of two sets is a set containing all elements of both sets. 
  - `intersection` => `&`
    - intersection of two sets is a set containing common elements of both sets.
  - `difference` => `-`
    - difference of two sets is a set containing all the elements in the first set but not second.
  - `symmetric_difference` => `^`
    -  symmetric_difference of two sets is a set containing all elements which are not common to both sets.
* Set Comparisons
   -  `issubset()` => It returns True if all elements of second set are in  first set, else False.
   -  `issuperset()` = It returns True if all elements of second set are in  first set, else False.
   -  `isdisjoint()` => It returns True when no common elements, else False.   


##### Dictionaries Methods
* `get()` => The `get()` method returns `None` if the key is not found.
  - `my_dictionary.get("key")`
* use Square brackets  => when we use the square brackets [] to access the key-value, keyError is raised in case key is not found in the dictionary.
  - `my_dictionary["key"]`
* adding a key-value pair
   -  `my_dictionary["key"] = value`
* modifying existing items 
   -  `my_dictionary["key"] = value` 
* deleting an existing items
   -  `del my_dictionary["key"]` \
* Dictionary Views
  - `keys()` => `keys()` method returns a view object of the type dict_keys that holds a list of all keys
  - `values()` => `values()` method returns a view object that displays a list of all the values in the dictionary.
  - `items()` => `items()` method returns a view object that displays a list of dictionary's key-value tuple pairs.


##### Built-in Functions
* len() => find number of items/characters in a sequence
* round()
* id()
* min()
* max()
* sum()
* sorted() => it creates a new sorted list
* range()
* reversed()
* all()
* any()
* enumarate()
* unicode
   -  chr()
   -  ord()


##### Higher Order Functions
* map(function, sequence)
* filter(function, sequence)
* reduce(function, sequence)

##### libraries
```Python 
# libraries
# Import Library

print("----permutations, combinations-------")

from itertools import permutations, combinations


my_list = [1,2,3,4,5]

from itertools import permutations, combinations

items = [1,2,3,4]

# permutations
items = [1, 2, 3, 4]
my_permutations = list(permutations(my_list))
print(my_permutations)

# combinations
my_combinations = list(combinations(my_list, 3))
print(my_combinations)

print("----reduce-------")
# reduce() function is defined in the functools module.
# reduce function takes first two items of a sequence as arguments.
# reduce(function_name, sequence)

from functools import reduce


def sum_of_numbers(acc, curr):
    return acc + curr


my_list = [1, 2, 3, 4, 5, 6]
sum_of_list = reduce(sum_of_numbers, my_list)
print(sum_of_list)  # 21


print("----copy, deepcopy---")

import copy
# A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements. 

original_list = [1, [2, 3], 4]

shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)  


# Modify the shallow copy
shallow_copy[0] = 100
shallow_copy[1][0] = 200

# Modify the deep copy
deep_copy[0] = 1000
deep_copy[1][0] = 2000

print(original_list)  # [100, [200, 3], 4]
print(shallow_copy)  # [100, [200, 3], 4]
print(deep_copy)     # [1000, [2000, 3], 4]

print("==================")

```


##### del
* we can delete a variable.  
* `del` is a statement that is used to delete an item at a specific index from a list. If the specified index does not exist, it raises an IndexError. 
```Python 
my_list = [1, 2, 3, 2]
del my_list[1]

del my_list

```

It is recommended to use `remove` when you want to remove an item by its value and `del` when you want to remove an item by its index.


