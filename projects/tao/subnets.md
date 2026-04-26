# Bittensor Subnets

## Overview
Subnets are the "lifeblood" of the Bittensor network. Each subnet is an independent, incentivized marketplace for a specific digital commodity.

## Subnet Mechanics
1.  **Creation**: Subnet creators (SNCs) register a new subnet and define its unique **Incentive Mechanism**.
2.  **Specialization**: Each subnet specializes in one task. For example:
    *   **SN 1**: Text Prompting
    *   **SN 5**: Image Generation
    *   **SN 21**: File Storage
    *   **SN 126**: Poker AI (Experimental)
3.  **Incentive Mechanisms**: SNCs write Python-based code that dictates how Validators should score the work of Miners. This creates a competitive market where the best models/services rise to the top.
4.  **Emission Allocation**: The Bittensor root network periodically allocates a portion of the total TAO emission to each subnet based on its perceived value and performance.

## Current Network Status (April 2026)
*   **Capacity Expansion**: The network has expanded its capacity from 32 subnets to **128 subnets**.
*   **Active Subnets**: There are currently active subnets reaching up to SN 126.
*   **Diversity**: The range of tasks has moved beyond simple LLMs into niche scientific and financial domains like protein folding, poker simulation, and weather prediction.

## Discovering Subnets
The most reliable way to track subnets and their performance is via:
*   [TAO.app Explorer](https://www.tao.app/explorer)
*   [TAOstats Subnet Index](https://taostats.io/subnets)

## Governance
Subnet slots are limited. New subnets must "compete" for a slot by paying a registration cost in TAO, which is periodically burned or recycled, depending on network governance rules.
