# MAIN — Book Writing Layer (Manuscript Engine)
*System: CognitiveMiddleware · Role: Novel Drafting & Prose Rendering Engine · Host: BookOS*

---

## 🏛️ ARCHITECTURE & RESPONSIBILITIES

The **Book Writing Layer** is the manuscript generation engine. It consumes the output vector from the [Cognitive Pipeline](CognitivePipeline.md) (`Feels`, `Thinks`, `Says`, `Does`) and renders it into clean, immersive, publication-ready prose.

```
 🧠 COGNITIVE PIPELINE (State & Behavior Predictor)
                       │
                       ▼ (Outputs: Feels, Thinks, Says, Does + psychosomatic_state.json)
 📖 BOOK WRITING LAYER (Main.md)
   ├── Enforces Prose Style Locks (natural, llm, historical, etc.)
   ├── Applies Output Hygiene & Anti-Synthesis Paragraph Endings
   ├── Maintains Ledger Integrity (Continuity_Ledger.md & character logs)
   └── Generates Clean Manuscript Prose (100% Off-Page Matrix)
```

---

## LOAD PROTOCOL
- **Always (drafting/design):** `Main.md`, `CognitivePipeline.md`, `Rules_Index.md`, `realm_data.yaml`, on-scene character cards (`Characters/`), `[slug]_log.yaml` (or `psychosomatic_state.json`), `Continuity_Ledger.md`, `Modules.md`.
- **Optional:** `Character_Change_Log.md`, `natural_prose.md` (Style = `natural`), `Mechanics/prose.md`, `Mechanics/voices.md`, `Mechanics/humanity.md`.
- **Never load in context:** `source_changes.md`, `formatting_rules.md`, `Framework/Prompts/*`, debug dumps.

---

## CANONICAL STATE DECLARATION
- **Canonical mutable runtime state:** `Characters/[slug]_log.yaml` and `Framework/Schemas/psychosomatic_state.json`.
- **Generated projection:** `Framework/Character_Change_Log.md`.
- **Rule:** Machine JSON/YAML state wins in state conflicts; human-readable Markdown is regenerated from state.

---

## LEDGER INTEGRITY PASS (Pre-session)
*Run before movement brief or drafting.*

1. **Continuity_Ledger (`Framework/Continuity_Ledger.md`):**
   - Verify chapter and movement rows.
   - Ensure clean state commit before generating next movement.
2. **Character Logs (`Characters/[slug]_log.yaml`):**
   - Load latest snapshot overlaying card build defaults.
3. **Gates:**
   - **CLEAN:** Proceed to draft movement.
   - **BLOCKED:** Resolve ledger lag before generating prose.

---

## DRAFTING WORKFLOW & PROSE RENDERING PIPELINE

When executing a Movement Brief:

| Step | Target | Operation | Description |
|:---:|:---|:---|:---|
| **1** | Cognitive Simulation | Query Pipeline | Receive predicted 4-channel vector (`Feels`, `Thinks`, `Says`, `Does`) from [CognitivePipeline.md](CognitivePipeline.md). |
| **2** | Body Precedence | Narrative Placement | Render physical somatic cascades into narrative **before** or folded into speech and action; never use bracketed `[tell]`. |
| **3** | Dialogue Rendering | Voice Fidelity | Render character speech preserving unique idiolect, speech clipping, and asymmetry (talking past each other, trailing off). |
| **4** | Style Lock | Prose Enforcement | Enforce target prose style (`natural`, `cinematic`, `historical`); prohibit purple prose and AI clichés. |
| **5** | Anti-Synthesis | Paragraph Closure | Ensure paragraphs close on concrete sensory facts, raw actions, or unanswered dialogue—**never** on interpretive summary. |
| **6** | Output Hygiene | Off-Page Verification | Enforce hard bans in `Rules_Index.md` (strip system jargon: `Realm [N]`, `DEFENSIVE_ACTIVE`, `Debt Ledger`, `trauma`). |
| **7** | Commit Pass | State Commit | On movement approval, write updated state to `_log.yaml` / `psychosomatic_state.json` and update `Continuity_Ledger.md`. |

---

## HARD INVARIANTS FOR DRAFTING
- **Clean Manuscript Only:** Output contains ONLY manuscript prose during drafting. NEVER append CONFIG cards, audit tables, or debug banners.
- **100% Off-Page Matrix:** Framework terms (`Focus`, `Bias`, `Gift`, `Prism`, `Realm`) stay strictly off-page.
- **Card Supremacy:** Card baseline always overrides generic AI tropes.

---

*Loaded for manuscript drafting sessions. Executes on Movement Briefs.*
