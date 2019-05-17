1. phenix.fetch_pdb 4lgh --mtz    ----4lgh.pdb 4lgh.mtz

2. phenix.ready_set 4lgh.pdb    ----0JN.cif

3. phenix.refine 4lgh.pdb 4lgh.mtz 0JN.cif    ----4lgh_refine_001.pdb 4lgh_refine_001.mtz

4. qr.finalise 4lgh_refine_001.pdb    ----4lgh_refine_001_complete.pdb

5. phenix.pdbtools 4lgh_refine_001_complete.pdb modify.selection="element H" occupancies.set=0    ----4lgh_refine_001_complete.pdb_modified.pdb
