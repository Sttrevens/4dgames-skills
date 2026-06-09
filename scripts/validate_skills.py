#!/usr/bin/env python3
"""Validate the lightweight 4D Games skills index."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
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


def main() -> int:
    errors: list[str] = []
    seen: set[str] = set()
    for skill in load_skills():
        name = skill.get("name")
        if not name:
            errors.append("skill missing name")
            continue
        if name in seen:
            errors.append(f"duplicate skill: {name}")
        seen.add(name)
        if not (ROOT / "skills" / name / "SKILL.md").exists():
            errors.append(f"{name}: missing skills/{name}/SKILL.md")
        for field in ("category", "tagline", "description"):
            if not skill.get(field):
                errors.append(f"{name}: missing {field}")
    if errors:
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(seen)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
