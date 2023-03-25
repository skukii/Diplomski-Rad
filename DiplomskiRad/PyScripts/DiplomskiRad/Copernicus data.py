import xarray as xr

fn = 'era5_temperature_sub_area.nc'

data_hourly = xr.open_dataset(fn)
df_hourly = data_hourly.to_dataframe()

data_monthly = xr.open_dataset('monthly.nc')
df_monthly = data_hourly.to_dataframe()