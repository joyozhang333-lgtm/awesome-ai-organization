"""
Weekly auto-updater for awesome-ai-organization.
- Fetches latest star counts from GitHub API
- Updates README.md and README-zh.md in place
"""

import re
import os
import requests

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# Map display text -> GitHub "owner/repo"
REPOS = {
    "MetaGPT": "FoundationAgents/MetaGPT",
    "AutoGen / AG2": "microsoft/autogen",
    "CrewAI": "crewAIInc/crewAI",
    "ChatDev": "OpenBMB/ChatDev",
    "gstack": "garrytan/gstack",
    "CAMEL": "camel-ai/camel",
    "OpenHands": "All-Hands-AI/OpenHands",
    "AutoGPT": "Significant-Gravitas/AutoGPT",
    "Dify": "langgenius/dify",
    "Flowise": "FlowiseAI/Flowise",
    "n8n": "n8n-io/n8n",
    "AgentVerse": "OpenBMB/AgentVerse",
    "AGENTS.md": "agentsmd/agents.md",
}


def get_stars(owner_repo: str) -> int | None:
    url = f"https://api.github.com/repos/{owner_repo}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            return r.json().get("stargazers_count")
    except Exception:
        pass
    return None


def format_stars(count: int) -> str:
    if count >= 1000:
        k = count / 1000
        return f"{k:.0f}k+" if k >= 10 else f"{k:.1f}k+"
    return str(count)


def update_file(filepath: str) -> int:
    """Update star counts in a README file. Returns number of replacements."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    changes = 0
    for name, repo in REPOS.items():
        stars = get_stars(repo)
        if stars is None:
            continue
        label = format_stars(stars)
        # Match patterns like "| 65k+ |" or "| 10k+ |" or "| 19k+ star" after the repo name
        # The star count appears in table cells after the repo link
        escaped = re.escape(name)
        pattern = rf"(\[{escaped}\]\([^)]+\)\s*\|)\s*[\d,.]+k?\+?\s*(\|)"
        replacement = rf"\1 {label} \2"
        new_content, n = re.subn(pattern, replacement, content)
        if n > 0:
            content = new_content
            changes += n
            print(f"  {name}: {label} ({stars})")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return changes


if __name__ == "__main__":
    print("Updating README.md...")
    c1 = update_file("README.md")
    print(f"  {c1} updates\n")

    print("Updating README-zh.md...")
    c2 = update_file("README-zh.md")
    print(f"  {c2} updates\n")

    print(f"Total: {c1 + c2} star counts updated.")
