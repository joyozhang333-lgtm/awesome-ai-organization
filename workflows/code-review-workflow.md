# Code Review Workflow

An automated code review pipeline using AI employees.

## Overview

```
PR Created → Security Scan → Code Review → Test Generation → Human Approval → Ship
```

## Roles Needed

| Step | AI Role | Tool | Config |
|------|---------|------|--------|
| 1. Security | AI Security Auditor | Claude Code | trailofbits/skills |
| 2. Review | AI Code Reviewer | Claude Code | gstack `/review` |
| 3. Testing | AI QA Engineer | Claude Code | gstack `/qa` |
| 4. Approval | Human | — | Manual review |
| 5. Ship | AI Release Manager | Claude Code | gstack `/ship` |

## Using gstack (Garry Tan's Setup)

```bash
# Step 1: Review the PR
/review

# Step 2: Run QA tests
/qa

# Step 3: If everything passes, ship it
/ship
```

## Using Claude Code Skills

### Security Scan
```
Prompt: "Review this diff for security vulnerabilities.
Check for: SQL injection, XSS, command injection, auth bypasses,
hardcoded secrets, path traversal, and SSRF."
```

### Code Review
```
Prompt: "Review this PR. Focus on: correctness, error handling,
test coverage, naming clarity, and unnecessary complexity.
Provide a verdict: APPROVE, REQUEST CHANGES, or NEEDS DISCUSSION."
```

### Test Generation
```
Prompt: "Generate tests for the new code in this PR.
Cover: happy path, edge cases, error scenarios.
Use the project's existing test framework and patterns."
```

## Tips
- Security scan should always run first — block merging if critical issues found
- AI code review catches ~80% of issues a human reviewer would find
- Always have a human do final approval for production deployments
- Use the AI-generated tests as a starting point, not the final word
