cd /work/scratch-pw2/ptg21/u-cq041/netcdf_OPT/

ncrename -O -v mass_fraction_of_o3_in_air,mole_fraction_of_o3_in_air GLOBAL_BB_o3_vmr_1995_2015.nc GLOBAL_BB_o3_vmr_1995_2015.nc
ncatted -O -a units,mole_fraction_of_o3_in_air,m,c,"mol mol-1" GLOBAL_BB_o3_vmr_1995_2015.nc GLOBAL_BB_o3_vmr_1995_2015.nc
ncatted -O -a standard_name,mole_fraction_of_o3_in_air,m,c,"mole_fraction_of_o3_in_air" GLOBAL_BB_o3_vmr_1995_2015.nc GLOBAL_BB_o3_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_isoprene_in_air,mole_fraction_of_isoprene_in_air GLOBAL_BB_c5h8_vmr_1995_2015.nc GLOBAL_BB_c5h8_vmr_1995_2015.nc
ncatted -O -a units,mole_fraction_of_isoprene_in_air,m,c,"mol mol-1" GLOBAL_BB_c5h8_vmr_1995_2015.nc GLOBAL_BB_c5h8_vmr_1995_2015.nc
ncatted -O -a standard_name,mole_fraction_of_isoprene_in_air,m,c,"mole_fraction_of_isoprene_in_air" GLOBAL_BB_c5h8_vmr_1995_2015.nc GLOBAL_BB_c5h8_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_methane_in_air,mole_fraction_of_methane_in_air GLOBAL_BB_ch4_vmr_1995_2015.nc GLOBAL_BB_ch4_vmr_1995_2015.nc
ncatted -O -a units,mole_fraction_of_methane_in_air,m,c,"mol mol-1" GLOBAL_BB_ch4_vmr_1995_2015.nc GLOBAL_BB_ch4_vmr_1995_2015.nc
ncatted -O -a standard_name,mole_fraction_of_methane_in_air,m,c,"mole_fraction_of_methane_in_air" GLOBAL_BB_ch4_vmr_1995_2015.nc GLOBAL_BB_ch4_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_carbon_monoxide_in_air,mole_fraction_of_carbon_monoxide_in_air GLOBAL_BB_co_vmr_1995_2015.nc GLOBAL_BB_co_vmr_1995_2015.nc
ncatted -O -a units,mole_fraction_of_carbon_monoxide_in_air,m,c,"mol mol-1" GLOBAL_BB_co_vmr_1995_2015.nc GLOBAL_BB_co_vmr_1995_2015.nc
ncatted -O -a standard_name,mole_fraction_of_carbon_monoxide_in_air,m,c,"mole_fraction_of_carbon_monoxide_in_air" GLOBAL_BB_co_vmr_1995_2015.nc GLOBAL_BB_co_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_formaldehyde_in_air,mole_fraction_of_formaldehyde_in_air GLOBAL_BB_hcho_vmr_1995_2015.nc GLOBAL_BB_hcho_vmr_1995_2015.nc
ncatted -O -a units,mole_fraction_of_formaldehyde_in_air,m,c,"mol mol-1" GLOBAL_BB_hcho_vmr_1995_2015.nc GLOBAL_BB_hcho_vmr_1995_2015.nc
ncatted -O -a standard_name,mole_fraction_of_formaldehyde_in_air,m,c,"mole_fraction_of_formaldehyde_in_air" GLOBAL_BB_hcho_vmr_1995_2015.nc GLOBAL_BB_hcho_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_nitrogen_dioxide_in_air,mole_fraction_of_nitrogen_dioxide_in_air GLOBAL_BB_no2_vmr_1995_2015.nc GLOBAL_BB_no2_vmr_1995_2015.nc
ncatted -O -a units,mole_fraction_of_nitrogen_dioxide_in_air,m,c,"mol mol-1" GLOBAL_BB_no2_vmr_1995_2015.nc GLOBAL_BB_no2_vmr_1995_2015.nc
ncatted -O -a standard_name,mole_fraction_of_nitrogen_dioxide_in_air,m,c,"mole_fraction_of_nitrogen_dioxide_in_air" GLOBAL_BB_no2_vmr_1995_2015.nc GLOBAL_BB_no2_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_nitrogen_monoxide_in_air,mole_fraction_of_nitrogen_monoxide_in_air GLOBAL_BB_no_vmr_1995_2015.nc GLOBAL_BB_no_vmr_1995_2015.nc
ncatted -O -a units,mole_fraction_of_nitrogen_monoxide_in_air,m,c,"mol mol-1" GLOBAL_BB_no_vmr_1995_2015.nc GLOBAL_BB_no_vmr_1995_2015.nc
ncatted -O -a standard_name,mole_fraction_of_nitrogen_monoxide_in_air,m,c,"mole_fraction_of_nitrogen_monoxide_in_air" GLOBAL_BB_no_vmr_1995_2015.nc GLOBAL_BB_no_vmr_1995_2015.nc

ncrename -O -v mass_fraction_of_hydroxyl_radical_in_air,mole_fraction_of_hydroxyl_radical_in_air GLOBAL_BB_oh_vmr_1995_2015.nc GLOBAL_BB_oh_vmr_1995_2015.nc
ncatted -O -a units,mole_fraction_of_hydroxyl_radical_in_air,m,c,"mol mol-1" GLOBAL_BB_oh_vmr_1995_2015.nc GLOBAL_BB_oh_vmr_1995_2015.nc
ncatted -O -a standard_name,mole_fraction_of_hydroxyl_radical_in_air,m,c,"mole_fraction_of_hydryoxyl_radical_in_air" GLOBAL_BB_oh_vmr_1995_2015.nc GLOBAL_BB_oh_vmr_1995_2015.nc
