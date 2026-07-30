# Changelog

All notable changes to the **CognitiveMiddleware** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to standard Semantic Versioning / chronological release tracking.

---

## [Unreleased] - 2026-07-29

### Added
- **Full-Body Anatomical Cascade Engine**: Expanded the somatic layer across 6 interconnected body zones (Cranial/Ocular, Vocal/Cervical, Thoracic/Respiratory, Abdominal/Visceral, Pelvic/Kinesthetic, Peripheral/Grounding). Enforced the **Multi-Zone Cascade Rule** requiring all physical tells to engage at least 2 linked body zones across `humanity.md`, `realm_data.yaml`, `Main.md`, and `Rules_Index.md`.
- **Dual-Aspect Psyche Matrix (Wound & Gift)**: Expanded CognitiveMiddleware to include positive psychological dimensions alongside character wounds. Introduced `cognitive_gift`, `generative_anchor`, and `generative_stance` to character cards.
- **Generative Prism Engine**: Implemented `GENERATIVE_ACTIVE` state and Generative Prism intercept processing (`Resonant Hearing`, open somatics, warm syntactical cadence under trust/flow/safety).
- **Positive Archetype & Gift Catalog**: Expanded catalog pairing every Wound with its Generative Virtue counterpart (`Debt Ledger` ↔ `Sacred Stewardship`, `Saviour Complex` ↔ `True Sanctuary`, `System Architect` ↔ `Illuminated Symmetry`, `Mirror` ↔ `Resonant Truth`, `Insulation` ↔ `Sanctuary Bridge`, `Dissolution` ↔ `Threshold Vision`).
- **Positive Psychological Hygiene & Linting**: Added hard bans in `Rules_Index.md` and automated regex checks in `linter.py` for positive therapy-speak (`cognitive gift`, `sacred anchor`, `virtue lens`, `self-actualization`, `empowerment`, `safe space`, `healing journey`) and engine gift names.
- **Local Machine Agent Safeguards**: Added strict local machine agent requirement for prompt file write operations (`b9d29c8`).
- **Silent Instant Prompt Generation**: Implemented fast, zero-latency image prompt tags and background prompt creation without blocking turn execution (`4297d03`).

### Changed
- **Instruction-to-Constraint Optimization**: Converted informal, procedural drafting advice and narrative instructions across `humanity.md`, `voices.md`, `prose.md`, `Main.md`, and `Rules_Index.md` into explicit declarative constraint tables using `MUST`, `NEVER`, `SCOPE`, `PRECEDENCE`, and `INVARIANT` blocks.
- **Live Image Still Routing**: Updated rendering specifications to save stills directly to `Images/{slug}/` and automatically purge transient `.prompt.md` files post-generation to conserve storage (`3d44403`, `4465555`).

---

## [1.2.0] - 2026-07-23

### Added
- **Character Engine Vocal Synthesis**: Introduced vocal behavior profiles, verbal defense mechanisms, conversational stance rules, and dual-register synthesis into character cards (`e868cce`).
- **Motion-Driven Visual Layer**: Integrated auto-rendering of image layers triggered dynamically by scene movement in `CharacterRuntime` (`45191eb`).

### Changed
- **Simulator Streamlining**: Refactored private `CharacterRuntime` to streamline author live testing and chat drop-ins (`74f4119`).
- **Private Directory Security**: Untracked `Simulator/Private/` from git and added default exclusion patterns to `.gitignore` (`81e1c79`).

---

## [1.1.0] - 2026-07-17

### Added
- **Embodiment Baseline Pipeline**: Added body-first physical and sexed/hormonal capacity baselines in `Framework/Main.md` to feed silently into runtime filters (`725e431`).
- **One-Switch `/adult` Toggle**: Added `/adult on|off` command in `CharacterRuntime` for quick activation of heat/intimacy protocols during private RP sessions (`725e431`).
- **Obsidian Visual Relations Canvas**: Added linkified character relationship structures and visual canvas support (`56724fe`).
- **World Builder & Degradation Protocols**: Integrated world builder prompt utilities and system degradation handling into core framework (`001dfc2`).

### Changed
- **Product Scope Refinement**: Positioned CognitiveMiddleware as a 100% off-page drafting middle layer for fiction, categorizing `Simulator/` as an optional side tool (`a4d89b7`).
- **Module Renaming**: Renamed `Sexuality` module to `Erotica Protocol` (`erotica.md`) with act-agnostic scene craft scope (`725e431`, `872ac97`).
- **Dual Licensing Model**: Introduced hybrid MIT license for the core framework engine and CC BY-SA 4.0 for documentation (`0cf1d39`).
- **Local Character Separation**: Carved out named character cards (`Characters/`) from open distribution as author-local files (`9ac3ecb`).

---

## [1.0.0] - 2026-07-15 - 2026-07-16

### Added
- **Tripartite Filtering System**: Split character worldview into Cultural Bias & Occupation (background) and Cognitive Bias / Wound (dynamic situational filter) (`5804cdb`).
- **Transformation Engine & Depth of Knowledge**: Added transformation weights, memory recall filters, and somatic tell decay logs (`1bb8218`, `7527be4`).
- **Automated Prose Linter**: Integrated `Framework/linter.py` with cross-platform wrapper scripts (`scripts/run.py`, `scripts/unix/deploy.sh`, `scripts/windows/deploy.ps1`) (`9a3e658`).
- **Historical Character Importing & Safety Gates**: Added temporal awareness gating, historical character import rules, and visual appearance verification (`20bfed8`, `5328dc9`, `7a8019e`).

### Changed
- **YAML Frontmatter Optimization**: Converted verbose markdown character cards and realm profiles to pure YAML arrays (`realm_data.yaml`), reducing mandatory token load by 46%-57% (`261f48c`, `2c8f330`, `OPTIMIZATION_SUMMARY.md`).

---

## [0.9.0] - 2026-07-12 - 2026-07-14

### Added
- **Single Entry Point (`Main.md`)**: Consolidated load stack, workflow commands, and execution loop into `Framework/Main.md` (`7ec5732`).
- **Central Rules Index (`Rules_Index.md`)**: Consolidated hard bans, cleanup protocols, and dialogue rules (`23579c9`).
- **Somatic-Cognitive Engine**: Enforced "body-first, mind-second" sequence where somatic reactions precede cognitive labeling and dialogue (`humanity.md`).

### Changed
- **Project Rebranding**: Renamed project from *PsycheFramework* / *Psyche Framework* to **CognitiveMiddleware** (`35d2f4f`, `9b8b139`).
- **Off-Page Matrix Guarantee**: Hard-banned system jargon, realm numbers, bias names, and bracketed debug output from draft manuscript prose (`8a8cc6a`, `d8004e6`).
- **Modular Directory Restructure**: Moved chat playground tools to `Simulator/playground.md` and decoupled drafting runtime from live chat (`e8c5cc5`, `69f111d`).

### Initial Release
- **Initial Commit**: Established initial body-first psychological framework, 10 Realms somatic model, and markdown-native runtime (`030713d`).
