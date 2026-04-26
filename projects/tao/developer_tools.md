# Bittensor Developer Tools

## Primary Tools

### 1. BTCLI (Bittensor Command Line Interface)
The `btcli` is the Swiss Army knife for Bittensor developers and users.
*   **Installation**: Included with the Python SDK (`pip install bittensor`).
*   **Key Capabilities**:
    *   `btcli wallet new_coldkey`: Create a new coldkey (main wallet).
    *   `btcli wallet new_hotkey`: Create a hotkey (active identity for mining/validating).
    *   `btcli subnet register`: Register a miner/validator on a subnet.
    *   `btcli stake add`: Stake TAO to a validator.
    *   `btcli list`: View all wallets and their balances.

### 2. Bittensor Python SDK
A robust Python library for building network participants.
*   **Repo**: [github.com/opentensor/bittensor](https://github.com/opentensor/bittensor)
*   **Core Modules**:
    *   `bittensor.Subtensor`: Interface for interacting with the blockchain.
    *   `bittensor.Wallet`: Management of keys and signatures.
    *   `bittensor.Metagraph`: Local view of a subnet's state (nodes, weights, dividends).
    *   `bittensor.Dendrite/Axon`: The networking layer for sending/receiving requests between nodes.

### 3. Subtensor (The Chain)
Developers can run their own local "Lite Node" to speed up interactions and queries without relying on public endpoints.
*   **Tech Stack**: Built on Substrate (Polkadot ecosystem).

## Mining & Validating
*   **Miner Template**: [github.com/opentensor/subnets](https://github.com/opentensor/subnets) provides boilerplate code for creating new miners.
*   **Validator Template**: Essential for those wanting to manage their own incentive mechanisms.

## Local Development
For testing, developers use **Subtensor (Lite)** or **Local Chain** setups to iterate on incentive mechanisms without spending real TAO.
