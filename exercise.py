import matplotlib.pyplot as plt
cities = ["East London", "Cape Town", "Kimberley", "Durban"]
rainfall = [140, 200, 120, 157]
x_pos = [i for i, _ in enumerate(cities)]
# making visuals and labeling
plt.bar(x_pos, rainfall, color="violet")
plt.xlabel(cities)
plt.ylabel("Rainfall in (mm)")
plt.title("Rainfall for the 4 main cities in SA")
plt.xticks(x_pos, cities)
plt.show()


# import numpy as np
#
#
# test_marks = [98, 78, 68, 73, 72, 97, 88, 60, 94, 95, 80, 73, 82]
#
# print(np.mean(test_marks)
