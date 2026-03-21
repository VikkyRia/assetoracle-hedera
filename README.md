# AssetOracle

**One-liner:**
The Complete RWA Infrastructure Stack

---

## Project Overview

AssetOracle is a modular infrastructure layer for **Real World Assets (RWAs)** that enables secure verification, tokenization, and lifecycle automation. It combines AI-powered analysis, decentralized verification, and blockchain-based ownership systems to create a unified platform for managing real-world assets across data, authenticity, and execution.

---

## Problem Statement

* RWA data is fragmented across registries, custodians, and multiple platforms
* Tokenized assets often lack verifiable ownership and document authenticity
* Asset workflows rely heavily on disconnected Web2 tools and manual processes
* Fraud risks and lack of transparency reduce trust in RWA markets

---

## Solution Statement

AssetOracle provides a **unified, trustless infrastructure layer** that:

* Aggregates and normalizes asset data from multiple sources
* Uses AI to detect fraud and generate risk and investment scores
* Verifies asset ownership and documents on-chain
* Enables fractional tokenization using native blockchain infrastructure
* Automates asset lifecycle workflows with intelligent systems

---

## Product

AssetOracle consists of three core layers:

### Data Oracle

* Aggregates multi-source RWA data
* Normalizes and structures asset information
* Provides AI-powered analytics and scoring

### Authenticity Layer

* Verifies asset documents on-chain
* Generates ownership proofs and verification certificates
* Maintains immutable audit trails

### Automation Layer

* AI-driven workflows for asset lifecycle management
* Event-based triggers and notifications
* Reduces manual operations and improves efficiency

---

## Architecture

```
Frontend (React + Hedera Wallet)
        │
        ▼
Backend API (Express.js)
• Asset Registration
• User Management
• Verification Workflows
• Portfolio Tracking
        │
 ┌──────┴────────┐
 ▼               ▼
AI Service       Hedera Layer
(Groq LLM)       (HTS + HCS + Smart Contracts)

• Fraud Detection   • Tokenization (HTS)
• Risk Scoring      • Verification Logs (HCS)
• Analysis Engine   • Ownership Registry
```

---

## Tech Stack

### Frontend Stack

* React → Component-based UI for asset dashboards and workflows
* Hedera Wallet Integration → Enables user authentication and on-chain interactions

---

### Backend Stack

* Express.js → Backend API for asset registration, verification workflows, and user management
* Portfolio Tracking → Tracks user asset ownership and tokenized holdings
* Verification Engine → Manages asset validation and authenticity processes

---

### AI Stack

* Groq LLM → AI-powered fraud detection, document analysis, and risk scoring
* Hedera AI Agent Services → Generates asset insights, verification signals, and investment metrics

---

## Blockchain Stack - Hedera Integrations

AssetOracle leverages Hedera’s native services for performance, security, and scalability:

### Hedera Token Service (HTS)

* Enables fractional ownership of RWAs
* Eliminates need for custom token contracts
* Supports low-cost, high-speed transactions

### Hedera Consensus Service (HCS)

* Stores asset verification and audit events
* Creates tamper-proof and publicly verifiable records

### Smart Contracts

* Handle verification logic and ownership registry
* Manage NFT certificates for verified assets
* Coordinate token issuance and ownership tracking

### Hedera SDKs

* Power seamless integration across frontend and backend
* Enable interaction with Hedera network services

### Hedera AI Agent

* Generates asset insights
* Aggregates verification signals
* Provides investment metrics

---

## Quick Start

### Prerequisites

* Node.js 18+
* Hedera testnet account
* PostgreSQL database

### Backend

```bash
cd backend
npm install
cp .env.example .env
# Configure Hedera credentials
npm run dev
```

### Frontend

```bash
cd frontend
bun install
bun run dev
```

### AI Service

```bash
cd ai-service
pip install -r requirements.txt
python api.py
```

---

## Features

* Complete backend API (20+ endpoints)
* AI-powered fraud detection
* Property verification workflow
* User portfolio management
* File upload system
* React frontend with wallet connection
* HTS token creation for fractional ownership
* HCS topic for verification audit trail
* Smart contract deployment to Hedera testnet
* HashConnect wallet integration
* Hedera SDK integration in backend

---

## Hackathon Track Alignment

**Theme 2: DeFi & Tokenization**

AssetOracle demonstrates:

1. **Tokenized Real-World Assets** — Properties → HTS tokens
2. **Composable Systems** — Modular architecture (API, AI, Contracts)
3. **High Throughput** — Hedera enables real-time verification
4. **Low Fees** — Makes fractional ownership economically viable
5. **Programmable Finance** — Smart contracts automate verification

---

## Repository Structure

```
├── backend/          # Express.js API
├── frontend/         # React + TypeScript UI
├── contracts/        # Hedera smart contracts
├── ai-service/       # AI fraud detection
└── docs/             # Documentation
```

---

## Team

**Victoria** — Backend Engineer (2+ years, 3MTT Hackathon Winner)
**Noah** — AI/ML Engineer (4+ years, Google Hackathon 3rd place)

---

## Closing

AssetOracle is building the **core infrastructure for the future of Real World Assets**.

By combining:

* AI-powered intelligence
* Blockchain-based verification
* Automated workflows

we enable a **trustless, scalable, and accessible RWA ecosystem** for developers, platforms, and investors.

---

## Links

* **Live Demo**: https://assetoracle-hedera-frontend.vercel.app/
* **Video Demo**: https://youtu.be/FjnUMUw3e-I

