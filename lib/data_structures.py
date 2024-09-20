spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    max_heat = max(food["heat_level"] for food in spicy_foods)
    return [food for food in spicy_foods if food["heat_level"] == max_heat]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) - Heat Level: {food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if food["cuisine"].lower() == cuisine.lower()]

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        print(f"{food['name']} ({food['cuisine']}) - Heat Level: {food['heat_level']}")

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)

# Example usage:
print(get_names(spicy_foods))  # ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']
print(get_spiciest_foods(spicy_foods))  # [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}]
print_spicy_foods(spicy_foods)
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))  # [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}]
print_spiciest_foods(spicy_foods)
print(get_average_heat_level(spicy_foods))  # 6.0

# Adding a new spicy food
create_spicy_food(spicy_foods, {"name": "Sichuan Hot Pot", "cuisine": "Sichuan", "heat_level": 10})
print_spicy_foods(spicy_foods)  # Check updated list
