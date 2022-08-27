#!/usr/bin/env python

import numpy as np
import netCDF4
import xarray as xr
import sys
jobid=sys.argv[1]
disk=sys.argv[2]

JASMIN=True

geovols='/gws/nopw/j04/ukca_vol2/ptg21/geovols/geovol_192x144x85.nc'
outdir='/homes/users/ptg21/output/'+jobid+'/'

geovol = xr.open_dataset(geovols)
vol      = geovol['vol_theta'] # m3
vol      = vol*1E6   # cm-3

tropmask = xr.open_dataset(disk+jobid+'/'+jobid+'_trop_mask.nc')

print('ox prod')
filename=disk+jobid+'/'+jobid+'_ox_prod.nc'
ncfile2      = xr.open_dataset(filename)

p1 = ncfile2.ox_prod_ho2_no*tropmask.trop_mask
ho2no_tot   = p1.sum(axis=(1,2,3))*0.048*360.*3600.*24. #kg O3 per 360day year
ho2no_tot.to_netcdf(jobid+'_ho2no_tot.nc') 

p2 = ncfile2.ox_prod_meoo_no*tropmask.trop_mask
meo2no_tot  = p2.sum(axis=(1,2,3))*0.048*360.*3600.*24.
meo2no_tot.to_netcdf(jobid+'_meo2no_tot.nc')

p3 = ncfile2.ox_prod_no_ro2*tropmask.trop_mask
ro2no_tot   = p3.sum(axis=(1,2,3))*0.048*360.*3600.*24.
ro2no_tot.to_netcdf(jobid+'_ro2no_tot.nc')

p4 = ncfile2.ox_prod_oh_inorgacid*tropmask.trop_mask
ohrcooh_tot = p4.sum(axis=(1,2,3))*0.048*360.*3600.*24.
ohrcooh_tot.to_netcdf(jobid+'_ohrcooh_tot.nc')

p5 = ncfile2.ox_prod_oh_orgnitrate*tropmask.trop_mask
ohrono2_tot = p5.sum(axis=(1,2,3))*0.048*360.*3600.*24.
ohrono2_tot.to_netcdf(jobid+'_ohrono2_tot.nc')

p6 = ncfile2.ox_prod_orgnitrate_photol*tropmask.trop_mask
hvrono2_tot = p6.sum(axis=(1,2,3))*0.048*360.*3600.*24.
hvrono2_tot.to_netcdf(jobid+'_hvrono2_tot.nc')

p7 = ncfile2.ox_prod_oh_panrxns*tropmask.trop_mask
ohpan_tot   = p7.sum(axis=(1,2,3))*0.048*360.*3600.*24.
ohpan_tot.to_netcdf(jobid+'_ohpan_tot.nc')  

netp = p1 + p2 + p3 + p4 + p5 + p6 + p7
netp.to_netcdf(jobid+'_totp.nc')

netp_tot = ho2no_tot + meo2no_tot + ro2no_tot + ohrcooh_tot + ohrono2_tot + hvrono2_tot + ohpan_tot
netp_tot.to_netcdf(jobid+'_ann_mean_totp.nc')

netp_tot_cmip6 = ho2no_tot + meo2no_tot + ro2no_tot 
netp_tot_cmip6.to_netcdf(jobid+'_ann_mean_totp_cmip6.nc')

print('ox loss')

filename=disk+jobid+'/'+jobid+'_ox_loss.nc'
ncfile3     = xr.open_dataset(filename)

l1  = (ncfile3.ox_loss_o1d_h2o*tropmask.trop_mask)
o1dh2o_tot= l1.sum(axis=(1,2,3))*0.048*360.*3600.*24.
o1dh2o_tot.to_netcdf(jobid+'_o1dh2o_tot.nc') 

l2 = (ncfile3.ox_loss_minor_rxns*tropmask.trop_mask)
mlr_tot = l2.sum(axis=(1,2,3))*0.048*360.*3600.*24.
mlr_tot.to_netcdf(jobid+'_mlr_tot.nc')

l3 = (ncfile3.ox_loss_ho2_o3*tropmask.trop_mask)
ho2o3_tot  = l3.sum(axis=(1,2,3))*0.048*360.*3600.*24.
ho2o3_tot.to_netcdf(jobid+'_ho2o3_tot.nc')

l4 = (ncfile3.ox_loss_oh_o3*tropmask.trop_mask) 
oho3_tot  = l4.sum(axis=(1,2,3))*0.048*360.*3600.*24.
oho3_tot.to_netcdf(jobid+'_oho3_tot.nc')

l5  = (ncfile3.ox_loss_o3_alkene*tropmask.trop_mask)
o3alk_tot = l5.sum(axis=(1,2,3))*0.048*360.*3600.*24.
o3alk_tot.to_netcdf(jobid+'_o3alk_tot.nc')

l6  = (ncfile3.ox_loss_n2o5_h2o*tropmask.trop_mask)
n2o5h2o_tot = l6.sum(axis=(1,2,3))*0.048*360.*3600.*24.
n2o5h2o_tot.to_netcdf(jobid+'_n2o5h2o.nc')

l7 = (ncfile3.ox_loss_no3_chemloss*tropmask.trop_mask)
no3loss_tot  = l7.sum(axis=(1,2,3))*0.048*360.*3600.*24.
no3loss_tot.to_netcdf(jobid+'_no3loss_tot.nc')

netl = l1 + l2 + l3 + l4 + l5 + l6 + l7
netl_tot = o1dh2o_tot + mlr_tot + ho2o3_tot + oho3_tot + o3alk_tot + n2o5h2o_tot + no3loss_tot
netl_tot_cmip6 = o1dh2o_tot + ho2o3_tot + oho3_tot 

netl.to_netcdf(jobid+'_totl.nc')
netl_tot.to_netcdf(jobid+'_ann_mean_totl.nc')
netl_tot_cmip6.to_netcdf(jobid+'_ann_mean_totl_cmip6.nc')

print('oy dep')

ncfile = xr.open_dataset(disk+jobid+'/'+jobid+'_o3_dry_dep_3d.nc')
o3dd = (ncfile.ozone_dry_dep_3d*tropmask.trop_mask)
o3dd_ann_tot  = o3dd.sum(axis=(1,2,3))*0.048*360.*3600.*24.
o3dd_ann_tot.to_netcdf(jobid+'_o3dd_ann_tot.nc')

ncfile = xr.open_dataset(disk+jobid+'/'+jobid+'_noy_dry_dep_3d.nc')
noy_dd = (ncfile.noy_dry_dep_3d*tropmask.trop_mask)
noydd_ann_tot  = noy_dd.sum(axis=(1,2,3))*0.048*360.*3600.*24.
noydd_ann_tot.to_netcdf(jobid+'_noydd_ann_tot.nc')

ncfile = xr.open_dataset(disk+jobid+'/'+jobid+'_noy_wet_dep_3d.nc')
noy_wd = (ncfile.noy_wet_dep_3d*tropmask.trop_mask)
noy_wd_ann_tot  = noy_wd.sum(axis=(1,2,3))*0.048*360.*3600.*24.
noy_wd_ann_tot.to_netcdf(jobid+'_noywd_ann_tot.nc')

print('STE')
ncfile = xr.open_dataset(disk+jobid+'/'+jobid+'_o3-STE.nc')
ste = (ncfile.ste*tropmask.trop_mask)
ste_ann_tot  = ste.sum(axis=(1,2,3))*0.048*360.*3600.*24.
ste_ann_tot.to_netcdf(jobid+'_ste_ann_tot.nc')

