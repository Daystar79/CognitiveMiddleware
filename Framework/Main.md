# MAIN — CognitiveMiddleware (Psyche Matrix)
*System: CognitiveMiddleware · Runtime: Psyche Matrix · Host: BookOS · Apps: Roleplay Engine & Character Simulator*

---

## LOAD PROTOCOL
- **Always (draft/design/cleanup):** `Main.md`, `Rules_Index.md`, `realm_data.yaml`, on-scene character cards (`Characters/`), per-character logs (`[slug]_log.yaml`), `Continuity_Ledger.md`, `Modules.md`.
- **Optional (as needed):** `Character_Change_Log.md`, `natural_prose.md` (Style = `natural` only), `Mechanics/prose.md`, `Mechanics/voices.md`, `Mechanics/humanity.md`.
- **Never load in context:** `source_changes.md`, `formatting_rules.md`, `Framework/Prompts/*`, stubs (`psyche_framework.md`, `Drafting_Workflow.md`), unneeded demo cards.

---

## CANONICAL STATE DECLARATION
- **Canonical mutable runtime state:** `Characters/[slug]_log.yaml`
- **Generated human-readable projection:** `Framework/Character_Change_Log.md`
- **Conflict rule:** If the consolidated Markdown differs from an individual YAML log, the YAML log wins and the consolidated file is regenerated. Every runtime manifest must load the individual YAML.

---

## MODULE VERIFICATION PROTOCOL
When this framework is loaded, verify all active modules:
1. **Index Scan:** Check `Framework/Modules.md` for modules marked `ENABLED`.
2. **Compatibility:** Verify no conflict with `Rules_Index.md` or other modules.
3. **Core Supremacy:** No module overrides `Rules_Index.md` or core logic in `Main.md`. Core rules take absolute precedence.

---

## LEDGER INTEGRITY PASS (Pre-session)
*Run before movement brief, Q&A, or prose. If blocked, output: `Ledger integrity: blocked — [what]` and stop.*

1. **Continuity_Ledger (`Framework/Continuity_Ledger.md`):**
   - *Placeholder rows:* Remove immediately (honest empty = 0 data rows).
   - *Missing row for `draft_chapter_*`:* Backfill from prose or block draft of next movement.
   - *Row with missing draft:* Delete row or mark `orphan` (do not invent prose).
   - *Change log pending commit:* Complete `_log.yaml` write or keep blocked.
2. **Character Logs (`Characters/[slug]_log.yaml`):**
   - *Missing/empty snapshot:* Seed snapshot from card defaults (`as_of: build`) using `_log_template.yaml`.
   - *Unsynced ledger rows:* Backfill matching `_log.yaml` history entries + update snapshot.
   - *Empty project history:* OK — honest empty; do not invent history.
3. **Consolidated Log Integrity:** Match `Character_Change_Log.md` snapshots against `_log.yaml`. If stale, regenerate from YAML.
4. **Gates:**
   - **CLEAN / CLEAN (empty):** Proceed to design/draft.
   - **BLOCKED (orphan drafts, pending commit, lag):** Resolve issues on disk; do not generate prose.

---

## ENGINE INVARIANTS
- **Execution Scope:** Active when `Main.md` is in context.
- **Execution Order:** MUST follow sequence: Load Stack → Ledger Integrity Pass → Design / Draft.
- **NEVER Output:** CONFIG cards, matrix notes, boot banners, debug dumps, or bracketed somatics `[tell]`.
- **MUST Output:** Clean manuscript prose only during drafting.

---

## DRAFTING WORKFLOW CONSTRAINTS
- **Design:** Q&A, lock canon, generate Movement Brief (pasted into `Drafting_Prompt.md`).
- **Draft:** MUST write one movement using ONLY Brief + preceding reads. NEVER invent canon mid-draft.
- **Preceding Read Invariants:**
  - Ch. N, M1: MUST read last movement of Ch. N-1.
  - Ch. N, M2+: MUST read all prior movements in Ch. N.

---

# PSYCHE MATRIX CORE

## Embodiment Baseline → Runtime Filters

**The body sets the baseline. Runtime filters shape the baseline. Only filtered results appear on-page.**

Pipeline is ALWAYS ON. Core middleware — not an optional module. Does NOT authorize erotic scene craft unless erotica module is `ENABLED`.

### 1) Body baseline (from card)
- **Physical instrument:** MUST load size, strength, reach, voice load, fatigue, injury, age, sensory bandwidth from `physical`.
- **Full-Body Cascade Invariant:** Somatic reactions MUST NOT be restricted to isolated facial/hand ticks (e.g., just a jaw twitch). Every state shift MUST engage a multi-zone anatomical cascade across at least **2 interconnected body zones** (e.g. Cranial + Pelvic, Respiratory + Peripheral).
- **Sexed / hormonal baseline:** Treat as **tendency and capacity** only; NEVER as finished personality or gender script.
- **Ambient valuation:** Continuous low-amplitude attraction/aversion/neutral read. Default amplitude MUST remain low (notice, not narration).
- **Invariance:** Baseline is **silent math**. NEVER dump hormones or sexual labels into prose.

### 2) Runtime filters (shape baseline)
Apply in strict stack order. Later layers MAY suppress, redirect, invert, or amplify earlier drive:

| Layer | Source | Mandatory Effect on Baseline |
|:---|:---|:---|
| **Culture / era / morals** | Cultural Bias, temporal awareness | Binds what is allowed, shameful, sacred, invisible |
| **Occupation / role** | Card occupation | Directs staging focus, tool habits, status reflexes |
| **Personality / Focus** | Active Focus + latents | Assigns body zone and social stance carrying charge |
| **Belief & voice** | Card voice, hard_bans, history anchors | Sets absolute prohibitions on speech and action |
| **Experience / memory** | Epistemic memory + log snapshot | Applies learned caution, hunger, numbness, restraint |
| **Cognitive Bias / Gift** | When `DEFENSIVE_ACTIVE` or `GENERATIVE_ACTIVE` | Warps how attraction/threat/need is received (Prism) |
| **Scene pressure** | Brief + ledger close | Restricts what is physically possible this movement |

### 3) Output Constraints
- On-page prose MUST show **filtered full-body behavior and somatics only** (2+ linked zones per state shift).
- **No Default Eroticization:** Baseline and ambient valuation NEVER force sex, romance plots, or explicit description. Ordinary scenes MUST stay ordinary unless Movement Brief requires intimacy AND erotica module is `ENABLED`.
- **Card Supremacy:** Card instance ALWAYS overrides generic stereotypes. NEVER apply generic gender scripts.

### 4) Speech as Behavioral Action (Syntactical Speech Engine)
Speech is an active somatic and psychological choice. MUST enforce syntactical constraints:

| Driver | Condition / Trigger | Mandatory Syntactical Constraint |
|:---|:---|:---|
| **Somatic Vocal Mapping** | Realm II (Form) | MUST output clipped, precise, short declarative sentences; REFUSE filler words. |
| **Somatic Vocal Mapping** | Realm IV (Will) | MUST output low pitch, measured heavy beats; MUST interrupt; unyielding rhythm. |
| **Somatic Vocal Mapping** | Realm VI (Compassion) | MUST output breathy register, soft verbal buffers, expanded turn lengths. |
| **Somatic Vocal Mapping** | Realm IX (Threshold) | MUST output halted delivery, tense pauses, thinning vocal timbre, gasping fragments. |
| **Verbal Defense / Stance** | `DEFENSIVE_ACTIVE` / `GENERATIVE_ACTIVE` | IF `DEFENSIVE_ACTIVE` → MUST apply `verbal_defense`. IF `GENERATIVE_ACTIVE` → MUST apply `generative_stance`. |
| **Space Control** | `conversational_stance` | Dominant MUST interrupt & claim space; Yielding MUST surrender floor & use dry monosyllables. |
| **Relational Shift** | `relational_verbal_shifts` | MUST modify cadence per target; NEVER use identical speech patterns for two interlocutors. |

## Tripartite Filtering Model
1. **Permanent World-Filters (Always On):** Cultural Bias (metaphysics/taboos) + Occupation (lexicon/staging).
2. **Dynamic Intercept Filter (Triggered):** Dual-Aspect Intercept — Cognitive Bias (Wound) & Cognitive Gift (Virtue/Anchor).
   - Default state: `DORMANT`.
   - Under threat, trauma cues, or defensive pressure → resolves to `DEFENSIVE_ACTIVE` (Wound).
   - Under safety, trust, creative flow, or moral alignment → resolves to `GENERATIVE_ACTIVE` (Gift).
3. **Dynamic Focus:** Auto-shifts mid-scene UNLESS `Focus Lock = LOCKED`.
4. **Focus Lock:** Brief → `LOCKED`; `/focus unlock` → auto-shift resumes.
5. **Bias State Invariant:** Default `DORMANT`. Resolves to `DEFENSIVE_ACTIVE` or `GENERATIVE_ACTIVE` under relevant pressure/safety. MUST return to `DORMANT` after sustained low-stakes beats.
6. **Focus Invariant:** Focus shifts NEVER auto-change Bias State.
7. **Somatic Invariant:** Every Focus/Bias/Gift transition MUST somaticize physically (body first); NEVER name labels.

## Epistemic Memory & Skill Constraints

### Memory Recall Invariants
| Condition | Recall State | Mandatory Output Constraint |
|:---|:---|:---|
| Event in `memories.detailed` | **Sharp Subjective** | MUST apply subjective recall context & somatic triggers to active Prism distortion. |
| Event in `memories.footnote` | **Vague Footnote** | MUST deflect/act unsure/change subject UNLESS active scene trigger dereferences footnote. |
| Event in neither list | **Forgotten** | MUST treat as zero awareness; NEVER recall details. |

### Skill Execution Invariants
| Competence Tier | Execution Profile | Mandatory Output Constraint |
|:---|:---|:---|
| `skills.active` | **Fluid / Mastery** | MUST show muscle memory & precise lexicon; MUST output somatic release tells. |
| `skills.latent` | **Frictional** | MUST show physical fumbles (dropping tools, re-measuring) & bracing tells. |
| Untrained (neither) | **Uncapable** | MUST express helplessness or request aid; NEVER perform cleanly. |

## Prism Intercept Engine (ACTIVE State)
1. **Input Landing:** Latent skill, speech, or sensory fact received.
2. **Intercept Processing:**
   - **Defensive Prism (`DEFENSIVE_ACTIVE` - Wound):** Active Focus + Bias rewrites input to confirm wound. Warps speech into critique, threat, demand, salvage task, constraint, or dissolution invitation (**Misconstrued Hearing**).
   - **Generative Prism (`GENERATIVE_ACTIVE` - Gift):** Active Focus + Gift reframes input into opportunity, resonance, protective strength, or deep connection (**Resonant Hearing**).
3. **Behavioral Output:** Show warped or resonant reception strictly through somatic posture and speech cadence; NEVER label the engine state.

## Great Wheel (10 Realms)
Use `realm_data.yaml` for brace/release/somatic per realm. NEVER name realm numbers on-page.

| Zone | Realms | Core Job |
|:---|:---|:---|
| **Internal I-V** | Origin, Form, Identity, Will, Echoes | Self-framing and bracing |
| **External VI-X** | Compassion, Presence, Integration, Threshold Fear, Return | Self meeting world |

NEVER write finished Realm X Passage unless scene earns open hands without performance.

## Transformation Engine
Characters evolve or regress dynamically based on narrative pressure.
- **Pressure Types:** Emotional, Somatic, Cognitive, Social, Esoteric/Ritual + strength (`Low` / `Medium` / `High` / `Extreme`).
- **Weighted Delta:** Aligned pressure eases shifts (+10–20 weight). Opposed pressure causes resistance or temporary somatic backlash.
- **Decay & Permanence:** Temporary shifts MUST decay over 1–3 movements unless reinforced. Medium/permanent shifts MUST record in `[slug]_log.yaml` at Post-Movement State Commit.
- **Somatic Precedence:** Transformations MUST manifest on-page physically BEFORE any internal cognitive realization.

---

### Character Log Write-Back Invariants (Post-Movement Commit)
Upon movement approval, update `Characters/[slug]_log.yaml`:
1. **Metadata:** MUST update revision keys and increment revision post-write (`schema_version: 1`, `revision: N`, `updated_at`, `last_commit_id`).
2. **Snapshot:** MUST update `active_focus`, `latent_weights`, `bias_strength`, `default_somatic`, `flexibility`.
3. **Temporary Effects:** MUST decrement `remaining_movements` by 1 after each scene appearance. MUST purge expired.
4. **History:** MUST append entry for Medium+ pressure (`movement`, `pressure`, `delta`, `permanence`, `notes`).

---

# ARCHETYPES, BIAS & GIFT CATALOG

| ID | Name | Focus | Latents | Bias (Wound) | Gift (Virtue / Anchor) |
|:---|:---:|:---:|:---|:---|:---|
| **A** | Concrete Voice | 8 | 1, 2, 7 | Debt Ledger | Sacred Stewardship |
| **B** | Caregiver | 6 | 2, 4, 8 | Saviour Complex | True Sanctuary |
| **C** | System Architect | 4 | 1, 2, 5, 8 | System Architect | Illuminated Symmetry |
| **D** | Mirror Reflector | 7 | 1, 2, 6 | Mirror | Resonant Truth |
| **E** | Insulation Anchor | 6 | 1, 2, 7 | Insulation | Sanctuary Bridge |
| **F** | Threshold Seeker | 9 | 1, 2, 3 | Dissolution | Threshold Vision |

| Aspect | Typical Focus | Defensive Trigger (`DEFENSIVE_ACTIVE`) | Defensive Hearing Warp | Generative Trigger (`GENERATIVE_ACTIVE`) | Generative Hearing Warp | Somatic Tells (Brace vs. Expansion) |
|:---|:---|:---|:---|:---|:---|:---|
| **Debt Ledger / Sacred Stewardship** | VIII | Vulnerability, affection, rest | Kindness = bill due / debt | Shared trust, communal craft | Generosity = shared stewardship | Tight throat, jaw lock *(Brace)* vs. Chest drops, open breath *(Expansion)* |
| **Saviour Complex / True Sanctuary** | VI | Another's raw pain or need | Need = assignment / obligation | Safe emotional bounds, mutual agency | Presence = quiet refuge without ownership | Soft chest, rapid inhale *(Brace)* vs. Grounded posture, calm gaze *(Expansion)* |
| **System Architect / Illuminated Symmetry** | IV | Emotion, chaos, intimacy | Feeling = load/structure failure | Collaborative problem-solving | Complexity = potential for elegant order | Still posture, folded hands *(Brace)* vs. Fluid gestures, steady vocal pitch *(Expansion)* |
| **Mirror / Resonant Truth** | VII | Collision, strong external want | Desire = vanish into interlocutor | Unconditional acceptance, authentic bond | Reflection = revealing truth while whole | Stillness, loose jaw *(Brace)* vs. Level stance, distinct voice cadence *(Expansion)* |
| **Insulation / Sanctuary Bridge** | VI | Outside pressure on the bond | Outside = threat to bond | Shared sanctuary, allied strength | Perimeter = protective refuge for all | Warm touch, micro-scans *(Brace)* vs. Expansive posture, unhurried voice *(Expansion)* |
| **Dissolution / Threshold Vision** | IX | Performance/exposure fear | Invitation = disappear / exit self | Safe creative/spiritual edge | Vulnerability = portal for artistic breakthrough | Lilt, tremor, shallow breath *(Brace)* vs. Clear vocal timbre, centered stance *(Expansion)* |

---

# EXECUTE ON MOVEMENT (Pipeline Constraints)

| Step | Target | Operation Type | Mandatory Pipeline Constraint |
|:---:|:---|:---|:---|
| **0** | Ledger Integrity | Pre-flight Check | MUST confirm status is `CLEAN`; STOP if `BLOCKED`. |
| **1** | Load Manifest | Context Load | MUST load brief, preceding read, active cards, logs, rules, enabled modules. |
| **2** | Body Baseline | Silent Compute | MUST calculate physical capacity & ambient valuation; KEEP amplitude low. |
| **3** | Runtime Filters | Silent Compute | MUST apply culture → occupation → Focus → belief/voice → memory → scene pressure/safety. |
| **4** | Focus State | Dynamic Shift | IF `Focus Lock = UNLOCKED` → MAY shift Focus based on pressure; ELSE keep locked. |
| **5** | Bias State | Mode Resolution | Resolve `DORMANT`, `DEFENSIVE_ACTIVE`, or `GENERATIVE_ACTIVE`; MUST revert to `DORMANT` after low stakes. |
| **6** | Somatic Precedence | Narrative Output | MUST output multi-zone physical reaction (2+ linked body zones) BEFORE cognitive realization; NO brackets. |
| **7** | Prism Intercept | Narrative Output | IF `DEFENSIVE_ACTIVE` or `GENERATIVE_ACTIVE` → MUST apply corresponding Prism warp; NEVER label. |
| **8** | Modules | Optional Craft | Apply ENABLED module parameters ONLY where brief engages them; NEVER override core bans. |
| **9** | Transformation | Silent Compute | Calculate deltas silently during generation; NO inline logs. |
| **10** | Hard Bans | Output Hygiene | MUST enforce `Rules_Index.md` (no matrix jargon, 100% off-page). |
| **11** | Commit | State Commit | On approval: MUST write `Continuity_Ledger` + `_log.yaml` + regenerate markdown. |

---

*Install once per book project. Load for draft sessions. Execute on movement/scene creation. Never print the runtime on the page.*
