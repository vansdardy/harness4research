import numpy as np

from stabrank.stabrank_core import run_sa_pauli_expansion


def compressed_states():
    """Return normalized compressed representatives of e, k, and D."""
    e = np.full(32, 1 / np.sqrt(32), dtype=complex)
    k = np.empty(32, dtype=complex)
    for y_int in range(32):
        y = [(y_int >> (4 - j)) & 1 for j in range(5)]
        x = [sum(y) % 2, *y]
        s = sum(x[j] * x[l] for j in range(6) for l in range(j + 1, 6))
        k[y_int] = (-1) ** s / np.sqrt(32)
    b = (-1 + 1j) / 2
    c = (-1 - 1j) / 2
    d = b * e + c * k
    d /= np.linalg.norm(d)
    return e, k, d


e, k, d = compressed_states()
target = np.kron(d, d)
known = [np.kron(e, e), np.kron(e, k), np.kron(k, e), np.kron(k, k)]

for omitted in range(4):
    initial = [v for j, v in enumerate(known) if j != omitted]
    result = run_sa_pauli_expansion(
        target=target,
        n_orig=10,
        p_prime=2,
        k_subset_size=3,
        initial_basis=initial,
        initial_temperature=0.5,
        cooling_rate=0.99,
        num_iterations_at_temp=400,
        min_temperature=1e-4,
        atol=1e-9,
        two_func_perturb_prob=0.4,
        random_replace_prob=0.05,
        use_real_qubit_moves=False,
        clifford_ratio=0.5,
        early_exit_threshold=1e-12,
        seed=7300 + omitted,
        num_chains=16,
    )
    _, basis, coefficients, error, cost, _ = result
    print(f"omitted={omitted} error={error:.16g} cost={cost:.16g}", flush=True)
    if error < 1e-10:
        np.savez_compressed(
            "sandbox/d_square_3.npz",
            target=target,
            coefficients=coefficients,
            **{f"basis_{j}": value for j, value in enumerate(basis)},
        )
        break
