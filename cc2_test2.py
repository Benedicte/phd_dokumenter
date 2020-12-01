import psi4

psi4.set_memory('500 MB')
#psi4.set_options({'units' : 'bohr'})
psi4.set_module_options('scf', {'e_convergence': '1e-12'})

LiH = psi4.geometry( """
0 1
units Bohr
Li  0.0  0.0  0.0   
H   0.0  0.0  3.0800
""")

#psi4.set_options({
#"reference": "rhf"})

print("psi4")
psi4.energy('scf/cc-pvdz')
#psi4.energy('cc2/cc-pvdz')
#psi4.energy('mp2/cc-pvdz')

