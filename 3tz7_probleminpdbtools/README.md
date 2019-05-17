We only tested the ligand of the non-covalent connection protein, some of the ligand don't have enough hydrogens after phenix.pdbtools.

1. phenix.fetch_pdb 3tz7 --mtz    ----3tz7.pdb 3tz7.mtz

2. phenix.refine 3tz7.pdb 3tz7.mtz    ----3tz7_refine_001.pdb 3tz7_refine_001.mtz

3. qr.finalise 3tz7_refine_001.pdb    ----3tz7_refine_001_complete.pdb

4. phenix.pdbtools 3tz7_refine_001_complete.pdb modify.selection="element H" occupancies.set=0    ----3tz7_refine_001_complete.pdb_modified.pdb
