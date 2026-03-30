import json

def load_data():
    with open("data.json") as f:
        return json.load(f)

def print_hospitals(hospitals):
    print("\nAvailable Hospitals:")
    for loc, info in hospitals.items():
        print(f"{info['name']} | Location: {loc} | Cost: {info['cost']} | Type: {info['type']}")

def normalize_location(user_input, graph):
    user_input = user_input.strip().lower()

    for loc in graph.keys():
        if loc.lower() == user_input:
            return loc

    return None