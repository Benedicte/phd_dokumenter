import numpy as np
from quantum_systems import construct_pyscf_system_rhf
from coupled_cluster.mix import DIIS, AlphaMixer
from coupled_cluster.cc2 import CC2

molecule = "li 0.0 0.0 0.0; h 0.0 0.0 3.08 "
basis = "6-31G"
system = construct_pyscf_system_rhf(
    molecule,
    basis=basis,
    np=np,
    verbose=False,
    add_spin=True,
    anti_symmetrize=True,
)

conv_tol = 1e-12
cc2 = CC2(system, mixer=AlphaMixer, verbose=False)
t_kwargs = dict(tol=conv_tol, theta=0)
l_kwargs = dict(tol=conv_tol, theta=0)

cc2.compute_ground_state(t_kwargs=t_kwargs, l_kwargs=l_kwargs)
print("Ground state energy: {0}".format(cc2.compute_energy()))
#dm1 = cc2.compute_one_body_density_matrix()
dip_mom_z = np.trace(np.dot(dm1, system.dipole_moment[2]))
print(f"dip_mom_z={dip_mom_z}")
