"""Check generated reading notes for obsolete tool-signature footers."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re

SIGNATURES = (
    re.compile(
        r"分析采用\s*(?:norman-paper-reading|paper-reading(?:-notes)?)"
        r"\s*(?:技能|定制技能)"
    ),
    re.compile(
        r"Analysis\s+performed\s+using\s+(?:the\s+)?"
        r"(?:norman-paper-reading|paper-reading(?:-notes)?)\b",
        re.IGNORECASE,
    ),
)


class NoteText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def has_tool_signature(content, is_html=False):
    if is_html:
        parser = NoteText()
        parser.feed(content)
        content = "".join(parser.parts)
    return any(pattern.search(content) for pattern in SIGNATURES)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notes", nargs="+", type=Path)
    args = parser.parse_args()
    failed = False
    for note in args.notes:
        try:
            content = note.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as error:
            print(f"FAIL {note}: {error}")
            failed = True
            continue
        if has_tool_signature(content, note.suffix.lower() in (".html", ".htm")):
            print(f"FAIL {note}: obsolete tool signature detected")
            failed = True
        else:
            print(f"PASS {note}")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
