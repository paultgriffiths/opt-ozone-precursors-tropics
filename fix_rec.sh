for zzFilename in *.nc; do
    [ -e "$zzFilename" ] || continue
    # ... rest of the loop body
		echo ${zzFilename} ${zzFilename}.fix
    ncks -O --mk_rec_dmn time ${zzFilename} ${zzFilename}.fix
done
