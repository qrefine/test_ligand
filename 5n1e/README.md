1. phenix.fetch_pdb 5n1e --mtz    ----5n1e.pdb 5n1e.mtz

2. phenix.ready_set 5n1e.pdb ----9NT.cif

3. phenix.refine 5n1e.pdb 5n1e.mtz 9NT.cif ----5n1e_refine_001.pdb 5n1e_refine_001.mtz

4. phenix.python rm_low_occ_conformers.py    ----5n1e_refine_001_rmconformers.pdb

5. qr.finalise 5n1e_refine_001_rmconformers.pdb    ----5n1e_refine_001_complete.pdb

6. phenix.pdbtools 5n1e_refine_001_rmconformers_complete.pdb modify.selection="element H" occupancies.set=0    ----5n1e_refine_001_complete.pdb_modified.pdb