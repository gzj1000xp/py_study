import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("survey.csv")
# print(df)

plt.figure(figsize=(12, 8))
ax1 = plt.subplot(1, 2, 1)
# estimator负责控制aggregate的类型：len为计数（count）；np.median为计算中位数；mean为平均值。
sns.barplot(data=df, x="Gender", y="Response", estimator=len)
# sns.barplot(data=df, x="Gender", y="Response", estimator=np.median)
plt.title("Count")

ax2 = plt.subplot(1, 2, 2)
# hue参数添加一个关键项，如下就是不同年龄段不同性别的response。
sns.barplot(data=df, x="Age Range", y="Response", hue="Gender")
plt.title("Age & Gender")

plt.show()
