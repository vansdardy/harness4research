import itertools
import numpy as np

w = np.exp(1j*np.pi/4)
A = np.array([[0, np.conj(w)], [w, 0]], complex)

def bits(z, n=6):
    return np.array([(z >> (n-1-j)) & 1 for j in range(n)], int)

G = np.zeros(64, complex)
G[0] = 1/np.sqrt(2)
G[-1] = -1j/np.sqrt(2)
E = np.zeros(64, complex)
K = np.zeros(64, complex)
for z in range(64):
    x = bits(z)
    if x.sum() % 2 == 0:
        E[z] = 2**(-2.5)
        K[z] = 2**(-2.5) * (-1)**(sum(x[j]*x[k] for j in range(6) for k in range(j+1,6)))

base = [G,E,K]
coef = np.array([.5,(-1+1j)/2,(-1-1j)/2])
cat = sum(c*v for c,v in zip(coef,base))
assert np.linalg.norm(cat-sum(c*v for c,v in zip(coef,base))) < 1e-12

def apply_local(v, mask):
    ten = v.reshape([2]*6)
    for q in range(6):
        if (mask >> q) & 1:
            ten = np.tensordot(A, ten, axes=(1,q))
            ten = np.moveaxis(ten, 0, q)
    return ten.reshape(-1)

pool=[]; labels=[]
for mask in range(64):
    if mask.bit_count()%2: continue
    for j,v in enumerate(base):
        u=apply_local(v,mask)
        # canonical global phase for dedup
        nz=np.flatnonzero(np.abs(u)>1e-10)[0]
        u=u*np.exp(-1j*np.angle(u[nz]))
        if not any(abs(np.vdot(t,u))>1-1e-10 for t in pool):
            pool.append(u); labels.append((mask,j))
P=np.array(pool).T
print('pool',len(pool),'rank',np.linalg.matrix_rank(P))
R=np.max(np.abs(P.conj().T@P-np.eye(len(pool))))
print('max offdiag/diag deviation',R)

H=P.conj().T@P
h=P.conj().T@cat
N=len(pool)
pairs=np.array([(i,j) for i in range(N) for j in range(N)],int)
b=(h[:,None]*h[None,:]).reshape(-1)

def gram_to_all(sel):
    # rows indexed all candidates, cols selected
    out=[]
    for k in sel:
        a,bp=pairs[k]
        out.append((H[:,a][:,None]*H[:,bp][None,:]).reshape(-1))
    return np.array(out).T

def fit(sel):
    Q=gram_to_all(sel)[sel,:]
    bs=b[sel]
    c=np.linalg.lstsq(Q,bs,rcond=1e-11)[0]
    err=max(0.,1-np.real(np.vdot(bs,c)))
    return err,c,Q

rng=np.random.default_rng(4)
best=(1,None)
for restart in range(3000):
    sel=[]
    for step in range(8):
        if not sel:
            corr=b.copy(); den=np.ones(N*N)
        else:
            Q=gram_to_all(sel)[sel,:]
            bs=b[sel]
            c=np.linalg.lstsq(Q,bs,rcond=1e-10)[0]
            GS=gram_to_all(sel)
            corr=b-GS@c
            inv=np.linalg.pinv(Q,rcond=1e-10)
            den=1-np.real(np.einsum('ij,jk,ik->i',GS,inv,GS.conj()))
        score=np.abs(corr)**2/np.maximum(den,1e-10)
        score[sel]=-1
        # randomised restricted candidate list
        top=np.argpartition(score,-min(80,len(score)))[-min(80,len(score)):]
        vals=np.maximum(score[top],0)
        temp=0.08 + .35*(restart%7)/6
        probs=(vals/vals.max())**(1/temp)
        probs/=probs.sum()
        sel.append(int(rng.choice(top,p=probs)))
    err,c,Q=fit(sel)
    if err<best[0]:
        best=(err,sel.copy())
        print('best',restart,err,[(labels[pairs[k,0]],labels[pairs[k,1]]) for k in sel])
    if err<1e-18:
        print('FOUND',sel,c)
        break
