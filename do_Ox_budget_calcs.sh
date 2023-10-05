#! /usr/bin/env bash
if [[ $# -eq 0 ]]
then
        echo "JOBID argument not supplied"
        exit 1
else
        echo $1
	declare -a zzJobID=$1
	declare -a zzDisk=/work/scratch-pw/ptg21/
	python generate_netcdf_ukesm_o3_budget.py ${zzJobID} ${zzDisk}
	./do_mv.sh ${zzJobID} ${zzDisk}
	python calc_budget_xarray.py ${zzJobID} ${zzDisk}
#	python ox_budget_calcs.py ${zzJobID} ${zzDisk}
fi
