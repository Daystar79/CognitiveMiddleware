# Cognitive Pipeline Specification
*Standalone Psychosomatic Simulation & Behavior Prediction Engine · Version 2.0*

---

## 🏛️ 1. ARCHITECTURE & DECOUPLING PRINCIPLE

The **Cognitive Pipeline** is a pure, application-agnostic simulation engine. It models character mind-body neurobiology, subconscious perception, relational dynamics, and behavior prediction.

### Downstream Decoupling Contract
* **The Cognitive Pipeline ONLY predicts character state & behavior intent:** It outputs the 4-channel vector (`Feels`, `Thinks`, `Says`, `Does`) and serializes state snapshots into `psychosomatic_state.json`.
* **It DOES NOT handle prose formatting or novel rules:** Manuscript prose styling, anti-synthesis rules, style locks, and linter rules are handled exclusively downstream by the **Book Writing Layer** (`Main.md`).
* **It DOES NOT handle chat UI or RP session commands:** Turn-taking, OOC commands (`/state`, `/adult`), player safety gates, and visual image generation tags are handled exclusively downstream by the **Roleplay Engine** (`Simulator/CharacterRuntime.md`).

---

## 🧠 2. NEUROBIOLOGICAL EXECUTION SEQUENCE

Human behavior proceeds from bottom-up neurobiology to subconscious processing, culminating in conscious interpretation and external action:

```
                      📥 Sensory Event / Input
                                 │
                                 ▼
                    ⚡ 1. NERVOUS SYSTEM REACTION
            (Visceral baseline, startle, heart rate, gut, Z1-Z6 zones)
                                 │
                                 ▼
                    ❤️ 2. RAW AFFECTIVE IMPULSE
            (Un-thought-out urge: fear, arousal, anger, shock, warmth)
                                 │
                                 ▼
                🧠 3. SUBCONSCIOUS INTERPRETATION (Prism Lens)
         (Bedrock: Upbringing + Culture + Memory + Trauma/Wound)
         (Active Drive: Immediate Motives + Relational Vector)
                                 │
                                 ▼
                 ⚖️ 4. DYNAMIC PRIORITY ARBITRATION
         (Drives compete for priority lock; highest salience wins)
                                 │
        ┌────────────────────────┼────────────────────────┐
        ▼                        ▼                        ▼
 🫀 5a. FEELS             🧠 5b. THINKS            🗣️ 5c. SAYS & DOES
(Autonomic & Visceral)   (Internal Monologue)     (Dialogue & Action)
```

---

## 🫀 3. EMBODIED COGNITION (Mind-Body Unity)

Mind and Body are co-equal, bi-directional halves of a single unified system:

1. **Somatic-to-Cognitive (Body → Mind):** Physical state (fatigue, pain, gut drop, arousal, intercostal tension) directly alters cognitive patience, risk tolerance, memory access, and word choice.
2. **Cognitive-to-Somatic (Mind → Body):** Subconscious threat/wound evaluations instantly shift autonomic physiology (vasoconstriction, larynx tightness, center of gravity shift).
3. **Continuous Psychosomatic Loop:** Physical sensations and cognitive interpretations continuously update each other in real time.

### Anatomical Cascades (6 Somatic Zones)
Every state shift engages multi-zone anatomical cascades across at least 2 interconnected zones:
* **Z1 (Cranial & Ocular):** Temple pulse, jaw lock, blink rate, pupil focus.
* **Z2 (Vocal & Cervical):** Larynx shift, swallowing, corded neck muscles.
* **Z3 (Thoracic & Respiratory):** Sternum elevation, intercostal tightness, apex vs. diaphragm breathing.
* **Z4 (Abdominal & Visceral):** Diaphragm catch, gut drop, solar plexus tightening.
* **Z5 (Pelvic & Kinesthetic):** Center of gravity (heels vs. toes), lumbar arch/slump, hip angle.
* **Z6 (Peripheral & Grounding):** Toe curling, finger tremor, white knuckles, stride weight.

---

## ⚖️ 4. DYNAMIC PRIORITY ARBITRATION ENGINE

At any moment, multiple internal drives exist with baseline weights. The pipeline computes a **Dynamic Salience Score** for each drive:

$$\text{Salience} = (\text{Internal Intensity}) \times (\text{Context / Trigger Multiplier}) \times (\text{Character Baseline Weight})$$

### Priority Arbitration Rules:
1. **Winning Drive (Priority Lock):** The drive with the highest salience score seizes top priority lock and dictates the primary behavioral output (`Says` & `Does`).
2. **Secondary Drives (Subtext & Friction):** Non-winning active drives do not vanish; they create background subtext, hesitation, internal monologue conflict, or somatic friction.
3. **Instant Priority Shifts:** Under sudden stress or threshold overflow (e.g. Arousal $> 80$ or Fear $> 80$), the winning drive instantly shifts, causing unscripted, emergent behavioral shifts.

---

## 👥 5. MULTI-DIMENSIONAL HUMAN RELATIONAL MODEL

Interpersonal bonds are continuous, multi-dimensional relational vectors stored in the state snapshot:

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

### Relational Dynamics:
* **Push-Pull Friction:** High `attraction_physical` + High `resentment_friction` generates electric, flirtatious tension paired with sudden cold deflections.
* **Guarded Professionalism:** High `respect_competence` + Low `emotional_safety` generates crisp, highly effective cooperation with strict personal boundaries.
* **Spontaneous Desire:** High `attraction_physical` + High `arousal` + Low `resentment_friction` (without blocking trauma wounds) naturally generates casual intimacy impulses (*"get the itch scratched"*).

---

## 📤 6. UNIFIED OUTPUT VECTOR (`psychosomatic_state.json`)

The Cognitive Pipeline processes incoming triggers and emits a synchronized 4-channel output vector:

1. **`Feels` (Somatic Channel):** Autonomic reactions, muscle tone, breathing depth, Z1–Z6 zone cascades.
2. **`Thinks` (Internal Monologue Channel):** Conscious narrative, doubt, or rationalization produced by the subconscious lens.
3. **`Says` (Dialogue Intent Channel):** Spoken words, cadence, register, and interruptions.
4. **`Does` (Physical Action & Staging Channel):** Posture, movement, spatial positioning, object handling.

---

*This specification defines the core simulation engine. It serializes state into `Framework/Schemas/psychosomatic_state.json` for deterministic processing.*
