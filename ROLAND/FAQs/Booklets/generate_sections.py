from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SOURCE_PATH = BASE_DIR / "booklet_prompts.json"
OUTPUT_ROOT = BASE_DIR / "generated_sections"


def slugify_booklet(parent_key: str) -> str:
    prefix, _, title = parent_key.partition("—")
    booklet_id = prefix.strip().replace(" ", "_")
    title_slug = "_".join(title.strip().lower().replace("/", " ").split())
    return f"{booklet_id}_{title_slug}"


def render_markdown(booklet_title: str, section_title: str, url_slug: str, question: str) -> str:
    return (
        f"# {booklet_title}\n\n"
        f"## {section_title}\n\n"
        f"url_slug: {url_slug}\n\n"
        f"Prompt:\n{question}\n"
    )


def main() -> None:
    data = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))

    if OUTPUT_ROOT.exists():
        for existing in OUTPUT_ROOT.rglob("*.md"):
            existing.unlink()

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    generated = []
    for booklet_title, sections in data.items():
        booklet_folder = OUTPUT_ROOT / slugify_booklet(booklet_title)
        booklet_folder.mkdir(parents=True, exist_ok=True)

        if len(sections) != 1:
            raise ValueError(f"Expected exactly one section per booklet for '{booklet_title}'.")

        section_title, entry = next(iter(sections.items()))
        markdown = render_markdown(
            booklet_title=booklet_title,
            section_title=section_title,
            url_slug=entry["url_slug"],
            question=entry["question"],
        )
        output_file = booklet_folder / "01_section.md"
        output_file.write_text(markdown, encoding="utf-8")
        generated.append(output_file)

    if len(generated) != 10:
        raise ValueError(f"Expected exactly 10 generated section files; found {len(generated)}.")

    print(f"Generated {len(generated)} section files.")


if __name__ == "__main__":
    main()
