# Engineering Department Setup

A complete blueprint for building an AI-powered engineering department.

## Team Structure

```
AI Tech Lead
├── AI Backend Engineer
├── AI Frontend Engineer
├── AI QA Engineer
├── AI Security Engineer
└── AI DevOps Engineer
```

## Role Configurations

### AI Tech Lead
- **Tool:** Claude Code with gstack
- **Skills:** `/plan-eng-review`, `/review`, architecture decisions
- **Responsibilities:** Code review, architecture, technical decisions
- **Autonomy level:** High — can approve non-critical changes

### AI Backend Engineer
- **Tool:** Claude Code or Cursor
- **Skills:** Language-specific skills (Python, TypeScript, Go)
- **Responsibilities:** API development, database design, business logic
- **Autonomy level:** Medium — needs review for production changes

### AI Frontend Engineer
- **Tool:** Cursor with React/Next.js rules
- **Skills:** Vercel agent-skills, UI component generation
- **Responsibilities:** UI implementation, responsive design, accessibility
- **Autonomy level:** Medium — needs design review

### AI QA Engineer
- **Tool:** Claude Code with gstack
- **Skills:** `/qa`, `/qa-design-review`, playwright-skill
- **Responsibilities:** Test writing, bug detection, regression testing
- **Autonomy level:** High — can run tests independently

### AI Security Engineer
- **Tool:** Claude Code
- **Skills:** trailofbits/skills, hexstrike-ai
- **Responsibilities:** Security scanning, vulnerability detection, audit
- **Autonomy level:** High for scanning, needs human for remediation decisions

### AI DevOps Engineer
- **Tool:** Claude Code with gstack
- **Skills:** `/ship`, AWS MCP servers
- **Responsibilities:** CI/CD, deployment, infrastructure
- **Autonomy level:** Low — all production deployments need human approval

## Workflow

```
Feature Request
  → AI Tech Lead (breaks down tasks)
  → AI Engineers (implement)
  → AI QA (test)
  → AI Security (scan)
  → AI Tech Lead (review)
  → Human (approve)
  → AI DevOps (deploy)
```

## Governance Rules

1. **All production deployments require human approval**
2. **Security findings above "Medium" require human review**
3. **Architecture changes require human sign-off**
4. **AI-generated code must pass automated tests before review**
5. **Weekly human audit of AI decisions and code quality**

## Metrics to Track

| Metric | Target | Frequency |
|--------|--------|-----------|
| PR review time | <30 min | Per PR |
| Bug escape rate | <5% | Weekly |
| Test coverage | >80% | Per PR |
| Security scan pass rate | 100% critical | Per PR |
| Deployment frequency | Daily | Weekly |
