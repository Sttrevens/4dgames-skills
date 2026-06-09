#!/usr/bin/env python3
"""Mirror upstream skill repos into ./skills/<name>/.

`skills.yaml` remains the index source of truth. For entries with
`source_type: repo`, this script shallow-clones the upstream repo and mirrors the
configured `skill_path` into `skills/<name>/`.

Bundled and related-project skills are intentionally left alone.
"""
from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from validate_skills import load_skills

ROOT = Path(__file__).resolve().parent.parent
MIRROR_ROOT = ROOT / "skills"
EXCLUDES = {
    ".git",
    ".github",
    "__pycache__",
    ".pytest_cache",
    ".DS_Store",
    "node_modules",
    ".venv",
    "venv",
}


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    for item in src.iterdir():
        if item.name in EXCLUDES:
            continue
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, ignore=shutil.ignore_patterns(*EXCLUDES))
        else:
            shutil.copy2(item, target)


def main() -> int:
    skills = load_skills()
    for skill in skills:
        if skill["source_type"] != "repo":
            continue
        name = skill["name"]
        repo = skill["repo"]
        skill_path = skill["skill_path"]
        with tempfile.TemporaryDirectory() as tmp:
            clone_dir = Path(tmp) / "repo"
            subprocess.check_call(
                ["git", "clone", "--depth", "1", f"https://github.com/{repo}.git", str(clone_dir)],
                stdout=subprocess.DEVNULL,
            )
            src = clone_dir if skill_path == "." else clone_dir / skill_path
            if not (src / "SKILL.md").exists():
                raise SystemExit(f"{name}: SKILL.md not found at {repo}:{skill_path}")
            copy_tree(src, MIRROR_ROOT / name)
            print(f"Mirrored {name} from {repo}:{skill_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
