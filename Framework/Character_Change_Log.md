---
generated_from: Characters/*_log.yaml
generated_at: 2026-07-23T00:00:00Z
schema_version: 1
---

# Character Change Log
*Matrix evolution ledger — consolidated quick reference for the author.*

**Individual logs** (`Characters/[slug]_log.yaml`) are the **durable** mutable runtime state (focus, weights, skills, memories, history, relational baselines). **Live** per-tick snapshots follow `Framework/Schemas/psychosomatic_state.json` and are owned by the Cognitive Pipeline — they are not a second durable source of truth. **YAML always wins:** If this consolidated Markdown file differs from an individual YAML log, the YAML log wins and this consolidated file is regenerated.

**This file** is a generated, human-readable quick reference projection for all character snapshots and history. Routine post-movement saves should update the individual log files and regenerate or synchronize this consolidated log as part of the Post-Movement State Commit.

Do not write `transformation_history` (or movement-by-movement deltas) onto character cards.

**Session boot:** Main.md **Ledger Integrity Pass** runs first. Honest empty History is valid; empty Snapshot is not (seed from cards). Placeholder Continuity rows must not leave History “pending.”

---

## Post-Movement State Commit

On **every approved movement**, execute the Post-Movement State Commit:
1. Write story continuity to `Framework/Continuity_Ledger.md`.
2. Update canonical per-character runtime state (`Characters/[slug]_log.yaml`).
3. Regenerate or synchronize this consolidated human-readable log (`Framework/Character_Change_Log.md`).

| Save | File | Owns |
|:---|:---|:---|
| **Story ledger** | `Framework/Continuity_Ledger.md` | Day/time, draft path, **scene** somatic close, plot/continuity beats |
| **Character log** | `Characters/[slug]_log.yaml` | Durable Focus/weight/somatic/bias-strength evolution + history of pressure events |
| **Consolidated log** | This file | Regenerated human-readable snapshot and history reference for all characters |

- Continuity_Ledger without character logs = incomplete matrix continuity.
- Character logs without Continuity_Ledger = incomplete scene continuity.
- Character cards are **not** the change log. Optional rare card rewrite only if the author permanently retires an identity field (e.g. renamed bias, rebuilt voice) — not routine post-movement work.
- Temporary tells that will decay: Continuity_Ledger close only. Do not invent permanent rows here.
- Medium / High / Extreme pressure or any permanent shift: **must** update Current Snapshot + append a Movement History entry (in `_log.yaml` and mirrored here). Missing rows after such pressure = failed commit.

### Load order (next design/draft)
0. **Ledger Integrity Pass** (Main.md) — clean empty/placeholder ledgers first
1. On-scene character cards (identity, voice, bias name, build defaults)
2. **Durable runtime state:** per-slug `_log.yaml` snapshot (overrides card Focus / weights / baseline somatic / bias_strength when present). Live ticks: pipeline snapshot schema.
3. Continuity_Ledger latest **real** row (scene time, props, close body state)

### Integrity notes for this file
| Condition | Handle |
|:---|:---|
| Snapshot empty | Seed from active cards (`As of: build`) |
| History empty, no Continuity rows | OK — do not invent entries |
| Continuity has committed rows, History missing those movements | Backfill or block draft |

---

## Current Matrix Snapshot
*Overwrite cells when a durable change commits. `As of` = last movement that wrote this character. Seed one row per active character from card build defaults when the cast is created.*

| Character | Active Focus | Latent weights | Bias strength | Default somatic | Flexibility | As of |
| :--- | :--- | :--- | :---: | :--- | :---: | :---: |
| Cass | IV — Will | I:5 II:10 V:5 VIII:5 | 70 | Still posture; unhurried movements; level gaze; hands folded loosely | 35 | build |
| Helen | VI — Compassion | II:10 IV:10 VIII:10 | 80 | Chest soft; open hands; sudden inhale; weight toward other; close proximity | 50 | build |
| Lior | IX — Threshold Fear | I:5 II:10 III:5 | 75 | Lilt in voice; fingers trembling; rapid shallow breathing; wide sight focus | 65 | build |
| Nora | VI — Compassion | I:10 II:10 VII:10 | 65 | Warm touch; chest breathing; eyes scanning faces; jaw soft | 55 | build |
| Reed | VIII — Integration | I:10 II:15 VII:10 | 75 | Throat tight; shoulders high; chest breathing; jaw locking | 30 | build |
| Wren | VII — Presence | I:15 II:15 VI:10 | 65 | Physical stillness; sight landing without attachment; loose jaw | 60 | build |

---

## Movement History
*Append a section per approved movement. One table row per on-scene character who had pressure or durable change; or a single “No durable matrix change” note.*

### Template (copy per movement)

```markdown
### [Ch] M[#] — [optional title]
| Character | Pressure | Delta | Permanence | Notes |
| :--- | :--- | :--- | :--- | :--- |
| [Name] | Emotional/High | bias_strength +10; default somatic → jaw lock baseline | permanent | [optional] |
| [Name] | — | none | temporary | Close state only → Continuity_Ledger |
```

### Entries

*(no approved movements)*
