"""sample script to show errors."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import perceptron
# from pudb import set_trace


df = pd.read_csv('https://archive.ics.uci.edu/ml/'
'machine-learning-databases/iris/iris.data', header=None)
# df.tail()

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

x = df.iloc[0:100, [0, 2]].values

ppn = perceptron.Perceptron(eta=0.1, n_iter=10)
ppn.fit(x, y)

plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.ylabel('Anzahl der Fehlklassifizierungen')
plt.show()
