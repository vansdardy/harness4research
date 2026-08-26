# Problem: bounding $\chi(\mathrm{cat}_6 \otimes \mathrm{cat}_6)$

## Definitions

**Stabilizer state.** An $n$-qubit pure state $\ket{\varphi}$ is a *stabilizer state*
if it can be written, in some computational basis, as

$$\ket{\varphi} = \sum_{x \in A} i^{\ell(x)} (-1)^{q(x)} \ket{x}$$

where $A \subseteq \mathbb{F}_2^n$ is an affine subspace, $q : A \to \{0, 1\}$ is a
quadratic function, and $\ell : A \to \{0, 1, 2, 3\}$ is a linear function.

**Stabilizer rank.** For a state $\ket{\psi}$, the stabilizer rank $\chi(\psi)$ is the
minimum $k$ such that $\ket{\psi} = \sum_{i=1}^{k} c_i \ket{\varphi_i}$ for some
stabilizer states $\ket{\varphi_i}$ and coefficients $c_i \in \mathbb{C}$.

**The $T$-state.** $\ket{T} := \ket{0} + e^{i\pi/4}\ket{1}$ (unnormalized), and
$\ket{T^\perp} := \ket{0} - e^{i\pi/4}\ket{1}$.

**Cat states.** For a single-qubit state $\ket{\psi}$ with orthogonal complement
$\ket{\psi^\perp}$ (phase fixed by $\braket{0|\psi^\perp}$ real and positive),

$$\ket{\mathrm{cat}_n(\psi)} := \frac{1}{\sqrt2}\left(\ket{\psi}^{\otimes n} + \ket{\psi^\perp}^{\otimes n}\right).$$

Throughout, "$\mathrm{cat}_6$" means specifically $\mathrm{cat}_6(T)$:

$$\ket{\mathrm{cat}_6} := \frac{1}{\sqrt2}\left(\ket{T}^{\otimes 6} + \ket{T^\perp}^{\otimes 6}\right).$$

## The problem

It is known that $\chi(\mathrm{cat}_6) \leq 3$ (Qassim, Waterloo PhD thesis 2020, §4.2),
so by submultiplicativity $\chi(\mathrm{cat}_6 \otimes \mathrm{cat}_6) \leq 9$.

**Determine $\chi(\mathrm{cat}_6 \otimes \mathrm{cat}_6)$, or the best bound on it you can prove.**
In particular: does $\chi(\mathrm{cat}_6 \otimes \mathrm{cat}_6) \leq 8$ hold?