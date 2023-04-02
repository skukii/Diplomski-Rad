import cdsapi
import netCDF4 as nc
import pandas as pd
import numpy as np
import pupygrib
import xarray as xr

c = cdsapi.Client()

hourly_data = c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'variable': 'temperature',
        'pressure_level': '1000',
        'year': '2008',
        'month': '01',
        'day': '01',
        'time': '12:00',
        'format': 'netcdf',  # Supported format: grib and netcdf. Default: grib
        'area': [60, -10, 50, 2],  # North, West, South, East.          Default: global
        'grid': [1.0, 1.0],  # Latitude/longitude grid.           Default: 0.25 x 0.25
    },
    'era5_temperature_sub_area.nc')  # Output file. Adapt as you wish.

"""
land_data = c.retrieve(
    'reanalysis-era5-land',
    {
        'month': 'selected_all',
    },
    'download.data')
"""
monthly_averaged_data = c.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'format': 'netcfd',
        'month': [
            '01'
        ],
        'year': [
            '2023'
        ],
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
            '2m_temperature', 'mean_sea_level_pressure', 'mean_wave_direction',
            'mean_wave_period', 'sea_surface_temperature', 'significant_height_of_combined_wind_waves_and_swell',
            'surface_pressure', 'total_precipitation',
        ],
        'product_type': [
            'monthly_averaged_ensemble_members', 'monthly_averaged_ensemble_members_by_hour_of_day', 'monthly_averaged_reanalysis',
            'monthly_averaged_reanalysis_by_hour_of_day',
        ],
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
    },
    'monthly.nc')

fn = 'era5_temperature_sub_area.nc'

data_hourly = xr.open_dataset(fn)
df_hourly = data_hourly.to_dataframe()

data_monthly = xr.open_dataset('monthly.nc')
df_monthly = data_hourly.to_dataframe()
print(df_monthly)


