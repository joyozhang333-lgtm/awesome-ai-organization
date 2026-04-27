# Awesome AI Organization [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

> Build your AI-powered team. Frameworks, role templates, workflows, and real-world playbooks for running an organization with AI employees.

[English](README.md) | [简体中文](README-zh.md)

[![Resources](https://img.shields.io/badge/resources-150+-blue.svg)](#contents)
[![Templates](https://img.shields.io/badge/templates-30+-orange.svg)](#ready-to-use-templates)
[![License: CC0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)

---

**Why this list?** Everyone's talking about AI agents. But nobody has assembled a single resource for the real question: *How do I actually build and run an AI-powered organization?*

This repo connects the dots between frameworks, role design, workflow automation, and governance — so you can go from "I want AI employees" to a functioning AI team.

---

## Contents

- [Multi-Agent Frameworks](#multi-agent-frameworks)
- [AI Role & Employee Templates](#ai-role--employee-templates)
- [Workflow Recipes](#workflow-recipes)
- [AI Department Blueprints](#ai-department-blueprints)
- [AI Governance & Audit](#ai-governance--audit)
- [Commercial AI Employee Platforms](#commercial-ai-employee-platforms)
- [Case Studies & Playbooks](#case-studies--playbooks)
- [Protocols & Standards](#protocols--standards)
- [Ready-to-Use Templates](#ready-to-use-templates)
- [Further Reading](#further-reading)

---

## Multi-Agent Frameworks

Frameworks for building teams of AI agents that collaborate.

| Framework | Stars | Language | Best For |
|-----------|-------|----------|----------|
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 67k+ | Python | Simulating a full software company (PM → Architect → Engineer) |
| [AutoGen / AG2](https://github.com/microsoft/autogen) | 57k+ | Python | Multi-agent conversations, flexible team topologies |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 50k+ | Python | Role-playing AI crews with delegation |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | 33k+ | Python | Virtual software company simulation |
| [gstack](https://github.com/garrytan/gstack) | 85k+ | Markdown | YC CEO's Claude Code setup — CEO, Eng Manager, QA roles |
| [CAMEL](https://github.com/camel-ai/camel) | 17k+ | Python | Role-playing agent pairs, OWL workforce |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | — | Python | Lightweight multi-agent orchestration |
| [LangGraph](https://github.com/langchain-ai/langgraph) | — | Python | Graph-based workflow orchestration |
| [Google ADK](https://github.com/google/adk-python) | — | Python | Google's agent development kit |

### Framework Comparison

| Feature | MetaGPT | CrewAI | ChatDev | AG2 | gstack |
|---------|---------|--------|---------|-----|--------|
| Pre-defined roles | ✅ PM, Architect, Engineer | ✅ Custom roles | ✅ CEO, CTO, Dev, QA | ❌ Custom only | ✅ CEO, Eng Mgr, QA |
| Department structure | Implicit (SOPs) | Crews as teams | Phase-based | Group chats | Skill-based |
| Delegation | ✅ | ✅ | ✅ | ✅ | ❌ |
| No-code setup | ❌ | ❌ | ✅ (v2) | ❌ | ✅ (Markdown) |
| MCP support | ❌ | ✅ | ❌ | ❌ | ✅ |
| Best audience | Developers | Developers | Beginners | Researchers | Non-technical |

---

## AI Role & Employee Templates

Pre-built role definitions you can use to create AI employees.

### Leadership & Strategy

| Role | Source | Tool | Description |
|------|--------|------|-------------|
| [AI CEO / Product Reviewer](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | CEO-mode plan review — rethink problems, find 10-star products |
| [AI Engineering Manager](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | Lock in execution plans, architecture, edge cases |
| [AI Product Manager](https://github.com/FoundationAgents/MetaGPT) | MetaGPT | Python | Generates PRDs from requirements |

### Engineering

| Role | Source | Tool | Description |
|------|--------|------|-------------|
| [AI Architect](https://github.com/FoundationAgents/MetaGPT) | MetaGPT | Python | System design from PRD |
| [AI Code Reviewer](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | Pre-landing PR review for SQL safety, trust boundaries |
| [AI QA Engineer](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | Systematic QA testing with fix loop |
| [AI Release Manager](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | Ship workflow — test, review, bump, push, PR |
| [AI Doc Engineer](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | Post-ship documentation updates |

### Marketing & Content

| Role | Source | Tool | Description |
|------|--------|------|-------------|
| [AI Content Writer](https://github.com/blader/humanizer) | Blader | Claude Code | Human-like writing, removes AI traces |
| [AI Social Media Publisher](https://github.com/wshuyi/x-article-publisher-skill) | wshuyi | Claude Code | Publish articles to X/Twitter |
| [PM Skills Marketplace](https://github.com/phuryn/pm-skills) | phuryn | All agents | 100+ skills for discovery, strategy, launch, growth |

### Security & Compliance

| Role | Source | Tool | Description |
|------|--------|------|-------------|
| [AI Security Auditor](https://github.com/trailofbits/skills) | Trail of Bits | Claude Code | Vulnerability detection, audit workflows |
| [AI Pentester](https://github.com/0x4m4/hexstrike-ai) | 0x4m4 | Claude Code, MCP | 150+ cybersecurity tools |
| [AI Bug Bounty Hunter](https://github.com/shuvonsec/claude-bug-bounty) | shuvonsec | Claude Code | Recon, IDOR, XSS, SSRF, report generation |

### Design & Creative

| Role | Source | Tool | Description |
|------|--------|------|-------------|
| [AI Designer](https://github.com/GLips/Figma-Context-MCP) | GLips | Cursor, Claude Code | Figma layout info for AI agents |
| [AI Diagram Maker](https://github.com/yctimlin/mcp_excalidraw) | yctimlin | Claude Code | Excalidraw diagram creation |
| [AI Video Editor](https://github.com/Ceeon/videocut-skills) | Ceeon | Claude Code | Video editing agent |
| [AI Game Developer](https://github.com/htdt/godogen) | htdt | Claude Code | Build Godot 4 projects from descriptions |

---

## Workflow Recipes

End-to-end workflows for common organizational tasks.

### Software Development Workflow
```
Requirements → AI PM (PRD) → AI Architect (Design) → AI Engineer (Code) → AI QA (Test) → AI Release Manager (Ship)
```
**Tools:** MetaGPT, ChatDev, or gstack

### Content Creation Pipeline
```
Topic Research → AI Writer (Draft) → AI Editor (Polish) → AI Designer (Visuals) → AI Publisher (Post)
```
**Tools:** humanizer + x-article-publisher-skill + Figma-Context-MCP

### Code Review Workflow
```
PR Created → AI Security Scan → AI Code Review → AI Test Generation → Human Approval → AI Ship
```
**Tools:** gstack (/review → /qa → /ship)

### Social Media Workflow
```
Trend Analysis → Content Generation → Brand Voice Check → Visual Creation → Scheduling → Analytics
```
**Tools:** CrewAI + custom agents

### Incident Response Workflow
```
Alert → AI Triage → Root Cause Analysis → Fix Generation → AI QA → Deploy → Post-mortem
```
**Tools:** gstack + hexstrike-ai

---

## AI Department Blueprints

How to structure AI teams by department.

### Engineering Department
| Role | Responsibility | Recommended Tool |
|------|---------------|-----------------|
| Tech Lead | Architecture decisions, code review | gstack `/plan-eng-review` |
| Developer | Feature implementation | Claude Code / Cursor |
| QA Engineer | Testing, bug detection | gstack `/qa` |
| DevOps | CI/CD, deployment | gstack `/ship` |
| Security | Vulnerability scanning | trailofbits/skills |

### Marketing Department
| Role | Responsibility | Recommended Tool |
|------|---------------|-----------------|
| Content Strategist | Topic research, planning | CrewAI custom agent |
| Copywriter | Blog posts, social copy | humanizer |
| Social Media Manager | Publishing, engagement | x-article-publisher-skill |
| Designer | Visual content | Figma-Context-MCP |
| Analytics | Performance tracking | Custom MCP server |

### Product Department
| Role | Responsibility | Recommended Tool |
|------|---------------|-----------------|
| Product Manager | PRD, roadmap | MetaGPT / gstack `/plan-ceo-review` |
| UX Researcher | User feedback analysis | CrewAI custom agent |
| Data Analyst | Metrics, A/B tests | claude-scientific-skills |

### Operations Department
| Role | Responsibility | Recommended Tool |
|------|---------------|-----------------|
| Process Analyst | Workflow analysis, bottleneck identification | Claude Code + database MCP |
| Automation Engineer | Workflow automation, integrations | n8n / Dify |
| Finance Assistant | Expense tracking, budget analysis | Claude Code + spreadsheet MCP |
| Compliance Officer | Policy checks, audit preparation | Claude Code + clawsec |

### Customer Support Department
| Role | Responsibility | Recommended Tool |
|------|---------------|-----------------|
| Tier-1 Support | FAQ handling, ticket classification | Claude Code + knowledge base MCP |
| Tier-2 Technical | Complex troubleshooting, log analysis | Claude Code + logs MCP |
| Knowledge Base Manager | Help articles, content gap analysis | Claude Code + CMS |
| Customer Success | Onboarding, churn risk detection | Claude Code + CRM MCP |

> Detailed blueprints with workflows, governance rules, and metrics: [/departments](departments/)

---

## AI Governance & Audit

Tools and practices for managing AI employees responsibly.

| Resource | Description |
|----------|-------------|
| [clawsec](https://github.com/prompt-security/clawsec) | Security skill suite — drift detection, audit, integrity verification |
| [claude-reflect](https://github.com/BayramAnnakov/claude-reflect) | Self-learning system that captures corrections and preferences |
| [Backlog.md](https://github.com/MrLesk/Backlog.md) | Human-AI collaboration management in git |
| [ide-rule-detector](https://github.com/spiffy-oss/ide-rule-detector) | Detect malicious AI rule files |

### Best Practices
- **Human-in-the-loop:** Always require human approval for external-facing actions
- **Audit trails:** Use git-based workflows so every AI action is tracked
- **Role boundaries:** Define clear scope for each AI employee — what they CAN and CANNOT do
- **Regular calibration:** Review AI output quality weekly, adjust prompts/skills
- **Cost monitoring:** Track API usage per AI employee to manage costs

---

## Commercial AI Employee Platforms

For comparison — closed-source platforms offering similar capabilities.

### Full-Stack AI Employee Platforms

| Platform | Focus | Pricing | Key Feature |
|----------|-------|---------|-------------|
| [Junior](https://thejunior.ai) | AI software engineer | Freemium | Autonomous coding agent, GitHub integration |
| [Lindy.ai](https://lindy.ai) | General AI employees | $0-299/mo | 4,000+ integrations, no-code |
| [Emika](https://emika.ai) | Enterprise AI employees | Enterprise | Ranked #1 AI employee platform 2026 |
| [Ema](https://ema.co) | Universal AI employee | Enterprise | 200+ pre-built workflows, EmaFusion model |
| [Relevance AI](https://relevanceai.com/workforce) | AI workforce teams | Enterprise | Collaborative AI agent teams |
| [Sintra AI](https://sintra.ai) | Business AI helpers | Enterprise | 12 specialized AI employees |

### AI Team & Workforce Platforms

| Platform | Focus | Key Feature |
|----------|-------|-------------|
| [Teammates.ai](https://teammates.ai) | AI team members | Pre-built AI teammates for sales, support, ops |
| [Beam.ai](https://beam.ai) | AI agent workforce | 200+ pre-built agents, enterprise orchestration |
| [Teamster.ai](https://teamster.ai) | AI team builder | Build custom AI teams for any workflow |
| [FlockX](https://flockx.io) | AI agent teams | Multi-agent collaboration platform |
| [Gumloop](https://gumloop.com) | AI workflow automation | Visual workflow builder with AI agents |
| [EverWorker](https://everworker.ai) | AI digital workers | Autonomous task execution, 24/7 operation |

### Specialized AI Employees

| Platform | Specialty | Key Feature |
|----------|-----------|-------------|
| [TabHR](https://tabhr.ai) | AI HR employee | Recruiting, onboarding, employee management |
| [SketricGen](https://sketricgen.com) | AI business analyst | Data analysis, report generation |
| [Devin](https://devin.ai) | AI software engineer | Full-stack autonomous coding |
| [Factory](https://factory.ai) | AI coding agents | Drafter (PRs), Code Review, Migration agents |

### Open-Source Alternatives for Self-Hosting

| Framework | Stars | Best For |
|-----------|-------|----------|
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 72k+ | Self-hosted AI software engineer (formerly OpenDevin) |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 184k+ | Autonomous AI agent platform |
| [Dify](https://github.com/langgenius/dify) | 139k+ | LLMOps platform — build AI workflows visually |
| [Flowise](https://github.com/FlowiseAI/Flowise) | 52k+ | Drag-and-drop LLM flow builder |
| [n8n](https://github.com/n8n-io/n8n) | 186k+ | Workflow automation with AI agent nodes |
| [AgentVerse](https://github.com/OpenBMB/AgentVerse) | 5.0k+ | Multi-agent simulation and collaboration |
| [agentUniverse](https://github.com/alipay/agentUniverse) | 1k+ | Ant Group's multi-agent framework |
| [AWS Agent Squad](https://github.com/awslabs/agent-squad) | — | AWS multi-agent orchestrator |

---

## Case Studies & Playbooks

Real-world examples of AI-powered organizations.

| Case | What They Did | Key Takeaway |
|------|--------------|--------------|
| [Garry Tan's gstack](https://github.com/garrytan/gstack) | YC CEO open-sourced 13+ Claude Code skills simulating a full eng org | Non-technical leaders can build AI teams with markdown skills |
| [MetaGPT → MGX](https://mgx.dev/) | AI software company that generates full repos from one requirement | Assembly-line SOPs work better than free-form agent chat |
| [ChatDev](https://chatdev.ai/) | Virtual company with CEO/CTO/Dev/QA producing software | Role specialization improves output quality |
| [CrewAI Enterprise](https://crewai.com) | Framework powering thousands of AI teams in production | Delegation between agents is key to complex tasks |

---

## Protocols & Standards

The infrastructure layer for AI organizations.

| Protocol | Purpose | Status |
|----------|---------|--------|
| [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) | Agent ↔ Tool connectivity | Industry standard, 97M+ SDK downloads |
| [A2A (Agent-to-Agent)](https://google.github.io/A2A/) | Agent ↔ Agent communication | Google-led, emerging standard |
| [AGENTS.md](https://github.com/agentsmd/agents.md) | Universal agent config format | 19k+ stars, cross-tool |
| [SKILL.md](https://skillsmp.com/) | Portable skill format | Emerging standard |

---

## Ready-to-Use Templates

Copy these templates directly into your project.

### 📁 [/roles](roles/)
Pre-built AI employee role definitions.

### 📁 [/workflows](workflows/)
End-to-end workflow configurations.

### 📁 [/departments](departments/)
Department-level team setups.

> See the [templates README](roles/README.md) for installation instructions.

---

## Further Reading

- [The Coming Agent Economy](https://adtools.org/buyers-guide/the-coming-agent-economy-how-marketplaces-for-ai-agent-skills-will-reshape-the-software-ecosystem) — How AI skill marketplaces will reshape software
- [AI-First Company Principles](https://getaitopia.io/resources/ai-first-whitepaper) — Building AI into operational DNA
- [Strategic Guide to Agentic Enterprise 2026](https://cosmo-edge.com/ai-first-organization-agentic-strategy/) — From AI-augmented to AI-first
- [How to Build an AIOS for Founders](https://www.aifire.co/p/how-to-build-an-ai-operating-system-aios-for-founders-2026) — AI Operating System concept

---

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

**What we're looking for:**
- New AI role templates (with real-world testing)
- Workflow recipes that actually work
- Case studies of AI-powered teams
- Tools and frameworks we missed

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
