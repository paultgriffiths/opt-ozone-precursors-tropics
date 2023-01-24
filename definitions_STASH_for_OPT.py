''' Assign information to STASH numbers.
Such as variable names, units, conversion factors.
'''
#################################################################### 
# ASSIGN INFORMATION TO STASH NUMBERS

# Standard names than iris reads can be in file in "python:> help(iris.std_names)": /usr/local/shared/ubuntu-12.04/x86_64/python2.7-iris/1.6.1/local/lib/python2.7/site-packages/Iris-1.6.1-py2.7.egg/iris/std_names.py

#-------------------------------------------------------------------

# conversion factor= cspecies=M(var)/M(air)=M(var)/28.97g.mol-1
#################################################################### 

def UKCA_callback(cube, field, filename):
    if cube.attributes['STASH'] == 'm01s00i002':
        cube.rename(name='eastward_wind')

    if cube.attributes['STASH'] == 'm01s00i003':
        cube.rename(name='northward_wind')

    if cube.attributes['STASH'] == 'm01s00i012':
        cube.rename(name='qcf')

    if cube.attributes['STASH'] == 'm01s00i004':
        cube.rename(name='theta')

    if cube.attributes['STASH'] == 'm01s00i010':
        cube.rename(name='h2o')

    if cube.attributes['STASH'] == 'm01s00i025':
        cube.rename(name='bl_depth')

    if cube.attributes['STASH'] == 'm01s00i408':
        cube.rename(name='air_pressure')

    if cube.attributes['STASH'] == 'm01s16i004':
        cube.rename(name='air_temperature')

    if cube.attributes['STASH'] == 'm01s34i150':
        cube.rename(name='aoa')

    if cube.attributes['STASH'] == 'm01s30i201':
        cube.rename(name='u-plevs')

    if cube.attributes['STASH'] == 'm01s30i202':
        cube.rename(name='v-plevs')

    if cube.attributes['STASH'] == 'm01s30i203':
        cube.rename(name='w-plevs')

    if cube.attributes['STASH'] == 'm01s30i451':
        cube.rename(name='trop_p')

    if cube.attributes['STASH'] == 'm01s30i452':
        cube.rename(name='trop_t')

    if cube.attributes['STASH'] == 'm01s30i453':
        cube.rename(name='tropopause_altitude')

#    if cube.attributes['STASH'] == 'm01s34i361':
#        cube.rename(name='airmass_trop')

#--------------------------------------------------------------
# Tracers UKCA
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i001':
        cube.rename(name='mass_fraction_of_o3_in_air')

    if cube.attributes['STASH'] == 'm01s34i002':
        cube.rename(name='mass_fraction_of_nitrogen_monoxide_in_air')

    if cube.attributes['STASH'] == 'm01s34i003':
        cube.rename(name='NO3')

    if cube.attributes['STASH'] == 'm01s34i005':
        cube.rename(name='N2O5')

    if cube.attributes['STASH'] == 'm01s34i006':
        cube.rename(name='HONO2')

    if cube.attributes['STASH'] == 'm01s34i008':
        cube.rename(name='H2O2')

    if cube.attributes['STASH'] == 'm01s34i009':
        cube.rename(name='mass_fraction_of_methane_in_air')

    if cube.attributes['STASH'] == 'm01s34i010':
        cube.rename(name='mass_fraction_of_carbon_monoxide_in_air')

    if cube.attributes['STASH'] == 'm01s34i011':
        cube.rename(name='mass_fraction_of_formaldehyde_in_air')

    if cube.attributes['STASH'] == 'm01s34i012':
        cube.rename(name='MeOOH')

    if cube.attributes['STASH'] == 'm01s34i014':
        cube.rename(name='C2H6')

    if cube.attributes['STASH'] == 'm01s34i015':
        cube.rename(name='EtOOH')

    if cube.attributes['STASH'] == 'm01s34i016':
        cube.rename(name='MeCHO')

    if cube.attributes['STASH'] == 'm01s34i017':
        cube.rename(name='PAN')

    if cube.attributes['STASH'] == 'm01s34i018':
        cube.rename(name='C3H8')

    if cube.attributes['STASH'] == 'm01s34i021':
        cube.rename(name='EtCOH')

    if cube.attributes['STASH'] == 'm01s34i022':
        cube.rename(name='Me2CO')

    if cube.attributes['STASH'] == 'm01s34i027':
        cube.rename(name='mass_fraction_of_isoprene_in_air')

    if cube.attributes['STASH'] == 'm01s34i041':
        cube.rename(name='Cl')

    if cube.attributes['STASH'] == 'm01s34i042':
        cube.rename(name='ClO')

    if cube.attributes['STASH'] == 'm01s34i043':
        cube.rename(name='Cl2O2')

    if cube.attributes['STASH'] == 'm01s34i044':
        cube.rename(name='ClO2')

    if cube.attributes['STASH'] == 'm01s34i045':
        cube.rename(name='Br')

    if cube.attributes['STASH'] == 'm01s34i046':
        cube.rename(name='BrO')

    if cube.attributes['STASH'] == 'm01s34i049':
        cube.rename(name='N2O')

    if cube.attributes['STASH'] == 'm01s34i050':
        cube.rename(name='HCl')

    if cube.attributes['STASH'] == 'm01s34i054':
        cube.rename(name='ClONO2')

    if cube.attributes['STASH'] == 'm01s34i059':
        cube.rename(name='O3P')

    if cube.attributes['STASH'] == 'm01s34i081':
        cube.rename(name='mass_fraction_of_hydroxyl_radical_in_air')

    if cube.attributes['STASH'] == 'm01s34i082':
        cube.rename(name='HO2')

    if cube.attributes['STASH'] == 'm01s34i996':
        cube.rename(name='mass_fraction_of_nitrogen_dioxide_in_air')

    if cube.attributes['STASH'] == 'm01s34i105':
        cube.rename(name='AITKEN_MODE_SOLUBLE_BC_MMR')

    if cube.attributes['STASH'] == 'm01s34i107':
        cube.rename(name='Accumulation_mode_sol_number')

    if cube.attributes['STASH'] == 'm01s34i108':
        cube.rename(name='Accumulation_mode_sol_h2so4_mmr')

    if cube.attributes['STASH'] == 'm01s34i109':
        cube.rename(name='ACC_MODE_SOLUBLE_BC_MMR')

    if cube.attributes['STASH'] == 'm01s34i115':
        cube.rename(name='COARSE_MODE_SOLUBLE_BC_MMR')

    if cube.attributes['STASH'] == 'm01s34i120':
        cube.rename(name='AITKEN_MODE_INSOLUBLE_BC_MMR')

    if cube.attributes['STASH'] == 'm01s34i149':
        cube.rename(name='PassiveO3')

    if cube.attributes['STASH'] == 'm01s34i151':
        cube.rename(name='O1D')

    if cube.attributes['STASH'] == 'm01s34i152':
        cube.rename(name='NO2')

#--------------------------------------------------------------
#?# unit Dobson? conversion factor
    if cube.attributes['STASH'] == 'm01s34i172':
        cube.rename(name='Ozone_column')
#--------------------------------------------------------------
# Reaction fluxes
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s50i001':
        cube.rename(name='ox_prod_HO2_NO')

    if cube.attributes['STASH'] == 'm01s50i002':
        cube.rename(name='ox_prod_MeOO_NO')

    if cube.attributes['STASH'] == 'm01s50i003':
        cube.rename(name='ox_prod_NO_RO2')

    if cube.attributes['STASH'] == 'm01s50i004':
        cube.rename(name='ox_prod_OH_inorgAcid')

    if cube.attributes['STASH'] == 'm01s50i005':
        cube.rename(name='ox_prod_OH_orgNitrate')

    if cube.attributes['STASH'] == 'm01s50i006':
        cube.rename(name='ox_prod_orgNitrate_photol')

    if cube.attributes['STASH'] == 'm01s50i007':
        cube.rename(name='ox_prod_OH_PANrxns')

    if cube.attributes['STASH'] == 'm01s50i011':
        cube.rename(name='ox_loss_O1D_H2O')

    if cube.attributes['STASH'] == 'm01s50i012':
        cube.rename(name='ox_loss_minor_rxns')

    if cube.attributes['STASH'] == 'm01s50i013':
        cube.rename(name='ox_loss_HO2_O3')

    if cube.attributes['STASH'] == 'm01s50i014':
        cube.rename(name='ox_loss_OH_O3')

    if cube.attributes['STASH'] == 'm01s50i015':
        cube.rename(name='ox_loss_O3_alkene')

    if cube.attributes['STASH'] == 'm01s50i016':
        cube.rename(name='ox_loss_N2O5_H2O')

    if cube.attributes['STASH'] == 'm01s50i017':
        cube.rename(name='ox_loss_NO3_chemloss')

    if cube.attributes['STASH'] == 'm01s50i021':
        cube.rename(name='ozone_dry_dep_3D')

    if cube.attributes['STASH'] == 'm01s50i022':
        cube.rename(name='noy_dry_dep_3D')

    if cube.attributes['STASH'] == 'm01s50i031':
        cube.rename(name='noy_wet_dep_3D')

    if cube.attributes['STASH'] == 'm01s50i041':
        cube.rename(name='ch4_oh_rxn_flux')

    if cube.attributes['STASH'] == 'm01s50i051':
        cube.rename(name='ste')
    
    if cube.attributes['STASH'] == 'm01s50i052':
        cube.var_name='trop_o3_tendency'
   
    if cube.attributes['STASH'] == 'm01s50i054':
        cube.var_name='atm_o3_tendency'
   
    if cube.attributes['STASH'] == 'm01s50i061':
        cube.rename(name='airmass_trop')

    if cube.attributes['STASH'] == 'm01s50i062':
        cube.rename(name='trop_mask')

    if cube.attributes['STASH'] == 'm01s50i063':
        cube.rename(name='atmosphere_mass_per_gridbox')

    if cube.attributes['STASH'] == 'm01s50i156':
        cube.rename(name='nox_ems')

    if cube.attributes['STASH'] == 'm01s50i157':
        cube.rename(name='ch4_ems')

    if cube.attributes['STASH'] == 'm01s50i158':
        cube.rename(name='co_ems')

    if cube.attributes['STASH'] == 'm01s50i159':
        cube.rename(name='hcho_ems')

    if cube.attributes['STASH'] == 'm01s50i160':
        cube.rename(name='c2h6_ems')

    if cube.attributes['STASH'] == 'm01s50i161':
        cube.rename(name='c3h8_ems')

    if cube.attributes['STASH'] == 'm01s50i162':
        cube.rename(name='me2co_ems')

    if cube.attributes['STASH'] == 'm01s50i163':
        cube.rename(name='mecho_ems')

    if cube.attributes['STASH'] == 'm01s50i164':
        cube.rename(name='c5h8_ems')

    if cube.attributes['STASH'] == 'm01s50i172':
        cube.rename(name='nox_aircraft_ems')

    if cube.attributes['STASH'] == 'm01s50i218':
        cube.var_name='NAT'

    if cube.attributes['STASH'] == 'm01s50i220':
        cube.rename(name='trop_ch4_burden')
   
    if cube.attributes['STASH'] == 'm01s50i101':
        cube.var_name='jo2'
   
    if cube.attributes['STASH'] == 'm01s34i966':
        cube.rename(name='aerosol_sa_density')

    if cube.attributes['STASH'] == 'm01s34i973':
        cube.rename(name='ho2_aerosol_loss_rate_coefficient')

    if cube.attributes['STASH'] == 'm01s34i974':
        cube.rename(name='n2o5_aerosol_loss_rate_coefficient')

#--------------------------------------------------------------
# Emissions
#--------------------------------------------------------------
    if cube.attributes['STASH'] == 'm01s34i451':
        cube.rename(name='ch4_apparent_ems')

    if cube.attributes['STASH'] == 'm01s00i302':
        cube.rename(name='ch4_ems')



