#2 Hero vs Monster combat game

#Write a program that uses randomness and the random module to simulate a battle between a hero and a monster.
# Setup:
# Start by defining these variables:
# hero_hp = 10
# monster_hp = 20

# hero_min_attack = 5
# hero_max_attack = 8

# monster_min_attack = 3
# monster_max_attack = 12

# Battle rules:
# Repeat the following steps until either the hero or monster has hp < 1:
# Randomly decide who attacks (hero or monster).
# Randomly determine damage within the attacker’s attack range.
# Subtract the damage from the opponent’s HP.
# Print the attacker, the damage, and the remaining HP of the defender.

# Example output:
# Battle begins! Hero HP = 10, Monster HP = 20.
# Monster attacks and deals 5 damage.
# Hero now has 5 HP.
# Hero attacks and deals 6 damage.
# Monster now has 14 HP.
# ...
# Monster wins!

#.
# 3 Child Height Estimator


# A method to estimate a child’s adult height works as follows:
# 1. Add the mother’s and father’s heights.
# 2. If the child is a girl, subtract 13.
# 3. If the child is a boy, add 13.
# 4. Divide the result by 2.

# Example:
# If the mother’s height is 165 cm and the father’s is 189 cm:
# • For a girl: (165 + 189 − 13) / 2 = 170.5 cm
# • For a boy: (165 + 189 + 13) / 2 = 183.5 cm

# Implementation
# 1. Write a function
# def estimate_length(sex: str, mother: float, father: float) -> float:
# The function should return the estimated adult height (in cm) based on the child’s sex ("F" for girl, "M" for boy) and the parents’ heights.

# 2. Write another function
# def print_estimates(mother: float, father: float):
# This function should call estimate_length() twice — once for a girl and once for a boy — and print both estimated heights.

# 3. Test the functions
# Use mother = 165 and father = 189.
# The expected output should look like:
# Estimated height for girl: 170.5 cm
# Estimated height for boy: 183.5 cm

def estimate_length(sex: str, mother: float, father: float) -> float:
    # Step 1: Add mother’s and father’s heights
    total_height = mother + father

    # Step 2 and 3: Adjust the height based on the sex
    if sex == "F":  # If girl
        total_height -= 13
    elif sex == "M":  # If boy
        total_height += 13

    # Step 4: Divide by 2 to get the estimated adult height
    return total_height / 2


# 2. Write another function
def print_estimates(mother: float, father: float):
    # Ask the user for the child's sex (either 'M' or 'F')
    sex = input("Enter the child's sex ('F' for girl, 'M' for boy): ").strip().upper()

    # Validate input
    if sex not in ['F', 'M']:
        print("Invalid input. Please enter 'F' for girl or 'M' for boy.")
        return

    # Estimate and print heights for both a girl and a boy
    girl_height = estimate_length("F", mother, father)
    boy_height = estimate_length("M", mother, father)

    # Print the results
    print(f"Estimated height for girl: {girl_height} cm")
    print(f"Estimated height for boy: {boy_height} cm")


# 3. Test the functions with user input
# Ask the user to enter the mother's and father's heights
try:
    mother_height = float(input("Enter the mother's height in cm: "))
    father_height = float(input("Enter the father's height in cm: "))

    # Call the print_estimates function to display the results
    print_estimates(mother_height, father_height)
except ValueError:
    print("Invalid input. Please enter numerical values for heights.")


# 4 — Validating Airplane Callsigns


# Airplane callsigns follow this pattern:
# 1. Start with two or three uppercase letters (A–Z)
# 2. Followed by a dash (–)
# 3. Then three to five digits (0–9)

# Examples of valid callsigns:
# AX-1234
# FIN-12345
# SWE-123

# Examples of invalid callsigns:
# AX-12
# FIN-123456
# FIN-1234.0
# AX-123A
# FIN-!2345
# GETA-123
# FI-12345
# AX+1234

# Implementation
# Write a function: def validate_callsign(callsign: str) -> bool:
# The function should check whether a given callsign is valid and return a boolean value (True or False).

# Then show how to let the user enter a callsign (using input()), call validate_callsign(), and print a message based on the result.

# Example output:
# Enter a callsign: AX-1234
# Valid callsign

# Enter a callsign: GETA-123
# Invalid callsign

# Implementation
# Write a function: def validate_callsign(callsign: str) -> bool:
import re


def validate_callsign(callsign: str) -> bool:
    # Define the regular expression pattern for a valid callsign
    pattern = r'^[A-Z]{2,3}-\d{3,5}$'

    # Use re.match() to check if the callsign matches the pattern
    if re.match(pattern, callsign):
        return True
    else:
        return False


# Let the user enter a callsign (using input())
callsign = input("Enter a callsign: ").strip()

# Call validate_callsign() and print a message based on the result
if validate_callsign(callsign):
    print("Valid callsign")
else:
    print("Invalid callsign")



#5 Parking Garage Program


#Initialize Garage
#Create a 3×6 garage (3 floors, 6 spots per floor) as a list of lists of strings, with each spot initially empty ("").
#Function: park_car
#park_car(garage: list[list[str]], floor: int, slot: int, car: str) -> str
#Attempts to park a car (license plate) at the given floor and slot.

#Rules & Checks
#Only park in empty spots.
#A car cannot occupy multiple spots.
#Floors and slots must be within valid ranges.
#Works for any garage size.

#Return Messages
#"Invalid floor, must be between 1 and {max_floor}"
#"Invalid spot, must be between 1 and {max_slots}"
#"The spot is occupied"
#"[Reg. Number] is already parked"
#"[Reg. Number] is now parked"


# Initialize Garage: 3 floors × 6 spots per floor
garage = [["" for _ in range(6)] for _ in range(3)]

# Function: park_car
def park_car(garage: list[list[str]], floor: int, slot: int, car: str) -> str:
    max_floor = len(garage)
    max_slots = len(garage[0]) if max_floor > 0 else 0

    # Check floor validity (1-based index)
    if floor < 1 or floor > max_floor:
        return f"Invalid floor, must be between 1 and {max_floor}"

    # Check slot validity (1-based index)
    if slot < 1 or slot > max_slots:
        return f"Invalid spot, must be between 1 and {max_slots}"

    # Check if car is already parked
    for f in garage:
        if car in f:
            return f"{car} is already parked"

    # Check if spot is empty
    if garage[floor - 1][slot - 1] != "":
        return "The spot is occupied"

    # Park the car
    garage[floor - 1][slot - 1] = car
    return f"{car} is now parked"

# Interactive parking loop
while True:
    print("\n--- Parking Garage ---")
    for i, floor in enumerate(garage, start=1):
        floor_display = [spot if spot != "" else "[Empty]" for spot in floor]
        print(f"Floor {i}: {', '.join(floor_display)}")

    action = input("\nEnter 'park' to park a car or 'quit' to exit: ").lower()

    if action == "quit":
        print("Exiting program.")
        break
    elif action == "park":
        car = input("Enter car registration number: ")
        try:
            floor = int(input("Enter floor (1-3): "))
            slot = int(input("Enter slot (1-6): "))
        except ValueError:
            print("Floor and slot must be numbers.")
            continue

        message = park_car(garage, floor, slot, car)
        print(message)
    else:
        print("Invalid action. Type 'park' or 'quit'.")



# 6 — Birdwatching Log with Dictionary


# Write a program for birdwatchers.
# Use a dictionary to keep track of how many times each bird species has been observed.
# Use bird names as keys and their number of sightings as values.

# Start by initializing a dictionary named sightings with the following data:
# sightings = {
#     "Crow": 4,
#     "Pelican": 1
# }

# Implement the following functions

# 1. print_sightings(sightings: dict[str, int])
# Print all bird sightings in the following format.
# Be sure to use the correct singular or plural form (“observation” / “observations”).

# Example output:
# Crow: 4 observations
# Pelican: 1 observation

# 2. add_sighting(sightings: dict[str, int], bird: str)
# Add one observation for the given bird.
# If the bird isn’t already in the dictionary, add it with a starting count of 1.

# Test the functions
# Start with: print_sightings(sightings)
# Output:
# Crow: 4 observations
# Pelican: 1 observation
# Then: add_sighting(sightings, "Merganser")
# print_sightings(sightings)

# Output:
# Crow: 4 observations
# Pelican: 1 observation
# Merganser: 1 observation

# Finally: add_sighting(sightings, "Pelican")
# print_sightings(sightings)

# Output:
# Crow: 4 observations
# Pelican: 2 observations
# Merganser: 1 observation


# Initialize the sightings dictionary
sightings = {
    "Crow": 4,
    "Pelican": 1
}

# 1. Function to print all bird sightings
def print_sightings(sightings: dict[str, int]):
    for bird, count in sightings.items():
        # Use singular or plural form based on the count
        observation = "observation" if count == 1 else "observations"
        print(f"{bird}: {count} {observation}")

# 2. Function to add a sighting for a bird
def add_sighting(sightings: dict[str, int], bird: str):
    if bird in sightings:
        sightings[bird] += 1  # Increment the count if the bird is already in the dictionary
    else:
        sightings[bird] = 1  # Add the bird with an initial count of 1 if it's not in the dictionary

# Test the functions

# Print initial sightings
print("Initial bird sightings:")
print_sightings(sightings)

# Add a new bird sighting (Merganser)
print("\nAfter adding Merganser:")
add_sighting(sightings, "Merganser")
print_sightings(sightings)

# Add another sighting for an existing bird (Pelican)
print("\nAfter adding another sighting for Pelican:")
add_sighting(sightings, "Pelican")
print_sightings(sightings)