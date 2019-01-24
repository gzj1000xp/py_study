from matplotlib import pyplot as plt

# 误差柱状图
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the bar graph here
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=15)

ax1 = plt.subplot()
ax1.set_xticks(range(len(drinks)))
ax1.set_xticklabels(drinks)

plt.show()
