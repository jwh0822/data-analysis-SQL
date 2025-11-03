# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.
start_fuel_level = 0
num_astronauts = 0
shuttle_altitude = 0




# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 
start_fuel_level = int(input("Enter the starting fuel level: "))
while start_fuel_level <= 0 or start_fuel_level <= 5000 or start_fuel_level > 30000:
    print("Invalid Entry!")
    print("Enter a positive value between 5000 and 30000")
    start_fuel_level = int(input("Enter a positive number: "))
    




# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
num_astronauts = int(input("Enter the number of astronauts: ")) 
while num_astronauts < 1 or num_astronauts > 7:
    print("Invalid Entry!")
    print("Enter a number between 1 - 7")
    num_astronauts = int(input("Enter the number of astronauts: "))

  
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.
while start_fuel_level - 100 * num_astronauts > 0:
    shuttle_altitude += 50
    start_fuel_level -= 100 * num_astronauts


# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.
print(f"The shuttle gained an altitude of {shuttle_altitude}km and has {start_fuel_level}kg of fuel left.")

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”
if shuttle_altitude >= 2000:
    print("Orbit achieved!")
else:
    print("Failed to reach orbit")