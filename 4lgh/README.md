Q: The ligand 0JN lost 3 hydrogens afier doing refinement. Actually hydrogens were not present in cif file generated by elbow.

0JN_download_from_www.rcsb.org (49 atoms), 4lgh_refine_001_complete.pdb_modified.pdb_modified.pdb(46 atoms)

commands:

1. phenix.fetch_pdb 4lgh --mtz    ----4lgh.pdb 4lgh.mtz

2. phenix.ready_set 4lgh.pdb    ----0JN.cif 0JN.pdb (46 atoms, created by elbow)

3. phenix.refine 4lgh.pdb 4lgh.mtz 0JN.cif    ----4lgh_refine_001.pdb 4lgh_refine_001.mtz

4. qr.finalise 4lgh_refine_001.pdb    ----4lgh_refine_001_complete.pdb

5. phenix.pdbtools 4lgh_refine_001_complete.pdb modify.selection="element H" occupancies.set=0    ----4lgh_refine_001_complete.pdb_modified.pdb

6. phenix.pdbtools 4lgh_refine_001_complete.pdb_modified.pdb keep="resname 0JN" ----4lgh_refine_001_complete.pdb_modified.pdb_modified.pdb(46 atoms)
