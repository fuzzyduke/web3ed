# Gensyn Litepaper (Legacy) Summary

## The Verification Problem
The core challenge is verifying that machine learning training work was actually performed by a node without requiring full re-computation, which is inefficient and expensive. Zero-Knowledge proofs are currently too slow for large models.

## Proposed Solution: The Verification Game
Gensyn uses a **probabilistic verification protocol** combined with a **Graph-based Pinpoint Challenge**.

### Game Theory & Incentives
- **Forced Errors**: To prevent verifiers from becoming lazy (the "verifier's dilemma"), the protocol periodically introduces forced errors with high rewards ("jackpot payouts").
- **Whistleblowers**: Independent monitors ensure verifiers are doing their jobs.
- **On-chain Arbitration**: Disputes are narrowed down to a single operation and settled definitively on-chain.

## Protocol Roles
*   **Submitters**: Users providing models/data and paying for compute.
*   **Solvers**: The workers performing the training and generating "Proof-of-Learning" (weight updates/checkpoints).
*   **Verifiers**: Nodes checking random segments of the Solver's work against distance thresholds.
*   **Whistleblowers**: Audit verifiers and challenge them if they detect negligence or malice.

## Proof-of-Learning Details
- Based on research by Jia et al. (2021).
- Uses **checkpoints** (model weights and data indices).
- **Distance Thresholds**: Verifiers ensure weight updates follow the expected trajectory within a specific distance.
- **Proof Stacking**: Allows for verifying models built on top of other proven base models.

## Transition to "Legacy" Status
The litepaper is considered legacy because Gensyn is pivoting to a **custom Ethereum Rollup** with a more advanced cryptographic proof system and a focus on **bitwise-perfect reproducibility** via the **Reproducible Execution Environment (REE)** and a specialized ML compiler.
