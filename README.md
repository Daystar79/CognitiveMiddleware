# CognitiveMiddleware
**An invisible, file-native cognitive layer for AI-assisted long-form drafting and character runtime.**

Body-first psychology, dual-aspect psyche (wound ↔ gift), realm-aware somatics — running **off-page** so manuscripts and RP stay clean of system jargon.

---

## What it is

CognitiveMiddleware is a **psychological / physical runtime for characters**, plus thin application layers:

| Layer | File | Job |
|---|---|---|
| **Cognitive Pipeline** | `Framework/CognitivePipeline.md` | Mind-body simulation → `Feels` / `Thinks` / `Says` / `Does` |
| **Book Writing Layer** | `Framework/Main.md` | Manuscript prose, style locks, ledgers |
| **Roleplay Engine** | `Simulator/CharacterRuntime.md` | Interactive chat host, OOC commands |
| **Rules & somatics** | `Rules_Index.md`, `Psychology/realm_data.yaml` | Hard bans + body catalogs |
| **State** | `Characters/[slug]_log.yaml` + live snapshot schema | Durable vs per-tick state |

It targets common AI fiction defects: therapy-speak, perfect recall, symmetric dialogue, filler, and framework jargon leakage.

---

## Core pillars

| Pillar | Why it matters |
|---|---|
| **Body before insight** | Somatic tells precede labeled emotion and dialogue |
| **Dual-aspect psyche** | Wound *and* gift modes — not trauma-only engines |
| **4-channel output** | Structured intent vector for any downstream app |
| **Durable + live state** | Logs for continuity; psychosomatic snapshot per tick |
| **100% off-page matrix** | Rules + linter keep system terms out of prose |

---

## System architecture

```
                 Cognitive Pipeline
          (psych / physical character runtime)
             Feels · Thinks · Says · Does
            + psychosomatic_state schema
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
   Book Writing Layer           Roleplay Engine
      (Main.md)               (CharacterRuntime.md)
   manuscript prose              live chat RP
```

**State:**
- **Card** (`Characters/[slug].md`) — build identity (immutable defaults)
- **Log** (`Characters/[slug]_log.yaml`) — durable runtime evolution
- **Live snapshot** — matches `Framework/Schemas/psychosomatic_state.json` each tick

**Module system:** Downstream applications register injectors in [`Framework/Modules.md`](Framework/Modules.md) to enter the cognitive loop at defined hooks (`pre_somatic`, `affect_filter`, `pre_arbitration`, `post_vector`, `app_render`, `on_commit`). Core pipeline always runs; modules are subordinate and cannot override Rules_Index, prism law, or age invariants. Core ships with an empty active module registry.

---

## Quick start (drafting)

1. Load `Framework/Main.md` + `CognitivePipeline.md` + `Rules_Index.md` + `Psychology/realm_data.yaml`
2. Load on-scene character cards and their `_log.yaml` overlays
3. Run ledger integrity pass; execute movement brief through the pipeline
4. Render clean prose; on approval, commit durable fields to the log

## Quick start (RP)

1. Paste `Simulator/CharacterRuntime.md` into a chat host
2. Load a character pack (card + log)
3. Play; use `/state`, `/save`, `/adult` (host depiction ceiling toggle) as needed

## Deploy to other book folders

From this repository:

```bash
python scripts/run.py deploy              # interactive
python scripts/run.py deploy MyBookName   # named target under parent dir
```

Deploy ships the pipeline, schema, Main, Rules, realm data, simulator, scripts, and mechanics craft files.

---

## License & disclaimer

- Software utilities (`.py`): **MIT**
- Framework specs / markdown: **CC BY-SA 4.0** — see [LICENSE.md](LICENSE.md)
- Compliance and 18+ terms: [DISCLAIMER.md](DISCLAIMER.md)

Author-local cast files and private simulator sessions stay private (see LICENSE §3 and `.gitignore`).
