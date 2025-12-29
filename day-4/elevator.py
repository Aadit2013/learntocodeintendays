#!/usr/bin/env python3
"""
Elevator program that calculates direction and floors traveled
"""

def main():
    # Get floor to ignore (optional)
    floor_to_ignore_input = input("Enter floor to ignore (press enter for none): ")
    floor_to_ignore = int(floor_to_ignore_input) if floor_to_ignore_input else None
    
    # Get current floor and destination floor as input
    current_floor = int(input("Enter current floor: "))
    destination_floor = int(input("Enter destination floor: "))
    
    # Calculate the difference
    floors_traveled = abs(destination_floor - current_floor)
    
    # Check if floor to ignore falls between current and destination floors
    if floor_to_ignore is not None:
        min_floor = min(current_floor, destination_floor)
        max_floor = max(current_floor, destination_floor)
        if min_floor < floor_to_ignore < max_floor:
            floors_traveled -= 1
    
    # Determine direction
    if destination_floor > current_floor:
        direction = "UP"
    elif destination_floor < current_floor:
        direction = "DOWN"
    else:
        direction = "SAME"
    
    # Display results
    print("\n" + "="*40)
    print(f"Current floor: {current_floor}")
    print(f"Destination floor: {destination_floor}")
    print(f"Direction: {direction}")
    print(f"Floors traveled: {floors_traveled}")
    print("="*40)


if __name__ == "__main__":
    main()
