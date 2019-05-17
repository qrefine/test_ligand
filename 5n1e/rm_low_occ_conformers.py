import os
import iotbx.pdb
import time

def have_conformers(pdb_hierarchy):
  for model in pdb_hierarchy.models():
    for chain in model.chains():
      for residue_group in chain.residue_groups():
        if residue_group.have_conformers():
          return True
  return False

def run(file_name):
  pdb_inp = iotbx.pdb.input(file_name = file_name)
  pdb_hierarchy = pdb_inp.construct_hierarchy()
  if (have_conformers(pdb_hierarchy=pdb_hierarchy)):
    print "Starting remove low occ conformers"
    pdb_hierarchy.remove_alt_confs(always_keep_one_conformer=True)
    cs = pdb_inp.crystal_symmetry()
    pdb_hierarchy.write_pdb_file(file_name = file_name[:15]+"_rmconformers.pdb",
                                 crystal_symmetry = cs)
  else:
    print "No conformers"

if __name__ == '__main__':
  t0 = time.time()
  run(file_name = "5n1e_refine_001.pdb")
  print  "Time: %6.4f" % (time.time() - t0)
