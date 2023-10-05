#! /usr/bin/env bash
if [[ $# -eq 0 ]]  
then  
	echo "JOBID argument not supplied"
	exit 1
else
	echo $1
	declare -a zzJobID=$1
	declare -a zzTempDir=/work/scratch-pw2/ptg21/${zzJobID}/pp_files_ox_eval_pm/
	mkdir -p ${zzTempDir}
	cp call_template_for_OPT_archive ${zzTempDir}/
	cd ${zzTempDir}
	/opt/moose/external-client-version-wrapper/bin/moo select -f call_template_for_OPT_archive moose:crum/${zzJobID}/apm.pp ./
fi



