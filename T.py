# 5 Parking Garage Program - Interactive Version

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










