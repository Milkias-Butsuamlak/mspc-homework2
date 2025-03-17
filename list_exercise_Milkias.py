from rich import print
# -

# ## Exercise
# Let's practice some list comprehension. These tasks were taken from [here](https://gist.github.com/ryanorsinger/f7d7c1dd6a328730c04f3dc5c5c69f3a) (go and give him a star ;)).

# +
# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())


# -

# **Exercise 1** - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]


uppercased_fruits=[fruit.upper() for fruit in fruits]
print("using list comprehension syntax:   ",uppercased_fruits)

# **Exercise 2** - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]


capitalized_fruits=[fruit.capitalize() for fruit in fruits]
print("Capitalized using list comprehension syntax:   ",capitalized_fruits)

# **Exercise 3** - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.


# +
# Define a set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# List comprehension to find fruits with more than two vowels
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if sum(1 for letter in fruit if letter in vowels)>2]

print("fruits with>2 vowels using list comprehension syntax:   ",fruits_with_more_than_two_vowels)
# -

# **Exercise 4** - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']


fruits_with_only_two_vowels= [fruit for fruit in fruits if sum(1 for letter in fruit if letter in vowels)==2]
print("fruits with 2 vowels using list comprehension syntax:   ",fruits_with_only_two_vowels)

# **Exercise 5** - make a list that contains each fruit with more than 5 characters


fruits_with_more_than_5_letters= [fruit for fruit in fruits if sum(1 for letter in fruit)>5]
print("fruits with>5 letters using list comprehension syntax:   ",fruits_with_more_than_5_letters)

# **Exercise 6** - make a list that contains each fruit with exactly 5 characters


fruits_with_5_letters= [fruit for fruit in fruits if sum(1 for letter in fruit)==5]
print("fruits with 5 letters using list comprehension syntax:   ",fruits_with_5_letters)

# **Exercise 7** - Make a list that contains fruits that have less than 5 characters


fruits_with_less_than_5_letters= [fruit for fruit in fruits if sum(1 for letter in fruit)<5]
print("fruits with<5 letters using list comprehension syntax:   ",fruits_with_less_than_5_letters)

# **Exercise 8** - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]


# +
number_of_charcters_per_fruit=[]
for fruit in fruits:
    count=0
    for letter in fruit:
        count=count+1
    number_of_charcters_per_fruit.append(count)
print("number of charcters per fruit: ", number_of_charcters_per_fruit)

# List comprehension
lc_number_of_charcters_per_fruit=[len(fruit) for fruit in fruits]
print("number of charcters per fruit using list comprehension: ", lc_number_of_charcters_per_fruit)
    
# -

# **Exercise 9** - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"


fruits_with_letter_a= [fruit for fruit in fruits if "a"  in fruit]
print("fruits with letter a using list comprehension:", fruits_with_letter_a)

# **Exercise 10** - Make a variable named even_numbers that holds only the even numbers 

even_numbers=[number for number in numbers if number%2 == 0]
print("even numbers using list comprehension: ", even_numbers)


# **Exercise 11** - Make a variable named odd_numbers that holds only the odd numbers


odd_numbers=[number for number in numbers if number%2 != 0]
print("odd numbers using list comprehension: ", odd_numbers)


# **Exercise 12** - Make a variable named positive_numbers that holds only the positive numbers


positive_numbers=[number for number in numbers if number > 0]
print("positive numbers using list comprehension: ", positive_numbers)


# **Exercise 13** - Make a variable named negative_numbers that holds only the negative numbers


negative_numbers=[number for number in numbers if number < 0]
print("positive numbers using list comprehension: ", negative_numbers)
