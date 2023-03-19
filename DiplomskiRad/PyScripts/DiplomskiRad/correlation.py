import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cop_pin_osijek_clean.csv")

corr_matrix = df.corr()
sn.heatmap(corr_matrix, annot=True)
plt.show()
print(corr_matrix)
corr_matrix.to_csv("correlation_pin_cop_osijek.csv")