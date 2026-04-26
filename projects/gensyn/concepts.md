# Gensyn Core Concepts

## Distance Thresholds
Standard ML training is often non-deterministic due to parallelization and hardware-specific math implementations. 

### Mechanism:
*   **Profiling**: Before a task is broadly distributed, it is run on "trusted" hardware to establish expected output variance.
*   **Threshold Generation**: These distances (divergences) are mapped into a threshold.
*   **Validation**: Verifiers check if the Solver's outputs fall within this acceptable "distance" from the ground truth. If it exceeds the threshold, it triggers a challenge.

---

## Proof of Availability
Ensures that compute providers actually have the data and model weights they claim to be using.

### Function:
Prevents "lazy" solvers from simply copying results from other nodes or claiming they are working on a task without possessing the required resources. It is a prerequisite for both Solvers and Verifiers.

---

## Refereed Delegation
Instead of every node verifying every task (full replication), the network delegates work to single nodes and uses a "referee" system to settle disputes only when they arise. This allows the network to scale compute linearly with the number of nodes.
