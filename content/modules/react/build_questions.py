# Generates content/modules/react/questions.json from seed JSON files.
# Run: python3 content/modules/react/build_questions.py
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    # Ordered: seeds 01-78, then large batches 079-135, 136-207, 208-300
    part_names = [
        "seed_01_10.json",
        "seed_11_20.json",
        "seed_21_30.json",
        "seed_31_40.json",
        "seed_41_50.json",
        "seed_51_60.json",
        "seed_61_70.json",
        "seed_71_78.json",
        "chunk_079_135.json",
        "chunk_136_207.json",
        "chunk_208_300.json",
    ]
    all_items: list[dict] = []
    for name in part_names:
        p = ROOT / name
        if not p.is_file():
            raise SystemExit(f"Missing {p}")
        chunk = json.loads(p.read_text(encoding="utf-8"))
        if not isinstance(chunk, list):
            raise SystemExit(f"{p} must be a JSON array")
        all_items.extend(chunk)
    if len(all_items) != 300:
        raise SystemExit(f"expected 300 items, got {len(all_items)}")
    for i, item in enumerate(all_items, start=1):
        expect = f"react-{i:03d}"
        if item.get("id") != expect:
            raise SystemExit(f"index {i}: id {item.get('id')!r} != {expect!r}")
    out = ROOT / "questions.json"
    out.write_text(json.dumps(all_items, indent=2) + "\n", encoding="utf-8")
    print("Wrote", out, "—", len(all_items), "items")


if __name__ == "__main__":
    main()
