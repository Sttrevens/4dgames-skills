#!/usr/bin/env python3
"""Render README.md skill table from skills.yaml."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
SKILLS = ROOT / "skills.yaml"


def load_skills() -> list[dict]:
    skills: list[dict] = []
    current: dict | None = None
    for raw in SKILLS.read_text().splitlines():
        line = raw.rstrip()
        if line.startswith("  - "):
            if current:
                skills.append(current)
            current = {}
            key, value = line[4:].split(":", 1)
            current[key.strip()] = value.strip()
        elif current is not None and line.startswith("    "):
            key, value = line.strip().split(":", 1)
            current[key.strip()] = value.strip()
    if current:
        skills.append(current)
    return skills


def render(skills: list[dict]) -> str:
    rows = ["| Skill | Category | Description |", "|---|---|---|"]
    for skill in sorted(skills, key=lambda item: (item["category"], item["name"])):
        name = skill["name"]
        rows.append(
            f"| [`{name}`](skills/{name}) | {skill['category']} | {skill['tagline']} |"
        )
    return "\n".join(rows)


def replace_block(text: str, body: str) -> str:
    pattern = re.compile(
        r"<!-- SKILLS:START -->.*?<!-- SKILLS:END -->",
        re.DOTALL,
    )
    replacement = f"<!-- SKILLS:START -->\n{body}\n<!-- SKILLS:END -->"
    if not pattern.search(text):
        raise SystemExit("README.md is missing SKILLS markers")
    return pattern.sub(replacement, text)


def main() -> int:
    skills = load_skills()
    README.write_text(replace_block(README.read_text(), render(skills)))
    print(f"Rendered {len(skills)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
