from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ven-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# fixme bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# fixme so that each bar is centered
xs = [i+0.1 for i, _ in enumerate(movies)]
print(xs)
# fixme plt bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# fixme label x-axis with mobie names names at bar centers
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.savefig('../image/oscars.png')
plt.show()