# Incident Response Workflow

A structured workflow for handling production incidents with AI employees.

## Overview

```
Alert → Triage → Diagnosis → Fix → Verify → Deploy → Post-mortem
```

## Roles Needed

| Step | AI Role | Tool |
|------|---------|------|
| 1. Alert | Monitoring System | PagerDuty / Grafana |
| 2. Triage | AI Incident Commander | Claude Code |
| 3. Diagnosis | AI Root Cause Analyst | Claude Code + logs |
| 4. Fix | AI Engineer | Claude Code / Cursor |
| 5. Verify | AI QA Engineer | gstack `/qa` |
| 6. Deploy | AI Release Manager | gstack `/ship` |
| 7. Post-mortem | AI Technical Writer | Claude Code |

## Severity Levels

| Level | Response Time | Example |
|-------|--------------|---------|
| P0 - Critical | Immediate | Service down, data loss |
| P1 - High | <15 min | Major feature broken, security breach |
| P2 - Medium | <1 hour | Degraded performance, minor feature broken |
| P3 - Low | <4 hours | Cosmetic issue, non-critical bug |

## AI Triage Prompt
```
You are an Incident Commander. An alert has been triggered:

[Paste alert details]

1. Classify severity (P0-P3)
2. Identify affected systems and users
3. List possible root causes (most likely first)
4. Recommend immediate actions
5. Identify who needs to be notified
```

## Post-mortem Template
```markdown
## Incident Post-mortem — [Date] — [Title]

### Summary
[What happened, when, how long, who was affected]

### Timeline
| Time | Event |
|------|-------|
| HH:MM | Alert triggered |
| HH:MM | Triage started |
| HH:MM | Root cause identified |
| HH:MM | Fix deployed |
| HH:MM | Service restored |

### Root Cause
[Technical explanation]

### Impact
- Users affected: [number]
- Duration: [minutes/hours]
- Revenue impact: [if applicable]

### What Went Well
- [Things that worked]

### What Went Wrong
- [Things that didn't work]

### Action Items
| Action | Owner | Due Date |
|--------|-------|----------|
| [Preventive measure] | [person] | [date] |
```
