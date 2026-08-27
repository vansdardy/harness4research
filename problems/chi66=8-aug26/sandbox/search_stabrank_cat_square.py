import numpy as np
from stabrank.stabrank_core import run_sa_pauli_expansion

w=np.exp(1j*np.pi/4)

def bits(z,n): return [(z>>(n-1-j))&1 for j in range(n)]

G=np.zeros(32,complex); E=np.zeros(32,complex); K=np.zeros(32,complex)
for z in range(32):
    y=bits(z,5); x=[sum(y)%2]+y; wt=sum(x)
    if wt in (0,6):
        G[z]=(1 if wt==0 else -1j)/np.sqrt(2)
    E[z]=2**(-2.5)
    K[z]=2**(-2.5)*(-1)**(sum(x[j]*x[k] for j in range(6) for k in range(j+1,6)))
base=[G,E,K]
c=np.array([.5,(-1+1j)/2,(-1-1j)/2])
cat=sum(a*v for a,v in zip(c,base))
target=np.kron(cat,cat)
target/=np.linalg.norm(target)
known=[np.kron(a,b) for a in base for b in base]

for seed in range(8):
    initial=[known[j] for j in range(9) if j != seed%9]
    result=run_sa_pauli_expansion(
        target=target,n_orig=10,p_prime=2,k_subset_size=8,
        initial_basis=initial,initial_temperature=1.0,cooling_rate=.995,
        num_iterations_at_temp=1000,min_temperature=1/2000,atol=1e-8,
        two_func_perturb_prob=.35,random_replace_prob=.05,
        use_real_qubit_moves=False,clifford_ratio=.5,
        early_exit_threshold=1e-10,seed=100+seed,num_chains=16)
    _, funcs, coeffs, err, cost, trace=result
    print('seed',seed,'err',err,'cost',cost,flush=True)
    if err<1e-9:
        np.savez_compressed('sandbox/cat_square_8.npz',target=target,coeffs=coeffs,
                            **{f'basis_{j}':v for j,v in enumerate(funcs)})
        break
