import os
import sys

import iris
import numpy as np

import definitions_STASH_for_OPT as def_STASH
from stash_list_for_OPT_ap4 import lst_ap4
from stash_list_for_OPT_pm import lst

# Only use for files with more than one timestep as iris does not output that dimension if only one step in it. 

def ret_stash_string(i):
  isec=i//1000
  sec="{:02d}".format(isec)
  it="{:03d}".format(i-(1000*isec))
  return 'm01s'+sec+'i'+it


jobid='u-cb159'
disk='/work/scratch-pw2/ptg21/' 

outputdir=disk+jobid+'/netcdf_OPT/'
inputdir= disk+jobid+'/pp_files_for_OPT_archive_pm/'
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

#### PM stream

# name = []
# stash_list = []
# for i in lst:
#     name.append(i[0])
#     stash_list.append(i[1])

# print ('\n'+jobid+'\npm')
# # prepare STASH codes
# path_to_files=inputdir+'/'+jobid+'a.pm'
# for z in range(0,len(stash_list)):
#   for decade in np.arange(199,202):
#    decade = str(decade) 
#    stash=[]
#    field_constr=[]
#    for i in stash_list[z]:
#        stashdir = inputdir+'/'
#        stash.append(ret_stash_string(i))
#        field_constr.append(iris.AttributeConstraint(STASH=ret_stash_string(i)))
#        print ('stash : ')
#        print (stashdir)
#    # load pp files and output netCDF
#    outfile=outputdir+'BASE_'+decade+'0'+name[z]+'.nc'
#    print(outfile)
#    field=iris.load(stashdir+'*'+decade+'*.pp',field_constr,callback=def_STASH.UKCA_callback)
#    print (field)
#    iris.save(field, outfile)
 
 
 
#### AP4 stream 
inputdir= disk+jobid+'/pp_files_for_OPT_archive_ap4/'

name = []
stash_list = []
for i in lst_ap4:
    name.append(i[0])
    stash_list.append(i[1])
    
print ('\n'+jobid+'\npm')

path_to_files=inputdir+'/'+jobid+'a.pm'

for z in range(0,len(stash_list)):
  for decade in np.arange(199,202):
   decade = str(decade) 
   stash=[]
   field_constr=[]
   for i in stash_list[z]:
       stashdir = inputdir+'/'
       stash.append(ret_stash_string(i))
       field_constr.append(iris.AttributeConstraint(STASH=ret_stash_string(i)))
       print ('stash : ')
       print (stashdir)
   # load pp files and output netCDF
   outfile=outputdir+'BASE_'+decade+'0'+name[z]+'.nc'
   print(outfile)
   field=iris.load(stashdir+'*'+decade+'*.pp',field_constr,callback=def_STASH.UKCA_callback)
   print (field)
   iris.save(field, outfile)
 
