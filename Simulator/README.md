# Simulator (optional)

**CognitiveMiddleware’s product core** is the Cognitive Pipeline (psychological / physical character runtime) plus the book-writing layer under `Framework/`.

This folder is a **side tool**: live chat against a card so you can stress-test behaviour before writing — or run private RP sessions. It ships because the same pipeline is useful off-manuscript; it is not the only product surface.

## CharacterRuntime.md

Drop-in host. Paste into a chat (no git required). Queries `Framework/CognitivePipeline.md` each turn.

| Control | Intent |
|---|---|
| Default play | Character fidelity from card + log + pipeline (switchless) |
| `/state` | Optional OOC inspect of live psychosomatic snapshot (debug only) |
| `/visual` / `/render` | Optional image layer (off by default) |

**Persistence:** Live snapshots update each tick; durable merges into `_log.yaml` happen automatically on scene break / medium+ shift / session close. No behavioral “adult mode” or manual save required for psychology.

**Private directory:** `Private/` is git-ignored and not deployed. Do not commit private session files.

**Image layer:** `Images/CharacterRenderingEngine.md` is **off by default**. Force a frame with `/render`, or toggle with `/visual off|fast|prompts|live`.

## When to use what

| Goal | Use |
|---|---|
| Write a novel / movement | `Framework/Main.md` + pipeline + Rules + realm_data + cards + logs |
| Check a card in chat | This simulator |
| Private live RP | This simulator · keep packs private · age invariants always apply |

## License & disclaimers

CC BY-SA 4.0 for the runtime text (root [LICENSE.md](../LICENSE.md)). Your packs and private sessions are your data.

**Compliance & 18+:** Intimate modeling is restricted to adult users (18+) and canonically adult fictional characters (`canon_adult: true`, age ≥ 18). Minors are never sexual subjects. See root **[DISCLAIMER.md](../DISCLAIMER.md)**.
