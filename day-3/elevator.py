#!/usr/bin/env python3
"""
Elevator program that calculates direction and floors traveled
"""

def main():
    # Get current floor and destination floor as input
    current_floor = int(input("Enter current floor: "))
    destination_floor = int(input("Enter destination floor: "))
    
    # Calculate the difference
    floors_traveled = abs(destination_floor - current_floor)
    
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
