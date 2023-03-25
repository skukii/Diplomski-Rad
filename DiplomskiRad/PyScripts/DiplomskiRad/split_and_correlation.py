import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cop_pin_osijek_clean.csv")

wind = df[["u10", "v10", "wind-speed","wind-dir"]]
rain = df[["rain", "rain-rate", "crr", "tcrw"]]
air_conditions = df[["sp", "out-hum", "dew-pt", "bar", "dew2m", "temp2m"]]
temperature = df[["dew-pt", "dew2m", "temp2m", "max2mt", "min2mt", "temp-out","hi-temp","low-temp"]]


wind.to_csv("pin_cop_osijek_wind.csv")
rain.to_csv("pin_cop_osijek_rain.csv")
air_conditions.to_csv("pin_cop_osijek_air_conditions.csv")
temperature.to_csv("pin_cop_osijek_temperature.csv")

corr_matrix = wind.corr()
corr_matrix.to_csv("pin_cop_osijek_wind_corr.csv")
corr_matrix = rain.corr()
corr_matrix.to_csv("pin_cop_osijek_rain_corr.csv")
corr_matrix = air_conditions.corr()
corr_matrix.to_csv("pin_cop_osijek_air_conditions_corr.csv")
corr_matrix = temperature.corr()
corr_matrix.to_csv("pin_cop_osijek_temperature_corr.csv")

