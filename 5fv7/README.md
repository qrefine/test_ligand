1. phenix.fetch_pdb 5fv7 --mtz    ----5fv7.pdb 5fv7.mtz

2. phenix.ready_set 5fv7.pdb ----R3Z.cif

3. phenix.refine 5fv7.pdb 5fv7.mtz R3Z.cif ----5fv7_refine_001.pdb 5fv7_refine_001.mtz

4. qr.finalise 5fv7_refine_001.pdb ----5fv7_refine_001_complete.pdb

5. phenix.pdbtools 5fv7_refine_001_complete.pdb modify.selection="element H" occupancies.set=0 ----5fv7_refine_001_complete.pdb_modified.pdb
