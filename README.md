# test_ligand
We only tested the ligand of the non-covalent connection protein, some of the ligand don't have enough hydrongen after phenix.pdbtools.

phenix.fetch_pdb 4cjl --mtz        ----4cjl.pdb    4cjl.mtz

phenix.ready_set 4cjl.pdb        ----9PA.cif

phenix.refine 4cjl.pdb 4cjl.mtz 9PA.cif        ----4cjl_refine_001.pdb    4cjl_refine_001.mtz

qr.finalise 4cjl_refine_001.pdb         ----4cjl_refine_001_complete.pdb

phenix.pdbtools 4cjl_refine_001_complete.pdb modify.selection="element H" occupancies.set=0         ----4cjl_refine_001_complete.pdb_modified.pdb

phenix.python ligand.py         ----9PA.pdb
