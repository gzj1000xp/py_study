from matplotlib import pyplot as plt


# 并列柱状图
def xvalue(n, t, d, w):
    # n = 1  # This is our first dataset (out of 2)
    # t = 2  # Number of datasets
    # d = 6  # Number of sets of bars
    # w = 0.8  # Width of each bar
    return [t * element + w * n for element in range(d)]


drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

store1_x = xvalue(1, 2, 6, 0.8)
plt.bar(store1_x, sales1)

store2_x = xvalue(2, 2, 6, 0.8)
plt.bar(store2_x, sales2)

# ax = plt.subplot()
# ax.set_xticks(range(len(drinks)))
# ax.set_xticklabels(drinks)


plt.show()
