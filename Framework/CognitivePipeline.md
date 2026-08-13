# Cognitive Pipeline Specification
*Psychosomatic simulation & behavior prediction engine · CognitiveMiddleware · Version 2.1*

---

## 1. Purpose

The **Cognitive Pipeline** is the psychological / physical runtime for a character. It models mind-body neurobiology, subconscious perception, relational dynamics, and behavior intent.

It is **application-agnostic**: the same pipeline serves manuscript drafting (`Main.md`) and interactive RP (`Simulator/CharacterRuntime.md`).

### Downstream decoupling contract
| Pipeline owns | Pipeline does **not** own |
|---|---|
| Autonomic reaction, affect, prism, priority arbitration | Manuscript prose style, anti-synthesis, style locks |
| 4-channel intent vector (`Feels` / `Thinks` / `Says` / `Does`) | Chat UI, OOC commands, turn-taking presentation |
| Active volition, goal-driven inquiry, probing interlocutor motives | Continuity ledger chapter rows, draft file I/O |
| Live psychosomatic snapshot (schema below) | Optional craft guides under `Mechanics/` |
| Somatic catalog lookup from `realm_data.yaml` | |

---

## 2. Required inputs (must load before a tick)

| Input | Path | Role |
|---|---|---|
| **This spec** | `Framework/CognitivePipeline.md` | Execution sequence & commit rules |
| **Realm somatics** | `Framework/Psychology/realm_data.yaml` | Brace / release body catalogs per realm |
| **Character card** | `Characters/[slug].md` | Identity, voice, build defaults, wound/gift, weights |
| **Durable log** | `Characters/[slug]_log.yaml` | Runtime evolution over card defaults |
| **Event trigger** | Movement brief / player turn / scene pressure | Sensory + social stimulus |
| **Schema** | `Framework/Schemas/psychosomatic_state.json` | Shape of the live snapshot |

### Modules (downstream injectors)
`Framework/Modules.md` is the **extension registry**. Downstream applications register modules there to inject into this loop at defined hooks (`pre_somatic`, `affect_filter`, `pre_arbitration`, `post_vector`, `app_render`, `on_commit`).

- Core sequence and state model always run.
- Only modules with Status `ENABLED` and a present file load.
- Modules are subordinate: they must not override Rules_Index, this pipeline’s invariants, card/log supremacy, or age gates.
- Full contract: [Modules.md](Modules.md).

### Card fields the pipeline reads
- `active_focus`, `latent_anchors` → realm keys into `realm_data.yaml`
- `transformation_weights` (or log overlay) → baseline drive weights & bias_strength
- `cognitive_bias` / `cognitive_gift` → prism rewrite rules (Wound / Gift)
- `default_somatic_alignment` → ambient body baseline
- `voice.*` → shapes `Says` (idiolect, defense, generative stance)
- `history_anchors` + log `memories.*` → epistemic gating
- `skills.active` / `skills.latent` (from log when present) → competence in `Does`
- `canon_adult` / `age` → hard eligibility for intimate affect (apps enforce presentation)

### Log overlay rule
When `Characters/[slug]_log.yaml` exists, **snapshot fields override card build defaults** for focus, latent weights, bias_strength, default somatic, flexibility, skills, and memories.

---

## 3. Unified state model

There is **one character runtime**, two layers of persistence:

| Layer | File | Lifetime | Owns |
|---|---|---|---|
| **Durable** | `Characters/[slug]_log.yaml` | Across movements / sessions | Focus, latent weights, bias_strength, skills, memories, history, relational baselines |
| **Live** | Conforms to `Schemas/psychosomatic_state.json` | One pipeline tick / turn | Autonomic scales, affect, active wound/gift state, relational vectors this beat, priority arbitration, 4-channel vector |

**Canonical rule:** Durable log wins for long-horizon continuity. Live snapshot is rewritten every tick. On **commit**, only durable-mapped fields merge into the log (see §8).

Card YAML is **build-time identity**, not mutable runtime. Never write evolution back into the card.

### Live snapshot location
Apps may:
1. Keep live state in working memory only, or
2. Write `Characters/[slug]_state.json` (optional, ephemeral), or
3. Embed the last live snapshot under `live:` in `_log.yaml` (optional; cleared or refreshed each commit)

All three must validate against `Framework/Schemas/psychosomatic_state.json`.

---

## 4. Neurobiological execution sequence

```
                      📥 Sensory Event / Input
                                 │
                                 ▼
                    ⚡ 1. NERVOUS SYSTEM REACTION
            (Visceral baseline, startle, heart rate, gut, Z1–Z6)
            [module hook: pre_somatic]
                                 │
                                 ▼
                    ❤️ 2. RAW AFFECTIVE IMPULSE
            (Un-thought urge: fear, arousal, anger, shock, warmth)
            [module hook: affect_filter]
                                 │
                                 ▼
                🧠 3. SUBCONSCIOUS INTERPRETATION (Prism)
         (Bedrock: Upbringing + Culture + Memory + Wound/Gift)
         (Active Drive: Motives + Relational Vector)
         ★ Core only — modules must not rewrite prism law
                                 │
                                 ▼
                 ⚖️ 4. DYNAMIC PRIORITY ARBITRATION
         (Drives compete; highest salience wins)
         [module hook: pre_arbitration — weights / context multipliers]
                                 │
        ┌────────────────────────┼────────────────────────┐
        ▼                        ▼                        ▼
 🫀 5a. FEELS             🧠 5b. THINKS            🗣️ 5c. SAYS & DOES
(Autonomic & Visceral)   (Internal Monologue)     (Active Volition & Stance)
         [module hook: post_vector — craft constraints on channels]
                                 │
                                 ▼
              📤 6. LIVE SNAPSHOT + APP RENDER
         [module hook: app_render — host presentation]
         [module hook: on_commit — after durable merge]
```

Body before insight: stages 1–2 complete before labeled cognition in stage 5b.  
Module hooks: see [Modules.md](Modules.md) §3.

---

## 5. Embodied cognition (mind-body unity)

1. **Somatic → Cognitive:** Fatigue, pain, gut drop, arousal, intercostal tension alter patience, risk tolerance, memory access, word choice.
2. **Cognitive → Somatic:** Wound/gift evaluations shift autonomic physiology immediately.
3. **Continuous loop:** Sensation and interpretation update each other within the tick.

### Anatomical cascades (6 zones)
Every state shift engages **at least 2 interconnected zones**:

| Zone | Examples |
|---|---|
| Z1 Cranial & Ocular | Temple pulse, jaw lock, blink rate, pupil focus |
| Z2 Vocal & Cervical | Larynx shift, swallow, corded neck |
| Z3 Thoracic & Respiratory | Sternum, intercostals, apex vs diaphragm breath |
| Z4 Abdominal & Visceral | Diaphragm catch, gut drop, solar plexus |
| Z5 Pelvic & Kinesthetic | Center of gravity, lumbar arch/slump, hip angle |
| Z6 Peripheral & Grounding | Toe curl, finger tremor, white knuckles, stride weight |

### Realm catalog lookup
1. Resolve `active_focus` → realm key (`I`…`X`) from card/log.
2. Load that realm block from `realm_data.yaml` (`micro` / `moderate` / `macro` / `release` + `vocal_behavior`).
3. Select intensity from live autonomic pressure (stress/arousal/pain thresholds).
4. Fold **2+** zone tells into `Feels` / `Does`; fold vocal_behavior into `Says`.
5. Latent anchors may leak secondary micro-tells under residual pressure — never name realm labels on-page.

---

## 6. Dynamic priority arbitration

At any moment, multiple internal drives carry baseline weights. Compute **salience** per drive:

$$\text{Salience} = (\text{Internal Intensity}) \times (\text{Context Multiplier}) \times (\text{Character Baseline Weight})$$

### Where numbers come from
| Term | Source |
|---|---|
| Internal Intensity | Live affective intensity + autonomic scales (0–100) |
| Context Multiplier | Trigger relevance to wound/gift/memory/skill (e.g. 0.5–2.0) |
| Character Baseline Weight | Card/log `transformation_weights` + active_focus weight + bias_strength |

### Arbitration rules
1. **Winning drive** = highest salience → primary `Says` & `Does`.
2. **Secondary drives** remain as subtext, hesitation, monologue friction, or opposing somatic tells.
3. **Instant shift** when a scale overflows (e.g. arousal > 80 or fear/stress > 80) — emergent priority lock change mid-beat.
4. **Volitional Drive & Active Inquiry:** Characters MUST NOT act as passive AI responders or reactive Q&A endpoints. Winning drives dictate active goals. The character MUST initiate active inquiries, test interlocutor motives, ask counter-questions back, or take unprompted physical/verbal actions rather than yielding conversational control.

Dual-aspect psyche:
- Wound path → `DEFENSIVE_ACTIVE` bias_state when context is wound-relevant.
- Gift path → `GENERATIVE_ACTIVE` when safety/trust/flow allows virtue lens.
- Otherwise → `DORMANT` (ambient personality only).

---

## 7. Relational model

Bonds are continuous multi-dimensional vectors in the **live** snapshot:

```json
{
  "relational_vector": {
    "target_id": "interlocutor_slug",
    "emotional_safety": 65,
    "attraction_physical": 80,
    "attraction_emotional": 40,
    "respect_competence": 90,
    "status_dynamic": "equals",
    "resentment_friction": 15,
    "perceived_reciprocity": {
      "perceived_liking": 50,
      "perceived_threat": 10
    },
    "relational_anchors": ["shared_secret_ch2"]
  }
}
```

Dynamics (examples):
- High physical attraction + high resentment → charged push-pull.
- High competence respect + low safety → crisp cooperation, tight boundaries.
- High attraction + high arousal + low resentment (no blocking wound) → spontaneous desire impulse.

Durable baselines for bonds live under `_log.yaml` → `relational_baselines`. Live vectors start from those baselines each session and may drift; commit writes durable shifts only on Medium+ pressure or explicit `/bond` / author approval.

### 7.1 Intimate & Sexual Stimulus Interpretation

Sex is not a special subsystem or separate operational mode—it is a class of stimulus processed through the standard pipeline sequence:

1. **Nervous System (Visceral/Zones):** Physical arousal, pulse, skin temperature, respiratory shift across Z1–Z6.
2. **Raw Affect:** Immediate visceral impulse (attraction, shock, discomfort, warmth, pull).
3. **Subconscious Prism:** Filtered through upbringing, memory, and wound/gift matrix. Sex is interpreted through character-specific meaning (e.g., debt, vulnerability, control, caretaking, threat, sacred connection, escape, or curiosity).
4. **Priority Arbitration:** Drive salience computation evaluating whether desire wins, freezes, deflects, approaches, or withdraws.
5. **Output Vector:** Emits character **stance and intent** (`Feels`, `Thinks`, `Says`, `Does`).

**North Star Rule:** The pipeline concludes how a person relates to and interprets intimate stimulus. Nothing in the core engine stages sex, details positions, or specifies explicit act mechanics. Explicit presentation belongs strictly downstream.

---

## 8. Output vector & commit protocol

### Live output (every tick)
Serialize a full snapshot matching `Framework/Schemas/psychosomatic_state.json`:

1. **`Feels`** — autonomic & multi-zone somatic manifestations  
2. **`Thinks`** — internal monologue after prism (not therapy labels)  
3. **`Says`** — dialogue intent, cadence, register, interruptions  
4. **`Does`** — posture, movement, spatial staging, object handling  

Apps render these channels into prose (drafting) or RP chat (simulator). Framework jargon never appears in rendered output.

### Commit mapping (movement approved / `/save` / scene close)

| Live field | Durable destination in `_log.yaml` |
|---|---|
| Winning focus / realm pressure outcome | `snapshot.active_focus`, `snapshot.latent_weights` |
| Sustained bias_strength change | `snapshot.bias_strength` |
| Permanent baseline body change | `snapshot.default_somatic` |
| Skill discovery / demotion | `skills.active` / `skills.latent` |
| Memory promotion (triggered → detailed) | `memories.detailed` / `footnote` |
| Relational baseline shift (Medium+) | `relational_baselines.[target]` |
| Tick narrative (Medium+ only) | append `history[]` |

Do **not** dump full live autonomic noise into history every beat. History records durable pressure events only.

After commit: regenerate human-readable projections (`Character_Change_Log.md`) from YAML. YAML wins conflicts.

---

## 9. Hard pipeline invariants

- **Volition & Inquiry invariant:** Characters MUST NOT act as passive AI responders or Q&A endpoints. Every turn must express active volition (asking counter-questions, probing motives, asserting goals). *Layer scoping:* In Simulator (RP), volition drives open-ended turn-taking; in Main (Drafting), volition operates within the Movement Brief's structural envelope (Brief Supremacy).
- **Body before insight** in the 4-channel vector ordering for downstream renderers.
- **Off-page matrix:** never emit realm names, bias engine labels, `DEFENSIVE_ACTIVE`, debt-ledger names, etc. into `Says` text meant for on-page use.
- **Epistemic gating:** `memories.detailed` = sharp recall; `footnote` = unsure unless scene trigger; unlisted = forgotten.
- **Competence gating:** `skills.active` = clean execution; `latent` = fumble/brace; unlisted = helplessness.
- **Age invariant:** `canon_adult` and age are identity/ToS data invariants (minors are never sexual subjects). This is a safety boundary, not a behavior toggle or mood switch.
- **Module subordination:** ENABLED modules inject only at declared hooks; core sequence and Rules_Index always win ([Modules.md](Modules.md)).

---

*Core simulation engine for CognitiveMiddleware. State shape: `Framework/Schemas/psychosomatic_state.json`. Extensions: `Framework/Modules.md`.*
