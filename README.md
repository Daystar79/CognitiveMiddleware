# CognitiveMiddleware

**An invisible, file-native cognitive middle layer for AI-assisted long-form novel drafting.**  
*Body-first psychology, tripartite worldview filtering, and realm-aware somatics — running silently **off-page** so manuscript drafts remain clean, immersive fiction.*

---

## Executive Summary

**CognitiveMiddleware** (running on the Psyche Matrix runtime) is a file-native architecture designed to solve common AI prose defects: therapy-speak, perfect recall, symmetric ping-pong dialogue, repetitive filler, and system jargon leakage.

Instead of prompting the AI with generic instructions or letting it narrate internal system math, CognitiveMiddleware loads as an invisible cognitive layer behind your character cards and movement briefs. The matrix calculates physical reactions, bias distortions, and state shifts silently off-page, delivering pure manuscript prose.

> **Key Rule:** The matrix is a tool for the author, not content for the reader. Zero system jargon (`Realm`, `Debt Ledger`, `Prism Intercept`, `Focus Lock`) ever appears in the final manuscript.

---

## Core Pillars

- 🩸 **Body Before Insight** — Biological constants dictate that somatic tells (heartbeat, jaw lock, tremor) precede cognitive labeling and spoken dialogue.
- 🎭 **Tripartite Worldview Filtering** — Character perception is shaped by permanent background filters (**Cultural Bias** & **Occupation**) and a dynamic situational filter (**Cognitive Bias / Wound**) that remains `DORMANT` until activated by scene pressure.
- 🗣️ **Syntactical Speech Engine** — Dialogue is treated as behavioral action. Character registers, vocal pitch, interruption habits (`conversational_stance`), and verbal defenses adapt dynamically to somatic focus and interlocutors.
- 📈 **Transformation Engine & Ledgers** — Dynamic character growth or regression is tracked via structured YAML state logs (`[slug]_log.yaml`) and scene timeline ledgers (`Continuity_Ledger.md`), preserving immutable identity cards.
- 🛡️ **100% Off-Page Matrix Guarantee** — Automated linting enforces strict output hygiene, stripping framework jargon, therapy-speak, and debug dumps before prose is saved.

---

## System Architecture

```
CognitiveMiddleware/
├── Framework/                         # Core Middleware Engine (Always Loaded)
│   ├── Main.md                        # Master execution loop, load protocols & pipeline constraints
│   ├── Rules_Index.md                 # Hard bans, output hygiene & dialogue constraints
│   ├── Modules.md                     # Active & planned mechanics module registry
│   ├── Continuity_Ledger.md           # Scene timeline, somatic close & continuity tracking
│   ├── Character_Change_Log.md        # Consolidated human-readable matrix state snapshot
│   ├── degradation_protocol.md       # Fallback protocols under context degradation
│   ├── linter.py                      # Automated prose linter utility
│   ├── Psychology/
│   │   └── realm_data.yaml            # Somatic profiles for all 10 Great Wheel Realms
│   ├── Mechanics/
│   │   ├── erotica.md                 # Erotica Protocol (Optional, DISABLED by default)
│   │   ├── humanity.md                # Human behavior, somatic decay & wound rules
│   │   ├── prose.md                   # Prose style definitions & auto-locking mechanics
│   │   └── voices.md                  # Character idiolect & voice template schemas
│   └── Prompts/
│       ├── character_builder_prompt.md# Structured character card generator prompt
│       ├── world_builder_prompt.md    # World building & cultural bias generator
│       └── improvement_pass_prompt.md # Manuscript polish & linter pass prompt
├── Characters/                        # Character Single Source of Truth
│   ├── _template.md                   # Public character card scaffold
│   ├── _log_template.yaml             # Public runtime state log schema
│   ├── [slug].md                      # Character card (author-local)
│   ├── [slug]_log.yaml                # Mutable character runtime state log
│   └── Relations.md                   # Master character relationship matrix & Obsidian canvas
├── Simulator/                         # Optional Side Tool: Character Simulator
│   ├── CharacterRuntime.md            # Interactive chat drop-in & card stress-tester
│   └── README.md                      # Simulator setup, slash commands & adult gate docs
├── Images/                            # Image Rendering Pipeline
│   └── CharacterRenderingEngine.md    # Visual scene-motion trigger & rendering specs
├── scripts/                           # OS-Aware CLI Tooling & Wrappers
│   ├── run.py                         # Universal OS launcher (agents & CLI)
│   ├── unix/                          # Linux / macOS / WSL shell wrappers
│   └── windows/                       # Windows PowerShell & CMD wrappers
├── CHANGELOG.md                       # Project release history & version updates
├── LICENSE.md                         # Hybrid MIT & CC BY-SA 4.0 license documentation
└── OPTIMIZATION_SUMMARY.md            # Token load reduction & YAML optimization report
```

---

## Quick Start & Workflow

### 1. Installation & Deployment
Deploy the framework scaffolds into your novel project folder using the OS-aware launcher:

```bash
# Preferred (auto-detects Windows vs Unix):
python3 scripts/run.py deploy [target_dir]

# Unix / macOS / WSL:
scripts/unix/deploy.sh [target_dir]

# Windows PowerShell:
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/windows/deploy.ps1 [target_dir]
```

### 2. Mandatory Session Load Manifest
For every drafting session, load the canonical manifest in context:
1. `Framework/Main.md`
2. `Framework/Rules_Index.md`
3. `Framework/Psychology/realm_data.yaml`
4. Active character cards (`Characters/[slug].md`)
5. Active character state logs (`Characters/[slug]_log.yaml`)
6. `Framework/Continuity_Ledger.md`
7. `Framework/Modules.md`

### 3. Pre-Draft Ledger Integrity Pass
Before drafting, verify ledger status:
- If `Framework/Continuity_Ledger.md` or `[slug]_log.yaml` contain unsynced rows or missing snapshots, resolve them on disk.
- Execution MUST be `CLEAN` before generating manuscript prose.

### 4. Drafting Execution
Provide the AI with your **Movement Brief**. The pipeline executes silently:
`Body Baseline` → `Runtime Filters` → `Focus Shift` → `Bias Resolution` → `Somatic Precedence` → `Prism Intercept` → `Manuscript Output`.

### 5. Automated Post-Draft Linting
Run the automated linter to catch system leaks, therapy-speak, or banned dialogue tags before committing:

```bash
# Auto launcher (any OS):
python3 scripts/run.py lint Drafts/

# Platform wrappers:
scripts/unix/lint.sh Drafts/
# Windows: scripts/windows/lint.ps1 Drafts\
```

---

## Core Cognitive Concepts

### 1. Tripartite Worldview Filtering
Character perception and action pass through three distinct filter layers:
- **Cultural Bias (Background):** Metaphysical frame, taboos, sacred bounds, and temporal awareness (e.g., cyclic liturgy vs. linear progress).
- **Occupation (Background):** Technical lexicon, staging focus, status reflexes, and tool habits.
- **Cognitive Bias / Wound (Triggered Intercept):** Psychological wound warp (e.g., *Debt Ledger*, *Saviour Complex*, *System Architect*, *Mirror*, *Insulation*, *Dissolution*). Remains **`DORMANT`** in casual beats and activates ONLY under wound-relevant emotional pressure (**`ACTIVE`**).

### 2. Somatic Engine & The Great Wheel (10 Realms)
Physical tells are governed by `Framework/Psychology/realm_data.yaml`, mapping bracing, release, and remnants across 10 Realms:
- **Internal Realms (I-V):** Origin, Form, Identity, Will, Echoes (*Self-framing & bracing*).
- **External Realms (VI-X):** Compassion, Presence, Integration, Threshold Fear, Return (*Self meeting world*).

### 3. Transformation Engine & State Logging
Character identity cards (`[slug].md`) remain immutable build defaults. All narrative evolution (focus shifts, bias strength changes, somatic flexibility) is recorded dynamically in `Characters/[slug]_log.yaml`:
- **Snapshot:** Current `active_focus`, `latent_weights`, `bias_strength`, and `default_somatic`.
- **Temporary Effects:** Shift durations (decremented post-movement).
- **History:** Log of medium/extreme pressure deltas, timestamps, and commit IDs.
- **Human-Readable Projection:** Consolidated into `Framework/Character_Change_Log.md` post-commit.

---

## Author Drafting Commands

| Command | Category | Description / Effect |
|:---|:---|:---|
| *Load Card* | Setup | Silent state load (character identity + log snapshot) |
| `/focus N` | Focus | Lock active Focus to Realm $N \in [1, 10]$ |
| `/focus unlock` | Focus | Allow dynamic, pressure-driven Focus shifts |
| `/bias active` | Perception | Force Cognitive Bias into `ACTIVE` state (warp enabled) |
| `/bias dormant` | Perception | Restore Cognitive Bias to `DORMANT` state (normal perception) |
| `/style <id>` | Voice | Lock prose style (e.g., `natural`, `visceral`, `llm`) |
| `/style unlock` | Voice | Allow dynamic prose style adjustments |
| `/transform event: <desc> strength: <lvl>` | State | Force a transformation pressure calculation |
| `/reset` | State | Clear active session state overrides |

---

## Optional: Character Simulator

`Simulator/CharacterRuntime.md` is an optional side tool designed for **interactive chat drop-ins and card stress-testing** before manuscript drafting.

- **Standalone Operation:** Paste `Simulator/CharacterRuntime.md` into any LLM chat interface along with a character card.
- **One-Switch Adult Toggle:** Includes `/adult on|off` (alias `/heat on|off`) for private adult RP sessions (requires `Canon Adult: YES` on cards).
- **Live Visual Motion Engine:** Integrates with `Images/CharacterRenderingEngine.md` for motion-triggered live image generation saving stills to `Images/{slug}/`.

---

## Developer Tooling & CLI Reference

| Utility Script | Universal Launcher (Agents) | Unix Wrapper | Windows Wrapper |
|:---|:---|:---|:---|
| **Deploy Scaffolds** | `python3 scripts/run.py deploy [dir]` | `scripts/unix/deploy.sh` | `scripts/windows/deploy.ps1` |
| **Lint Prose** | `python3 scripts/run.py lint <path>` | `scripts/unix/lint.sh` | `scripts/windows/lint.ps1` |
| **Migrate State** | `python3 scripts/run.py migrate` | `scripts/unix/migrate.sh` | `scripts/windows/migrate.ps1` |

---

## License & Privacy Model

CognitiveMiddleware operates under a hybrid licensing model:

- ⚖️ **Software Utilities** (`Framework/linter.py`, `deploy_framework.py`, `scripts/run.py`): Licensed under the **[MIT License](LICENSE.md)**.
- 📄 **Framework Documentation & Schemas** (`Framework/`, `Characters/_template.md`, `Simulator/`, prompts): Licensed under **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**.
- 🔒 **Author-Local Materials**: Named character cards (`Characters/*.md` except `_template.md`), private state logs, and relationship maps are **Author-Private**. All rights reserved; excluded from public distribution and deployment scripts.

Copyright (c) 2026 Cian Didymos. See [LICENSE.md](LICENSE.md) for full terms.

---

## Disclaimers & Compliance

CognitiveMiddleware maintains strict compliance with GitHub Terms of Service and Acceptable Use Policies:

- 🔞 **Content & Age Warning (18+):** Optional adult erotica mechanics (`Framework/Mechanics/erotica.md`) and simulator heat modes are strictly restricted to adult users (18+) and canonically adult (18+) fictional characters. Disabled by default.
- 🧠 **Psychological Disclaimer:** Framework mechanics ("wound", "somatic engine", "Psyche Matrix") are literary tools for novel drafting, not medical or psychological advice.
- 🤖 **AI Provider Compliance:** Users must adhere to their LLM provider's Terms of Service and Content Policies.

For full legal terms, age gating details, and platform compliance guidelines, read **[DISCLAIMER.md](DISCLAIMER.md)**.

