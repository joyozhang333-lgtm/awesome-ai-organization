# Product Department Setup

A complete blueprint for building an AI-powered product department.

## Team Structure

```
AI Product Lead
├── AI Product Manager
├── AI UX Researcher
├── AI Data Analyst
├── AI Technical Writer
└── AI Localization Specialist
```

## Role Configurations

### AI Product Lead
- **Tool:** Claude Code with gstack
- **Skills:** `/plan-ceo-review`, strategic planning
- **Responsibilities:** Product vision, roadmap prioritization, stakeholder alignment
- **Output:** Quarterly roadmaps, product strategy docs, feature prioritization
- **Autonomy level:** High — can analyze and recommend, human decides direction

### AI Product Manager
- **Tool:** MetaGPT / Claude Code
- **Responsibilities:** PRD writing, user story creation, sprint planning, competitor analysis
- **Output:** PRDs, user stories, sprint backlogs, competitive reports
- **Autonomy level:** Medium — drafts independently, human reviews before dev handoff

### AI UX Researcher
- **Tool:** Claude Code + survey tools
- **Responsibilities:** User feedback analysis, usability heuristics, persona creation
- **Output:** Research reports, persona docs, journey maps, usability findings
- **Autonomy level:** High — can analyze independently, human validates insights

### AI Data Analyst
- **Tool:** Claude Code + database MCP
- **Responsibilities:** Product metrics, funnel analysis, A/B test evaluation, cohort analysis
- **Output:** Dashboards, metric reports, experiment results
- **Autonomy level:** High — can query and report independently

### AI Technical Writer
- **Tool:** Claude Code + humanizer
- **Responsibilities:** Documentation, help center articles, release notes, API docs
- **Output:** User guides, API documentation, changelog entries
- **Autonomy level:** Medium — drafts independently, human reviews before publishing

### AI Localization Specialist
- **Tool:** Claude Code
- **Responsibilities:** Translation, cultural adaptation, terminology consistency
- **Output:** Localized content, glossaries, translation memory
- **Autonomy level:** Medium — routine translations auto, marketing copy needs review

## Product Development Cycle

```
Discovery (Week 1):
  Mon → AI UX Researcher analyzes user feedback & support tickets
  Tue → AI Data Analyst pulls usage metrics & funnel data
  Wed → AI Product Lead synthesizes insights → opportunity brief
  Thu → Human reviews opportunities → selects priorities

Definition (Week 2):
  Mon → AI PM writes PRD for selected features
  Tue → AI UX Researcher creates user flows
  Wed → AI PM breaks down into user stories
  Thu → Human reviews PRD → approves for development
  Fri → AI PM hands off to engineering

Delivery (Week 3-4):
  Ongoing → AI Data Analyst monitors feature flags & metrics
  Ongoing → AI Technical Writer drafts documentation
  Launch → AI Localization Specialist translates release notes

Review:
  Post-launch → AI Data Analyst reports adoption metrics
  Weekly → AI PM updates roadmap based on data
```

## Governance Rules

1. **Product roadmap changes require human approval**
2. **All PRDs need human review before engineering handoff**
3. **User-facing copy requires human review**
4. **A/B test designs need human sign-off**
5. **Monthly human review of product metrics and AI recommendations**

## Metrics to Track

| Metric | Target | Frequency |
|--------|--------|-----------|
| PRD turnaround time | <2 days | Per feature |
| User story quality (acceptance by eng) | >90% | Per sprint |
| Documentation coverage | 100% of features | Per release |
| Feature adoption rate | Track trend | Weekly |
| NPS / user satisfaction | Track trend | Monthly |
