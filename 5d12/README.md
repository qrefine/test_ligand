5d12 have ligand G97, but the phenix database don't have the reatraints ligand G97.


1. phenix.fetch_pdb 5d12 --mtz     ----5d12.pdb 5d12.mtz

2. phenix.refine 5d12.pdb 5d12.mtz    ----5d12_refine_001.pdb 5d12_refine_001.mtz

3. qr.finalise 5d12_refine_001.pdb    ----5d12_refine_001_complete.pdb

4. phenix.pdbtools 5d12_refine_001_complete.pdb modify.selection="element H" occupancies.set=0     ----5d12_refine_001_complete.pdb_modified.pdb
