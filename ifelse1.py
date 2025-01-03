# Input: A rating value
rating = float(input("Enter the rating (0 to 5): "))

# Rating system using if/elif/else
if rating > 4.5:
    print("Extraordinary")
elif rating > 4:
    print("Excellent")
elif rating > 3:
    print("Good")
elif rating > 2:
    print("Fair")
else:
    print("Poor")
