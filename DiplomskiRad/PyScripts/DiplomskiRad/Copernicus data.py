import cdsapi
import netCDF4 as nc
import pandas as pd
import numpy as np
import pupygrib
import xarray as xr

fn = 'era5_temperature_sub_area.nc'

data_hourly = xr.open_dataset(fn)
df_hourly = data_hourly.to_dataframe()

data_monthly = xr.open_dataset('monthly.nc')
df_monthly = data_hourly.to_dataframe()
print(df_monthly)