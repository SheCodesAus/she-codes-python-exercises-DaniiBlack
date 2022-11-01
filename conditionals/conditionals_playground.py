# var = None (None is aplaceholder to mitigate error messages in VS code)
# if using nested if statements, the code will get lost in the nest if the author doesn't bring it back properly.
# Ie. if ABC
#        if FYT
# else:
# ^^ Incorrect because the else is in the wrong place and the code will not know how to come back. 
is_raining = False
is_cold = True


print(type(is_raining))
print(type(is_cold))

print(is_raining)
print(is_cold)
print(is_raining and is_cold)
print(is_raining and not is_cold)


is_raining = True
is_cold = True 
print(is_raining)
print(not is_raining)
print(is_raining or is_cold)
print(is_raining and not is_cold)
print(is_raining or not is_cold)
print(not is_raining and not is_cold)

temperature = 16
print(temperature < 18)
wind_chill = 3
print(wind_chill > 4)
print(temperature - wind_chill < 16)
name = "Scarlett"
print(name == "Hayley")
print(name != "Hayley")

## if statements 
is_raining = False

# if 
if is_raining:
    print("Take an umbrella.")
else:
    print("Do not take an umbrella")

# if, elif, else
if temperature - wind_chill < 16:
    print("Take a jumper.")
elif temperature - wind_chill > 30:
    print("EUCK, it's so hot today, stay home.")
else:
    print("Wow, what a lovely day!")

# nested if statements 
if temperature - wind_chill < 16 and is_raining:
    print("Just stay home.")
else:
    if is_raining:
        print("You'll need an umbrella today.")
    if temperature - wind_chill < 16:
        print("You'll need a jumper today.")