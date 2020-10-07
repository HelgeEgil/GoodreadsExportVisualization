from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter
import pandas as pd
import numpy as np
import seaborn as sns

gr = pd.read_csv("goodreads_library_export.csv", delimiter=",", engine="python")

X = gr["Date Read"]
Y = gr["Original Publication Year"]
pg = gr["Number of Pages"]

na = (~pd.isna(X)) * (~pd.isna(Y)) * (~pd.isna(Y))

Y = Y[na]
X = X[na]
pg = pg[na]

X = pd.to_datetime(X)

Xdt = X.copy()

Y = np.array(Y, dtype=np.float64)
X = np.array(X.dt.year + X.dt.day/365, dtype=np.float64)

age = X - Y

age += 0.5 #

xinterval = [1, 3, 10, 30, 100, 300, 1000, 3000]

sns.scatterplot(Xdt, age, size=pg, alpha=0.6)

plt.xlabel("Finishing date")
plt.ylabel("Book age at reading [years]")
plt.yscale("log")
plt.grid(axis="y", alpha=0.5)

ax = plt.gca()
ax.set_yticks(xinterval)
ax.set_yticklabels(xinterval)
ax.yaxis.set_major_formatter(ScalarFormatter())

plt.show()
