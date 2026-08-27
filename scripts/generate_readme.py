#!/usr/bin/env python3
"""Regenerate the managed blocks of README.md from data/datasets.yaml.

Usage:
    python scripts/generate_readme.py            # write README.md
    python scripts/generate_readme.py --check     # exit 1 if README.md would change

Only the content between "<!-- NAME:START -->" / "<!-- NAME:END -->" marker pairs is
replaced. Everything else in an existing README.md (narrative text, headings without
markers) is left untouched. On a first run with no README.md present, an embedded
default skeleton is used. If you edit DEFAULT_SKELETON itself, delete README.md
before regenerating so the new skeleton text actually takes effect.
"""

import difflib
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "datasets.yaml"
README = ROOT / "README.md"

SECTIONS = ["Text, NLP, and LLM", "Speech and audio", "Vision, OCR, and multimodal"]

# (name, reason, source url or None) — hand-maintained. A resource lands here when it's
# announced but unreleased, described with no downloadable artifact, license-conflicted,
# or not yet independently verifiable. See CONTRIBUTING.md.
WATCHLIST = [
    ("Kazakh Text Corpus / Speech Corpus / AI Evaluation Benchmark Suite",
     "Announced in 2026 as more than 10B text tokens and over 10,000 speech hours (including "
     "1,000 manually transcribed \"gold standard\" hours) and a nine-dimension AI evaluation "
     "benchmark suite, from a joint initiative between the Qazaq Tili Qogamy and OpenAI, but no "
     "public dataset download was identified.",
     "https://turkystan.kz/article/282605-10-milliard-token-10-myn-sagat-audio-qazaq-tili-qogamy-men-openai-biregei-ai-infraqurylymyn-tanystyrdy"),
    ("National Corpus of the Kazakh Language (QazCorpus)",
     "Official searchable Kazakh corpus ecosystem with multiple subcorpora. The Main Corpus "
     "reports 31,105,900 word usages with morphological, semantic, lexical, phonetic, and "
     "phonological annotation. No independently verified bulk-download artifact and reusable "
     "dataset license could be confirmed, so it remains outside the main catalog.",
     "https://qazcorpus.kz/indexen.php"),
]

REPO = "Allessyer/awesome-kaz-datasets"

# Canonical task name -> short tag shown under the dataset name in the tables.
# Keep in sync with the task labels actually used in data/datasets.yaml.
TASK_ABBREV = {
    "Automatic speech recognition (ASR)": "ASR",
    "Multiple-choice QA": "MCQA",
    "Mathematical reasoning": "MATH",
    "Question answering": "QA",
    "Text-to-speech (TTS)": "TTS",
    "Machine translation": "MT",
    "Language modelling / pretraining": "LM",
    "Retrieval / RAG": "RAG",
    "OCR": "OCR",
    "Instruction tuning": "IFT",
    "Legal QA": "LQA",
    "Named entity recognition": "NER",
    "Text classification": "TC",
    "Sentiment classification": "SC",
    "Emotion / paralinguistic classification": "EPC",
    "Visual QA": "VQA",
    "Visual math reasoning": "VMR",
    "Handwriting recognition": "HTR",
    "Safety evaluation": "Safety",
    "Cultural QA": "CQA",
    "Instruction following": "IF",
    "Math reasoning": "MR",
    "Dependency parsing / POS tagging": "POS",
    "Text deduplication / similarity": "STS",
    "Morphological analysis": "MORPH",
    "Target-speaker ASR / speech separation": "TS-ASR",
    "Speaker verification": "SV",
    "Speech translation": "ST",
    "Spoken QA": "SQA",
    "Keyword spotting": "KWS",
    "Audio question answering": "AQA",
    "Audio captioning": "AC",
    "Cultural vision benchmark (text-to-image)": "T2I",
    "Audio-visual QA": "AVQA",
    "Layout analysis / document understanding": "DU",
    "Diagram QA": "DQA",
    "Visual speech recognition (lip reading)": "VSR",
    "Image classification": "IC",
}


def task_tag(task):
    return TASK_ABBREV.get(task, task)


def task_glossary(rows, cols=6, label=True):
    used = sorted(
        {t for d in rows for t in d.get("tasks", [])},
        key=lambda t: (task_tag(t).lower(), t.lower()),
    )
    # <strong>, not **bold** — this table is a multi-line HTML block, which GitHub
    # does not run markdown-inline parsing over (see the earlier badges bug).
    entries = [f"<strong>{task_tag(t)}</strong> — {t}" for t in used]
    rows_of_cells = [entries[i : i + cols] for i in range(0, len(entries), cols)]
    table_rows = []
    for row_cells in rows_of_cells:
        padded = row_cells + [""] * (cols - len(row_cells))
        table_rows.append("<tr>" + "".join(f'<td align="center" valign="middle">{c}</td>' for c in padded) + "</tr>")
    prefix = "**Abbreviations:**\n\n" if label else ""
    return prefix + '<table width="100%">\n' + "\n".join(table_rows) + "\n</table>"


def picture(alt, base, width="100%"):
    # Wide charts (growth line, bar comparison) use width="100%" so they fill
    # the README column. The heatmaps are inherently compact/dense — stretching
    # them to the same full column width blows the cells up far past their
    # native size, so those pass a fixed pixel width instead.
    return (
        '<picture>\n'
        f'  <source media="(prefers-color-scheme: dark)" srcset="assets/{base}-dark.svg">\n'
        f'  <img src="assets/{base}.svg" alt="{alt}" width="{width}">\n'
        '</picture>'
    )


DEFAULT_SKELETON = """<h1 align="center">
  <img src="https://emojiassets.saruwakakun.design/a/lg/1f1f0_1f1ff_1o53s.webp" width="34" valign="middle" alt="Kazakhstan flag">
  Awesome Kazakh Datasets
  <img src="https://emojiassets.saruwakakun.design/a/lg/1f1f0_1f1ff_1o53s.webp" width="34" valign="middle" alt="Kazakhstan flag">
</h1>

<p align="center">
  A curated, verified catalog of public datasets for Kazakh-language NLP, LLM, speech, and vision research.
</p>

<!-- BADGES:START -->
<!-- BADGES:END -->

<p align="center">
  <a href="#about">About</a> ·
  <a href="#text-nlp-and-llm">Text &amp; NLP</a> ·
  <a href="#speech-and-audio">Speech</a> ·
  <a href="#vision-ocr-and-multimodal">Vision &amp; OCR</a> ·
  <a href="#watchlist--announced-resources">Watchlist</a> ·
  <a href="#contributing">Contributing</a> ·
  <a href="#license">License</a>
</p>

---

## About

Kazakh is spoken by roughly 13 million people, yet reusable public datasets for it
are scattered across Hugging Face, GitHub, institutional pages, and archives with
no reliable map of what's actually downloadable today.

Every entry below is checked against its primary source, with release date, access
terms, and license recorded rather than assumed. Resources that are announced but
not yet independently verifiable go in the [Watchlist](#watchlist--announced-resources)
instead of the main tables. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full
inclusion policy and [CHANGELOG.md](CHANGELOG.md) for what's new.

<!-- LANDSCAPE:START -->
<!-- LANDSCAPE:END -->

## Text, NLP, and LLM

<!-- NLP_SECTION:START -->
<!-- NLP_SECTION:END -->

## Speech and audio

<!-- SPEECH_SECTION:START -->
<!-- SPEECH_SECTION:END -->

### English-Russian-Kazakh comparison by speech task

PLACEHOLDER_SPEECH_COMPARISON_IMG

The bars are conservative lower bounds, not estimates of every dataset in existence.
Subsets, mirrors, and known derivatives are excluded. For speaker verification (`*`),
a broader speaker-presence rule counts complete multilingual corpora when they
explicitly contain speakers of the language; these are **corpus-hours containing the
language**, not language-only hours, and possible cross-corpus overlap remains.

## Vision, OCR, and multimodal

<!-- VISION_SECTION:START -->
<!-- VISION_SECTION:END -->

## Watchlist / announced resources

Resources below are announced, described in a paper without a public artifact,
license-conflicted, or not yet independently verifiable as usable Kazakh-language
datasets. They are intentionally **not** part of the main catalog above. Where a
source is known, the entry links to it.

<!-- WATCHLIST:START -->
<!-- WATCHLIST:END -->

## Abbreviations

<!-- ABBREVIATIONS:START -->
<!-- ABBREVIATIONS:END -->

## Contributing

Missing a Kazakh dataset, or spotted outdated metadata? Contributions are welcome:

- **Add a dataset** — [open a submission issue](../../issues/new?template=dataset-submission.yml)
  or send a PR directly.
- **Fix or update an entry** — edit `data/datasets.yaml` and open a PR.
- **Report a stale number** — Hugging Face row counts and reported storage
  sizes may change over time; flag it with the current value from the
  [Dataset Server API](https://huggingface.co/docs/dataset-viewer/en/size).

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full inclusion criteria, required
metadata, and PR format.

## Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://kz.linkedin.com/in/allessyer/en">
        <img src="https://avatars.githubusercontent.com/u/71093827?v=4" width="80" height="80" alt="Assel Yermekova"><br>
        <sub><b>Assel Yermekova</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/in/alen-issayev/">
        <img src="https://avatars.githubusercontent.com/u/154399485?v=4" width="80" height="80" alt="Alen Issayev"><br>
        <sub><b>Alen Issayev</b></sub>
      </a>
    </td>
  </tr>
</table>

## License

This catalog's own content — the repository structure, documentation, generated
tables, and scripts — is released under the [MIT License](LICENSE). Datasets
linked from this catalog remain under their own respective licenses (recorded
per entry above); this MIT license does not extend to their contents.
"""

DEFAULT_SKELETON = DEFAULT_SKELETON.replace(
    "PLACEHOLDER_SPEECH_COMPARISON_IMG",
    picture(
        "Grouped vertical bars comparing public speech-data hours for Kazakh, Russian, and "
        "English across ASR, TTS, speech translation, emotion, keyword spotting, and speaker "
        "verification",
        "speech_task_hours_comparison",
    ),
).replace("REPO_PLACEHOLDER", REPO)


def load_datasets():
    doc = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    return doc["datasets"]


def released_sort_key(d):
    r = d.get("released")
    if not r or r == "Not reported":
        return (0, 0, 0)
    parts = str(r).split("-")
    year = int(parts[0])
    month = int(parts[1]) if len(parts) > 1 else 0
    return (1, year, month)


def last_name(name):
    return name.strip().split()[-1] if name else name


def author_and_org(d):
    authors = [a["name"] for a in (d.get("authors") or []) if a.get("name")]
    orgs = [o["name"] for o in (d.get("organization") or []) if o.get("name")]
    author_str = None
    if len(authors) == 1:
        author_str = authors[0]
    elif len(authors) == 2:
        author_str = f"{last_name(authors[0])} & {last_name(authors[1])}"
    elif len(authors) >= 3:
        author_str = f"{last_name(authors[0])} et al."
    org_str = " · ".join(orgs) if orgs else None
    return author_str, org_str


def author_line(d):
    # Individual/group author when known; falls back to the organization name
    # only when no author is recorded at all (e.g. an org-attributed release
    # like Til-Qazyna or Mozilla Foundation). Affiliation is not shown
    # alongside a named author — keeps the Dataset cell to name + one
    # attribution line, not name + author + affiliation.
    author_str, org_str = author_and_org(d)
    name = author_str or org_str
    if not name:
        return None
    author_link = (d.get("links") or {}).get("paper") or (d.get("links") or {}).get("doi")
    display = f"[{name}]({author_link})" if author_link and author_str else name
    return f"<sub>{display}</sub>"


def format_access(d):
    # License is intentionally not surfaced in the table — it stays in
    # data/datasets.yaml (the "properties") rather than in the display.
    return (d.get("access") or "unavailable").capitalize()


def format_storage(d):
    storage = d.get("storage") or {}
    value = storage.get("value")
    if value is None:
        return "Not reported"
    unit = storage.get("unit") or ""
    return f"{value} {unit}".strip()


def format_samples(d):
    scale = d.get("scale") or {}
    value = scale.get("value")
    if not value or value == "Not reported":
        return "Not reported"
    return str(value)


def dataset_row(d, idx):
    tags = " · ".join(task_tag(t) for t in (d.get("tasks") or [])) or "Not reported"
    data_url = (d.get("links") or {}).get("dataset")
    display_name = f"[{d['name']}]({data_url})" if data_url else d["name"]

    name_lines = [f"**{display_name}**"]
    al = author_line(d)
    if al:
        name_lines.append(al)
    name_lines.append(f"<sub>{format_access(d)}</sub>")
    name_cell = "<br>".join(name_lines)

    released = d.get("released") or "Not reported"
    return "| {idx} | {released} | {name} | {task} | {desc} | {storage} | {samples} |".format(
        idx=idx,
        released=released,
        name=name_cell,
        task=tags,
        desc=d.get("description") or "",
        storage=format_storage(d),
        samples=format_samples(d),
    )


def dataset_table(rows):
    header = (
        "| ID | Released | Dataset | Task | Description | Storage | Samples |\n"
        "|---:|---|---|---|---|---|---|"
    )
    ordered = sorted(rows, key=released_sort_key, reverse=True)
    body = "\n".join(dataset_row(d, i + 1) for i, d in enumerate(ordered))
    return header + "\n" + body


def build_section(datasets, section):
    rows = [d for d in datasets if d["section"] == section]
    return dataset_table(rows)


def build_landscape(datasets):
    caption = "<sub>Cumulative Kazakh dataset releases over time, by section.</sub>"
    return picture("Cumulative Kazakh dataset releases over time, by section", "dataset_growth") + "\n\n" + caption


def build_abbreviations(datasets):
    return task_glossary(datasets, cols=6, label=False)


def build_badges(datasets):
    # Markdown image syntax is not parsed inside a multi-line HTML block, so these
    # are plain <img> tags rather than ![]() — otherwise GitHub renders the literal
    # "![Datasets](...)" text instead of the badge.
    n = len(datasets)
    open_n = sum(1 for d in datasets if d["access"] == "open")
    open_pct = round(100 * open_n / n)
    stars = (
        f'<img alt="GitHub Repo stars" '
        f'src="https://img.shields.io/github/stars/{REPO}?style=flat&color=eda100">'
    )
    badges = [
        ("Datasets", str(n), "2a78d6"),
        ("Open access", f"{open_pct}%25", "2ea44f"),
        ("Last verified", "2026--08--21", "1baf7a"),
    ]
    parts = [stars] + [
        f'<img alt="{label}" src="https://img.shields.io/badge/{label.replace(" ", "_")}-{value}-{color}">'
        for label, value, color in badges
    ]
    return '<p align="center">\n  ' + "\n  ".join(parts) + "\n</p>"


def build_watchlist():
    lines = []
    for name, reason, url in WATCHLIST:
        title = f"**[{name}]({url})**" if url else f"**{name}**"
        lines.append(f"- {title} — {reason}")
    return "\n".join(lines)


BLOCKS = {
    "BADGES": build_badges,
    "LANDSCAPE": build_landscape,
    "NLP_SECTION": lambda datasets: build_section(datasets, "Text, NLP, and LLM"),
    "SPEECH_SECTION": lambda datasets: build_section(datasets, "Speech and audio"),
    "VISION_SECTION": lambda datasets: build_section(datasets, "Vision, OCR, and multimodal"),
    "WATCHLIST": lambda datasets: build_watchlist(),
    "ABBREVIATIONS": lambda datasets: build_abbreviations(datasets),
}


def apply_blocks(content, datasets):
    for name, builder in BLOCKS.items():
        start = f"<!-- {name}:START -->"
        end = f"<!-- {name}:END -->"
        si = content.find(start)
        ei = content.find(end)
        if si == -1 or ei == -1:
            raise ValueError(f"Marker pair {name} not found in README skeleton")
        replacement = builder(datasets)
        content = content[: si + len(start)] + "\n" + replacement + "\n" + content[ei:]
    return content


def main():
    check = "--check" in sys.argv
    datasets = load_datasets()

    base = README.read_text(encoding="utf-8") if README.exists() else DEFAULT_SKELETON
    # If the existing file predates this marker set (e.g. the pre-redesign layout
    # with DASHBOARD/per-section overview cards), fall back to the skeleton.
    if "<!-- ABBREVIATIONS:START -->" not in base:
        base = DEFAULT_SKELETON

    new_content = apply_blocks(base, datasets)

    if check:
        current = README.read_text(encoding="utf-8") if README.exists() else ""
        if current == new_content:
            print("OK: README.md is up to date.")
            return 0
        print("STALE: README.md does not match generated output. Run scripts/generate_readme.py.")
        print("".join(difflib.unified_diff(
            current.splitlines(keepends=True),
            new_content.splitlines(keepends=True),
            fromfile="README.md",
            tofile="generated README.md",
        )))
        return 1

    README.write_text(new_content, encoding="utf-8")
    print(f"Wrote {README}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
