# The dictionary below contains several colour names and a counter (defaulted to 0).
# Your task is to iterate over a list of colours and keep track of the number of times 
# each colour has occurred by updating the corresponding counter in this dictionary

## Expected output:
# blue: 2
# green: 1
# yellow: 1
# red: 1
# purple: 3
# orange: 2

# Input:
colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}

colours = [
    "purple",
    "red",
    "yellow",
    "blue",
    "purple",
    "orange",
    "blue",
    "purple",
    "orange",
    "green"
]

## Expected output:
# blue: 3
# green: 5
# yellow: 3
# red: 1
# purple: 4
# orange: 4
## Input: 
# colours = [
#     "orange",
#     "purple",
#     "blue",
#     "yellow",
#     "green",
#     "green",
#     "purple",
#     "purple",
#     "green",
#     "blue",
#     "green",
#     "orange",
#     "purple",
#     "blue",
#     "green",
#     "orange",
#     "orange",
#     "red",
#     "yellow",
#     "yellow"
# ]
