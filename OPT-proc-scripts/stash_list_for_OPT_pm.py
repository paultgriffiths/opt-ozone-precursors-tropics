

#################################################################### 
# Which STASH numbers to take for the netCDF file

# Do not use 00 as section indicator. 00010 = 8 ?!
#################################################################### 
lst=[
# Adapt for job:
['_o3',[34001]]
,['_co',[34010]]
,['_no',[34002]]
,['_no2',[34996]]
,['_hcho',[34011]]
,['_c5h8',[34027]]
,['_oh',[34081]]
,['_ch4',[34009]]
,['_air_mass',[50063]]
,['_p',[408]]
,['_q',[10]]
# ['_w',[150]]
,['_tropopause_ht',[30453]]
,['_temp',[16004]]
]

name = []
stash_list = []
for i in lst:
    name.append(i[0])
    stash_list.append(i[1])


