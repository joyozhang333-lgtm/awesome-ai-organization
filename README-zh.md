# Awesome AI Organization [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

> 用 AI 建立你的团队。框架、角色模板、工作流和实战手册——帮你用 AI 员工运营一个组织。

[English](README.md) | [简体中文](README-zh.md)

[![Resources](https://img.shields.io/badge/资源-150+-blue.svg)](#目录)
[![Templates](https://img.shields.io/badge/模板-30+-orange.svg)](#可直接使用的模板)
[![License: CC0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)

---

**为什么做这个列表？** 所有人都在谈 AI Agent，但没有人把真正的问题整合成一个资源：*我到底怎么用 AI 建立和运营一个组织？*

这个仓库把框架、角色设计、工作流自动化和治理连接在一起——让你从"我想要 AI 员工"走到一个真正运转的 AI 团队。

---

## 目录

- [多智能体框架](#多智能体框架)
- [AI 角色与员工模板](#ai-角色与员工模板)
- [工作流配方](#工作流配方)
- [AI 部门蓝图](#ai-部门蓝图)
- [AI 治理与审计](#ai-治理与审计)
- [商业 AI 员工平台](#商业-ai-员工平台)
- [案例研究与实战手册](#案例研究与实战手册)
- [协议与标准](#协议与标准)
- [可直接使用的模板](#可直接使用的模板)
- [延伸阅读](#延伸阅读)

---

## 多智能体框架

用于构建协作 AI 团队的框架。

| 框架 | Star 数 | 语言 | 最适合 |
|------|---------|------|--------|
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 67k+ | Python | 模拟完整软件公司（PM → 架构师 → 工程师） |
| [AutoGen / AG2](https://github.com/microsoft/autogen) | 57k+ | Python | 多智能体对话，灵活团队拓扑 |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 48k+ | Python | 角色扮演 AI 团队，支持委派 |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | 33k+ | Python | 虚拟软件公司模拟 |
| [gstack](https://github.com/garrytan/gstack) | 65k+ | Markdown | YC CEO 的 Claude Code 配置——CEO、工程经理、QA 角色 |
| [CAMEL](https://github.com/camel-ai/camel) | 17k+ | Python | 角色扮演智能体对，OWL 劳动力 |

### 框架对比

| 特性 | MetaGPT | CrewAI | ChatDev | AG2 | gstack |
|------|---------|--------|---------|-----|--------|
| 预定义角色 | ✅ PM、架构师、工程师 | ✅ 自定义角色 | ✅ CEO、CTO、开发、QA | ❌ 仅自定义 | ✅ CEO、工程经理、QA |
| 部门结构 | 隐式（SOP） | Crew 即团队 | 基于阶段 | 群聊 | 基于技能 |
| 委派能力 | ✅ | ✅ | ✅ | ✅ | ❌ |
| 零代码配置 | ❌ | ❌ | ✅ (v2) | ❌ | ✅ (Markdown) |
| MCP 支持 | ❌ | ✅ | ❌ | ❌ | ✅ |
| 最佳受众 | 开发者 | 开发者 | 初学者 | 研究者 | 非技术人员 |

---

## AI 角色与员工模板

可直接使用的 AI 员工角色定义。

### 领导与战略

| 角色 | 来源 | 工具 | 描述 |
|------|------|------|------|
| [AI CEO / 产品评审](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | CEO 模式——重新思考问题，寻找 10 星产品 |
| [AI 工程经理](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | 锁定执行计划、架构、边界情况 |
| [AI 产品经理](https://github.com/FoundationAgents/MetaGPT) | MetaGPT | Python | 从需求生成 PRD |

### 工程

| 角色 | 来源 | 工具 | 描述 |
|------|------|------|------|
| [AI 架构师](https://github.com/FoundationAgents/MetaGPT) | MetaGPT | Python | 从 PRD 生成系统设计 |
| [AI 代码审查员](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | PR 审查——SQL 安全、信任边界 |
| [AI QA 工程师](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | 系统化 QA 测试 + 修复循环 |
| [AI 发布经理](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | 发布流程——测试、审查、版本、推送、PR |
| [AI 文档工程师](https://github.com/garrytan/gstack) | Garry Tan | Claude Code | 发布后文档更新 |

### 营销与内容

| 角色 | 来源 | 工具 | 描述 |
|------|------|------|------|
| [AI 内容写手](https://github.com/blader/humanizer) | Blader | Claude Code | 人性化写作，去除 AI 痕迹 |
| [AI 社媒发布](https://github.com/wshuyi/x-article-publisher-skill) | wshuyi | Claude Code | 发布文章到 X/Twitter |
| [PM 技能市场](https://github.com/phuryn/pm-skills) | phuryn | 所有 Agent | 100+ 产品管理技能 |

### 安全与合规

| 角色 | 来源 | 工具 | 描述 |
|------|------|------|------|
| [AI 安全审计员](https://github.com/trailofbits/skills) | Trail of Bits | Claude Code | 漏洞检测、审计工作流 |
| [AI 渗透测试员](https://github.com/0x4m4/hexstrike-ai) | 0x4m4 | Claude Code, MCP | 150+ 网络安全工具 |
| [AI 漏洞赏金猎人](https://github.com/shuvonsec/claude-bug-bounty) | shuvonsec | Claude Code | 侦察、IDOR、XSS、SSRF |

### 设计与创意

| 角色 | 来源 | 工具 | 描述 |
|------|------|------|------|
| [AI 设计师](https://github.com/GLips/Figma-Context-MCP) | GLips | Cursor, Claude Code | Figma 布局信息 |
| [AI 图表制作](https://github.com/yctimlin/mcp_excalidraw) | yctimlin | Claude Code | Excalidraw 图表创建 |
| [AI 视频编辑](https://github.com/Ceeon/videocut-skills) | Ceeon | Claude Code | 视频编辑 Agent |

---

## 工作流配方

常见组织任务的端到端工作流。

### 软件开发工作流
```
需求 → AI PM（PRD）→ AI 架构师（设计）→ AI 工程师（编码）→ AI QA（测试）→ AI 发布经理（上线）
```

### 内容创作流水线
```
选题调研 → AI 写手（初稿）→ AI 编辑（润色）→ AI 设计师（配图）→ AI 发布（推送）
```

### 代码审查工作流
```
PR 创建 → AI 安全扫描 → AI 代码审查 → AI 测试生成 → 人工审批 → AI 发布
```

### 社交媒体工作流
```
趋势分析 → 内容生成 → 品牌调性检查 → 视觉创作 → 定时发布 → 数据分析
```

---

## AI 部门蓝图

按部门组织 AI 团队的方法。

### 工程部
| 角色 | 职责 | 推荐工具 |
|------|------|---------|
| 技术负责人 | 架构决策、代码审查 | gstack `/plan-eng-review` |
| 开发工程师 | 功能实现 | Claude Code / Cursor |
| QA 工程师 | 测试、缺陷检测 | gstack `/qa` |
| DevOps | CI/CD、部署 | gstack `/ship` |
| 安全工程师 | 漏洞扫描 | trailofbits/skills |

### 市场部
| 角色 | 职责 | 推荐工具 |
|------|------|---------|
| 内容策略师 | 选题调研、规划 | CrewAI 自定义 Agent |
| 文案 | 博客、社媒文案 | humanizer |
| 社媒运营 | 发布、互动 | x-article-publisher-skill |
| 设计师 | 视觉内容 | Figma-Context-MCP |

### 产品部
| 角色 | 职责 | 推荐工具 |
|------|------|---------|
| 产品经理 | PRD、路线图 | MetaGPT / gstack |
| 数据分析师 | 指标、A/B 测试 | claude-scientific-skills |

### 运营部
| 角色 | 职责 | 推荐工具 |
|------|------|---------|
| 流程分析师 | 工作流分析、瓶颈识别 | Claude Code + 数据库 MCP |
| 自动化工程师 | 工作流自动化、集成 | n8n / Dify |
| 财务助理 | 费用追踪、预算分析 | Claude Code + 表格 MCP |
| 合规专员 | 政策检查、审计准备 | Claude Code + clawsec |

### 客户支持部
| 角色 | 职责 | 推荐工具 |
|------|------|---------|
| 一线客服 | FAQ 处理、工单分类 | Claude Code + 知识库 MCP |
| 二线技术支持 | 复杂问题排查、日志分析 | Claude Code + 日志 MCP |
| 知识库管理 | 帮助文章、内容缺口分析 | Claude Code + CMS |
| 客户成功 | 入职引导、流失风险检测 | Claude Code + CRM MCP |

> 详细蓝图（含工作流、治理规则、指标）：[/departments](departments/)

---

## AI 治理与审计

负责任地管理 AI 员工的工具和实践。

| 资源 | 描述 |
|------|------|
| [clawsec](https://github.com/prompt-security/clawsec) | 安全技能套件——漂移检测、审计、完整性验证 |
| [claude-reflect](https://github.com/BayramAnnakov/claude-reflect) | 自学习系统，捕获纠正和偏好 |
| [Backlog.md](https://github.com/MrLesk/Backlog.md) | Git 中的人机协作管理 |

### 最佳实践
- **人在回路中：** 外部操作始终需要人工审批
- **审计追踪：** 使用 Git 工作流，每个 AI 操作都有记录
- **角色边界：** 明确定义每个 AI 员工能做和不能做什么
- **定期校准：** 每周审查 AI 输出质量，调整提示词/技能
- **成本监控：** 追踪每个 AI 员工的 API 使用量

---

## 商业 AI 员工平台

对比参考——提供类似能力的闭源平台。

### 全栈 AI 员工平台

| 平台 | 定位 | 价格 | 核心特点 |
|------|------|------|---------|
| [Junior](https://thejunior.ai) | AI 软件工程师 | 免费增值 | 自主编码 Agent，GitHub 集成 |
| [Lindy.ai](https://lindy.ai) | 通用 AI 员工 | $0-299/月 | 4,000+ 集成，零代码 |
| [Emika](https://emika.ai) | 企业 AI 员工 | 企业级 | 2026 年排名第一的 AI 员工平台 |
| [Ema](https://ema.co) | 通用 AI 员工 | 企业级 | 200+ 预置工作流，EmaFusion 模型 |
| [Relevance AI](https://relevanceai.com/workforce) | AI 劳动力团队 | 企业级 | 协作式 AI Agent 团队 |
| [Sintra AI](https://sintra.ai) | 商业 AI 助手 | 企业级 | 12 个专业 AI 员工 |

### AI 团队与劳动力平台

| 平台 | 定位 | 核心特点 |
|------|------|---------|
| [Teammates.ai](https://teammates.ai) | AI 团队成员 | 预置销售、客服、运营 AI 队友 |
| [Beam.ai](https://beam.ai) | AI Agent 劳动力 | 200+ 预置 Agent，企业编排 |
| [Teamster.ai](https://teamster.ai) | AI 团队构建器 | 为任何工作流构建自定义 AI 团队 |
| [FlockX](https://flockx.io) | AI Agent 团队 | 多 Agent 协作平台 |
| [Gumloop](https://gumloop.com) | AI 工作流自动化 | 可视化工作流构建器 |
| [EverWorker](https://everworker.ai) | AI 数字员工 | 自主任务执行，7×24 运行 |

### 专业 AI 员工

| 平台 | 专长 | 核心特点 |
|------|------|---------|
| [TabHR](https://tabhr.ai) | AI HR 员工 | 招聘、入职、员工管理 |
| [SketricGen](https://sketricgen.com) | AI 商业分析师 | 数据分析、报告生成 |
| [Devin](https://devin.ai) | AI 软件工程师 | 全栈自主编码 |
| [Factory](https://factory.ai) | AI 编码 Agent | PR 起草、代码审查、迁移 Agent |

### 可自托管的开源替代方案

| 框架 | Star 数 | 最适合 |
|------|---------|--------|
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | 71k+ | 自托管 AI 软件工程师（原 OpenDevin） |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 183k+ | 自主 AI Agent 平台 |
| [Dify](https://github.com/langgenius/dify) | 136k+ | LLMOps 平台——可视化构建 AI 工作流 |
| [Flowise](https://github.com/FlowiseAI/Flowise) | 52k+ | 拖拽式 LLM 流程构建器 |
| [n8n](https://github.com/n8n-io/n8n) | 183k+ | 工作流自动化 + AI Agent 节点 |
| [AgentVerse](https://github.com/OpenBMB/AgentVerse) | 5.0k+ | 多 Agent 模拟与协作 |

---

## 案例研究与实战手册

| 案例 | 做了什么 | 关键启示 |
|------|---------|---------|
| [Garry Tan 的 gstack](https://github.com/garrytan/gstack) | YC CEO 开源 13+ Claude Code 技能，模拟完整工程组织 | 非技术领导者可以用 Markdown 技能构建 AI 团队 |
| [MetaGPT → MGX](https://mgx.dev/) | AI 软件公司，从一个需求生成完整代码仓库 | 流水线式 SOP 比自由对话效果更好 |
| [ChatDev](https://chatdev.ai/) | 虚拟公司（CEO/CTO/开发/QA）生产软件 | 角色专业化提升输出质量 |

---

## 协议与标准

AI 组织的基础设施层。

| 协议 | 用途 | 状态 |
|------|------|------|
| [MCP](https://modelcontextprotocol.io/) | Agent ↔ 工具连接 | 行业标准，9700万+ SDK 下载 |
| [A2A](https://google.github.io/A2A/) | Agent ↔ Agent 通信 | Google 主导，新兴标准 |
| [AGENTS.md](https://github.com/agentsmd/agents.md) | 通用 Agent 配置格式 | 19k+ star，跨工具 |

---

## 可直接使用的模板

直接复制到你的项目中使用。

### 📁 [/roles](roles/) — AI 员工角色定义
### 📁 [/workflows](workflows/) — 端到端工作流配置
### 📁 [/departments](departments/) — 部门级团队配置

---

## 贡献

欢迎贡献！请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 许可证

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
