from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

# own imports
from Raschka.utils import plot_decision_regions


iris = datasets.load_iris()
x = iris.data[:, [2, 3]]
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=1, stratify=y)

sc = StandardScaler()
sc.fit(x_train)
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)

# x_combined = np.vstack((x_train, x_test))
# y_combined = np.hstack((y_train, y_test))

x_combined_std = np.vstack((x_train_std, x_test_std))
y_combined = np.hstack((y_train, y_test))

lr = LogisticRegression(C=100.0, random_state=1)
lr.fit(x_train_std, y_train)
plot_decision_regions(x_combined_std, y_combined, classifier=lr, test_idx=range(105, 150))

plt.xlabel('Länge eines Blütenblatts')
plt.ylabel('Breite eines Blütenblatts')
plt.legend(loc='upper left')
# plt.show()

result = lr.predict_proba(x_test_std[:3, :]).argmax(axis=1)

print(result)