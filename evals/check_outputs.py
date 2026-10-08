#!/usr/bin/env python3
"""Objective checks on eval outputs (complements human/LLM grading).

Usage: python3 evals/check_outputs.py evals/iteration-1
Prints, per run: whether key strings are present and whether the timed
ranges inside each prompt add up to the stated duration.
"""
import re
import sys
from pathlib import Path

LINES = {
    "pescador-rede-ptbr": ["Nó frouxo, peixe solto"],
    "hospital-shotlist": ["Ele está estável", "Mas não acordou", "Posso entrar", "Só cinco minutos"],
    "fogueira-reparo": [],
}
MUSIC_SYNONYMS = ["score", "bgm", "soundtrack", "instrumental", "melody", "ambient pad", "synth", "drone"]
RANGE = re.compile(r"(\d{1,2}(?:\.\d)?)\s*[–-]\s*(\d{1,2}(?:\.\d)?)\s*s(?:ec)?\b")
DURATION = re.compile(r"(?i)duration[^0-9\n]{0,20}(\d{1,2})\s*s")


def check(run: Path, eval_name: str) -> dict:
    texts = [p.read_text(errors="ignore") for p in (run / "outputs").glob("*") if p.suffix in {".md", ".html"}]
    text = "\n".join(texts)
    low = text.lower()
    res = {
        "chars": len(text),
        "lines_verbatim": all(l in text for l in LINES[eval_name]) if LINES[eval_name] else None,
        "no_music": "no music" in low,
        "music_synonyms": sum(s in low for s in MUSIC_SYNONYMS),
        "no_subtitles": "no subtitles" in low or "no subtitle" in low,
        "durations": DURATION.findall(text)[:6],
    }
    ends = [float(b) for _, b in RANGE.findall(text)]
    res["max_range_end"] = max(ends) if ends else None
    return res


def main(root: str) -> None:
    for eval_dir in sorted(Path(root).iterdir()):
        if not eval_dir.is_dir():
            continue
        for cfg in ("with_skill", "old_skill"):
            run = eval_dir / cfg
            if run.exists():
                print(f"{eval_dir.name:22s} {cfg:10s} {check(run, eval_dir.name)}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "evals/iteration-1")
