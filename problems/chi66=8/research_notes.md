The phase-state convention used here is

\[
T=|0\rangle+\omega|1\rangle,\qquad
T^\perp=|0\rangle-\omega|1\rangle,
\qquad \omega=e^{i\pi/4}.
\]

Consequently

\[
C=\sqrt2\sum_{\substack{x\in\mathbb F_2^6\\ |x|\text{ even}}}
\omega^{|x|}|x\rangle.
\]

The three-term decomposition follows by grouping amplitudes at weights $0,2,4,6$. With

\[
g=|0^6\rangle-i|1^6\rangle,\quad
e=\sum_{|x|\text{ even}}|x\rangle,\quad
k=\sum_{|x|\text{ even}}(-1)^{\binom{|x|}{2}}|x\rangle,
\]

one has

\[
C=2\sqrt2\,g+\frac{-1+i}{\sqrt2}e+\frac{-1-i}{\sqrt2}k.
\]

For the repetition-code support of $g$, using the affine coordinate $t\in\mathbb F_2$, the phase can be written $i^t(-1)^t=(-i)^t$. Thus all three terms fit the affine-quadratic stabilizer convention without a normalization ambiguity.

The vectors $g,e,k$ are independent. A linear relation evaluated at weights two and four forces the $e,k$ coefficients to vanish, after which the $g$ coefficient vanishes. Hence their nine pairwise tensor products are independent. This says only that the displayed tensor-product decomposition cannot be shortened by deletion; it gives no general rank-nine lower bound.

Qassim's Waterloo thesis title page gives 2020, while the official repository
records a February 19, 2021 deposit. It states the target conjecture as
equation (4.30) in §4.4, “Discussion, conjectures, and open problems”:

\[
\chi(\mathrm{cat}_6\otimes\mathrm{cat}_6)\leq 8.
\]

Equation (4.31) explains the conjectural exponent $3/8$. Pairing $2L$ copies into $L$ rank-eight blocks and contracting them in a chain would give cat states on $8L+2$ qubits with rank at most $8^L$, so

\[
\lim_{L\to\infty}\frac{\log_2 8^L}{8L+2}=\frac38.
\]

The lower bound $\chi(C^{\otimes2})\ge3$ is best presented using the published exact theorem $\chi(\mathrm{cat}_6)=3$, proved in the appendix of Qassim–Pashayan–Gosset, followed by the contraction of one block with $\langle0^6|$. The appendix proof of $\chi(\mathrm{cat}_5)>2$ uses a canonical form for pairs of stabilizer states and computer-assisted Pauli-spectrum comparisons. A short summary that omits the canonical-form proof, the restriction $0<|\gamma|\le1$, normalization factors, and the finite computation is not a self-contained proof and should not be presented as one.

Qassim–Pashayan–Gosset use normalized $T$ states. Their cat state equals $C/8$
under the convention of this problem, since the six factors of $1/\sqrt2$
contribute $1/8$ and the outer factor is unchanged. Overall nonzero scaling
leaves exact stabilizer rank invariant.

There is a rigorous restriction on decompositions product across the natural
$6|6$ cut. If

\[
C\otimes C=\sum_{j=1}^k c_j\alpha_j\otimes\beta_j
\]

with stabilizer factors, and the distinct left rays are independent, grouping
equal left rays gives $C\otimes C=\sum_p\alpha_p\otimes u_p$. Partial
contraction first shows that $C$ is in the left span. Uniqueness in the
independent left family then forces $u_p=\lambda_pC$ and
$C=\sum_p\lambda_p\alpha_p$. At least three $\lambda_p$ are nonzero, and each
corresponding group needs at least three right stabilizer states because
$\chi(C)=3$. Hence $k\ge9$. The same statement holds with left and right
exchanged.

More generally, write the amplitude-matrix identity as

\[
ADB^{\mathsf T}=CC^{\mathsf T},
\]

where $A,B$ contain the local stabilizer vectors and $D$ the nonzero
coefficients. If $r=\operatorname{rank}A$ and $r'=\operatorname{rank}B$, Sylvester's
inequality gives $r+r'\le k+1$. Partial contraction shows $C$ lies in each local
column span, so $r,r'\ge\chi(C)=3$. Thus for $k=8$ one necessarily has
$r+r'\le9$, and both local collections are dependent. This does not address
stabilizer summands entangled across the cut.

There is a second exact contraction. Let

\[
B=|00\rangle+i|11\rangle,
\qquad \langle B|=\langle00|-i\langle11|.
\]

Then

\[
\langle B|T,T\rangle=\langle B|T^\perp,T^\perp\rangle=2,
\qquad
\langle B|T,T^\perp\rangle
=\langle B|T^\perp,T\rangle=0.
\]

Contracting one qubit from each block of $C^{\otimes2}$ therefore gives

\[
\langle B|C^{\otimes2}
=T^{\otimes10}+(T^\perp)^{\otimes10}
=\sqrt2\,\mathrm{cat}_{10}.
\]

Choose a two-qubit Clifford $W$ with $W|00\rangle\propto B$. Then
$\langle B|\propto\langle00|W^\dagger$, so Bell contraction preserves stabilizer
states (or annihilates them) by Clifford closure followed by computational-basis
restriction. Thus

\[
\chi(C^{\otimes2})\ge\chi(\mathrm{cat}_{10})\ge3.
\]

No rigorous proof of $\chi(\mathrm{cat}_{10})\ge4$ was found. Pair-classification proves the threshold three for small cats, but improving this to four would require control of spans of three stabilizer states, for which the pair normal form does not directly generalize.

A focused rank-eight reduction comes from isolating the two-term part of the
known decomposition. Set

\[
D=be+ck,\qquad b=\frac{-1+i}{\sqrt2},\quad
c=\frac{-1-i}{\sqrt2}.
\]

Then

\[
C^{\otimes2}=8g^{\otimes2}+2\sqrt2(g\otimes D+D\otimes g)+D^{\otimes2},
\]

and therefore

\[
\chi(C^{\otimes2})\le 5+\chi(D^{\otimes2}).
\]

Thus $\chi(D^{\otimes2})\le3$ would prove the desired upper bound eight. The
ordinary product expansion gives four terms and recovers nine.

The five-qubit compression must be expressed as an invertible six-bit Clifford
map, not as a dimension-changing “reversible” map. Use

\[
(x_1,\ldots,x_6)\mapsto(p,y_1,\ldots,y_5)
=(x_1+\cdots+x_6,x_2,\ldots,x_6).
\]

Its inverse is

\[
x=(p+y_1+\cdots+y_5,y_1,\ldots,y_5).
\]

On the even-parity support \(p=0\), one has

\[
S(x)=q(y):=\sum_{j<k}y_jy_k+\sum_jy_j\pmod2,
\qquad
U D=-\sqrt2\,|0\rangle\otimes
\sum_y i^{-q(y)}|y\rangle.
\]

The scalar follows because \(b+c=-\sqrt2\) at \(q=0\) and
\(b-c=i\sqrt2=-\sqrt2(-i)\) at \(q=1\). Clifford invariance and contraction
with \(\langle0|\) give \(\chi(D)=\chi(d)\) and
\(\chi(D\otimes D)=\chi(d\otimes d)\).

It is essential that $q$ in the exponent is the Boolean value $0$ or $1$;
writing $i^{\sum_{j<k}y_jy_k+\sum_jy_j}$ as an unrestricted integer exponent
gives the wrong phase. The compressed full-support state is not stabilizer:
for $h=-q\pmod4$, the mixed second difference at $0$ in directions $e_1,e_2$
is $1\pmod4$, whereas every stabilizer exponent $L+2Q$ has even mixed second
differences. Hence $\chi(D)=2$ exactly.

The polar form of $q$ is

\[
B(y,z)=(\sum y)(\sum z)+y\cdot z.
\]

Its radical is generated by $r=1^5$, with $q(y+r)=q(y)+1$. Therefore the
ten-qubit phase $i^{-q(y)-q(z)}$ is the constant $-i$ on the affine graph
$z=y+r$. The uniform state on this graph is an exact stabilizer state entangled
across the $5|5$ cut. This is one plausible summand of a rank-three search, but
no exact completion by two other stabilizer states was found.

There is a rigorous finite support-dimension reduction for a possible
three-term decomposition of \(\psi=d\otimes d\). If the affine supports
\(A_1,A_2,A_3\) cover the full ten-bit support, then
\(\max_j\dim A_j\ge9\), because \(3\cdot2^8<2^{10}\). If any \(A_j\) is
proper, place it in an affine hyperplane \(H\) and restrict to the opposite
coset \(K\). The corresponding Pauli-\(Z\) projection kills that summand and
preserves the other stabilizer summands, so \(\chi(\psi|_K)\le2\). Therefore
a decomposition with at most three summands implies either (i) one of the 2046
hyperplane-coset restrictions has rank at most two, or (ii) every summand has
full support. Thus the second branch in the finite check must exclude
representations by at most three full-support stabilizer phases, including
repeated rays (which can be combined), rather than only triples of distinct
rays. Excluding these two cases would prove \(\chi(d\otimes d)=4\), but neither
exclusion has yet been carried out.

No ten-bit hyperplane-coset restriction of \(d\otimes d\) has rank one. Its
phase exponent modulo two has polar form \(B\oplus B\), whose radical has
dimension two and whose nondegenerate quotient has dimension eight. A totally
isotropic subspace therefore has dimension at most \(2+8/2=6\). A
full-support stabilizer phase on a nine-dimensional affine hyperplane would
force its direction space to be totally isotropic, because all mixed second
differences of a stabilizer exponent are even. Thus each restriction in the
finite branch has rank at least two; the case that remains to exclude is
exactly rank two.

If the five-dimensional graph \(z=y+1^5\) were one support and the other two
supports were proper, the other two must cover 992 points. Two proper affine
subspaces can do this only if both are disjoint nine-dimensional hyperplanes;
nonparallel hyperplanes have union 768. This restricts, but does not exclude,
using the graph slice.

The plane spanned by the two full-support stabilizers \(1\) and \((-1)^q\)
contains exactly those two stabilizer rays. A full-support combination has
amplitude ratio in \(\{\pm1,\pm i\}\) between the \(q=1\) and \(q=0\) level
sets. The ratios \(\pm1\) give the original rays, while \(\pm i\) give
\(i^{\pm q}\), excluded by the odd mixed second difference. If one level
amplitude vanishes, the support is a \(q\)-level set. Translation by
\(r=1^5\) swaps the levels because \(q(y+r)=q(y)+1\), so both have size 16.
The zero level is not affine: it contains \(0\),
\(u=e_1+e_2+e_3\), and \(v=e_1+e_2+e_4\), but not
\(u+v=e_3+e_4\). If the one level were affine, its complement would be an
affine hyperplane, contradicting the preceding fact. This rigidity alone does not imply
multiplicativity: the Lovitz–Steffan theorem proves rank four only for a
particular generic family and does not state that “exactly two stabilizer
rays in the plane” is a sufficient hypothesis.

Writing

\[
u=\sum_y|y\rangle,\qquad v=\sum_y(-1)^{q(y)}|y\rangle
\]

gives the useful exact form

\[
d=\frac{1-i}{2}(u+iv).
\]

Although this resembles a logical one-qubit magic state, \(u,v\) are not a
logical stabilizer basis of a common five-qubit stabilizer code. In graph-state
language their unsigned stabilizer intersection is controlled by the radical
\(\langle r\rangle\), and translation by \(r\) has opposite signs on the two
states.

The tensor-square plane has an exact rigidity statement: the only stabilizer
rays in
\(\operatorname{span}\{u\otimes u,u\otimes v,v\otimes u,v\otimes v\}\)
are those four product rays. Every vector in the plane is constant on the four
cells indexed by \((q(y),q(z))\), each of size 256. An affine support can use
only 1, 2, or 4 cells. One-cell supports and row/column two-cell supports have
a nonaffine \(q\)-level projection. Diagonal two-cell supports are levels of
the nonaffine quadratic \(q(y)+q(z)\). For full support, restrictions to fixed
\(y\) or \(z\) and the one-copy plane lemma force a two-by-two sign table.
Product sign tables are the four product rays; the only other class contains
\((-1)^{q(y)q(z)}\), whose exponent \(2q(y)q(z)\) has fourth additive
difference 2 modulo 4 in directions \((e_1,0),(e_2,0),(0,e_1),(0,e_2)\).
Thus a three-term decomposition of \(d^{\otimes2}\), if one exists, must use a
stabilizer outside this natural four-dimensional plane.

A suggested 64-point enlargement of the graph slice is not a stabilizer and
must not be used. On

\[
L=\{(y,y+sr):y\in\mathbb F_2^5,\ s\in\mathbb F_2\}
\]

the target phase is \((-1)^{q(y)}\) for \(s=0\) and \(-i\) for \(s=1\).
An exponent is

\[
H(y,s)=2q(y)+3s+2s q(y)\pmod4.
\]

The mixed third difference in coordinate directions \(e_1,e_2,s\) is 2
modulo 4, excluding a stabilizer phase. The error in the tempting formula
\(-2q(y)-s\) is treating \(q(y+r)=q(y)+1\pmod2\) as an equality of ordinary
integer representatives. Total isotropy of the direction space for
\(B\oplus B\) is necessary for this phase restriction to be stabilizer, but
is not sufficient.

For fixed qubit number there are only finitely many stabilizer rays. Hence
the set of states of stabilizer rank at most \(k\) is a finite union of
linear spans of at most \(k\) stabilizer rays and is Zariski- and
Euclidean-closed. There is therefore no separate border-stabilizer-rank
degeneration that could turn a failed exact rank-three decomposition into a
limiting rank-three decomposition on these ten qubits.

The canonical-pair lemma of Qassim--Pashayan--Gosset is consistent with this
compression: the two stabilizers $e,k$ are orthogonal, since translation by
$r$ flips $(-1)^q$. Their compressed supports are full, and their common
stabilizer structure reduces the nontrivial target to five qubits. The general
multiplicativity result of Lovitz--Steffan proves rank four only for a generic
family of rank-two states and does not decide the special algebraic phase here.

There is also the exact projection identity

\[
C^{\otimes2}=\sqrt2\,\frac{I+Z^{\otimes6}\otimes I^{\otimes6}}2
\,|\mathrm{cat}_{12}\rangle.
\]

Together with the $\mathrm{cat}_2$ contraction to $\mathrm{cat}_{10}$ this gives

\[
\chi(\mathrm{cat}_{10})\le\chi(C^{\otimes2})
\le\chi(\mathrm{cat}_{12}).
\]

Neither endpoint currently improves the numerical interval.

Stabilizer fidelity or extent must not be used as a rank lower bound without a precise theorem. The standard inequality $\xi(\psi)\ge1/F(\psi)$ concerns stabilizer extent; the tempting general inequality $\xi(\psi)\le\chi(\psi)$ does not follow from Cauchy–Schwarz because a rank-minimal stabilizer spanning set can have an ill-conditioned Gram matrix. Consequently a numerical extent value above four would not by itself certify stabilizer rank at least five.

Computational investigations, useful only as search guidance:

- The five-qubit Pauli-spectrum enumeration gave

  \[
  \mathrm{PS}(\mathrm{cat}_5):
  (-1/2)^{20},(-1/4)^{40},0^{782},
  (1/4)^{120},(1/2)^{60},1^2.
  \]

- Orthogonal canonical rank-two candidates had $710$ zero Pauli expectations. The nonorthogonal candidates $\gamma=\pm i$ had $722$ zeros. The candidate $\gamma=-1/2$ had $782$ zeros but thirty expectations of absolute value $3/4$.

- The Clifford $A=e^{-i\pi/4}SX$ has eigenvectors $T,T^\perp$ with eigenvalues $+1,-1$. Applying $A$ on any even subset of the six qubits fixes $C$. Applying these symmetries to $g,e,k$ generated $48$ distinct stabilizer rays spanning a $32$-dimensional subspace. Randomized searches over products of these rays found no exact eight-term witness. This is evidence only about that restricted pool.

- The parity support can be Clifford-compressed with the six-bit invertible map

  \[
  x\mapsto(x_1+\cdots+x_6,x_2,\ldots,x_6).
  \]

  Thus one cat state is Clifford-equivalent to a five-qubit state tensored
  with a stabilizer ancilla, and its square reduces in the same way to a
  ten-qubit target. A simulated-annealing search at rank eight did not yield a
  certificate; this is not evidence against the conjecture.

- A warm-started simulated-annealing search for a rank-three decomposition of
  the smaller target $D^{\otimes2}$ also did not improve on the residual of a
  leave-one-out four-product seed. This is search evidence only, not a lower
  bound on $\chi(D^{\otimes2})$.

The 2026 Labib–Russo four-copy qubit identity concerns the face-magic (their $T$-type) Clifford orbit, not the phase state used here (their $H$-type orbit), so it does not supply an eight-term decomposition for this problem.

Promising exact directions are an affine-quadratic search over genuinely entangled ten- or twelve-qubit stabilizer states, or a classification of three-stabilizer spans sufficient to decide whether $\chi(\mathrm{cat}_{10})\ge4$. Any numerical witness must retain exact tableau data and exact algebraic coefficients so that its amplitude identity can be certified.
