import psi4
from pyscf import gto, scf, cc



mol = gto.Mole()
mol.unit = "bohr"
mol.build( atom = '''Li  0 0 0; H 0 0 3.080''', basis = '6-31G')
scf.conv_tol= 1e-12
mf = scf.RHF(mol).run()
mycc = cc.CCSD(mf)
#cc2 = mycc.RCC2(nroots=1)
mycc.conv_tol=1e-12
mycc.kernel()

print("nuclear repulsion energy")
print(mol.energy_nuc())

print("pyscf")
print(mf.kernel())
print(mycc.kernel())
