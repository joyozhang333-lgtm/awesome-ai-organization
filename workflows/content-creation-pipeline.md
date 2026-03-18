# Content Creation Pipeline

A complete workflow for producing content with AI employees.

## Overview

```
Topic Research → Draft Writing → Editing & Polish → Visual Design → Publishing → Analytics
```

## Roles Needed

| Step | AI Role | Tool | Skill/Config |
|------|---------|------|-------------|
| 1. Research | AI Researcher | Claude Code | Web search + summarization |
| 2. Draft | AI Content Writer | Claude Code | [ai-content-writer.md](../roles/ai-content-writer.md) |
| 3. Edit | AI Editor | Claude Code | humanizer skill |
| 4. Design | AI Designer | Cursor + MCP | Figma-Context-MCP |
| 5. Publish | AI Publisher | Claude Code | x-article-publisher-skill |
| 6. Analytics | AI Analyst | Custom | Platform API integration |

## Step-by-Step

### Step 1: Topic Research
```
Prompt: "Research the top 5 trending topics in [industry] this week.
For each topic, provide: title idea, target audience, key points to cover,
and estimated search volume."
```

### Step 2: Draft Writing
```
Prompt: "Write a 1,500-word blog post about [topic].
Target audience: [audience]. Tone: conversational and authoritative.
Include: introduction with hook, 3-5 main sections, actionable takeaways, conclusion with CTA."
```

### Step 3: Editing
```
Prompt: "Review this draft for: AI-sounding phrases (remove them),
readability (aim for grade 8 level), flow (smooth transitions),
and SEO (include keywords naturally)."
```

### Step 4: Visual Design
Use Figma-Context-MCP to generate supporting visuals based on the content.

### Step 5: Publishing
Use x-article-publisher-skill or platform-specific tools to publish.

### Step 6: Analytics
Track performance metrics and feed back into topic research.

## Automation with CrewAI

```python
from crewai import Agent, Task, Crew

researcher = Agent(role="Content Researcher", goal="Find trending topics")
writer = Agent(role="Content Writer", goal="Write engaging articles")
editor = Agent(role="Editor", goal="Polish content to human quality")

crew = Crew(agents=[researcher, writer, editor], tasks=[...])
result = crew.kickoff()
```

## Tips
- Run the full pipeline once manually before automating
- The editing step is the most important — it's what makes AI content feel human
- Always have a human review before publishing to external channels
