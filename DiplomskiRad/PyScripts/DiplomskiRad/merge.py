import pandas as pd

cop = pd.read_csv('os_cop_analysis.csv')
pin = pd.read_csv('os_pin_analysis.csv')

t = cop["time"].tolist()
date = []
year = '2017'
for d in t:
    helper = d.split()
    date = str(helper[0].split("-")[2]) + '.' + str(helper[0].split("-")[1]) + '.' + year + " " + str(helper[1])
cop["date_full"] = date

date_pinova = []
t2 = pin["date"].tolist()
t_time = pin["time"].tolist()

for d in range(len(t2)):
    helper = t2[d].split(".")
    date_pinova = str(helper[0]) + '.' + str(helper[1]) + '.' + year + " " + str(t_time[d])
pin["date_full"] = date_pinova

both = pd.merge(cop, pin, how = 'inner', on='date_full').drop_duplicates()
print(both)

#both.to_csv("cop_pin_osijek.csv")