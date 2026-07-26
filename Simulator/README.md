# Simulator (optional)

**Cognitive Middleware’s product is the drafting middle layer** (`Framework/`, character cards, logs, ledgers, linter).  

This folder is a **side tool**: live chat against a card so you (or friends) can stress-test behaviour before writing — or run private RP sessions. It is shipped because the same psyche engine is useful off-manuscript; it is **not** the marketed product surface.

## CharacterRuntime.md

Self-contained drop-in. Paste the whole file into a chat (no git required).

| Mode | Intent |
|:---|:---|
| **TEST** (default) | Author fidelity — “how would this card act?” |
| **COMPANION** / **HEAT** | Optional live session modes (adult paths gated) |

**Private adult RP (one switch):** after loading a canon-adult pack, send **`/adult on`**. That sets adult authorization + HEAT mode. Toggle off with `/adult off`. Age gates stay absolute (no minors, no age-up). Optional: `/bond set trust:70 attraction:60` if the relationship is already established.

Persistence: Character Pack (CARD + MEMORY) via Drive/local/paste — see the runtime file.

**Image layer:** Visual rendering via `Images/CharacterRenderingEngine.md` is **off by default** (`visual.mode: off`) for zero turn latency in RP. Force a frame anytime with `/render`, or toggle auto motion rendering with `/visual off|fast|prompts|live`.

## When to use what

| Goal | Use |
|:---|:---|
| Write a novel / movement | `Framework/Main.md` + Rules + realm_data + cards + logs |
| Check a card in chat | This simulator, `/mode test` |
| Private live RP | This simulator · `/adult on` when both are adults · keep packs private |

## License & Disclaimers

CC BY-SA 4.0 for the runtime text (root [LICENSE.md](../LICENSE.md)). Your packs and private sessions are your data.

**Compliance & 18+ Warning:** Private adult RP features (`/adult on`) are strictly restricted to adult users (18+) and canonically adult (18+) fictional characters in compliance with GitHub Terms of Service. See root **[DISCLAIMER.md](../DISCLAIMER.md)** for full terms.

