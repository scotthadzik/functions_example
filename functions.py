# Conversion Calculator
# By: Scott Hadzik

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user

user_number = float(input("What number to convert? "))
user_unit = input("What unit is your number?")

if(user_unit == 'in'):
    #perform in to mm
    conv_number = user_number * 25.4
elif(user_unit == 'mm'):
    #perform mm to in
    conv_number = user_number / 25.4


print(conv_number)
print(user_unit)