import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr

def split_and_correlation(df):
    df["t2m"] = df["t2m"] - 273.15
    df["d2m"] = df["d2m"] - 273.15
    df["skt"] = df["skt"] - 273.15

    rain = df[["Rainfall.mean", "tcrw"]]
    air_conditions = df[["Air moisture.mean", "d2m", "t2m"]]
    temperature = df[["Air temperature.mean","t2m"]]
    ground_temp = df[["Ground temperature.mean","skt"]]
    wind = df[["Wind speed.mean", "Wind direction.mean", "u10", "v10"]]
    radiation = df[["cdir_real", "Global radiation.mean"]]

    rain.to_csv("pin_cop_bu_rain.csv")
    air_conditions.to_csv("pin_cop_bu_air_conditions.csv")
    temperature.to_csv("pin_cop_bu_temperature.csv")
    ground_temp.to_csv("pin_cop_bu_soil.csv")
    wind.to_csv("pin_cop_bu_wind.csv")
    radiation.to_csv("pin_cop_bu_rad.csv")

    corr_matrix = ground_temp.corr()
    corr_matrix.to_csv("pin_cop_bu_soil_corr.csv")
    corr_matrix = rain.corr()
    corr_matrix.to_csv("pin_cop_bu_rain_corr.csv")
    corr_matrix = air_conditions.corr()
    corr_matrix.to_csv("pin_cop_bu_air_conditions_corr.csv")
    corr_matrix = temperature.corr()
    corr_matrix.to_csv("pin_cop_bu_temperature_corr.csv")
    corr_matrix = wind.corr()
    corr_matrix.to_csv("pin_cop_bu_wind_corr.csv")
    corr_matrix = radiation.corr()
    corr_matrix.to_csv("pin_cop_bu_rad_corr.csv")

def novo_selo_script():
    data1 = xr.open_dataset('budimci1.nc')
    data2 = xr.open_dataset('budimci2.nc')
    df1 = data1.to_dataframe()
    df2 = data2.to_dataframe()
    t1 = df1["cdir"].index.levels[2]
    t2 = df2["cdir"].index.levels[2]
    df1["T"] = t1
    df2["T"] = t2
    df3 = df1.append(df2, ignore_index=True)

    data_pinova = pd.read_csv('stanica_ Budimci.csv')

    pinova_for_correlation = data_pinova
    copernicus_for_correlation = df3

    copernicus_for_correlation.to_csv("bu_cop_analysis.csv")
    pinova_for_correlation.to_csv("bu_pin_analysis.csv")



novo_selo_script()

#split_and_correlation(pd.read_csv("bu_pin_cop_merged.csv"))

