# Retsepile Koloko


import numpy as np
# import scipy as stats
from scipy import stats
# quartile

# Input of Data


marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]

# Calculating The Mean


my_mean = np.mean(marks_of_students)

# Next is the median


my_median = np.median(marks_of_students)

# Calculation of the mode


my_mode = stats.mode(marks_of_students)

# Calculating the Range


my_range = np.ptp(marks_of_students)

# Calculating the percentile


my_gentile = np.percentile(marks_of_students, 25)

print(my_mean)
print(my_median)
print(my_mode)
print(my_range)
print(my_gentile)
