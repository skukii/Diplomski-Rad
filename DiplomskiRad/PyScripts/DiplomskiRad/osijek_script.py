import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr

def split_and_correlation(df):
    wind = df[["u10", "v10", "wind-speed", "wind-dir"]]
    rain = df[["rain", "rain-rate", "crr", "tcrw"]]
    air_conditions = df[["sp", "out-hum", "dew-pt", "bar", "dew2m", "temp2m"]]
    temperature = df[["dew-pt", "dew2m", "temp2m", "max2mt", "min2mt", "temp-out", "hi-temp", "low-temp"]]

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

def osijek_script():
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

def osijek_merge():
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

    both = pd.merge(cop, pin, how='inner', on='date_full').drop_duplicates()

    # both.to_csv("cop_pin_osijek.csv")

split_and_correlation("cop_pin_osijek_clean.csv")
osijek_script()
osijek_merge()