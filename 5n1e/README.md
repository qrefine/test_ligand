Q: The ligand 9NT lost 2 hydrogens afier doing refinement.

commands:

1. phenix.fetch_pdb 5n1e --mtz    ----5n1e.pdb 5n1e.mtz

2. phenix.ready_set 5n1e.pdb    ----9NT.cif 9NT.pdb

3. phenix.refine 5n1e.pdb 5n1e.mtz 9NT.cif refinement.input.xray_data.r_free_flags.label=R-free-flags
   ----5n1e_refine_001.pdb 5n1e_refine_001.mtz

4. phenix.python rm_low_occ_conformers.py    ----5n1e_refine_001_rmconformers.pdb

5. qr.finalise 5n1e_refine_001_rmconformers.pdb    ----5n1e_refine_001_rmconformers_complete.pdb

6. phenix.pdbtools 5n1e_refine_001_rmconformers_complete.pdb modify.selection="element H" occupancies.set=0    ----5n1e_refine_001_rmconformers_complete.pdb_modified.pdb
 
7. phenix.pdbtools 5n1e_refine_001_rmconformers_complete.pdb_modified.pdb keep="resname 9NT" ---- 5n1e_refine_001_rmconformers_complete.pdb_modified.pdb_modified.pdb(26 atoms)
