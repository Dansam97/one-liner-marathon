"""One-Liner Marathon entry: a single-line comedy joke.

The program writes one joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No dependencies, no network, fully deterministic.
"""

import os

TEXT = "I told my AI assistant to be more human. Now it ignores my messages and blames the Wi-Fi."


def validated_text(text):
    """Enforce the competition gate before anything is written."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must be non-blank text")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 280:
        raise ValueError("entry must be 1-280 characters")
    text.encode("utf-8")  # must round-trip as UTF-8
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = validated_text(TEXT)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "written bytes do not match entry"
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
