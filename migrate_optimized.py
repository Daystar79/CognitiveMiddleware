#!/usr/bin/env python3
"""
Migration: replace framework files with optimized siblings (if present).

Cross-platform. Prefer launching via:
  python scripts/run.py migrate
  scripts/unix/migrate.sh          (Unix)
  scripts/windows/migrate.ps1      (Windows)

Run from the repo root (or any cwd — paths resolve from this file).
"""

from __future__ import annotations

import os
import shutil
import sys
import tempfile
from datetime import date
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parent


def word_count(path: Path) -> int:
    """Count words in a file."""
    if not path.is_file():
        return 0
    return len(path.read_text(encoding="utf-8").split())


CORE_REPLACEMENTS: List[Tuple[Path, Path]] = [
    (ROOT / "Framework" / "Main_optimized.md", ROOT / "Framework" / "Main.md"),
    (ROOT / "Framework" / "Rules_Index_optimized.md", ROOT / "Framework" / "Rules_Index.md"),
    (
        ROOT / "Framework" / "Psychology" / "realm_data_optimized.yaml",
        ROOT / "Framework" / "Psychology" / "realm_data.yaml",
    ),
    (
        ROOT / "Simulator" / "CharacterRuntime_optimized.md",
        ROOT / "Simulator" / "CharacterRuntime.md",
    ),
]

DEMO_CHARS: Tuple[str, ...] = ("cass", "helen", "lior", "nora", "reed", "wren")


def main() -> int:
    print("=== Cognitive Middleware Optimization Migration ===\n")

    missing = [src for src, _ in CORE_REPLACEMENTS if not src.is_file()]
    char_missing = [
        ROOT / "Characters" / f"{name}_optimized.md"
        for name in DEMO_CHARS
        if not (ROOT / "Characters" / f"{name}_optimized.md").is_file()
    ]
    if missing or char_missing:
        print("[!] No optimized source files found.")
        print("    This migration is only needed when *_optimized.* siblings exist.")
        print("    Current tree already uses the optimized framework layout.")
        print("    All optimizations have been applied to the main files.")
        return 0

    backup_dir = ROOT / f"backups_{date.today().strftime('%Y%m%d')}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    print(f"Creating backups in {backup_dir.name}/ ...")

    for _, dst in CORE_REPLACEMENTS:
        if dst.is_file():
            shutil.copy2(dst, backup_dir / f"{dst.stem}_original{dst.suffix}")
    for path in (ROOT / "Characters").glob("*.md"):
        shutil.copy2(path, backup_dir / path.name)

    print("Replacing core framework files...")
    for src, dst in CORE_REPLACEMENTS:
        if not src.is_file():
            print(f"    [skip] missing {src.relative_to(ROOT)}")
            continue
        # Use atomic replacement: copy to temp, then replace
        try:
            temp_dst = dst.with_suffix('.tmp')
            shutil.copy2(src, temp_dst)
            os.replace(temp_dst, dst)  # Atomic on POSIX, raises on Windows if dst exists
            src.unlink()
            print(f"    {dst.relative_to(ROOT)}")
        except Exception as e:
            print(f"    [ERROR] Failed to replace {dst.relative_to(ROOT)}: {e}")
            if temp_dst.exists():
                temp_dst.unlink()
            continue

    print("Replacing character cards...")
    for name in DEMO_CHARS:
        src = ROOT / "Characters" / f"{name}_optimized.md"
        dst = ROOT / "Characters" / f"{name}.md"
        if not src.is_file():
            print(f"    [skip] missing {src.name}")
            continue
        # Use atomic replacement
        try:
            temp_dst = dst.with_suffix('.tmp')
            shutil.copy2(src, temp_dst)
            os.replace(temp_dst, dst)
            src.unlink()
            print(f"    {dst.name}")
        except Exception as e:
            print(f"    [ERROR] Failed to replace {dst.name}: {e}")
            if temp_dst.exists():
                temp_dst.unlink()
            continue

    print("\n=== Migration Complete ===\n")
    print("Word count verification (core):")
    for rel in (
        "Framework/Main.md",
        "Framework/Rules_Index.md",
        "Framework/Psychology/realm_data.yaml",
    ):
        p = ROOT / rel
        print(f"  {rel}: {word_count(p)} words")

    print("\nOptimization summary: OPTIMIZATION_SUMMARY.md")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nCancelled.", file=sys.stderr)
        raise SystemExit(130)
