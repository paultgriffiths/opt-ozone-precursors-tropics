
ncrename -O -v .mass_fraction_of_methane_in_air,mole_fraction_of_methane_in_air BASE_ch4_vmr_1995_2015.nc BASE_ch4_vmr_1995_2015.nc
ncatted -O -a units,mole_fraction_of_methane_in_air,m,c,"mol mol-1" BASE_ch4_vmr_1995_2015.nc BASE_ch4_vmr_1995_2015.nc
ncatted -O -a standard_name,mole_fraction_of_methane_in_air,m,c,"mole_fraction_of_methane_in_air" BASE_ch4_vmr_1995_2015.nc BASE_ch4_vmr_1995_2015.nc

