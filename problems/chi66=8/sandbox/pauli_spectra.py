import itertools, numpy as np
w=np.exp(1j*np.pi/4)
I=np.eye(2); X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1,-1])
paulis=[I,X,Y,Z]

def kronall(xs):
    z=np.array([1.],complex)
    for x in xs: z=np.kron(z,x)
    return z

def hist(v):
    v=v/np.linalg.norm(v); out={}
    for ps in itertools.product(paulis,repeat=5):
        a=np.vdot(v,kronall(ps)@v)
        # Pauli expectations Hermitian, bin robustly
        key=round(float(np.real(a)),10)
        out[key]=out.get(key,0)+1
    return dict(sorted(out.items()))

T=np.array([1,w])/np.sqrt(2); Tp=np.array([1,-w])/np.sqrt(2)
cat=(kronall([T]*5)+kronall([Tp]*5))/np.sqrt(2)
print('cat',hist(cat))
zero=np.array([1,0]); one=np.array([0,1]); plus=np.array([1,1])/np.sqrt(2)
for gam in [(1+1j)/np.sqrt(2),(1-1j)/np.sqrt(2),(-1-1j)/np.sqrt(2),(-1+1j)/np.sqrt(2)]:
    v=kronall([zero]*5)+gam*kronall([one,zero,plus,plus,plus])
    print('orth',gam,hist(v))
for gam in [1j,-1j,-.5]:
    v=kronall([zero]*5)+gam*kronall([zero,plus,plus,plus,plus])
    print('nonorth',gam,hist(v))
