
# Ask the user for their Earth weight
earth_weight = float(input("Enter your weight on Earth (in kg): "))

# Ask the user for the planet number
planet_number = int(input("Enter the planet number (1-7): "))

# Initialize weight_on_planet
weight_on_planet = 0

# Calculate the weight based on the selected planet's gravity
if planet_number == 1:
    weight_on_planet = earth_weight * 0.38
    planet_name = "Mercury"
elif planet_number == 2:
    weight_on_planet = earth_weight * 0.91
    planet_name = "Venus"
elif planet_number == 3:
    weight_on_planet = earth_weight * 0.38
    planet_name = "Mars"
elif planet_number == 4:
    weight_on_planet = earth_weight * 2.53
    planet_name = "Jupiter"
elif planet_number == 5:
    weight_on_planet = earth_weight * 1.07
    planet_name = "Saturn"
elif planet_number == 6:
    weight_on_planet = earth_weight * 0.89
    planet_name = "Uranus"
elif planet_number == 7:
    weight_on_planet = earth_weight * 1.14
    planet_name = "Neptune"
else:
    print("Invalid planet number.")
    exit()

# Print the result
print(f"Your weight on {planet_name} would be {weight_on_planet:.2f} kg.")