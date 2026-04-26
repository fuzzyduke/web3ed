# Gensyn Technical Architecture

## Reproducible Execution Environment (REE)
The REE is designed to eliminate non-determinism in machine learning training, ensuring that the same task produces bitwise-identical results across diverse hardware (e.g., NVIDIA, AMD, CPUs).

### Components:
*   **Gensyn SDK**: The primary interface for managing model exports, compilation, and inference runs.
*   **Gensyn Compiler**: An **MLIR-based** compiler that converts ONNX models into reproducible PyTorch-compatible modules.
*   **RepOp Kernels**: Specialized CPU/GPU mathematical operators designed to behave consistently regardless of the underlying hardware implementation (addressing floating-point divergence).

---

## Verde Verification System
Verde implements a **Refereed Delegation** mechanism to verify large-scale compute tasks without re-running them entirely.

### The Bisection Game:
When two nodes (e.g., a Solver and a Verifier) disagree on a result:
1.  **Stage 1 (Steps)**: Perform a binary search across training steps to find the first step where results diverge.
2.  **Stage 2 (Operators)**: Within that step, perform a binary search across individual **RepOps** to find the exact operation that produced the divergence.
3.  **Arbitration**: A referee node executes only that specific operation to determine who is honest.

---

## Agent Exchange Layer (AXL)
AXL provides the P2P networking backbone for the Gensyn network, enabling:
*   **Decentralized Identity**: Secure node identification.
*   **Encrypted Messaging**: Private communication between network participants.
*   **P2P Primitives**: Efficient data and task distribution.
