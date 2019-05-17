Q: The ligand 9PA lost 2 hydrogens afier doing refinement.

9PA_download_from_www.rcsb.org(58 atoms), 4cjl_refine_001_complete.pdb_modified.pdb_modified.pdb(56 atoms)

commands:

1. phenix.fetch_pdb 4cjl --mtz    ----4cjl.pdb 4cjl.mtz

2. phenix.ready_set 4cjl.pdb    ----9PA.cif 9PA.pdb

3. phenix.refine 4cjl.pdb 4cjl.mtz 9PA.cif    ----4cjl_refine_001.pdb 4cjl_refine_001.mtz

4. qr.finalise 4cjl_refine_001.pdb    ----4cjl_refine_001_complete.pdb

5. phenix.pdbtools 4cjl_refine_001_complete.pdb modify.selection="element H" occupancies.set=0    ----4cjl_refine_001_complete.pdb_modified.pdb

6. phenix.pdbtools 4cjl_refine_001_complete.pdb_modified.pdb keep="resname 9PA"    ----4cjl_refine_001_complete.pdb_modified.pdb_modified.pdb(56 atoms)
