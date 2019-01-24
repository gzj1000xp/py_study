from matplotlib import pyplot as plt

# 叠加柱状图
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

plt.bar(range(len(drinks)), sales1, label="Location 1")
plt.bar(range(len(drinks)), sales2, bottom=sales1, label="Location 2")
plt.legend()

ax1 = plt.subplot()
ax1.set_xticks(range(len(drinks)))
ax1.set_xticklabels(drinks)

plt.show()
