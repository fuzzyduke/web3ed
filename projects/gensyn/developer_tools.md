# Gensyn Developer Tools & CLI

## Installation

### Agent eXchange Layer (AXL)
Used for building P2P agent applications and interacting with the network backbone.
```bash
curl -sSf https://axl.sh/install.sh | sh
```

### Gensyn SDK (REE)
The SDK is typically used within the REE container environment.

---

## CLI Usage (`gensyn-sdk`)

### Global Options:
*   `--verbose`: Enables detailed logging.
*   `--tasks-root <PATH>`: (Required) Path to the root directory for task data.

### Primary Subcommands:
*   **`run`**: Executes the full end-to-end pipeline (export -> compile -> infer).
*   **`export`**: Converts a model to the REE-compatible format.
*   **`compile`**: Runs the MLIR compiler to generate a reproducible module.
*   **`infer`**: Runs the actual inference task.
*   **`decode`**: Converts raw binary outputs into human-readable formats.

---

## SDKs
*   **AXL SDK**: For P2P messaging, identity management, and building decentralized agent services.
*   **Delphi SDK**: For building and interacting with prediction markets settled by the Gensyn network.
