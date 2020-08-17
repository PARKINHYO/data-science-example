from matplotlib import pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

#fixme We can make multiple calls to plt.plot
#fixme to show multiple series on the same chart
plt.plot(xs, variance, 'g-', label='variance') #fixme green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2') #fixme red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error') #fixme blue dotted line

#fixme Because we'be assigned labels to each series,
#fixme we can get a legend for free (loc=9 means "top center")
plt.legend(loc=9)
plt.xlabel("model complexity" )
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.savefig('../image/viz_line_chard.png')
plt.show()
plt.gca().clear()
