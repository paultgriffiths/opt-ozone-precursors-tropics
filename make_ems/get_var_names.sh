for zzFilename in *biomass*.nc; do
    ncdump -h ${zzFilename} | grep float
done
