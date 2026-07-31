# Scripts — Windows & Unix

Cross-platform launchers for deploy, lint, and migrate. Shared logic lives in Python; OS-specific wrappers only choose the right shell and Python binary.

## AI / agent rule (pick by OS)

| Host OS | Prefer | Alternate |
|:---|:---|:---|
| **Linux, macOS, BSD, WSL** | `python3 scripts/run.py <tool> …` | `scripts/unix/<tool>.sh …` |
| **Windows** | `python scripts/run.py <tool> …` | `scripts/windows/<tool>.ps1 …` (or `.cmd`) |

`scripts/run.py` **auto-detects** the OS and invokes the matching wrapper. Use it when unsure.

Override detection (tests only):

```bash
CM_FORCE_OS=windows python3 scripts/run.py deploy
CM_FORCE_OS=unix    python3 scripts/run.py lint Drafts/
```

## Tools

| Tool | Purpose | Example |
|:---|:---|:---|
| `deploy` | Push framework scaffolds to a sibling book folder | `… deploy MyNovel` |
| `lint` | Scan drafts for system leaks / banned fillers | `… lint Drafts/` |
| `migrate` | One-time `*_optimized` file promotion (no-op if none) | `… migrate` |
| `validate_state.py` | Check a psychosomatic JSON snapshot against the schema | `python3 scripts/validate_state.py [file]` |

## Layout

```
scripts/
  run.py                 # OS-aware dispatcher (preferred)
  README.md              # this file
  unix/
    deploy.sh
    lint.sh
    migrate.sh
  windows/
    deploy.ps1  deploy.cmd
    lint.ps1    lint.cmd
    migrate.ps1 migrate.cmd
```

Core implementations (cross-platform Python):

- `deploy_framework.py`
- `Framework/linter.py`
- `migrate_optimized.py`

## Humans

**Unix:**

```bash
chmod +x scripts/unix/*.sh scripts/run.py   # once
python3 scripts/run.py lint path/to/Drafts
scripts/unix/deploy.sh BookOS
```

**Windows (PowerShell):**

```powershell
python scripts/run.py lint .\Drafts
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\windows\deploy.ps1 BookOS
```

**Windows (CMD):**

```bat
scripts\windows\lint.cmd Drafts
scripts\windows\deploy.cmd
```
