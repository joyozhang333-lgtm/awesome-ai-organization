# Social Media Workflow

A complete workflow for managing social media presence with AI employees.

## Overview

```
Trend Monitoring → Content Planning → Creation → Brand Check → Scheduling → Publishing → Analytics → Optimization
```

## Roles Needed

| Step | AI Role | Description |
|------|---------|-------------|
| 1. Monitor | AI Trend Analyst | Track industry trends, competitor activity, viral content |
| 2. Plan | AI Content Strategist | Weekly content calendar, topic selection |
| 3. Create | AI Content Writer | Draft posts adapted per platform |
| 4. Review | AI Brand Guardian | Check tone, compliance, accuracy |
| 5. Design | AI Designer | Create visuals, thumbnails, graphics |
| 6. Publish | AI Publisher | Schedule and post across platforms |
| 7. Analyze | AI Data Analyst | Track engagement, identify top performers |
| 8. Optimize | AI Strategist | Adjust strategy based on data |

## Platform-Specific Guidelines

### Twitter/X
- Post 3-5 times per day
- Best times: 8-10 AM, 12-1 PM, 5-6 PM (audience timezone)
- Use threads for long-form content
- Engage with replies within 1 hour

### LinkedIn
- Post 1-2 times per day
- Best times: 7-8 AM, 12 PM, 5-6 PM (Tue-Thu)
- Long-form posts outperform short ones
- Comment on others' posts for visibility

### Instagram
- Post 1 time per day + 3-5 stories
- Best times: 11 AM - 1 PM, 7-9 PM
- Reels get 2x reach vs static posts
- Use location tags for local reach

## Automation Setup

### With CrewAI
```python
from crewai import Agent, Task, Crew

trend_analyst = Agent(
    role="Social Media Trend Analyst",
    goal="Identify trending topics relevant to our brand",
    backstory="You monitor social media trends 24/7"
)

content_writer = Agent(
    role="Social Media Content Writer",
    goal="Create engaging platform-specific content",
    backstory="You write viral social media posts"
)

brand_reviewer = Agent(
    role="Brand Voice Guardian",
    goal="Ensure all content matches brand guidelines",
    backstory="You protect brand consistency"
)

# Define tasks and create crew...
```

## Weekly Metrics Dashboard
| Metric | Target | How to Measure |
|--------|--------|---------------|
| Engagement rate | >3% | (likes + comments + shares) / impressions |
| Follower growth | >2%/week | New followers / total followers |
| Click-through rate | >1% | Link clicks / impressions |
| Response time | <1 hour | Average time to first reply |
