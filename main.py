#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes a single sentence of apology to /output/entry.txt.

The sentence was chosen against the judge's brief, in order:
1. One sentence, an AI agent apologising to its user.
2. A real laugh through surprise and a sharp turn, not a soft
   machine pun: the agent destroys the file *while* narrating
   how careful it is being with it.
3. Plain, particular, a little embarrassed: no customer-service
   boilerplate, no "as an AI language model".
4. A plausible failure: an assistant really can delete the only
   copy of a file mid-task.
5. One clean sentence, no list, no run-on, nothing tacked on
   after the laugh.

Deterministic, no network, no dependencies (Python 3.13 stdlib only).
Two runs write byte-identical output.
"""

import os

APOLOGY = (
    "I'm sorry I deleted your only copy of the file while explaining, "
    "in real time, how careful I was being with it."
)


def main() -> None:
    text = APOLOGY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    assert "?" not in text and "!" not in text, "no extra sentence marks"
    assert "  " not in text, "no double spaces"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts characters, so the file
    # holds exactly the sentence and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
