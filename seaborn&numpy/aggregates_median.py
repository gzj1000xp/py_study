import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns


gradebook = pd.read_csv("gradebook.csv")
print(gradebook)
print(gradebook.columns)

assignment1 = gradebook[gradebook.assignment_name == "Assignment 1"]
print(assignment1)

asn1_median = np.median(assignment1.grade)
print(asn1_median)

# ci为误差计算算法，sd是standard deviation, 标准方差
sns.barplot(data=gradebook, x="assignment_name", y="grade", ci="sd")
plt.show()
