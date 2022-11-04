################## WHILE LOOPS ##################

################## Q1 ##################
# Continuously ask the user to enter a number until they provide a blank input.
# Output the sum of all the numbers.

## Input: 3
## Output:
# ## Enter a number: 3
# ## Enter a number:
# ## 3

# input = input("Enter a number: ")
# num = int(input("Enter a number: "))
# var = range(0, num, 1)
inputted = input("Enter a number ")
num = 0
while inputted != "":
    num += int(inputted)
    inputted = input("Enter a number: ")
print(num)


## Input: 1, 8, 7
## Output: 
# # ## Enter a number: 1
# ## Enter a number: 8
# ## Enter a number: 7
# ## Enter a number: 
# ## 16

## Input: nothing/ blank 
## Output: 
# ## Enter a number: 
# ## 0


################## Q2 ##################
# Ask user to enter a number. Print all the odd numbers between 0 and that number
## Input: 9
## Output:
# ## Enter a number: 9
# ## 1
# ## 3
# ## 5
# ## 7
# ## 9




################## Q3 ##################
# Select a number. Ask the user to enter a number, output whether their number is less than or greater than the selected number. 
# Repeat this process until the user guesses the correct number.
## Output:
# ## Guess the number: 1
# ## Too low!
# ## Guess the number: 40
# ## Too high!
# ## Guess the number: 20
# ## Too low!
# ## Guess the number: 30
# ## Too high!
# ## Guess the number: 25
# ## Correct!

