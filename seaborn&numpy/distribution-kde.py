import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")


# kde: Kernel density estimator（核密度估计）
def kde():
    sns.kdeplot(set_one, shade=True)
    sns.kdeplot(set_two, shade=True)
    sns.kdeplot(set_three, shade=True)
    sns.kdeplot(set_four, shade=True)

    plt.show()


# box plot: 箱形图
def box():
    sns.boxplot(data=df, x="label", y="value")
    plt.show()


# violin（小提琴图）结合kde和box。包线为kde，中间白点为median（中位数），中间黑粗线为interquartile range（四分位距）；confidence interval（置信区间）95%。
def violin():
    sns.violinplot(data=df, x="label", y="value")
    plt.show()


# kde()
# box()
violin()
