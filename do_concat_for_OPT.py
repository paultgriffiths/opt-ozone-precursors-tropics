import xarray as xr

disk="/work/scratch-pw2/ptg21/u-cb159/netcdf_OPT/"

vars = [
  'mass_fraction_of_isoprene_in_air',
  "mass_fraction_of_methane_in_air",
  "mass_fraction_of_carbon_monoxide_in_air",
  'mass_fraction_of_formaldehyde_in_air',
  "mass_fraction_of_nitrogen_dioxide_in_air",
  'mass_fraction_of_nitrogen_monoxide_in_air',
  'mass_fraction_of_o3_in_air',
  "mass_fraction_of_hydroxyl_radical_in_air"]

conv_factors = {'mass_fraction_of_isoprene_in_air': 0.4252011156782149,
                'mass_fraction_of_methane_in_air': 0.943317457517492,
                'mass_fraction_of_nitrogen_monoxide_in_air': 0.9652969406118777,
                'mass_fraction_of_nitrogen_dioxide_in_air': 0.6295852714863279,
                'mass_fraction_of_carbon_monoxide_in_air': 1.0340842556229917,
                'mass_fraction_of_formaldehyde_in_air': 0.9646539665623127,
                'mass_fraction_of_o3_in_air': 0.6034689668104256,
                'mass_fraction_of_hydroxyl_radical_in_air': 1.7031046039865936}

varc=0
for var in ["c5h8", "ch4", "co",  "hcho", "no2", "no", "o3", "oh"]:
  vari=vars[varc]
  print(vari)
  print('open')
  conv = conv_factors[vari]
  data = xr.open_mfdataset(disk+'/BASE'+'_*_'+var+'.nc')
  new_data = data.copy(deep=True)
  new_data[vari].data[:] = new_data[vari].data[:] * conv
  new_data[vari].compute()
  print('save')
  new_data.to_netcdf(disk+'/BASE_'+var+'_vmr_1995_2015.nc')
  varc=varc+1

vars = [
  "eastward_wind",#u
  "northward_wind",#v
  'airmass_atm',
  "air_pressure",
  "air_temperature",
  "tropopause_ht"]
  
varc=0
for var in [ "u", "v", "air_mass", "p", "temp","tropopause_ht",]:
  vari=vars[varc]
  print(var)
  print('open')
  data = xr.open_mfdataset(disk+'/BASE'+'_*_'+var+'.nc')
  new_data = data.copy(deep=True)
  new_data[vari].compute()
  print('save')
  data.to_netcdf(disk+'/BASE_'+var+'_1995_2015.nc')
  varc=varc+1
