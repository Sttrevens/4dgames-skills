#!/usr/bin/env python3
"""Render README.md and README.en.md skill tables from skills.yaml."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
READMES = {
    "zh": ROOT / "README.md",
    "en": ROOT / "README.en.md",
}
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


def repo_url(skill: dict) -> str:
    return f"https://github.com/{skill['repo']}"


def source_label(skill: dict, lang: str) -> str:
    labels = {
        "repo": ("Upstream repo", "独立仓库"),
        "bundled": ("Bundled here", "本仓内置"),
        "related-project": ("Related project", "相关项目"),
    }
    en, zh = labels[skill["source_type"]]
    label = zh if lang == "zh" else en
    return f"[{label}]({repo_url(skill)})"


def render(skills: list[dict], lang: str) -> str:
    if lang == "zh":
        rows = ["| Skill | 分类 | 来源 | 描述 |", "|---|---|---|---|"]
        category_key = "category_zh"
        tagline_key = "tagline_zh"
    else:
        rows = ["| Skill | Category | Source | Description |", "|---|---|---|---|"]
        category_key = "category_en"
        tagline_key = "tagline_en"

    for skill in sorted(skills, key=lambda item: (item[category_key], item["name"])):
        name = skill["name"]
        rows.append(
            f"| [`{name}`](skills/{name}) | {skill[category_key]} | {source_label(skill, lang)} | {skill[tagline_key]} |"
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
    for lang, path in READMES.items():
        path.write_text(replace_block(path.read_text(), render(skills, lang)))
        print(f"Rendered {path.name} with {len(skills)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
