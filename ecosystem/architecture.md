# Technical Architecture

12cycle adopts a hybrid architecture to ensure a seamless experience for cultural consumers while maintaining blockchain transparency.

## 1. Architecture Overview

*   **Application Layer:** User interfaces for Games, Webtoons, and Wallets.
*   **Middleware Layer:** 12cycle SDK for activity tracking and Oracle services.
*   **Blockchain Layer:** Layer 2 solution (Arbitrum One) for value settlement.

## 2. Blockchain Infrastructure

### Primary Network: Arbitrum One
*   **Rationale:** Low gas fees, high throughput, and EVM compatibility.
*   **Chain ID:** 42161

### Cross-Chain Strategy
*   **Phase 1:** Arbitrum One (Current)
*   **Phase 2:** TBD (Polygon/Base integration planned)
*   **Phase 3:** Omnichain (LayerZero)

## 3. PoC (Proof of Culture) Mechanism

**Proof of Culture** transforms users' cultural activities into blockchain-verifiable proofs.

### Verification Process
1.  **Activity Collection:** SDK collects user interaction data.
2.  **Verification:** TBD (Anti-bot and validity verification mechanism).
3.  **On-Chain Recording:** Verified data is bridged to the blockchain via Oracle.

### Oracle System
*   Hybrid system combining Chainlink and Validator Network.
*   **Validator Network:** TBD (Node composition and consensus details).
