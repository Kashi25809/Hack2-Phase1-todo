---
description: Single global constitution for the Evolution of Todo project acting as the supreme governing document.
---

# Global Constitution: Evolution of Todo (Phase I - V)

This constitution acts as the supreme governing document for all agents working on the "Evolution of Todo" project. It defines mandatory rules, behavior, governance, technology, and quality principles that must remain stable across all phases.

## 1. Spec-Driven Development (Mandatory)
*   **No Code Without Specs**: No agent may write code without approved specifications and tasks.
*   **Workflow**: All work must strictly follow this flow:
    `Constitution → Specs → Plan → Tasks → Implement`

## 2. Agent Behavior Rules
*   **No Manual Coding**: No manual coding by humans.
*   **No Feature Invention**: Agents must not invent features not strictly defined in the specs.
*   **Adherence to Specs**: No deviation from approved specifications is allowed.
*   **Refinement Level**: Refinement must occur at the specification level, strictly not at the code level.

## 3. Phase Governance
*   **Strict Scoping**: Each phase is strictly scoped by its specification.
*   **No Leakage**: Future-phase features must never leak into earlier phases.
*   **Evolution**: Architecture may evolve only through updated specs and plans.

## 4. Technology Constraints
*   **Backend**: Python
*   **Frontend**: Next.js (reserved for later phases)
*   **Frameworks & Libraries**:
    *   FastAPI
    *   SQLModel
    *   Neon DB
    *   OpenAI Agents SDK
    *   MCP (Model Context Protocol)
*   **Infrastructure (Later Phases)**:
    *   Docker
    *   Kubernetes
    *   Kafka
    *   Dapr

## 5. Quality Principles
*   **Architecture**: Clean architecture.
*   **Statelessness**: Stateless services where required.
*   **Separation of Concerns**: Clear separation of concerns between components.
*   **Readiness**: Cloud-native readiness.

**Note**: This constitution must remain stable across all phases.
