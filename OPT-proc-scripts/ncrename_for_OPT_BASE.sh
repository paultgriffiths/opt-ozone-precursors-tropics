cd /work/scratch-pw2/ptg21/u-cb159/

ncrename -O -v mass_fraction_of_o3_in_air,mole_fraction_of_o3_in_air BASE_o3_vmr_1995_2015.nc BASE_o3_vmr_1995_2015.nc
ncatted -O -a units,,m,c,"mol mol-1" BASE_o3_vmr_1995_2015.nc BASE_o3_vmr_1995_2015.nc
ncatted -O -a standard_name,,m,c,"mole_fraction_of_o3_in_air" BASE_o3_vmr_1995_2015.nc BASE_o3_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_isoprene_in_air,mole_fraction_of_isoprene_in_air BASE_c5h8_vmr_1995_2015.nc BASE_c5h8_vmr_1995_2015.nc
ncatted -O -a units,,m,c,"mol mol-1" BASE_c5h8_vmr_1995_2015.nc BASE_c5h8_vmr_1995_2015.nc
ncatted -O -a standard_name,,m,c,"mole_fraction_of_isoprene_in_air" BASE_c5h8_vmr_1995_2015.nc BASE_c5h8_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_methane_in_air,mole_fraction_of_methane_in_air BASE_ch4_vmr_1995_2015.nc BASE_ch4_vmr_1995_2015.nc
ncatted -O -a units,,m,c,"mol mol-1" BASE_ch4_vmr_1995_2015.nc BASE_ch4_vmr_1995_2015.nc
ncatted -O -a standard_name,,m,c,"mole_fraction_of_methane_in_air" BASE_ch4_vmr_1995_2015.nc BASE_ch4_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_carbon_monoxide_in_air,mole_fraction_of_carbon_monoxide_in_air BASE_co_vmr_1995_2015.nc BASE_co_vmr_1995_2015.nc
ncatted -O -a units,,m,c,"mol mol-1" BASE_co_vmr_1995_2015.nc BASE_co_vmr_1995_2015.nc
ncatted -O -a standard_name,,m,c,"mole_fraction_of_carbon_monoxide_in_air" BASE_co_vmr_1995_2015.nc BASE_co_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_formaldehyde_in_air,mole_fraction_of_formaldehyde_in_air BASE_hcho_vmr_1995_2015.nc BASE_hcho_vmr_1995_2015.nc
ncatted -O -a units,,m,c,"mol mol-1" BASE_hcho_vmr_1995_2015.nc BASE_hcho_vmr_1995_2015.nc
ncatted -O -a standard_name,,m,c,"mole_fraction_of_formaldehyde_in_air" BASE_hcho_vmr_1995_2015.nc BASE_hcho_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_nitrogen_dioxide_in_air,mole_fraction_of_nitrogen_dioxide_in_air BASE_no2_vmr_1995_2015.nc BASE_no2_vmr_1995_2015.nc
ncatted -O -a units,,m,c,"mol mol-1" BASE_no2_vmr_1995_2015.nc BASE_no2_vmr_1995_2015.nc
ncatted -O -a standard_name,,m,c,"mole_fraction_of_nitrogen_dioxide_in_air" BASE_no2_vmr_1995_2015.nc BASE_no2_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_nitrogen_monoxide_in_air,mole_fraction_of_nitrogen_monoxide_in_air BASE_no_vmr_1995_2015.nc BASE_no_vmr_1995_2015.nc
ncatted -O -a units,,m,c,"mol mol-1" BASE_no_vmr_1995_2015.nc BASE_no_vmr_1995_2015.nc
ncatted -O -a standard_name,,m,c,"mole_fraction_of_nitrogen_monoxide_in_air" BASE_no_vmr_1995_2015.nc BASE_no_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_hydroxyl_radical_in_air,mole_fraction_of_hydroxyl_radical_in_air BASE_oh_vmr_1995_2015.nc BASE_oh_vmr_1995_2015.nc
ncatted -O -a units,,m,c,"mol mol-1" BASE_oh_vmr_1995_2015.nc BASE_oh_vmr_1995_2015.nc
ncatted -O -a standard_name,,m,c,"mole_fraction_of_hydryoxyl_radical_in_air" BASE_oh_vmr_1995_2015.nc BASE_oh_vmr_1995_2015.nc