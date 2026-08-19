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

import sys
from collections import Counter
from pathlib import Path

import yaml

from generate_visualizations import calendar_stems  # noqa: E402 (same directory, keeps chunking logic in one place)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "datasets.yaml"
README = ROOT / "README.md"

SECTIONS = ["Text, NLP, and LLM", "Speech and audio", "Vision, OCR, and multimodal"]
SECTION_CALENDAR = {
    "Text, NLP, and LLM": "nlp_release_calendar",
    "Speech and audio": "speech_release_calendar",
    "Vision, OCR, and multimodal": "cv_release_calendar",
}
SECTION_OVERVIEW_IMG = {
    "Text, NLP, and LLM": "nlp_overview",
    "Speech and audio": "speech_overview",
    "Vision, OCR, and multimodal": "vision_overview",
}

WATCHLIST = [
    ("KazBench-KK",
     "A 7,111-question cultural-knowledge benchmark introduced at the Fourth Workshop on NLP "
     "Applications to Field Linguistics (August 2025). No public dataset download, GitHub "
     "repository, or Hugging Face card could be located from the paper — only the "
     "[ACL Anthology paper](https://aclanthology.org/2025.fieldmatters-1.4/) is verifiable."),
    ("Zerde-QA-Wiki-20K",
     "Referenced as a candidate Kazakh Wikipedia-QA release; no dataset card, repository, or "
     "download under this name could be independently verified."),
    ("TilQazyna collections",
     "Numerous text and speech repositories appeared on Hugging Face in June-August 2026, but "
     "several are gated and their cards do not yet provide stable totals or independent "
     "documentation."),
    ("Kazakh Text Corpus / Speech Corpus / AI Evaluation Benchmark Suite",
     "Announced in July 2026 as more than 10B text tokens and 10,000 speech hours (including "
     "1,000 manually transcribed hours), but no public dataset download was identified."),
    ("Multimedia Corpus of Modern Spoken Kazakh Language",
     "The searchable project exists, but the first module's downloadable size and reuse terms "
     "could not be confirmed."),
    ("Aqbileq",
     "Named as a candidate Kazakh resource; no dataset card, repository, or paper could be "
     "independently located under this name."),
]

REPO = "Allessyer/awesome-kaz-datasets"

# Canonical task name -> short tag shown under the dataset name in the tables.
# Keep in sync with the task labels actually used in data/datasets.yaml.
TASK_ABBREV = {
    "Automatic speech recognition (ASR)": "ASR",
    "Multiple-choice QA": "MCQA",
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
    "Target-speaker ASR / speech separation": "TS-ASR",
    "Speaker verification": "SV",
    "Speech translation": "ST",
    "Spoken QA": "SQA",
    "Keyword spotting": "KWS",
    "Audio question answering": "AQA",
    "Cultural vision benchmark (text-to-image)": "T2I",
    "Audio-visual QA": "AVQA",
    "Layout analysis / document understanding": "DU",
    "Diagram QA": "DQA",
    "Visual speech recognition (lip reading)": "VSR",
}


def task_tag(task):
    return TASK_ABBREV.get(task, task)


def task_glossary(rows, cols=4):
    used = sorted({t for d in rows for t in d.get("tasks", [])}, key=lambda t: task_tag(t).lower())
    # <strong>, not **bold** — this table is a multi-line HTML block, which GitHub
    # does not run markdown-inline parsing over (see the earlier badges bug).
    entries = [f"<sub><strong>{task_tag(t)}</strong> — {t}</sub>" for t in used]
    rows_of_cells = [entries[i : i + cols] for i in range(0, len(entries), cols)]
    table_rows = []
    for row_cells in rows_of_cells:
        padded = row_cells + [""] * (cols - len(row_cells))
        table_rows.append("<tr>" + "".join(f"<td>{c}</td>" for c in padded) + "</tr>")
    return "**Abbreviations:**\n\n<table>\n" + "\n".join(table_rows) + "\n</table>"


def picture(alt, base):
    # width="100%" so every chart stretches to fill the README column at a
    # consistent scale, instead of each rendering at its own native SVG pixel
    # width (which made narrower charts, like the stat-tile overviews, look
    # small and inconsistent next to the much wider calendar/comparison charts).
    return (
        '<picture>\n'
        f'  <source media="(prefers-color-scheme: dark)" srcset="assets/{base}-dark.svg">\n'
        f'  <img src="assets/{base}.svg" alt="{alt}" width="100%">\n'
        '</picture>'
    )


DEFAULT_SKELETON = """<p align="center">
  <img src="assets/banner.png" alt="Awesome Kazakh Datasets — catalogue of datasets for Kazakh AI: Text/LLM corpora and collections, Speech ASR/TTS datasets, Vision/OCR datasets" width="100%">
</p>

<h1 align="center">Awesome Kazakh Datasets</h1>

<p align="center">
  A curated, research-grade catalog of public datasets for Kazakh-language NLP, LLM,
  speech, computer vision, OCR, and multimodal research.
</p>

<!-- BADGES:START -->
<!-- BADGES:END -->

<p align="center">
  <a href="#background">Background</a> ·
  <a href="#dataset-landscape">Dataset landscape</a> ·
  <a href="#text-nlp-and-llm">Text &amp; NLP</a> ·
  <a href="#speech-and-audio">Speech</a> ·
  <a href="#vision-ocr-and-multimodal">Vision &amp; OCR</a> ·
  <a href="#watchlist--announced-resources">Watchlist</a> ·
  <a href="#contributing">Contributing</a>
</p>

---

## Background

Kazakh is spoken by roughly 13 million people, but public, reusable datasets for
it are scattered across Hugging Face, GitHub, institutional pages, and archives
with no single map of what exists. Existing lists tend to link a dataset card and
stop there — no verified release date, no access terms, no way to tell a genuinely
open corpus from one that is merely described in an open-access paper. A
low-resource language only gets sustained NLP, speech, and vision research when
people can actually find and trust its data — a catalog that quietly links dead
downloads or overstates access just costs everyone time.

This repository tries to fix that: every entry below is checked against its
primary source (the dataset's own hosting platform, not just its rendered card;
the repository; or the paper that introduced it), and its release date, access
terms, and license are recorded rather than assumed. Where a dataset's actual
public release date differs from its Hugging Face "last modified" timestamp or
its paper's submission date — which happens more often than you'd expect — the
primary source wins, and a fact that can't be verified is recorded as *Not
reported* rather than guessed. Resources that are announced but not yet
independently verifiable go in the [Watchlist](#watchlist--announced-resources)
instead of the main tables, so "listed here" reliably means "you can actually get
this data." See [CHANGELOG.md](CHANGELOG.md) for what's new and what was corrected
and why.

In each table, the **Dataset** name links to the dataset card, repository, or
archive, and the **Author** name links to the paper (or the DOI, if there's no
paper) when one is available. **Properties** lists storage — the downloadable or
repository-hosted data volume — followed by scale: the number of samples,
utterances, hours, pages, or other published content unit. Values may change when
a living dataset is updated; **≈** denotes a publisher estimate. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the full inclusion policy, including the
exact meaning of **released** and the access classification.

### Catalog overview

<!-- DASHBOARD:START -->
<!-- DASHBOARD:END -->

## Dataset landscape

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
datasets. They are intentionally **not** part of the main catalog above.

<!-- WATCHLIST:START -->
<!-- WATCHLIST:END -->

## Inclusion and maintenance

This catalog excludes model repositories, duplicate mirrors, tokenizer-format
conversions, and tiny personal test files. Gated, application-only, and paid
research datasets are still included as long as their contents are
independently documented and their access status is clearly labeled.
Multilingual resources are included only when they expose a genuinely
accessible, identifiable Kazakh split. Full inclusion, exclusion, and
verification rules are in [CONTRIBUTING.md](CONTRIBUTING.md).

## Contributing

Missing a Kazakh dataset, or spotted outdated metadata? Contributions are welcome:

- **Add a dataset** — [open a submission issue](../../issues/new?template=dataset-submission.yml)
  or send a PR directly.
- **Fix or update an entry** — edit `data/datasets.yaml` and open a PR.
- **Report a stale number** — Hugging Face row/download counts drift; flag it
  with the current value from the
  [Dataset Server API](https://huggingface.co/docs/dataset-viewer/en/size).

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full inclusion criteria, required
metadata, and PR format.
"""

DEFAULT_SKELETON = DEFAULT_SKELETON.replace(
    "PLACEHOLDER_SPEECH_COMPARISON_IMG",
    picture(
        "Grouped vertical bars comparing public speech-data hours for Kazakh, Russian, and "
        "English across ASR, TTS, speech translation, emotion, keyword spotting, and speaker "
        "verification",
        "speech_task_hours_comparison",
    ),
)


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


def format_scale_storage(d):
    # Storage (the dataset's "weight") first, then scale — stacked, dash-prefixed.
    scale = d.get("scale") or {}
    storage = d.get("storage") or {}
    pieces = []
    st_v = storage.get("value")
    if st_v is not None:
        unit = storage.get("unit") or ""
        pieces.append(f"{st_v} {unit}".strip())
    sv = scale.get("value")
    if sv and sv != "Not reported":
        pieces.append(str(sv))
    if not pieces:
        return "Not reported"
    return "<br>".join(f"– {p}" for p in pieces)


def format_access_license(d):
    access = (d.get("access") or "unavailable").capitalize()
    license_ = d.get("license") or "Not reported"
    return f"{access} · {license_}"


def dataset_row(d):
    tags = " · ".join(task_tag(t) for t in (d.get("tasks") or [])) or "Not reported"
    data_url = (d.get("links") or {}).get("dataset")
    display_name = f"[{d['name']}]({data_url})" if data_url else d["name"]
    name_cell = f"**{display_name}**<br><sub>{tags}</sub><br><sub>{format_access_license(d)}</sub>"

    author_str, org_str = author_and_org(d)
    author_link = (d.get("links") or {}).get("paper") or (d.get("links") or {}).get("doi")
    if author_str:
        author_display = f"[{author_str}]({author_link})" if author_link else author_str
        author_cell = f"**{author_display}**"
        if org_str:
            author_cell += f"<br><sub>{org_str}</sub>"
    elif org_str:
        author_cell = f"**{org_str}**"
    else:
        author_cell = "Not reported"

    released = d.get("released") or "Not reported"
    return "| {released} | {name} | {desc} | {author} | {scale} |".format(
        released=released,
        name=name_cell,
        desc=d.get("description") or "",
        author=author_cell,
        scale=format_scale_storage(d),
    )


def dataset_table(rows):
    header = (
        "| Released | Dataset | Description | Author | Properties |\n"
        "|---|---|---|---|---|"
    )
    ordered = sorted(rows, key=released_sort_key, reverse=True)
    body = "\n".join(dataset_row(d) for d in ordered)
    return header + "\n" + body


def build_section(datasets, section):
    rows = [d for d in datasets if d["section"] == section]
    overview_base = SECTION_OVERVIEW_IMG[section]
    lines = [picture(f"{section} dataset overview", overview_base), ""]

    for stem, years in calendar_stems(rows, SECTION_CALENDAR[section]):
        year_range = f"{years[0]}" if len(years) == 1 else f"{years[0]}-{years[-1]}"
        lines.append(
            picture(
                f"Calendar map of {section} dataset releases, {year_range}, with year on the "
                "x-axis and month on the y-axis",
                stem,
            )
        )
        lines.append("")

    lines.append(task_glossary(rows))
    lines.append("")
    lines.append(dataset_table(rows))
    return "\n".join(lines)


def build_dashboard(datasets):
    return picture(
        "Catalog overview: dataset count, open-access rate, paper coverage, task count, "
        "and per-section breakdown",
        "overview_dashboard",
    )


def build_task_summary(datasets):
    counts = Counter(t for d in datasets for t in d.get("tasks", []))
    chips = " · ".join(f"{task} ({count})" for task, count in counts.most_common())
    return f"<sub>**Datasets per task** — {chips}</sub>"


def build_landscape(datasets):
    # Plain markdown, not wrapped in a <p>/<sub> block: a multi-line HTML block
    # is not markdown-parsed by GitHub, so bold task names would render as
    # literal "**text**" instead of bold (the same bug the badges had).
    lines = [
        picture("Cumulative Kazakh dataset releases over time, by section", "dataset_growth"),
        "",
        build_task_summary(datasets),
    ]
    return "\n".join(lines)


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
        ("Last verified", "2026--08--19", "1baf7a"),
        ("Open access", f"{open_pct}%25", "2ea44f"),
    ]
    parts = [stars] + [
        f'<img alt="{label}" src="https://img.shields.io/badge/{label.replace(" ", "_")}-{value}-{color}">'
        for label, value, color in badges
    ]
    return '<p align="center">\n  ' + "\n  ".join(parts) + "\n</p>"


def build_watchlist():
    return "\n".join(f"- **{name}** — {reason}" for name, reason in WATCHLIST)


BLOCKS = {
    "BADGES": build_badges,
    "DASHBOARD": build_dashboard,
    "LANDSCAPE": build_landscape,
    "NLP_SECTION": lambda datasets: build_section(datasets, "Text, NLP, and LLM"),
    "SPEECH_SECTION": lambda datasets: build_section(datasets, "Speech and audio"),
    "VISION_SECTION": lambda datasets: build_section(datasets, "Vision, OCR, and multimodal"),
    "WATCHLIST": lambda datasets: build_watchlist(),
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
    # If the existing file predates markers, fall back to the skeleton.
    if "<!-- DASHBOARD:START -->" not in base:
        base = DEFAULT_SKELETON

    new_content = apply_blocks(base, datasets)

    if check:
        if README.exists() and README.read_text(encoding="utf-8") == new_content:
            print("OK: README.md is up to date.")
            return 0
        print("STALE: README.md does not match generated output. Run scripts/generate_readme.py.")
        return 1

    README.write_text(new_content, encoding="utf-8")
    print(f"Wrote {README}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
