from bfs import bfs
from ucs import ucs
from utils import load_data, print_hospitals

data = load_data()
graph = data["locations"]
hospitals = data["hospitals"]

def menu():
    print("\n===== Smart Hospital Finder 🚀 =====")
    print("1. Find Nearest Hospital (BFS)")
    print("2. Find Cheapest Hospital (UCS)")
    print("3. View Hospitals")
    print("4. Emergency Mode 🚑")
    print("5. Exit")

def choose_type():
    print("\nSelect Hospital Type:")
    print("1. Government")
    print("2. Private")
    print("3. All")

    t = input("Enter choice: ")

    if t == "1":
        return ["Government"]
    elif t == "2":
        return ["Private"]
    else:
        return None  # All

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "5":
        print("Thank you for using Smart Hospital Finder!")
        break

    if choice == "3":
        print_hospitals(hospitals)
        continue

    # Select location
    locations_list = list(graph.keys())

    print("\nAvailable Locations:")
    for i, loc in enumerate(locations_list, start=1):
        print(f"{i}. {loc}")

    loc_choice = input("Select location (number): ")

    if not loc_choice.isdigit():
        print("❌ Invalid input!")
        continue

    loc_choice = int(loc_choice)

    if loc_choice < 1 or loc_choice > len(locations_list):
        print("❌ Invalid selection!")
        continue

    start = locations_list[loc_choice - 1]

    # Type filter
    allowed_types = choose_type()

    # BFS
    if choice == "1":
        node, path = bfs(graph, start, hospitals, allowed_types)

        if node:
            print(f"\n✅ Nearest Hospital: {hospitals[node]['name']} at {node}")
            print("Path:", " → ".join(path))
        else:
            print("No hospital found")

    # UCS
    elif choice == "2":
        node, cost, path = ucs(graph, start, hospitals, allowed_types)

        if node:
            print(f"\n💰 Cheapest Hospital: {hospitals[node]['name']} at {node}")
            print(f"Total Cost: {cost}")
            print("Path:", " → ".join(path))
        else:
            print("No hospital found")

    # Emergency Mode
    elif choice == "4":
        node, path = bfs(graph, start, hospitals)

        if node:
            print(f"\n🚑 EMERGENCY! Nearest Hospital: {hospitals[node]['name']} at {node}")
            print("Path:", " → ".join(path))
        else:
            print("No hospital found")

    else:
        print("❌ Invalid choice!")