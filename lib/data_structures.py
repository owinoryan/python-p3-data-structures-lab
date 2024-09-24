

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

# 1. get_names: Return a list of the names of each spicy food
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

# 2. get_spiciest_foods: Return spicy foods where heat level > 5
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

# 3. print_spicy_foods: Print the spicy foods formatted with heat level
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_emojis = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_emojis}')

# 4. get_spicy_food_by_cuisine: Find a spicy food by cuisine
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # In case no food matches the cuisine

# 5. print_spiciest_foods: Print only foods with heat level > 5
def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

# 6. get_average_heat_level: Return the average heat level of spicy foods
def get_average_heat_level(spicy_foods):
    total_heat_level = sum([food["heat_level"] for food in spicy_foods])
    return total_heat_level // len(spicy_foods)  # Integer division for an average

# 7. create_spicy_food: Add a new spicy food to the list
def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
