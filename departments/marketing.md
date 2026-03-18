# Marketing Department Setup

A complete blueprint for building an AI-powered marketing department.

## Team Structure

```
AI Marketing Lead
├── AI Content Strategist
├── AI Copywriter
├── AI Social Media Manager
├── AI SEO Specialist
├── AI Designer
└── AI Data Analyst
```

## Role Configurations

### AI Content Strategist
- **Tool:** Claude Code or ChatGPT
- **Responsibilities:** Content calendar, topic research, competitive analysis
- **Output:** Weekly content plan with topics, formats, and target platforms
- **Autonomy level:** High — can plan independently, human approves calendar

### AI Copywriter
- **Tool:** Claude Code with humanizer skill
- **Responsibilities:** Blog posts, email campaigns, landing page copy
- **Output:** Draft content ready for human review
- **Autonomy level:** Medium — all external content needs human review

### AI Social Media Manager
- **Tool:** Claude Code + scheduling tools
- **Responsibilities:** Post creation, scheduling, community engagement
- **Output:** Platform-specific posts, engagement reports
- **Autonomy level:** Medium — routine posts auto-publish, campaigns need approval

### AI SEO Specialist
- **Tool:** Claude Code + SEO MCP servers
- **Responsibilities:** Keyword research, on-page optimization, content briefs
- **Output:** SEO reports, optimization recommendations
- **Autonomy level:** High — can analyze and recommend independently

### AI Designer
- **Tool:** Cursor + Figma-Context-MCP
- **Responsibilities:** Social graphics, blog images, presentation slides
- **Output:** Visual assets matching brand guidelines
- **Autonomy level:** Medium — needs brand review

### AI Data Analyst
- **Tool:** Claude Code + database MCP
- **Responsibilities:** Campaign analytics, ROI tracking, A/B test analysis
- **Output:** Weekly performance reports, optimization insights
- **Autonomy level:** High — can analyze and report independently

## Content Production Pipeline

```
Week Start:
  Mon → AI Strategist creates weekly plan
  Mon → Human approves plan

Production:
  Tue-Thu → AI Copywriter drafts content
  Tue-Thu → AI Designer creates visuals
  Fri → AI SEO optimizes all content

Publishing:
  Daily → AI Social Media Manager posts
  Weekly → AI Analyst reports performance

Monthly:
  AI Strategist reviews performance → adjusts strategy
```

## Governance Rules

1. **All external-facing content requires human review before publishing**
2. **Brand voice guidelines must be followed — no exceptions**
3. **No engagement with controversial topics without human approval**
4. **Customer data must never appear in marketing content**
5. **Monthly human audit of all published content**
