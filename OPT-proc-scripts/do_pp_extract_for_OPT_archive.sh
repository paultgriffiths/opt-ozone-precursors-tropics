#! /usr/bin/env bash
if [[ $# -eq 0 ]]  
then  
	echo "JOBID argument not supplied"
	exit 1
else
	echo $1
	declare -a zzJobID=$1
	declare -a zzTempDir=/work/scratch-pw2/ptg21/${zzJobID}/pp_files_for_OPT_archive_pm/
	mkdir -p ${zzTempDir}
	cp call_template_for_OPT_archive_pm ${zzTempDir}/
	cd ${zzTempDir}
	/opt/moose/external-client-version-wrapper/bin/moo select -f call_template_for_OPT_archive_pm moose:crum/${zzJobID}/apm.pp ./

	cd /home/users/ptg21/OPT/OPT-proc-scripts/
	echo $1
	declare -a zzJobID=$1
	declare -a zzTempDir=/work/scratch-pw2/ptg21/${zzJobID}/pp_files_for_OPT_archive_ap4/
	mkdir -p ${zzTempDir}
	cp call_template_for_OPT_archive_ap4 ${zzTempDir}/
	cd ${zzTempDir}
	/opt/moose/external-client-version-wrapper/bin/moo select -f call_template_for_OPT_archive_ap4 moose:crum/${zzJobID}/ap4.pp ./
fi



