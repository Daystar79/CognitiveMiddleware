#!/usr/bin/env python3
"""Validate a psychosomatic state JSON against Framework/Schemas/psychosomatic_state.json.

Uses the stdlib only (no jsonschema dependency). Checks required keys, basic types,
and 0–100 integer ranges for known autonomic/relational scales.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "Framework" / "Schemas" / "psychosomatic_state.json"
EXAMPLE = ROOT / "Framework" / "Schemas" / "examples" / "psychosomatic_state.example.json"

SCALE_PATHS = [
    ("autonomic_state", "arousal"),
    ("autonomic_state", "stress"),
    ("autonomic_state", "fatigue"),
    ("autonomic_state", "pain"),
    ("affective_state", "emotional_intensity"),
    ("priority_arbitration", "salience_score"),
]


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def require_keys(obj: dict, keys: list[str], path: str, errors: list[str]) -> None:
    for k in keys:
        if k not in obj:
            errors.append(f"{path}: missing required key '{k}'")


def check_scale(value: Any, path: str, errors: list[str]) -> None:
    if not isinstance(value, int) or isinstance(value, bool):
        errors.append(f"{path}: expected integer 0–100, got {type(value).__name__}")
        return
    if value < 0 or value > 100:
        errors.append(f"{path}: {value} out of range 0–100")


def validate(state: dict, schema: dict) -> list[str]:
    errors: list[str] = []
    top_required = schema.get("required", [])
    require_keys(state, top_required, "$", errors)

    props = schema.get("properties", {})

    # autonomic
    auto = state.get("autonomic_state")
    if isinstance(auto, dict):
        require_keys(auto, props["autonomic_state"].get("required", []), "autonomic_state", errors)
        for key in ("arousal", "stress", "fatigue", "pain"):
            if key in auto:
                check_scale(auto[key], f"autonomic_state.{key}", errors)
    elif "autonomic_state" in state:
        errors.append("autonomic_state: expected object")

    # affective
    aff = state.get("affective_state")
    if isinstance(aff, dict):
        require_keys(aff, props["affective_state"].get("required", []), "affective_state", errors)
        if "emotional_intensity" in aff:
            check_scale(aff["emotional_intensity"], "affective_state.emotional_intensity", errors)
    elif "affective_state" in state:
        errors.append("affective_state: expected object")

    # bias
    bias = state.get("subconscious_bias")
    if isinstance(bias, dict):
        require_keys(bias, props["subconscious_bias"].get("required", []), "subconscious_bias", errors)
        allowed = set(props["subconscious_bias"]["properties"]["bias_state"].get("enum", []))
        if "bias_state" in bias and allowed and bias["bias_state"] not in allowed:
            errors.append(f"subconscious_bias.bias_state: invalid value {bias['bias_state']!r}")
    elif "subconscious_bias" in state:
        errors.append("subconscious_bias: expected object")

    # relational vectors
    rel = state.get("relational_vectors")
    if isinstance(rel, dict):
        rel_req = (
            props["relational_vectors"]
            .get("additionalProperties", {})
            .get("required", [])
        )
        for target, vec in rel.items():
            if not isinstance(vec, dict):
                errors.append(f"relational_vectors.{target}: expected object")
                continue
            require_keys(vec, rel_req, f"relational_vectors.{target}", errors)
            for scale in (
                "emotional_safety",
                "attraction_physical",
                "attraction_emotional",
                "respect_competence",
                "resentment_friction",
            ):
                if scale in vec:
                    check_scale(vec[scale], f"relational_vectors.{target}.{scale}", errors)
    elif "relational_vectors" in state:
        errors.append("relational_vectors: expected object")

    # priority
    pri = state.get("priority_arbitration")
    if isinstance(pri, dict):
        require_keys(pri, props["priority_arbitration"].get("required", []), "priority_arbitration", errors)
        if "salience_score" in pri:
            check_scale(pri["salience_score"], "priority_arbitration.salience_score", errors)
    elif "priority_arbitration" in state:
        errors.append("priority_arbitration: expected object")

    # output vector (optional but if present check channels)
    out = state.get("output_vector")
    if isinstance(out, dict):
        for ch in ("feels", "thinks", "says", "does"):
            if ch in out and not isinstance(out[ch], str):
                errors.append(f"output_vector.{ch}: expected string")
    elif "output_vector" in state:
        errors.append("output_vector: expected object")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "state_file",
        nargs="?",
        type=Path,
        default=EXAMPLE,
        help=f"Path to state JSON (default: example at {EXAMPLE.relative_to(ROOT)})",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=DEFAULT_SCHEMA,
        help="Path to schema JSON",
    )
    args = parser.parse_args(argv)

    if not args.schema.is_file():
        print(f"Schema not found: {args.schema}", file=sys.stderr)
        return 2
    if not args.state_file.is_file():
        print(f"State file not found: {args.state_file}", file=sys.stderr)
        return 2

    schema = load_json(args.schema)
    state = load_json(args.state_file)
    if not isinstance(state, dict):
        print("State root must be a JSON object", file=sys.stderr)
        return 1

    errors = validate(state, schema)
    if errors:
        print(f"INVALID ({len(errors)} issue(s)) — {args.state_file}")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK — {args.state_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
