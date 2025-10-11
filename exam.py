
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

    # Check floor validity
    if floor < 1 or floor > max_floor:
        return f"Invalid floor, must be between 1 and {max_floor}"

    # Check slot validity
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

# Example usage:
print(park_car(garage, 1, 3, "ABC123"))  # Park a car
print(park_car(garage, 1, 3, "XYZ789"))  # Spot occupied
print(park_car(garage, 4, 2, "DEF456"))  # Invalid floor
print(park_car(garage, 2, 2, "ABC123"))  # Already parked



#5.1 Now fully interactive so you can:
# Choose the floor (1–3)
# Choose the slot (1–6)
# Enter your car’s registration number

# 5 Parking Garage Program - Interactive Version

# Initialize Garage: 3 floors × 6 spots per floor
garage = [["" for _ in range(6)] for _ in range(3)]
#list comprehension that creates a list of lists (a 2D list).
#The outer list: [...] for _ in range(3) → runs 3 times, once for each floor.
# The inner list runs 6 times → creating 6 elements (slots) per floor.

# Function: park_car
def park_car(garage: list[list[str]], floor: int, slot: int, car: str) -> str:
    max_floor = len(garage)
    max_slots = len(garage[0]) if max_floor > 0 else 0

    # Check floor validity
    if floor < 1 or floor > max_floor:
        return f"Invalid floor, must be between 1 and {max_floor}"

    # Check slot validity
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
        print(f"Floor {i}: {floor}")

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
