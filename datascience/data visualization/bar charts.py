movies = ["Annie Hall", "Ven-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# fixme bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# fixme so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]
