import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr

def split_and_correlation(df):
    df["t2m"] = df["t2m"] - 273.15
    df["d2m"] = df["d2m"] - 273.15

    rain = df[["Rainfall.mean", "tcrw"]]
    rain.dropna()
    air_conditions = df[["Air moisture.mean", "d2m", "t2m"]]
    air_conditions.dropna()
    temperature = df[["Air temperature.mean","t2m"]]
    temperature.dropna()
    wind = df[["Wind speed.mean", "Wind direction.mean", "u10", "v10"]]
    wind.dropna()
    radiation = df[["cdir", "Global radiation.mean"]]
    radiation.dropna()

    rain.to_csv("pin_cop_sk_rain.csv")
    air_conditions.to_csv("pin_cop_sk_air_conditions.csv")
    temperature.to_csv("pin_cop_sk_temperature.csv")
    wind.to_csv("pin_cop_sk_wind.csv")
    radiation.to_csv("pin_cop_sk_rad.csv")

    corr_matrix = rain.corr()
    corr_matrix.to_csv("pin_cop_sk_rain_corr.csv")
    corr_matrix = air_conditions.corr()
    corr_matrix.to_csv("pin_cop_sk_air_conditions_corr.csv")
    corr_matrix = temperature.corr()
    corr_matrix.to_csv("pin_cop_sk_temperature_corr.csv")
    corr_matrix = wind.corr()
    corr_matrix.to_csv("pin_cop_sk_wind_corr.csv")
    corr_matrix = radiation.corr()
    corr_matrix.to_csv("pin_cop_sk_rad_corr.csv")

def novo_selo_script():
    data = xr.open_dataset('skenderovci.nc')
    df = data.to_dataframe()
    t = df["cdir"].index.levels[2]
    df["T"] = t

    data_pinova = pd.read_csv('Skenderovci.csv')

    pinova_for_correlation = data_pinova
    copernicus_for_correlation = df

    copernicus_for_correlation.to_csv("sk_cop_analysis.csv")
    pinova_for_correlation.to_csv("sk_pin_analysis.csv")



#novo_selo_script()

split_and_correlation(pd.read_csv("sk_pin_cop_merged.csv"))

