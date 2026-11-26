"""Entry for make.fun bounty u-motasimfuad-rejected-olympic-sports-9d83e7da.

Writes one text to /output/entry.txt. No network, deterministic.
"""
import os

TEXT = "DRAFT PLACEHOLDER LINE"


def write_entry(text, limit):
    n = len(text)
    assert text.strip(), "text is only white space"
    assert 1 <= n <= limit, f"length {n} outside 1..{limit}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return n


def main():
    n = write_entry(TEXT, 200)
    print(f"wrote entry.txt: {n} code points")


if __name__ == "__main__":
    main()
