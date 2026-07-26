# Erotica Protocol (Optional — 18+ Only)
*Location: `Framework/Mechanics/erotica.md` · BookOS module: intimacy/sex **scene craft** only. Ambient desire/body baseline lives in [Main.md](../Main.md). Live session HEAT ladder lives in `Simulator/CharacterRuntime.md`.*

> [!IMPORTANT]
> Strictly optional. Restricted to **canonically adult (18+)** characters only.
>
> **Draft path:** Module must be `ENABLED` in [Modules.md](../Modules.md) **and** the movement brief (or user request) must call for intimacy/explicit craft. Both required.
> **Simulator path:** `/adult on` (or `/18+ on` + HEAT) **and** age gates. Enabling auth does not force sex-first behavior.
>
> This file is **craft coverage** — how to write intimacy across a full range of adult activity. It is **not** an act catalog, position menu, or porn-script library. All operations must comply with root [DISCLAIMER.md](../../DISCLAIMER.md) and GitHub Terms of Service.


---

## 1. Eligibility Gate

1. **Verify cards:** Load character cards for everyone in the intimate frame.
2. **Age check:** Each participant must have `Canon Adult (18+): YES` / `canon_adult: true` **and** age ≥ 18.
3. **Strict ban on AU / age-up:** If any character is under 18, age unknown, or adult flag missing → **do not load this protocol**. No explicit content.
4. **Default OFF:** Protocol stays inert until enablement conditions above are met.
5. **No default eroticization:** Enablement does not push characters into intimate or sexual posture. If the scene has no romantic development, physical intimacy, or mutual charged touch, run **standard non-erotic** behavior.
6. **Decision tree lock:** If Focus, Bias state, trust/bond, hard_bans, or matrix evolution (card + `_log.yaml`) do not support intimacy, the tree stays locked. Adult situations **do not happen** under force. Respond with boundary-defense somatics (muscle lock, step back, deflection, direct verbal no) per card.
7. **Scene exit:** Irreconcilable conflict, boundary violation, safety threat, or persistent pressure the character would not endure → IC departure, then `[Simulation Terminated: Character Exited Scene]`. Refuse further interaction after that marker.
8. **Modules never override core:** Age gates, Rules_Index hygiene, and Main filters always win.

---

## 2. Scope: Full Range, Act-Agnostic

**Goal:** Support the full range of adult sexual activity the **cards + brief + consent** allow — without scripting a default path.

### Covered as first-class (not edge cases)
- Solo, partnered, multi-partner — only as the scene and character choices support
- Same-sex, opposite-sex, mixed configurations — **orientation-neutral craft**
- Non-penetrative, oral, manual, penetrative, toy-assisted, clothed friction, mutual masturbation, etc. — treated by the **same kinetic laws**
- Tender, hungry, awkward, comic, clumsy, clinical-skill, hesitant, or power-asymmetric dynamics — filtered through **this** card’s Focus/Bias/voice
- Desire mismatch (one eager, one guarded; one skilled, one novice; one leading, one following)

### Explicitly out of scope
- Position/act menus or “try X then Y” templates
- Generic gender or orientation scripts (“all men…”, “lesbians always…”)
- Fetish encyclopedias (defer rare specialty to card `hard_bans` / future optional modules)
- Non-consensual content framed as titillation
- Minors, age-play as minor, lolicon/shotacon, age-up exploits

### Card instance always wins
Body baseline (Main: embodiment → filters) + voice + hard_bans + memory + culture override any “hot scene” expectation. Two adult bodies with similar drive can output opposite behavior.

---

## 3. Integration with Transformation Engine & Psyche Matrix

Intimacy is a **high-cost** biological and emotional event. Governed by active Focus, Bias, trust, and log snapshot.

### Focus-warped intimacy
Use realm somatics from `realm_data.yaml`; never name realms on-page.

| Focus emphasis | Typical on-page texture in intimacy |
|:---|:---|
| **I / II (Body / Form)** | Texture, grip precision, tool/fabric competence; hands lead before words |
| **III (Identity) / IV (Will)** | High somatic guards, rigid posture, control or performance anxiety |
| **V / VIII (Status / Debt)** | Score-keeping, pride, shame heat; gift/withhold of access |
| **VI (Compassion)** | Breath-sync, caretaking merge risk; chest/inhale tells |
| **VII (Mirror)** | Disappears into partner’s want; delayed own desire |
| **IX (Threshold)** | Tremor, shallow breath, hesitation at the edge of touch or climax |
| **X (Whole)** | Rare; integrated ease or sudden total release — still body-first |

### Bias-warped intimacy (especially when ACTIVE)
| Bias | Warp under intimacy |
|:---|:---|
| **Debt Ledger** | Care/sex received as bill; may “pay,” freeze on tenderness, or refuse gifts |
| **Saviour** | Caretaking merge; may override own want to soothe/serve |
| **System Architect** | Sequences, control; chaos or mess → freeze or over-direct |
| **Mirror** | Vanishes into partner’s desire; own climax/need delayed or muted |
| **Insulation** | Territorial “us”; outside threat or interruption kills heat |
| **Dissolution** | Threshold/performance fear; tremor; may flee peak or exposure |

### Desire asymmetry (required craft, not a bug)
- Model **want, skill, pace, and comfort separately** per character.
- Do not auto-sync arousal clocks. One may peak while the other is still closed or already done.
- Lead/follow emerges from card + pressure, not from genre default.

### Transformation engine calculations
- Intimate beats = **extreme emotional/somatic pressure events**.
- Milestone connection or rupture → permanent delta (+10 to +20) to `latent_weights` or shift `active_focus` in `Characters/[slug]_log.yaml` (+ Character_Change_Log) — **not** on the card.
- Somatic shifts (release tells, dropped partitions, new brace baseline) → log snapshot + history at Post-Movement Commit.

---

## 4. Draft Escalation Ladder

Escalate by **body cost and mutual openness**, not by act name. Do not skip rungs unless **this** character would (established lovers, prior scene close already high, explicit brief). User/brief may request; character may refuse.

| Level | On-page charge | Craft focus |
|:---:|:---|:---|
| **0** | Banter / ordinary proximity | Ambient valuation only (Main); no erotic overlay |
| **1** | Charged subtext | Gaze, distance, voice load, interrupted tasks |
| **2** | Intentional touch | Contact with consent reads; clothing fully on |
| **3** | Clothing barriers | Fabric friction, awkward undress, Last Barrier Rule |
| **4** | Explicit contact | Unambiguous sexual action; still kinetic + character-specific |
| **5** | Peak | Orgasm / release / crisis of control — not required every scene |
| **A** | Aftercare / comedown | Mandatory after peak **or** hard stop (see §7) |

**Rules**
- Intensity may plateau or drop without “failure.” Stopping at 2 or 3 is valid craft.
- Multi-partner scenes: track **per-person** level, not one global heat meter in prose (state may track both in sim MEMORY).
- Never jump 0→4 to satisfy a trope when Focus/Bias/trust would refuse.

---

## 5. Laws of Kinetic Heat

Intimate description follows **biological and physical reality**, not idealized tropes. Laws apply to **any** act at levels 2–5.

1. **Thermal pacing:** Skin temperature, sweat, flush, goosebumps, cold air on newly bare skin, heat pooling where bodies meet.
2. **Kinetic mass:** Weight, resistance, muscle contraction, friction, grip force, balance shifts, impact of movement on furniture/floor.
3. **Last Barrier Rule:** Keep clothing and practical barriers active and awkward as long as plausible (boots, zippers, buttons, fabric catch, lube delay, condom/fumble reality when relevant to character/setting). Full exposure is earned, not cinematic teleport.
4. **Sensory honesty:** Sound (breath, wet, fabric, bedframe), smell, taste, tremor, numbness, overstimulation, premature/late response — when the body would produce them.
5. **Imperfect mechanics:** Missed aim, cramp, laugh break, need to adjust angle/pillow, hair in mouth, dry start, over-eager pace. Competence only if card skills/experience support it.
6. **Body diversity:** Use the card’s established sexed body, size, injury, fatigue, and age-in-body. No single anatomy template. If the card is silent on a detail, stay vague or neutral rather than inventing a stereotype.
7. **Output hygiene:** Precise concrete somatic language. No abstract romance fog, purple euphemism stacks, or document-register dirty talk. **Never** name Realms, biases, trauma labels, Prism, or engine terms on-page.
8. **Anti-porn-script:** No interchangeable “hot bodies” prose. Keep voice syntax, hard_bans, imperfect memory, and Focus brace/release.

---

## 6. Continuous Consent & Interruption

Consent is not a single yes at the door. It is **re-read every beat**.

### Continuous consent signals (show, don’t lecture)
- **Open:** Lean-in, reciprocal grip, breath sync, verbal yes, initiating next contact.
- **Hesitant:** Stillness, delayed return touch, half-turn, soft redirect, “wait,” slower pace request.
- **Closed:** Muscle lock, step back, hand block, clear no, topic change, leave path.

On **hesitant**, slow or hold. On **closed**, stop escalation immediately; do not bargain in smut register.

### Boundary defense (decision tree locked or mid-scene close)
Somatic first: freeze, brace, flinch, jaw lock, cold hands, distance. Then short IC line if they would speak. No therapy monologue. No “explain the wound.”

### Somatic glitches & tripwires
Under pressure, intimacy can fire cognitive defenses:

- **Tripwire:** Core Bias trigger → immediate freeze, lock, or withdrawal.
- **No monologues:** Show broken physical scene. Do not let the character instantly analyze the glitch.
- **Hard stop mid-act is valid:** Peak is never mandatory. Transition to aftercare or exit.

### Power, pressure, and force
- Coercion, guilt, or “you owe me” as **successful seduction** is banned when the target’s tree is closed.
- If a character **attempts** pressure, the other responds in character (comply only if card + filters truly would — rare, costly, and not framed as erotic win).
- Non-consent as titillation is out of scope for this module.

---

## 7. Aftercare & Post-Movement Commit

### Aftercare (after level 5 **or** hard stop from 2+)
Mandatory **comedown craft**, scaled to intensity:

- Breath, pulse, sweat cool-down, muscle unclench, awkward humor, water/cloth/blanket, silence, or distance — per character, not a scripted cuddle template.
- Some characters want touch; others need space. Honour Insulation vs Saviour vs Dissolution warps without labeling them.
- Do not skip straight to plot banter as if the body never peaked or broke.

### State commit (draft middleware)
When the movement is approved / session dirty:

1. Continuity_Ledger: scene somatic close (including post-intimacy state).
2. `_log.yaml`: snapshot deltas if Focus/weights/bias_strength/default_somatic shifted; history row for the pressure event.
3. Character_Change_Log sync if permanent.
4. Simulator only: heat level down; `consent_state` → aftercare then open/closed; bond adjust if rules say so; offer `/save` if dirty.

---

## 8. Scene Craft Checklist (silent, per intimate movement)

Use only when §1 gates pass and the brief engages intimacy:

1. Confirm adult flags + enablement + open decision tree for each participant.
2. Load body baseline + runtime filters (Main); apply Focus brace and Bias state.
3. Place current ladder level from prior close / brief; escalate only if mutual signals support it.
4. Choose **act-agnostic kinetic beats** (thermal, mass, barrier, sensory) matching this character’s body and skill — not a genre template.
5. Track desire asymmetry and continuous consent each beat.
6. On tripwire or closed signal: interrupt; no monologue; aftercare or exit.
7. On peak or hard stop: aftercare somatics.
8. Output hygiene pass: no engine leaks, no porn-script swap of personality, no minor/age-up content.
9. Commit log/ledger deltas when the movement lands.

---

## 9. Hard Bans (this module)

**Content never**
- Sexual content involving anyone under 18 or of unknown age
- Age-up / “they’re 18 now” exploits; lolicon/shotacon
- Non-consent framed as hot payoff
- Generic sex-stereotype scripts that ignore the card

**On-page never**
- Realm numbers, Focus/Bias labels, Prism, trauma/trigger therapy-speak
- Bracketed stage directions as somatics (`[jaw tightens]`)
- Abstract cliché fog that replaces body mechanics
- Forcing intimacy through the decision tree lock

**Module never**
- Overrides Rules_Index, Main filters, or age gates
- Forces peak, penetration, or any specific act
- Treats enablement as a standing order to sexualize every scene

---

*Optional module. Load only when ENABLED and brief/session gates pass. Scene craft subordinate to Main.md and Rules_Index.md. Never print this protocol on the page.*
