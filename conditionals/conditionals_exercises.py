# moths_in_house = False
# mitch_is_home = True

# if moths_in_house and mitch_is_home:
#     print("Hoooman! Help me get the moths!")
# elif not moths_in_house and not mitch_is_home:
#     print("No threats detected.")
# elif moths_in_house and not mitch_is_home:
#     print("Meooooooooooooow! Hissssss!")
# elif not moths_in_house and mitch_is_home:
#     print("Climb on Mitch.")
# else:
#     print("error in your code.")

# Teachers answer: can do nested. 
# if X
#   if Y
#   print()
# else etc 

## Q3, red light cameras.
from tokenize import Floatnumber


light_colour = "Red"
car_detected = True
# =: assignment, ==: comparison
if light_colour == "Red" and car_detected == True:
    print("Flash!")
else:
    print("Do nothing.")

## Q4
persons_height = 50
height_to_ride = 120

if persons_height >= height_to_ride:
    print("Hope on!")
elif persons_height < height_to_ride:
    print("Sorry, not today.")

##Q5
password = "password123"
username = "fleur"

if password == "password123" and username == "fleur":
    print("Correct!")
else:
    print("Incorrect.")

## Q6
### test an email validitiy. Must include '@' and '.' chars. 

email = "hayley@test.com"

if "@" not in email:
    if "." not in email:
        print("Invalid email")
    else:
        not email
        print("Incorrect email")
else:
    print("valid email address")

# Teachers answer:
if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")
