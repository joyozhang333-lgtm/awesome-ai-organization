# Software Development Workflow

A complete end-to-end workflow for AI-powered software development.

## Overview

```
Requirements → Planning → Design → Implementation → Review → QA → Security → Ship → Monitor
```

## Roles Needed

| Step | AI Role | Tool |
|------|---------|------|
| 1. Requirements | AI Product Manager | MetaGPT / Claude Code |
| 2. Planning | AI Tech Lead | gstack `/plan-eng-review` |
| 3. Design | AI Architect | MetaGPT / Claude Code |
| 4. Implementation | AI Engineer | Claude Code / Cursor |
| 5. Review | AI Code Reviewer | gstack `/review` |
| 6. QA | AI QA Engineer | gstack `/qa` |
| 7. Security | AI Security Engineer | trailofbits/skills |
| 8. Ship | AI Release Manager | gstack `/ship` |
| 9. Monitor | AI SRE | Claude Code + monitoring MCP |

## Detailed Steps

### 1. Requirements → PRD
```
Input: Feature request or user story
AI PM Action:
  - Analyze the request
  - Research competitors
  - Write PRD with acceptance criteria
  - Estimate scope (S/M/L/XL)
Output: PRD document ready for review
Human: Reviews and approves PRD
```

### 2. Planning → Task Breakdown
```
Input: Approved PRD
AI Tech Lead Action:
  - Break PRD into engineering tasks
  - Identify dependencies and risks
  - Estimate effort per task
  - Define architecture approach
Output: Task list with estimates, architecture doc
Human: Reviews plan, adjusts priorities
```

### 3. Design → Architecture
```
Input: Task breakdown
AI Architect Action:
  - Design system architecture
  - Define API contracts
  - Create data models
  - Document edge cases
Output: Architecture doc, API specs, data models
Human: Reviews architecture decisions
```

### 4. Implementation → Code
```
Input: Architecture doc + task list
AI Engineer Action:
  - Write code following architecture
  - Write unit tests alongside code
  - Follow existing code patterns
  - Create PR with description
Output: Pull request with code + tests
```

### 5. Review → Code Quality
```
Input: Pull request
AI Code Reviewer Action:
  - Check code quality and patterns
  - Verify SQL safety and trust boundaries
  - Check for OWASP vulnerabilities
  - Verify test coverage
  - Suggest improvements
Output: Review comments, approval or request changes
```

### 6. QA → Testing
```
Input: Reviewed PR
AI QA Engineer Action:
  - Run existing test suite
  - Write integration tests
  - Test edge cases from architecture doc
  - Verify acceptance criteria from PRD
  - Test for regressions
Output: Test results, bug reports if any
```

### 7. Security → Scan
```
Input: Code ready for merge
AI Security Engineer Action:
  - Run SAST (static analysis)
  - Check dependencies for CVEs
  - Verify authentication/authorization
  - Check for data exposure risks
Output: Security report, pass/fail
Human: Reviews any findings above "Medium"
```

### 8. Ship → Deploy
```
Input: All checks passed
AI Release Manager Action:
  - Merge to main branch
  - Bump version number
  - Update CHANGELOG
  - Create release tag
  - Deploy to staging → verify → deploy to production
Output: Release notes, deployment confirmation
Human: Approves production deployment
```

### 9. Monitor → Post-Deploy
```
Input: Production deployment
AI SRE Action:
  - Monitor error rates for 1 hour post-deploy
  - Check performance metrics
  - Verify key user flows
  - Alert if anomalies detected
Output: Post-deploy health report
```

## Automation with gstack

```bash
# Full workflow using gstack skills
claude "/plan-ceo-review"     # Step 1-2: Review requirements and plan
claude "/plan-eng-review"     # Step 3: Architecture review
# ... AI Engineer implements ...
claude "/review"              # Step 5: Code review
claude "/qa"                  # Step 6: QA testing
# ... Security scan ...
claude "/ship"                # Step 8: Ship to production
```

## Governance Rules

1. **All PRDs require human approval before development starts**
2. **Architecture changes require human sign-off**
3. **Security findings above "Medium" block deployment**
4. **Production deployments require human approval**
5. **Rollback authority: AI can auto-rollback if error rate >5%**
