#### Problem statement and conventions

I interpret “computational basis” as the fixed standard computational basis. Clifford changes of basis may be used explicitly because stabilizer rank is Clifford-invariant; an arbitrary orthonormal change of basis is not allowed.

A stabilizer state is normally a normalized ray. Throughout the proof I use nonzero, unnormalized representatives of such rays, which does not change stabilizer rank. In the affine-quadratic normal form, choose affine coordinates $t\in\mathbb F_2^d$ on the support $A$. The phase is read as

$$
i^{L(t)}(-1)^{Q(t)},
$$

where $L$ is a linear polynomial modulo $4$ and $Q$ is a quadratic polynomial modulo $2$ (constant and linear terms may be absorbed between the two factors). This is the standard meaning of the phase convention in the question.

#### Result

Let $C=|\mathrm{cat}_6\rangle$. The rigorous conclusion is

$$
\boxed{3\leq \chi(C\otimes C)\leq 9.}
$$

The upper bound is given by an exact nine-term decomposition below. The lower bound uses the published theorem $\chi(\mathrm{cat}_6)=3$ and a stabilizer contraction. I do not obtain an eight-term decomposition, nor a lower bound excluding rank eight. Thus the question whether

$$
\chi(C\otimes C)\leq8
$$

remains unresolved here; it is Qassim's Conjecture (4.30) in thesis §4.4.

#### An exact three-term decomposition of $C$

Put

$$
\omega=e^{i\pi/4},\qquad
V=\{x\in\mathbb F_2^6:|x|\equiv0\pmod2\},\qquad
S(x)=\sum_{1\leq j<k\leq6}x_jx_k\pmod2,
$$

and define the following unnormalized states:

$$
\begin{aligned}
|g\rangle&=|0^6\rangle-i|1^6\rangle,\\
|e\rangle&=\sum_{x\in V}|x\rangle,\\
|k\rangle&=\sum_{x\in V}(-1)^{S(x)}|x\rangle.
\end{aligned}
$$

All three are stabilizer states in the affine-quadratic sense. For $e$ and $k$, the support is the even-parity linear code and the phases are respectively $1$ and $(-1)^S$. For $g$, parametrize the repetition code by $x=t(1,1,1,1,1,1)$; the phase is

$$
i^t(-1)^t=(-i)^t,
$$

which gives exactly the two displayed amplitudes.

Since $T^\perp=ZT$,

$$
C=\frac1{\sqrt2}\bigl(T^{\otimes6}+(T^\perp)^{\otimes6}\bigr)
  =\sqrt2\sum_{x\in V}\omega^{|x|}|x\rangle.
$$

I claim that

$$
\boxed{
C
=
2\sqrt2\,|g\rangle
+\frac{-1+i}{\sqrt2}|e\rangle
+\frac{-1-i}{\sqrt2}|k\rangle.
}
\tag{1}
$$

For an even-weight string $x$,

$$
(-1)^{S(x)}=(-1)^{\binom{|x|}{2}},
$$

whose signs at weights $0,2,4,6$ are $+1,-1,+1,-1$. Set

$$
a=2\sqrt2,\qquad b=\frac{-1+i}{\sqrt2},\qquad
c=\frac{-1-i}{\sqrt2}.
$$

The amplitudes of $ag+be+ck$, grouped by Hamming weight, are

$$
\begin{array}{c|c|c}
|x|&\text{amplitude}&\sqrt2\,\omega^{|x|}\\ \hline
0&a+b+c=\sqrt2&\sqrt2\\
2&b-c=i\sqrt2&i\sqrt2\\
4&b+c=-\sqrt2&-\sqrt2\\
6&-ia+b-c=-i\sqrt2&-i\sqrt2.
\end{array}
$$

Both sides vanish on odd-weight strings, so this proves (1) on every computational-basis vector.

#### The nine-term upper bound

Let

$$
d_g=2\sqrt2,\qquad d_e=\frac{-1+i}{\sqrt2},\qquad
d_k=\frac{-1-i}{\sqrt2}.
$$

Tensoring (1) with itself gives the exact identity

$$
\boxed{
C\otimes C
=
\sum_{u,v\in\{g,e,k\}}d_ud_v\,|u\rangle\otimes|v\rangle.
}
\tag{2}
$$

The tensor product of two stabilizer states is a stabilizer state: its affine support is the Cartesian product of the two supports, while its linear and quadratic phases are the sums of the phases of the factors. Equation (2) is therefore a nine-term stabilizer decomposition, and

$$
\chi(C\otimes C)\leq9.
$$

For clarity, the nine states in this particular expansion are linearly independent. Indeed, a relation among $g,e,k$ evaluated on strings of weights $2$ and $4$ first forces the coefficients of $e,k$ to vanish, and then the coefficient of $g$ vanishes. Tensor products of two independent triples are independent. This only shows that one cannot delete a term from (2); it is not an obstruction to an eight-term decomposition using different, possibly entangled, stabilizer states.

There is a modest general obstruction to improving (2) while keeping every
summand product across the displayed $6|6$ cut. Suppose

$$
C\otimes C=\sum_{j=1}^k c_j\,|\alpha_j\rangle\otimes|\beta_j\rangle,
$$

where every $\alpha_j$ and $\beta_j$ is a six-qubit stabilizer state. Group
proportional left factors, absorbing proportionality constants into the
coefficients, and denote the distinct resulting left factors by
$\alpha_{(1)},\ldots,\alpha_{(m)}$. If these vectors are linearly independent,
the decomposition has the form

$$
C\otimes C=\sum_{p=1}^m |\alpha_{(p)}\rangle\otimes|u_p\rangle.
$$

Contracting the right block against a linear functional nonzero on $C$ first
shows that $C$ belongs to the span of the $\alpha_{(p)}$. Uniqueness of
coordinates in this independent left family then gives scalars $\lambda_p$ such
that

$$
C=\sum_{p=1}^m\lambda_p|\alpha_{(p)}\rangle,
\qquad |u_p\rangle=\lambda_p C.
$$

At least three $\lambda_p$ are nonzero because $\chi(C)=3$. For every such $p$,
the terms grouped into $u_p$ express a nonzero multiple of $C$ using the
stabilizer states $\beta_j$, and hence that group contains at least three terms.
Consequently $k\ge9$. Thus an eight-term decomposition consisting only of
product stabilizer states would have to use linearly dependent sets of distinct
left factors and, by the same argument, distinct right factors.

The necessary dependence can also be quantified without assuming the distinct
factors independent. Regard the decomposition as the amplitude-matrix identity

$$
ADB^{\mathsf T}=CC^{\mathsf T},
$$

where the columns of $A$ and $B$ are the amplitude vectors of $\alpha_j$ and
$\beta_j$, and $D=\operatorname{diag}(c_1,\ldots,c_k)$ after zero terms are
removed. If $r=\operatorname{rank}A$ and $r'=\operatorname{rank}B$, Sylvester's
rank inequality gives

$$
1=\operatorname{rank}(ADB^{\mathsf T})\ge r+r'-k.
$$

Moreover $C$ belongs to both column spans: contract the other tensor factor
against any linear functional nonzero on $C$. Since each column is a stabilizer
state and $\chi(C)=3$, it follows that $r,r'\ge3$. Any eight-term product-cut
decomposition must therefore satisfy

$$
3\le r,r',\qquad r+r'\le9.
$$

This argument does not apply to stabilizer states entangled across the $6|6$
cut, which are allowed in the definition of $\chi(C\otimes C)$.

#### A smaller exact target for an eight-term construction

Put

$$
b=\frac{-1+i}{\sqrt2},\qquad c=\frac{-1-i}{\sqrt2},\qquad
|D\rangle=b|e\rangle+c|k\rangle.
$$

Thus $C=2\sqrt2\,g+D$, and hence

$$
C\otimes C
=8\,g\otimes g+2\sqrt2\,(g\otimes D+D\otimes g)+D\otimes D.
\tag{3}
$$

Expanding each occurrence of $D$ in the two mixed terms costs two stabilizer
states. Consequently

$$
\boxed{\chi(C\otimes C)\leq 5+\chi(D\otimes D).}
\tag{4}
$$

In particular, an exact three-stabilizer decomposition of $D\otimes D$ would
prove the desired bound $\chi(C\otimes C)\leq8$.

This reduced target has a simple five-qubit description, but the compression
must be implemented as a six-bit reversible map. Let $U$ be the
computational-basis permutation induced by

$$
(x_1,\ldots,x_6)\longmapsto(p,y_1,\ldots,y_5)
  =(x_1+\cdots+x_6,x_2,\ldots,x_6).
$$

Its inverse is

$$
x=(p+y_1+\cdots+y_5,y_1,\ldots,y_5),
$$

so $U$ is an invertible linear transformation implemented by CNOT gates. On
the even-parity support $V$, the first output bit is $p=0$. If

$$
q(y)=\sum_{1\leq j<k\leq5}y_jy_k+\sum_{j=1}^5y_j\pmod2,
\tag{5}
$$

then $S(x)=q(y)$ when $p=0$. Since the amplitudes of $D$ are
$-\sqrt2$ for $S=0$ and $i\sqrt2$ for $S=1$, the exact transformed
state is

$$
|d\rangle=\sum_{y\in\mathbb F_2^5}i^{-q(y)}|y\rangle,
\qquad U|D\rangle=-\sqrt2\,|0\rangle\otimes|d\rangle.
\tag{6}
$$

Here $q(y)$ in the exponent is represented by the integer $0$ or $1$.
Clifford invariance, adjoining a stabilizer ancilla, and contraction with
$\langle0|$ give the two directions needed for

$$
\chi(D)=\chi(d),\qquad \chi(D\otimes D)=\chi(d\otimes d).
$$

Accordingly, the missing certificate in this route is a three-term
affine-quadratic decomposition of the ten-qubit phase function

$$
(y,z)\longmapsto i^{-q(y)-q(z)}.
\tag{7}
$$

The state $D$ really has rank two, rather than one. It already has the
two-term decomposition $be+ck$. On the other hand, a full-support stabilizer
phase has an exponent modulo four of the form $L+2Q$, so its mixed second
difference is even. For the exponent $h=-q\pmod4$ of (6), evaluated at
$0,e_1,e_2,e_1+e_2$, the values are $0,3,3,3$, and therefore

$$
\Delta_{e_1}\Delta_{e_2}h(0)=3-3-3+0=1\pmod4.
$$

Thus (6) is not a stabilizer state and $\chi(D)=2$.

There are exactly two stabilizer rays in the plane spanned by the two
full-support stabilizers $1$ and $(-1)^q$. Indeed, up to overall scale, any
vector in that plane has one amplitude $a+b$ on $q=0$ and another $a-b$ on
$q=1$. If it is a full-support stabilizer state, their ratio must lie in
$\{1,-1,i,-i\}$. Ratios $1$ and $-1$ give the original two rays. Ratios $i$
and $-i$ give phases proportional to $i^q$ and $i^{-q}$, and the same
mixed-second-difference calculation excludes both. If one amplitude vanishes,
the support is a level set of $q$, each of which has size 16. The zero level
is not affine: it contains $0$, $u=e_1+e_2+e_3$, and
$v=e_1+e_2+e_4$, but not $u+v=e_3+e_4$. The one level cannot be affine
either, because its complement would then be the opposite affine hyperplane.
Hence no further stabilizer ray occurs.

There is at least one exact entangled stabilizer slice in (7). The polar form
of $q$ is

$$
B(y,z)=\Bigl(\sum_jy_j\Bigr)\Bigl(\sum_jz_j\Bigr)+y\mathbin\cdot z,
$$

whose radical is generated by $r=1^5$, and $q(y+r)=q(y)+1$. Hence (7) is the
constant $-i$ on the affine graph $z=y+r$. The uniform state on that graph is
a stabilizer state entangled across the $5|5$ cut. This observation has not
been extended here to a three-term decomposition of the full phase function
(7); the ordinary four products of the two summands of $D$ remain the only
certified decomposition. Thus (4) currently reproduces nine, not eight.

There is, however, a finite support-dimension reduction for deciding whether
the missing three-term decomposition exists. Let

$$
|\psi\rangle=|d\rangle\otimes|d\rangle
$$

and suppose $\psi=\sum_{j=1}^3c_j\varphi_j$, where
$A_j\subseteq\mathbb F_2^{10}$ is the affine support of $\varphi_j$. Because
$\psi$ has full support, the $A_j$ cover $\mathbb F_2^{10}$; in particular,
at least one has dimension at least nine, since $3\cdot2^8<2^{10}$.

More strongly, either all three $A_j$ have full dimension, or some affine
hyperplane-coset restriction of $\psi$ has stabilizer rank at most two. To see
this, if $A_j$ is proper, place it inside an affine hyperplane $H$ and let
$K=\mathbb F_2^{10}\setminus H$, which is the opposite coset. Projection onto
$K$ is a Pauli-$Z$ eigenspace projection, so it takes every stabilizer state
to zero or a stabilizer state. It annihilates $\varphi_j$, leaving at most two
summands for $\psi|_K$.

Consequently, proving $\chi(d\otimes d)=4$ can be reduced to two exact tasks:
exclude rank at most two for each of the $2(2^{10}-1)=2046$ hyperplane-coset
restrictions, and exclude decompositions by three full-support stabilizer
phases. This is a finite reduction, not its completion; no classification or
exhaustive certificate carrying out those two tasks is supplied here. It
also constrains the five-dimensional graph slice: if it were one summand and
the other two supports were both proper, those two supports would have to be
the two complementary affine hyperplanes (otherwise their union has at most
$768<992$ points), although a full-support remaining summand is also possible.

#### The lower bound

Qassim, Pashayan, and Gosset prove in the appendix of *Improved Upper Bounds on the Stabilizer Rank of Magic States* that

$$
\chi(\mathrm{cat}_6)=3.
\tag{8}
$$

The paper uses $|T\rangle_{\rm norm}=2^{-1/2}(|0\rangle+\omega|1\rangle)$,
whereas the problem uses the unnormalized vector. Its cat state is consequently
$C/8$. Multiplication by a nonzero overall scalar does not affect stabilizer
rank, so (8) applies with the convention here.

Their proof first shows $\chi(\mathrm{cat}_5)>2$ by a canonical-form classification of pairs of stabilizer states and a finite Pauli-spectrum comparison, and then uses the computational-basis contraction $\langle0|\mathrm{cat}_6\rangle\propto\mathrm{cat}_5$. I use (8) as a cited theorem rather than claiming a self-contained reproduction of that classification and computer-assisted finite check.

Now contract the second six-qubit block of $C\otimes C$ with the stabilizer bra $\langle0^6|$. Since

$$
\langle0^6|C\rangle=\sqrt2,
$$

we obtain

$$
(I\otimes\langle0^6|)(C\otimes C)=\sqrt2\,C.
\tag{9}
$$

Contracting a stabilizer state with a computational-basis stabilizer bra gives either zero or another stabilizer state. In affine coordinates, one intersects the affine support with the equations fixing the contracted coordinates and restricts the same affine-quadratic phase to that intersection. Hence an $r$-term decomposition of $C\otimes C$ would induce an at-most-$r$-term decomposition of $C$. Equations (8) and (9) imply

$$
\chi(C\otimes C)\geq3.
$$

#### A further exact contraction

There is a useful further reduction of the lower-bound problem. Let

$$
|B\rangle=|00\rangle+i|11\rangle,
$$

which is a two-qubit stabilizer state, and contract its bra against one qubit from each copy of $C$. Writing $U=T^\perp$, direct calculation gives

$$
\langle B|T,T\rangle=\langle B|U,U\rangle=2,
\qquad
\langle B|T,U\rangle=\langle B|U,T\rangle=0.
$$

Therefore, up to the harmless ordering of the ten uncontracted qubits,

$$
\langle B|\,C\otimes C
=T^{\otimes10}+U^{\otimes10}
=\sqrt2\,|\mathrm{cat}_{10}\rangle.
\tag{10}
$$

For completeness, choose a two-qubit Clifford $W$ such that
$W|00\rangle\propto|B\rangle$. Then $\langle B|\propto\langle00|W^\dagger$.
Thus contraction with $\langle B|$ is a Clifford operation on the contracted
qubits followed by computational-basis restriction, and it maps each stabilizer
summand to zero or a stabilizer state. Therefore

$$
\chi(C\otimes C)\geq\chi(\mathrm{cat}_{10}).
\tag{11}
$$

This is precisely the $\mathrm{cat}_2$ contraction used by Qassim, Pashayan,
and Gosset to construct larger cats. At present it does not strengthen the
numerical lower bound: computational-basis contractions show
$\chi(\mathrm{cat}_{10})\geq\chi(\mathrm{cat}_6)=3$, while no proof of
$\chi(\mathrm{cat}_{10})\geq4$ is supplied here. Equation (11) nevertheless
identifies a concrete smaller exact-rank problem whose solution would
immediately improve the lower bound.

There is also an exact relation in the other direction. Let

$$
\Pi=\frac12(I+Z^{\otimes6}\otimes I^{\otimes6}).
$$

The state $\mathrm{cat}_{12}$ is supported on strings of even total parity.
Projecting its first six qubits onto even parity therefore forces each block to
have even parity. Comparing computational-basis amplitudes gives

$$
\boxed{C\otimes C=\sqrt2\,\Pi|\mathrm{cat}_{12}\rangle.}
\tag{12}
$$

Pauli projection maps a stabilizer state to zero or a stabilizer state, so
together with (11) this gives the rigorous sandwich

$$
\chi(\mathrm{cat}_{10})\leq\chi(C\otimes C)
\leq\chi(\mathrm{cat}_{12}).
\tag{13}
$$

No bound on $\mathrm{cat}_{12}$ strong enough to improve nine is established
here.

#### Remaining open issues

1. **Eight-term upper bound.** The gap is whether the upper bound after (2) can be lowered to eight. The exact product construction (2) was analyzed, including the independence of its nine summands. The product-cut argument also forces strong dependencies in any eight-term decomposition of product stabilizer states, but it does not constrain genuinely entangled stabilizer summands. Equation (4) reduces one concrete route to finding a three-term decomposition of the ten-qubit phase function (7); the radical supplies one entangled affine slice but not the other required terms. The support-dimension argument further reduces exclusion of this route to hyperplane restrictions and the full-support case, but those finite checks were not completed. Either a three-term certificate for (7), or an affine-quadratic description of eight different stabilizer summands with an exact amplitude verification, would close the upper-bound gap.

2. **Lower bound above three.** The gap in (9)–(13) is that the contractions certify only rank three. The $\mathrm{cat}_2$ contraction (10) reduces to $\mathrm{cat}_{10}$, but the cited small-cat classification does not prove $\chi(\mathrm{cat}_{10})\geq4$; the projection from $\mathrm{cat}_{12}$ also supplies no stronger number. Excluding all three-stabilizer spans containing $\mathrm{cat}_{10}$, or finding another contraction with a known rank-four output, would close this gap; it would improve the interval but would not settle the eight-term conjecture.

3. **Exact value.** The final gap is that ranks $3,4,\ldots,9$ remain compatible with the upper decomposition and lower contractions. Those are the two proof mechanisms used here, and neither supplies matching bounds. An exact $k$-term witness together with an exclusion of all ranks below $k$ would determine the value.
