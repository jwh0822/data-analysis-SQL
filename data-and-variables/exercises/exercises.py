# 1. Declare and assign the variables here:
shuttleName = "Determination"
shuttleSpeed = 17500
distMars = 225000000
distMoon = 384400
milesPerKM = 0.621
# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttleName))
print(type(shuttleSpeed))
print(type(distMars))
print(type(distMoon))
print(type(milesPerKM))

# Code your solution to exercises 3 and 4 here:
milesToMars = distMars * milesPerKM
hoursToMars = milesToMars / shuttleSpeed
daysToMars = hoursToMars / 24

print(shuttleName + " will take ")
print(daysToMars)
print("days to reach Mars.")
print("")
print("")

# Code your solution to exercise 5 here
milesToMoon = distMoon * milesPerKM
hoursToMoon = milesToMoon / shuttleSpeed
daysToMoon = hoursToMoon / 24
print(shuttleName + " will take ")
print(daysToMoon)
print("days to reach the Moon.")
