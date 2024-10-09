import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
df = pd.read_csv("adult.csv")
df.info()
sns.set(font_scale=1.5)
sns.catplot(x="relationship", y="age", data=df,
kind="point",hue='income',
capsize=0.4,ci=None,aspect=2)
plt.xticks(rotation=90)
plt.show()
sns.set(font_scale=1)
sns.relplot(x="educational-num", y="hours-per-week",
data=df, kind="line",row='income' ,
ci=None,
hue="relationship",
style="relationship",markers=True,dashes=False,aspect=2)
plt.show()