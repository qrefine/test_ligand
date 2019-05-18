from __future__ import division
import iotbx.pdb
import mmtbx.model
from libtbx.utils import null_out
import os
import string
import numpy as np
from ase.io import write
from ase.units import kcal, mol
from ase.units import Hartree, Bohr
from ase.calculators.general import Calculator
import copy
import re

def xtbtpdb(path,k):
    pdb_file = path+"/"+str(k)+".pdb"
    pdb_inp = iotbx.pdb.input(file_name=pdb_file)
    model = mmtbx.model.manager(model_input=pdb_inp,
                              process_input=True,
                              log=null_out())
    hierarchy = model.get_hierarchy()
    cs = pdb_inp.crystal_symmetry()
    f=open(path+"/"+"xtbopt.xyz")
    x=[0 for i in range(len(hierarchy.atoms()))]
    y=[0 for i in range(len(hierarchy.atoms()))]
    z=[0 for i in range(len(hierarchy.atoms()))]
    i=0
    j=0
    for line in f:
        if i >= 2:
            #print(line.split(" ",3)[3])
            #x[j]=line.split(" ",3)[1]
            #y[j]=line.split(" ",3)[2]
            #z[j]=line.split(" ",3)[3]
            #print(re.findall(r"\d+\.?\d*",line)[0])
            x[j]=re.findall(r"\d+\.?\d*",line)[0]
            y[j]=re.findall(r"\d+\.?\d*",line)[1]
            z[j]=re.findall(r"\d+\.?\d*",line)[2]
            #print(z[j])
            i=i+1
            j=j+1
        else: 
            i=i+1

    i=0
    #print(x[i])
    for atoms in hierarchy.atoms():
        xx=float(x[i])
        yy=float(y[i])
        zz=float(z[i])
        atoms.set_xyz(new_xyz=(xx,yy,zz))
        #atoms.xyz=(xx,yy,zz)
        #print(atoms.xyz)
        i=i+1
    hierarchy.write_pdb_file(file_name=path+"/"+str(k)+"_xtbopt.pdb",crystal_symmetry=cs)
    f.close()

for i in [0.3,0.6,0.9,1.2,1.5]:
    for k in range(10):
        path="./"+str(i)+"/xyz/"+str(k)
        xtbtpdb(path,k)


    

