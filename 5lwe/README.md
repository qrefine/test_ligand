Q1: 5lwe have the ligand 79K, but the phenix database don't have the reatraints ligand 79K.

Q2: The ligand 79k lost 2 hydrogens afier doing refinement.

79K_download_from_www.rcsb.org (53 atoms), 5lwe_refine_001_complete.pdb_modified.pdb_modified.pdb(51 atoms)

commands:

1. phenix.fetch_pdb 5lwe --mtz ----5lwe.pdb 5lwe.mtz

2. phenix.ready_set 5lwe.pdb ----79K.cif 79K.pdb CLR.cif CLR.pdb MLI.cif MLI.pdb

3. phenix.refine 5lwe.pdb 5lwe.mtz 79K.cif CLR.cif MLI.cif ----5lwe_refine_001.pdb 5lwe_refine_001.mtz

4. qr.finalise 5lwe_refine_001.pdb ----5lwe_refine_001_complete.pdb

5. phenix.pdbtools 5lwe_refine_001_complete.pdb modify.selection="element H" occupancies.set=0 ----5lwe_refine_001_complete.pdb_modified.pdb

6. phenix.pdbtools 5lwe_refine_001_complete.pdb_modified.pdb keep="resname 79K" ----5lwe_refine_001_complete.pdb_modified.pdb_modified.pdb(51 atoms)