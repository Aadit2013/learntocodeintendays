#!/usr/bin/env python3
"""
Optimal Elevator Program - Fastest route to pick up and drop off all people
Uses SCAN algorithm to minimize travel distance
"""

def main():
    print("="*50)
    print("OPTIMAL ELEVATOR ROUTE PLANNER")
    print("="*50)
    
    # Get starting floor
    starting_floor = int(input("What floor is the elevator currently on? "))
    
    # Get number of people
    num_people = int(input("How many people need the elevator? "))
    
    people = []
    
    # Collect all people's current floors and destinations
    for i in range(1, num_people + 1):
        print(f"\nPerson {i}:")
        current_floor = int(input("  Current floor: "))
        destination_floor = int(input("  Destination floor: "))
        
        people.append({
            "person": i,
            "current": current_floor,
            "destination": destination_floor,
            "direction": "UP" if destination_floor > current_floor else "DOWN" if destination_floor < current_floor else "SAME"
        })
    
    # Separate people by direction
    going_up = [p for p in people if p["direction"] == "UP"]
    going_down = [p for p in people if p["direction"] == "DOWN"]
    going_same = [p for p in people if p["direction"] == "SAME"]
    
    # Sort by current floor to visit in optimal order
    going_up.sort(key=lambda x: x["current"])
    going_down.sort(key=lambda x: x["current"], reverse=True)
    
    # Create optimal route
    route = []
    total_floors = 0
    current_pos = starting_floor
    
    print("\n" + "="*50)
    print("OPTIMAL ELEVATOR ROUTE:")
    print("="*50)
    
    # First, go UP picking up people
    if going_up:
        print("\n[PHASE 1] Going UP")
        for person in going_up:
            floors_to_travel = abs(person["current"] - current_pos)
            total_floors += floors_to_travel
            current_pos = person["current"]
            print(f"  → Pick up Person {person['person']} at Floor {person['current']}")
            print(f"    (traveled {floors_to_travel} floors, total: {total_floors})")
        
        for person in going_up:
            floors_to_travel = abs(person["destination"] - current_pos)
            total_floors += floors_to_travel
            current_pos = person["destination"]
            print(f"  → Drop off Person {person['person']} at Floor {person['destination']}")
            print(f"    (traveled {floors_to_travel} floors, total: {total_floors})")
    
    # Then, go DOWN picking up people
    if going_down:
        print("\n[PHASE 2] Going DOWN")
        for person in going_down:
            floors_to_travel = abs(person["current"] - current_pos)
            total_floors += floors_to_travel
            current_pos = person["current"]
            print(f"  → Pick up Person {person['person']} at Floor {person['current']}")
            print(f"    (traveled {floors_to_travel} floors, total: {total_floors})")
        
        for person in going_down:
            floors_to_travel = abs(person["destination"] - current_pos)
            total_floors += floors_to_travel
            current_pos = person["destination"]
            print(f"  → Drop off Person {person['person']} at Floor {person['destination']}")
            print(f"    (traveled {floors_to_travel} floors, total: {total_floors})")
    
    # Handle same floor (no movement needed)
    if going_same:
        print("\n[PHASE 3] Same Floor (No movement)")
        for person in going_same:
            print(f"  → Person {person['person']} is already at destination (Floor {person['current']})")
    
    print("\n" + "="*50)
    print(f"TOTAL FLOORS TRAVELED: {total_floors}")
    print(f"FINAL ELEVATOR POSITION: Floor {current_pos}")
    print("="*50)
    
    # Draw elevator path diagram - EASY FORMAT
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + " "*15 + "🛗 ELEVATOR PATH DIAGRAM 🛗" + " "*15 + "█")
    print("█" + " "*58 + "█")
    print("█"*60)
    
    all_people = people
    all_floors = set([starting_floor] + [p["current"] for p in all_people] + [p["destination"] for p in all_people])
    max_floor = max(all_floors)
    min_floor = min(all_floors)
    
    # Create a map of which floors have which people
    pickup_floors = {}
    dropoff_floors = {}
    
    for p in all_people:
        if p["current"] not in pickup_floors:
            pickup_floors[p["current"]] = []
        pickup_floors[p["current"]].append(p["person"])
        
        if p["destination"] not in dropoff_floors:
            dropoff_floors[p["destination"]] = []
        dropoff_floors[p["destination"]].append(p["person"])
    
    # Draw diagram from top to bottom
    for floor in range(max_floor, min_floor - 1, -1):
        line = ""
        
        # Mark starting position
        if floor == starting_floor:
            line = f"  FLOOR {floor:2d}  |████████| START 🔴 "
        else:
            line = f"  FLOOR {floor:2d}  |████████|"
        
        # Mark pickups with BIG arrows
        if floor in pickup_floors:
            line += f"  ⬆️  PICK UP Person {pickup_floors[floor]} "
        
        # Mark dropoffs with BIG arrows
        if floor in dropoff_floors:
            line += f"  ⬇️  DROP OFF Person {dropoff_floors[floor]} "
        
        print(line)
        
        # Draw vertical movement arrows between floors
        if floor > min_floor:
            if floor in going_up or any(p["current"] == floor for p in going_up):
                print("            |    ⬆️⬆️⬆️    |")
            elif floor in going_down or any(p["current"] == floor for p in going_down):
                print("            |    ⬇️⬇️⬇️    |")
            else:
                print("            |           |")
    
    print("\n" + "█"*60)


if __name__ == "__main__":
    main()
