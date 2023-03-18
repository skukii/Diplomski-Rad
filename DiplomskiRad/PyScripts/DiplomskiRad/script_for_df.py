import pandas as pd
import numpy as np
import xarray as xr


data = xr.open_dataset('osijek-coperrnicus.nc')
df = data.to_dataframe()


data_pinova = pd.read_excel('Osijek-Pinova.xlsx')
data_pinova = data_pinova[["date", "time", "temp-out", "hi-temp", "low-temp", "out-hum", "dew-pt",
       "wind-speed", "wind-dir", "bar", "rain",
       "rain-rate"]]


df.to_csv("osijek-cop.csv")


pinova_for_correlation = data_pinova[(data_pinova.date != '12.07.17') & (data_pinova.date != '27.07.17')]
copernicus_for_correlation = df.iloc[24:]
copernicus_for_correlation = copernicus_for_correlation.iloc[:-24]
print(pinova_for_correlation)
print(copernicus_for_correlation)

copernicus_for_correlation.to_csv("os_cop_analysis.csv")
pinova_for_correlation.to_csv("os_pin_analysis.csv")