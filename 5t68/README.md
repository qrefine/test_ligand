1. phenix.fetch_pdb 5t68 --mtz    ----5t68.pdb 5t68.mtz

2. phenix.ready_set 5t68.pdb    ----77V.cif

3. phenix.refine 5t68.pdb 5t68.mtz 77V.cif    ----5t68_refine_001.pdb 5t68_refine_001.mtz

4. qr.finalise 5t68_refine_001.pdb    ----5t68_refine_001_complete.pdb

5. phenix.pdbtools 5t68_refine_001_complete.pdb modify.selection="element H" occupancies.set=0    ----5t68_refine_001_complete.pdb_modified.pdb

