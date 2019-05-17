3tz9 have the ligand AQU, but the phenix database don't have the reatraints ligand AQU.


1. phenix.fetch_pdb 3tz9 --mtz    ----3tz9.pdb 3tz9.mtz

2. phenix.refine 3tz9.pdb 3tz9.mtz    ----3tz9_refine_001.pdb 3tz9_refine_001.mtz

3. qr.finalise 3tz9_refine_001.pdb    ----3tz9_refine_001_complete.pdb

4. phenix.pdbtools 3tz9_refine_001_complete.pdb modify.selection="element H" occupancies.set=0 ----3tz9_refine_001_complete.pdb_modified.pdb
