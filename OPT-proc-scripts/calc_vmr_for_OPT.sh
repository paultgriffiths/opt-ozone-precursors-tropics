# C5H8 28.9647/68.12 
# NO 28.9647/30.006
# NO2 28.9647/46.006
# CO 28.9647/28.010
# HCHO 28.9647/30.026
# O3 28.9647/47.997
# RMM AIR 28.9647
# VMR = RMM AIR / RMM GAS * MMR
cd /work/scratch-pw2/ptg21/u-cb159/netcdf_OPT
cdo -mulc,0.4252011156782149 BASE_c5h8_1995_2015.nc ../BASE_c5h8_1995-2015.nc 
cdo -mulc,0.9652969406118777 BASE_no_1995_2015.nc ../BASE_no_1995-2015.nc 
cdo -mulc,0.6295852714863279 BASE_no2_1995_2015.nc ../BASE_no2_1995-2015.nc 
cdo -mulc,1.0340842556229917 BASE_co_1995_2015.nc ../BASE_co_1995-2015.nc 
cdo -mulc,0.9646539665623127 BASE_hcho_1995_2015.nc ../BASE_hcho_1995-2015.nc 
cdo -mulc,0.6034689668104256 BASE_o3_1995_2015.nc ../BASE_o3_1995-2015.nc 