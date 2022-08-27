#! /usr/bin/env bash
if [[ $# -eq 0 ]]
then
        echo "JOBID argument not supplied"
        exit 1
else
        echo $1
	declare -a zzJobID=$1
	declare -a zzDisk=/work/scratch-pw/ptg21/
	cd ${zzDisk}/${zzJobID}/netcdf_trop_ox_budget/
	mv ${zzJobID}_2010_air_mass.nc ../${zzJobID}_air_mass.nc
	mv ${zzJobID}_2010_noy_dry_dep_3d.nc ../${zzJobID}_noy_dry_dep_3d.nc
	mv ${zzJobID}_2010_noy_wet_dep_3d.nc ../${zzJobID}_noy_wet_dep_3d.nc
	mv ${zzJobID}_2010_o3_dry_dep_3d.nc ../${zzJobID}_o3_dry_dep_3d.nc
	mv ${zzJobID}_2010_o3.nc ../${zzJobID}_o3.nc
	mv ${zzJobID}_2010_o3-STE.nc ../${zzJobID}_o3-STE.nc
	mv ${zzJobID}_2010_ox_loss.nc ../${zzJobID}_ox_loss.nc
	mv ${zzJobID}_2010_ox_prod.nc ../${zzJobID}_ox_prod.nc
	mv ${zzJobID}_2010_trop_air_mass.nc ../${zzJobID}_trop_air_mass.nc
	mv ${zzJobID}_2010_trop_mask.nc ../${zzJobID}_trop_mask.nc
fi
