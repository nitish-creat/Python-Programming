import numpy as np
import pandas as pd

math = np.array([85,90,78,92,99])
science = np.array([80,85,88,92,86])

df = pd.DataFrame({'Math' : math , 'Science' : science})
cov_matrix = df.cov()
print("Covariance Matrix:\n",cov_matrix)
corr_matrix = df.corr()
print("Correaltion matrix: ",corr_matrix)
print(df.describe())
