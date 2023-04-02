import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr

def split_and_correlation(df):
    rain = df[["rain", "tcrw"]]
    air_conditions = df[["air-hum", "dew2m", "temp2m"]]
    temperature = df[["air-temp-1.8m-2m","dew2m","temp2m"]]
    soil = df[["soil-temp","soil1","soil2","soil3","soil4"]]

    rain.to_csv("pin_cop_ns_rain.csv")
    air_conditions.to_csv("pin_cop_ns_air_conditions.csv")
    temperature.to_csv("pin_cop_ns_temperature.csv")
    soil.to_csv("pin_cop_ns_soil.csv")

    corr_matrix = soil.corr()
    corr_matrix.to_csv("pin_cop_ns_soil_corr.csv")
    corr_matrix = rain.corr()
    corr_matrix.to_csv("pin_cop_ns_rain_corr.csv")
    corr_matrix = air_conditions.corr()
    corr_matrix.to_csv("pin_cop_ns_air_conditions_corr.csv")
    corr_matrix = temperature.corr()
    corr_matrix.to_csv("pin_cop_ns_temperature_corr.csv")

def novo_selo_script():
    data = xr.open_dataset('novi_rok.nc')
    df = data.to_dataframe()

    data_pinova = pd.read_excel('NovoSeloRok-Pinova.xlsx')
    data_pinova = data_pinova[["dateandtime", "air-temp-1.8m-2m", "air-hum", "air-temp-1m", "soil-temp", "rain"]]

    df.to_csv("novo-selo-cop.csv")

    pinova_for_correlation = data_pinova
    copernicus_for_correlation = df

    copernicus_for_correlation.to_csv("ns_cop_analysis.csv")
    pinova_for_correlation.to_csv("ns_pin_analysis.csv")

def novo_selo_merge():
    cop = pd.read_csv('ns_cop_analysis.csv')
    pin = pd.read_csv('ns_pin_analysis.csv')

    t = cop["time"].tolist()
    date = []
    year = '2019'
    for d in t:
        helper = d.split()
        date_helper = str(helper[0].split("-")[2]) + '.' + str(helper[0].split("-")[1]) + '.' + year + " " + str(helper[1])
        date.append(date_helper)
    cop["date_full"] = date

    date_pinova = []
    t2 = pin["dateandtime"].tolist()
    hour_pinova = []

    for d in range(len(t2)):
        helper = t2[d].split(".")
        date_pinova_helper = str(helper[0]) + '.' + str(helper[1]) + '.' + year + " " + str(helper[-1])
        date_pinova.append(date_pinova_helper)
        hour_pinova.append(str(str(helper[-1]).split(":")[1]))
    pin["date_full"] = date_pinova
    pin["hour_full"] = hour_pinova

    cop.to_csv("ns_cop_analysis_clean.csv")
    pin.to_csv("ns_pin_analysis_clean.csv")

    #both = pd.merge(cop, pin, how='inner', on='date_full'.values()).drop_duplicates()

    #both.to_csv("cop_pin_novoselorok.csv")

novo_selo_script()
novo_selo_merge()

split_and_correlation(pd.read_csv("ns_cop_pin_merged.csv"))