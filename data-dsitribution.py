import matplotlib.pyplot as plt
import numpy as np

marks = np.array([70, 45, 98, 12])
names = np.array(["Thandokazi", "Masithembe", "Mzwandile", "Zipho"])

plt.bar(names, marks)
plt.show()
