from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# fixme create a line chart, years on x-axis, gdp on
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title("Nominal GDP")

# fixme add a label to the y-axis
plt.ylabel("Billions of $")

# fixme save the file
plt.savefig('../image/viz_gdp.png')

plt.show()

# fixme Get the current Axes and clear
plt.gca().clear()

