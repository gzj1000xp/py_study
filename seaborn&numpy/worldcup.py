from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# fig1
df = pd.read_csv("WorldCupMatches.csv")

# DataFrame添加列
df["Total Goals"] = df["Home Team Goals"] + df["Away Team Goals"]
print(df.head(10))
sns.set_style("whitegrid")
sns.set_context("poster", font_scale=0.6)
f, ax = plt.subplots(figsize=(12, 7))
# ax = sns.barplot(data=df, x="Year", y="Total Goals")
ax = sns.barplot(data=df, x="Year", y="Total Goals")
ax.set_title("Goals in each match")

# plt.show()

# fig2
df_goals = pd.read_csv("goals.csv")
print(df_goals.head())
sns.set_context("notebook", font_scale=1.25)
sns.set_palette("Spectral")
f,ax2 = plt.subplots(figsize=(12, 7))
ax2 = sns.boxplot(x=df_goals["year"], y=df_goals["goals"])
ax2.set_title("Goals")

plt.show()
