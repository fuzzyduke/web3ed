# Gensyn Project Research

## Overview
Gensyn is a decentralized infrastructure layer for AI compute, creating a global, permissionless marketplace for machine learning training. It allows anyone with hardware to provide compute power, verified by a novel proof-of-learning protocol.

### Key Problem Solved
Addresses the high cost and centralization of AI training by democratizing access to compute and ensuring verifiable execution without full re-computation.

---

## Technical Architecture

### Node Roles
*   **Submitters:** Task creators who provide models and data.
*   **Solvers:** Compute providers who train models and generate proofs.
*   **Verifiers:** Probabilistically check proofs of learning.
*   **Whistleblowers:** Audit Verifiers to maintain network integrity.

### Core Mechanisms
*   **Proof-of-Learning:** A probabilistic verification mechanism using graph-based pinpoint challenges.
*   **Reproducible Execution Environment (REE):** Ensures ML training is bitwise-reproducible across different hardware.
*   **Ethereum Rollup:** Evolved from a Substrate L1 to a custom Ethereum Rollup for ML tasks.

---

## Developer Ecosystem
*   **Documentation:** [docs.gensyn.ai](https://docs.gensyn.ai/)
*   **Delphi:** A permissionless prediction market built on Gensyn for verifiable settlement.
*   **Verde:** The verification system framework.
*   **REE Toolchain:** Used for ensuring model compatibility and reproducibility.

---

## Tokenomics
*   **Token:** $AI
*   **Dynamics:** 
    *   Submitters pay in $AI.
    *   Solvers/Verifiers stake $AI.
    *   Rewards for honest work; slashing for malicious behavior.

---

## Current Status
*   **Phase:** Public Testnet (as of March 2025).
*   **Primary App:** Delphi (used for stress-testing).
*   **Next Steps:** Phased rollout toward Mainnet.
