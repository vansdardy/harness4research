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

Qassim's Waterloo thesis is dated February 19, 2021 in the official repository record. It states the target conjecture as equation (4.30), near the end of §4.3:

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

After even-parity compression

\[
x=(y_1+\cdots+y_5,y_1,\ldots,y_5),
\]

one has

\[
S(x)=q(y):=\sum_{j<k}y_jy_k+\sum_jy_j\pmod2,
\qquad
D\simeq \sum_y i^{-q(y)}|y\rangle.
\]

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

- The parity support can be Clifford-compressed by setting

  \[
  x=(y_1+\cdots+y_5,y_1,\ldots,y_5).
  \]

  Thus one cat state is Clifford-equivalent to a five-qubit state and its square to a ten-qubit target. A simulated-annealing search at rank eight did not yield a certificate; this is not evidence against the conjecture.

- A warm-started simulated-annealing search for a rank-three decomposition of
  the smaller target $D^{\otimes2}$ also did not improve on the residual of a
  leave-one-out four-product seed. This is search evidence only, not a lower
  bound on $\chi(D^{\otimes2})$.

The 2026 Labib–Russo four-copy qubit identity concerns the face-magic (their $T$-type) Clifford orbit, not the phase state used here (their $H$-type orbit), so it does not supply an eight-term decomposition for this problem.

Promising exact directions are an affine-quadratic search over genuinely entangled ten- or twelve-qubit stabilizer states, or a classification of three-stabilizer spans sufficient to decide whether $\chi(\mathrm{cat}_{10})\ge4$. Any numerical witness must retain exact tableau data and exact algebraic coefficients so that its amplitude identity can be certified.
