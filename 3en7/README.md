1. phenix.fetch_pdb 3en7 --mtz    ----3en7.pdb 3en7.mtz

2. phenix.ready_set 3en7.pdb    ----ABJ.cif

3. phenix.refine 3en7.pdb 3en7.mtz ABJ.cif    ----3en7_refine_001.pdb 3en7_refine_001.mtz

4. qr.finalise 3en7_refine_001.pdb    ----3en7_refine_001_complete.pdb

5. phenix.pdbtools 3en7_refine_001_complete.pdb modify.selection="element H" occupancies.set=0    ----3en7_refine_001_complete.pdb_modified.pdb
