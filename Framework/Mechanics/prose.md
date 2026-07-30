---
title: "Prose Protocol"
description: "Optional detail pack governing session-level prose styles and selection/lock states."
type: "supplementary_protocol"
role: "Prose style catalog and selection lock state machine"
load_protocol: "Load when styling overrides or catalog auditing are needed"
---

# Prose Protocol
*Optional detail pack. Session defaults and lock-on-select also live in [Main.md](../Main.md) §3a. Load this file only when you need the full catalog/state machine.*

> [!IMPORTANT]
> **Prose style is user-selected.** Do not force the house "Natural / asymmetric" pack (Anthony/Barker lane) unless chosen.  
> **Default = `llm`** (model fluent prose), status **unlocked** until the writer makes an explicit style choice.  
> **Once the writer selects a style, it LOCKS** for the rest of the session (or until explicit unlock / full reset).

Psychology (matrix, voice, somatics) stays in force regardless of style. Style only changes **how the narrative is written**, not who the character is.

---

## Related

- **Drafting entry:** [Main.md](../Main.md)
- **Natural / asymmetric pack (optional):** [natural_prose.md](../natural_prose.md)
- **Card-building voices:** [voices.md](./voices.md)
- **Hard bans:** [Rules_Index.md](../Rules_Index.md)

---

## 1. DECLARATIVE PROSE STYLE INVARIANTS

| Rule ID | Constraint Type | Target Scope | Mandatory Pipeline Constraint |
|:---:|:---:|:---|:---|
| **PRS-01** | **INVARIANT** | Session Scope | Prose style is session-wide; changing active character MUST NOT change active prose style. |
| **PRS-02** | **INVARIANT** | Default Initializer | MUST initialize session at `Prose Style = llm`, `Style Lock = UNLOCKED` unless brief specifies style. |
| **PRS-03** | **PRECEDENCE** | Explicit Lock Supremacy | Explicit style selection (`/style <id>` or brief) MUST immediately set `Style Lock = LOCKED`. |
| **PRS-04** | **NEVER** | Silent Drift | WHILE `Style Lock = LOCKED`: NEVER permit model drift toward natural, literary, or custom texture. |
| **PRS-05** | **MUST** | Auto-Lock Trigger | IF `Style Lock = UNLOCKED` after first movement: MUST auto-set `Style Lock = LOCKED` to active style. |
| **PRS-06** | **INVARIANT** | Module Loading | IF `Prose Style = natural`: MUST load `natural_prose.md`. IF `llm`: MUST NOT load `natural_prose.md`. |

---

## 2. SELECTION & LOCK STATE MACHINE CONSTRAINTS

| Event / Trigger | Pre-Condition | Action / State Delta | System Output Constraint |
|:---|:---|:---|:---|
| **Session Start** | No prior state | Set `Style = llm`, `Lock = UNLOCKED` | Silent state initialization. |
| **Brief Specification** | Brief contains `Prose Style: <id>` | Set `Style = <id>`, `Lock = LOCKED` | System note: `Style locked: <id>`. |
| **Command `/style <id>`** | Any state | Set `Style = <id>`, `Lock = LOCKED` | System note: `Style locked: <id>`. |
| **Drift Request** | `Lock = LOCKED` | REJECT change; maintain active style | Output refusal: `Style is locked (<id>). Use /style unlock.` |
| **Command `/style unlock`** | `Lock = LOCKED` | Set `Lock = UNLOCKED`; keep active style | System note: `Style unlocked.` |
| **First Turn Auto-Lock** | `Lock = UNLOCKED` post-turn 1 | Set `Lock = LOCKED`; keep active style | System note: `Style auto-locked to <id>.` |

---

## 3. Style catalog

| ID | Name | When to use | Engine notes |
|:---|:---|:---|:---|
| **`llm`** / **`default`** | Model default | Ordinary LLM fluency | No house-style constraints. Clear, competent narrative. Still honor character voice + matrix. |
| **`natural`** | Natural / asymmetric (house) | Anti-AI texture: jagged rhythm, drift, fumble, anti-synthesis | **Load full** [natural_prose.md](../natural_prose.md). Anthony/Barker-adjacent — optional, not automatic. |
| **`clean`** | Clean commercial | Genre readability | Short–medium sentences, clear beats, light sensory, minimal figurative density. |
| **`literary`** | Literary lyrical | Interior, image-led | Longer cadence allowed; image and motif; still no therapy summary endings unless user asks. |
| **`hardboiled`** | Hardboiled / lean | Crime, noir pressure | Spare verbs, concrete nouns, dry understatement, minimal adverb. |
| **`cinematic`** | Cinematic | Scene-as-shot | Visual framing, cut-friendly paragraphs, external action over interior essay. |
| **`minimal`** | Minimal | Extreme restraint | Short lines, white space, almost no figurative language. |
| **`romantic`** | Warm romantic | Soft heat, non-explicit by default | Gesture and timing; avoid purple metaphor stacks. |
| **`custom`** | User-defined | User pastes a style brief | Follow their brief only; do not re-impose `natural` rules. |

Aliases:

- `default`, `normal`, `standard`, `model` → **`llm`**
- `house`, `asymmetric`, `anthony`, `barker`, `anthony/barker`, `anti-ai` → **`natural`**
- `noir`, `lean` → **`hardboiled`**
- `film`, `screen` → **`cinematic`**
- `sparse` → **`minimal`**

---

## 4. What always stays on (style-invariant)

| Layer | Stays on? |
|:---|:---|
| Character card / Focus / Bias / Prism | Yes |
| Character dialogue voice (A–F / card) | Yes |
| Canon Adult / 18+ gate | Yes |
| Never name realm/bias/trauma in character | Yes |
| Humanity: imperfect recall, biased hearing (if protocol loaded) | Yes |
| `natural_prose.md` jagged / fumble / anti-synthesis rules | **Only if style = `natural`** |
| Style lock once set | Yes, until unlock / force / reset |

---

## 5. Drafting vs chat RP (style)

| Context | Style control |
|:---|:---|
| **Drafting** ([Main.md](../Main.md)) | Brief or `/style` sets style → **LOCKED** for the pass |

### Output (drafting vs chat RP)

| Context | Somatics | Debug / matrix |
|:---|:---|:---|
| **Drafting** ([Main.md](../Main.md)) | Fold into narrative. **No brackets.** | **Never** print CONFIG, matrix notes, audit tables, or engine labels |

**Hard ban:** Do not dump turn-loop state, Focus/Bias labels, "Prism intercept", remnant/passage jargon, or post-scene matrix footnotes into draft files.

---

## 6. Commands / brief lines

```
/style llm              → set llm, LOCK
/style natural          → set natural, LOCK
/style hardboiled       → set hardboiled, LOCK
/style custom: …        → set custom brief, LOCK
/style unlock           → UNLOCK (style ID unchanged)
/style force cinematic  → set cinematic, stay LOCKED
/style                  → report current style + lock state
```

Drafting brief:

```
Prose Style: natural
Style Lock: LOCKED
```

---

## 7. Audit

1. What style is active, and is it **LOCKED**?
2. If LOCKED, refuse silent restyle; require unlock or force.
3. If `llm` → do **not** rewrite toward natural/asymmetric or any other style pack.
4. If `natural` → apply [natural_prose.md](../natural_prose.md) fully.
5. If UNLOCKED → maintain current style's characteristics; no drift toward any style pack.
6. After first character response with UNLOCKED style → verify auto-lock occurred.
7. Character voice fidelity is audited separately from prose style.
