age = 90
height = 120

# and
if age >= 8 and height >= 135:
    print("You can ride the ride!")
    
# or
if age >= 17 or height >= 160:
    print("You can ride super ride!")

# elif (else if)
if height < 120:   #below 120, too short
    print("You can't ride any rides :(")
elif height < 135: #above 120 but lower than 135
    print("You can ride level-1 rides.")
elif height < 200: #above 135 but lower than 200
    print("You can ride any ride!")
else:              #above 200, too tall
    print("Too tall to ride the rides:(")