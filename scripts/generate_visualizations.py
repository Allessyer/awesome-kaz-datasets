#!/usr/bin/env python3
"""Generate all SVG visualizations for the README from data/datasets.yaml.

Deterministic: same input always produces byte-identical output. No network access.

Every chart is rendered twice — a light variant (`name.svg`) and a dark variant
(`name-dark.svg`) — using the same validated categorical palette stepped for each
surface. README.md embeds both via `<picture>`/`prefers-color-scheme` so the chart
matches the reader's browser theme.
"""

from collections import Counter, defaultdict
from html import escape
from math import log10
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "datasets.yaml"
OUT = ROOT / "assets"

FONT = 'font-family:"Segoe UI",Inter,Arial,sans-serif'

SECTIONS = ["Text, NLP, and LLM", "Speech and audio", "Vision, OCR, and multimodal"]
SECTION_SHORT = {SECTIONS[0]: "Text/NLP", SECTIONS[1]: "Speech", SECTIONS[2]: "Vision"}
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# --- palette: validated categorical order (first three slots are all-pairs safe) ---
THEMES = {
    "light": {
        "surface": "#fcfcfb",
        "ink": "#0b0b0b",
        "ink_secondary": "#52514e",
        "ink_muted": "#898781",
        "grid": "#e1e0d9",
        "tile_stroke": "#e1e0d9",
        "blue": "#164a89",
        "orange": "#9a4422",
        "aqua": "#127250",
        "good": "#0ca30c",
        "na_fill": "#f3f2ee",
        "na_stroke": "#b9b7ae",
        "seq": ["#cde2fb", "#9ec5f4", "#5598e7", "#2a78d6", "#184f95"],
        "seq_text_dark_from": 2,  # index at which cell text should turn white
    },
    "dark": {
        "surface": "#1a1a19",
        "ink": "#ffffff",
        "ink_secondary": "#c3c2b7",
        "ink_muted": "#898781",
        "grid": "#2c2c2a",
        "tile_stroke": "#383835",
        "blue": "#3987e5",
        "orange": "#d95926",
        "aqua": "#199e70",
        "good": "#0ca30c",
        "na_fill": "#242422",
        "na_stroke": "#52514e",
        "seq": ["#184f95", "#1c5cab", "#256abf", "#3987e5", "#86b6ef"],
        "seq_text_dark_from": 3,
    },
}

LANG_NAMES = ("Kazakh", "Russian", "English")
LANG_SHORT = {"Kazakh": "kk", "Russian": "ru", "English": "eng"}


def load_datasets():
    doc = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    return doc["datasets"]


def year_of(released):
    if not released or released == "Not reported":
        return None
    return int(str(released)[:4])


def month_of(released):
    if not released or released == "Not reported" or len(str(released)) < 7:
        return None
    return int(str(released)[5:7])


def write_both(basename, render):
    """render(theme_dict) -> list[str] of SVG lines. Writes light + dark variants."""
    stem = basename[:-4] if basename.endswith(".svg") else basename
    for theme_name, palette in THEMES.items():
        lines = render(palette)
        suffix = "" if theme_name == "light" else "-dark"
        (OUT / f"{stem}{suffix}.svg").write_text("\n".join(lines) + "\n", encoding="utf-8")


def svg_header(width, height, t, extra_style=""):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="{width}" height="{height}" fill="{t["surface"]}"/>',
        f'<style>text{{{FONT};fill:{t["ink"]}}}'
        f'.title{{font-size:22px;font-weight:700}}'
        f'.sub{{font-size:12px;fill:{t["ink_secondary"]}}}'
        f'.muted{{font-size:11px;fill:{t["ink_muted"]}}}'
        f'.stat-label{{font-size:12px;fill:{t["ink_secondary"]};font-weight:600}}'
        f'.stat-value{{font-size:28px;font-weight:700}}'
        f'.axis{{font-size:12px;fill:{t["ink_muted"]}}}'
        f'.grid{{stroke:{t["grid"]};stroke-width:1}}'
        f'.legend{{font-size:12px;fill:{t["ink_secondary"]}}}'
        f'{extra_style}</style>',
    ]


# ---------------------------------------------------------------------------
# Stat-tile row — used for overview_dashboard.svg and the three *_overview.svg.
# No title baked into the image; README supplies the caption as markdown text.
# ---------------------------------------------------------------------------

def stat_tile_row(basename, tiles, footer_rows=None):
    def render(t):
        tile_w, tile_h = 176, 96
        gap = 14
        left, top, right = 20, 20, 20
        width = left + len(tiles) * tile_w + (len(tiles) - 1) * gap + right
        footer_h = 0
        if footer_rows:
            footer_h = 30 + len(footer_rows) * 32
        height = top + tile_h + footer_h + 20

        parts = svg_header(width, height, t)

        x = left
        for label, value, color_key in tiles:
            parts.append(f'<rect x="{x}" y="{top}" width="{tile_w}" height="{tile_h}" rx="10" fill="{t["surface"]}" stroke="{t["tile_stroke"]}" stroke-width="1"/>')
            c = t[color_key] if color_key else t["ink"]
            cx = x + tile_w / 2
            parts.append(f'<text x="{cx}" y="{top+44}" text-anchor="middle" class="stat-value" fill="{c}">{escape(str(value))}</text>')
            parts.append(f'<text x="{cx}" y="{top+70}" text-anchor="middle" class="stat-label">{escape(label)}</text>')
            x += tile_w + gap

        if footer_rows:
            fy = top + tile_h + 34
            for row_label, entries in footer_rows:
                parts.append(f'<text x="{left}" y="{fy}" class="stat-label">{escape(row_label)}</text>')
                bx = left + 130
                bar_w = width - right - bx
                total = sum(c for _, _, c in entries) or 1
                seg_x = bx
                for name, color_key, count in entries:
                    w = max(2, count / total * bar_w)
                    parts.append(f'<rect x="{seg_x}" y="{fy-14}" width="{max(0,w-2)}" height="18" rx="4" fill="{t[color_key]}"/>')
                    seg_x += w
                legend_x = bx
                ly = fy + 18
                for name, color_key, count in entries:
                    parts.append(f'<rect x="{legend_x}" y="{ly-9}" width="9" height="9" rx="2" fill="{t[color_key]}"/>')
                    label_text = f"{name} ({count})"
                    parts.append(f'<text x="{legend_x+13}" y="{ly}" class="legend">{escape(label_text)}</text>')
                    legend_x += 20 + 7 * len(label_text)
                fy += 32

        parts.append("</svg>")
        return parts

    write_both(basename, render)


def section_stats(datasets, section):
    rows = [d for d in datasets if d["section"] == section]
    n = len(rows)
    open_n = sum(1 for d in rows if d["access"] == "open")
    papers_n = sum(1 for d in rows if d.get("paper"))
    tasks_n = len({t for d in rows for t in d.get("tasks", [])})
    return rows, n, open_n, papers_n, tasks_n


def gen_overview_dashboard(datasets):
    n = len(datasets)
    open_n = sum(1 for d in datasets if d["access"] == "open")
    papers_n = sum(1 for d in datasets if d.get("paper"))
    licensed_n = sum(1 for d in datasets if d.get("license") and d["license"] != "Not reported")
    tasks_n = len({t for d in datasets for t in d.get("tasks", [])})

    tiles = [
        ("Datasets", str(n), None),
        ("Open access", f"{round(100*open_n/n)}%", "good"),
        ("With a paper", f"{round(100*papers_n/n)}%", None),
        ("Tasks covered", str(tasks_n), None),
        ("Explicit license", f"{round(100*licensed_n/n)}%", None),
    ]
    footer = [("By section", [
        (SECTION_SHORT[s], key, sum(1 for d in datasets if d["section"] == s))
        for s, key in zip(SECTIONS, ("blue", "orange", "aqua"))
    ])]
    stat_tile_row("overview_dashboard.svg", tiles, footer)


def gen_section_overview(datasets, section, filename):
    rows, n, open_n, papers_n, tasks_n = section_stats(datasets, section)
    tiles = [
        ("Datasets", str(n), None),
        ("Open access", f"{round(100*open_n/n)}%" if n else "0%", "good"),
        ("Tasks covered", str(tasks_n), None),
        ("With a paper", f"{round(100*papers_n/n)}%" if n else "0%", None),
    ]
    stat_tile_row(filename, tiles)


# ---------------------------------------------------------------------------
# Release calendar (per section) — sequential blue heat by releases/month.
# ---------------------------------------------------------------------------

def _wrap_name(name, max_chars):
    """Greedy word-wrap so long dataset names never overflow a calendar cell."""
    if len(name) <= max_chars:
        return [name]
    words = name.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= max_chars or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# Solid, high-contrast fill per section identity (instead of a subtle multi-step
# blue heat ramp, which several readers found too monotone/hard to read at a
# glance). Text color per accent is picked for contrast, not computed at
# render time, since we only ever draw on these three accents per theme.
TEXT_ON_ACCENT = {
    "light": {"blue": "#ffffff", "orange": "#ffffff", "aqua": "#ffffff"},
    "dark": {"blue": "#1a1a19", "orange": "#1a1a19", "aqua": "#1a1a19"},
}


def chunk_years(years, max_size=5):
    """Split a sorted year list into near-equal chunks of at most max_size years,
    so a calendar with a wide year span doesn't get squeezed down to illegible
    text when GitHub scales a very wide image to fit the README column."""
    n = len(years)
    if n <= max_size:
        return [years]
    num_chunks = -(-n // max_size)  # ceil division
    base, rem = divmod(n, num_chunks)
    chunks, i = [], 0
    for c in range(num_chunks):
        size = base + (1 if c < rem else 0)
        chunks.append(years[i : i + size])
        i += size
    return chunks


def calendar_stems(section_datasets, base_stem):
    """The list of (stem, years) this section's calendar is split into. Both
    generate_visualizations.py and generate_readme.py call this so the file
    names and the README's <picture> embeds always agree."""
    years = sorted({year_of(d["released"]) for d in section_datasets if month_of(d["released"])})
    chunks = chunk_years(years)
    if len(chunks) == 1:
        return [(base_stem, chunks[0])]
    return [(f"{base_stem}_{i+1}", chunk) for i, chunk in enumerate(chunks)]


def gen_release_calendar(datasets, section, filename, accent_key):
    section_datasets = [d for d in datasets if d["section"] == section]
    rows = [(d["released"], d["name"]) for d in section_datasets if month_of(d["released"])]
    grouped = defaultdict(list)
    for released, name in rows:
        grouped[(year_of(released), month_of(released))].append(name)

    base_stem = filename[:-4] if filename.endswith(".svg") else filename

    for stem, years in calendar_stems(section_datasets, base_stem):
        months = sorted({m for (y, m) in grouped if y in years})

        cell_w = 250
        name_font = 14
        line_h = 20
        max_chars = int((cell_w - 24) / (name_font * 0.52))
        wrapped = {key: [_wrap_name(name, max_chars) for name in names] for key, names in grouped.items() if key[0] in years}
        row_heights = {
            m: max(56, 24 + max((sum(len(w) for w in wrapped.get((y, m), [])) for y in years), default=0) * line_h)
            for m in months
        }

        def render(t, theme_name, years=years, months=months, wrapped=wrapped, row_heights=row_heights):
            left, top, right, bottom = 92, 50, 20, 20
            width = left + len(years) * cell_w + right
            height = top + sum(row_heights.values()) + bottom

            parts = svg_header(width, height, t, f'.name{{font-size:{name_font}px;font-weight:700}}.year{{font-size:20px;font-weight:700}}')

            fill = t[accent_key]
            text_color = TEXT_ON_ACCENT[theme_name][accent_key]

            for col, year in enumerate(years):
                x = left + col * cell_w
                parts.append(f'<text x="{x + cell_w/2}" y="{top-20}" text-anchor="middle" class="year">{year}</text>')
                y = top
                for m in months:
                    cell_h = row_heights[m]
                    names = grouped.get((year, m), [])
                    cell_fill = fill if names else t["surface"]
                    parts.append(f'<rect x="{x}" y="{y}" width="{cell_w-4}" height="{cell_h-4}" rx="6" fill="{cell_fill}" stroke="{t["grid"]}" stroke-width="1"/>')
                    line_y = y + 24
                    for lines in wrapped.get((year, m), []):
                        for line in lines:
                            parts.append(f'<text x="{x+12}" y="{line_y}" class="name" fill="{text_color}">{escape(line)}</text>')
                            line_y += line_h
                    y += cell_h

            y = top
            for m in months:
                cell_h = row_heights[m]
                parts.append(f'<text x="{left-14}" y="{y+cell_h/2+5}" text-anchor="end" class="axis">{MONTHS[m-1]}</text>')
                y += cell_h

            parts.append("</svg>")
            return parts

        for theme_name, palette in THEMES.items():
            suffix = "" if theme_name == "light" else "-dark"
            (OUT / f"{stem}{suffix}.svg").write_text("\n".join(render(palette, theme_name)) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Dataset growth (cumulative releases over time, one line per section)
# ---------------------------------------------------------------------------

def gen_dataset_growth(datasets):
    by_section = defaultdict(list)
    for d in datasets:
        y = year_of(d["released"])
        if y:
            by_section[d["section"]].append(y)

    all_years = sorted({y for ys in by_section.values() for y in ys})
    if not all_years:
        return
    year_range = list(range(all_years[0], all_years[-1] + 1))

    series = {}
    for section in SECTIONS:
        counts = Counter(by_section.get(section, []))
        cumulative, running = [], 0
        for y in year_range:
            running += counts.get(y, 0)
            cumulative.append(running)
        series[section] = cumulative

    max_val = max(v for vals in series.values() for v in vals) or 1

    def render(t):
        left, top, right, bottom = 50, 30, 150, 40
        plot_w, plot_h = max(560, 70 * len(year_range)), 300
        width, height = left + plot_w + right, top + plot_h + bottom

        parts = svg_header(width, height, t, ".endlabel{font-size:12px;font-weight:700}")

        baseline = top + plot_h
        for i in range(5):
            v = round(max_val * i / 4)
            y = baseline - (v / max_val) * plot_h
            parts.append(f'<line x1="{left}" y1="{y}" x2="{left+plot_w}" y2="{y}" class="grid"/>')
            parts.append(f'<text x="{left-10}" y="{y+4}" text-anchor="end" class="axis">{v}</text>')

        def px(i):
            return left + (i / max(1, len(year_range) - 1)) * plot_w

        for i, y in enumerate(year_range):
            if i % max(1, len(year_range) // 10) == 0 or i == len(year_range) - 1:
                parts.append(f'<text x="{px(i)}" y="{baseline+22}" text-anchor="middle" class="axis">{y}</text>')

        for section, key in zip(SECTIONS, ("blue", "orange", "aqua")):
            color = t[key]
            vals = series[section]
            points = " ".join(f"{px(i)},{baseline - (v/max_val)*plot_h}" for i, v in enumerate(vals))
            parts.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
            last_x, last_y = px(len(vals) - 1), baseline - (vals[-1] / max_val) * plot_h
            parts.append(f'<circle cx="{last_x}" cy="{last_y}" r="4" fill="{color}" stroke="{t["surface"]}" stroke-width="2"/>')
            parts.append(f'<text x="{last_x+10}" y="{last_y+4}" class="endlabel" fill="{color}">{SECTION_SHORT[section]} ({vals[-1]})</text>')

        parts.append("</svg>")
        return parts

    write_both("dataset_growth.svg", render)


# ---------------------------------------------------------------------------
# EN/RU/KK reference comparisons — manually curated external benchmarks. These
# are conservative, deduplicated lower bounds, not a claim about every corpus
# in existence; the sourcing/dedup rules are recorded in git history rather
# than reproduced in the README.
# ---------------------------------------------------------------------------

def compact(value):
    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}K"
    return f"{value:g}"


def vertical_bars(basename, subtitle, groups, unit):
    positive = [value for _, rows in groups for _, value in rows if value is not None and value > 0]
    max_log = int(log10(max(positive))) + 1
    lang_key = {"Kazakh": "blue", "Russian": "orange", "English": "aqua"}

    def render(t):
        left, top, right, bottom = 80, 60, 20, 76
        group_w, plot_h = 190, 400
        width = max(760, left + len(groups) * group_w + right)
        height = top + plot_h + bottom

        parts = svg_header(
            width, height, t,
            ".task{font-size:12px;font-weight:700}.lang{font-size:10px;font-weight:700;fill:" + t["ink_muted"] + "}"
            ".value{font-size:10px;font-weight:700}.na{stroke-dasharray:4 3}",
        )
        parts.append(f'<text x="20" y="20" class="muted">{escape(subtitle)}</text>')

        baseline = top + plot_h
        for exponent in range(max_log + 1):
            y = baseline - exponent / max_log * plot_h
            parts.append(f'<line x1="{left}" y1="{y}" x2="{width-right}" y2="{y}" class="grid"/>')
            parts.append(f'<text x="{left-9}" y="{y+4}" text-anchor="end" class="axis">10^{exponent}</text>')

        bar_w, gap = 34, 6
        for group_index, (task, rows) in enumerate(groups):
            available_w = width - left - right
            center = left + (group_index + .5) * available_w / len(groups)
            start = center - (3 * bar_w + 2 * gap) / 2
            for row_index, (language, value) in enumerate(rows):
                x = start + row_index * (bar_w + gap)
                if value is None:
                    parts.append(f'<rect x="{x}" y="{baseline-26}" width="{bar_w}" height="26" fill="{t["na_fill"]}" stroke="{t["na_stroke"]}" class="na"/>')
                    parts.append(f'<text x="{x+bar_w/2}" y="{baseline-10}" text-anchor="middle" class="value">N/A</text>')
                else:
                    bar_h = max(3, log10(value) / max_log * plot_h)
                    y = baseline - bar_h
                    parts.append(f'<rect x="{x}" y="{y}" width="{bar_w}" height="{bar_h}" rx="4" fill="{t[lang_key[language]]}"/>')
                    parts.append(f'<text x="{x+bar_w/2}" y="{max(top+10, y-6)}" text-anchor="middle" class="value">{compact(value)}</text>')
                parts.append(f'<text x="{x+bar_w/2}" y="{baseline+18}" text-anchor="middle" class="lang">{LANG_SHORT[language]}</text>')
            parts.append(f'<text x="{center}" y="{baseline+43}" text-anchor="middle" class="task">{escape(task)}</text>')

        legend_x = width - right - 3 * 100
        for language in LANG_NAMES:
            parts.append(f'<rect x="{legend_x}" y="{top-38}" width="10" height="10" rx="2" fill="{t[lang_key[language]]}"/>')
            parts.append(f'<text x="{legend_x+14}" y="{top-29}" class="legend">{language}</text>')
            legend_x += 100

        parts.append("</svg>")
        return parts

    write_both(basename, render)


def gen_speech_task_hours_comparison():
    vertical_bars(
        "speech_task_hours_comparison.svg",
        "Conservative, deduplicated lower bounds; not a claim about every corpus in existence.",
        [
            ("ASR", [("Kazakh", 2_358.5), ("Russian", 21_530.23), ("English", 60_670)]),
            ("TTS", [("Kazakh", 945.85), ("Russian", 6_083), ("English", 36_700)]),
            ("Speech translation", [("Kazakh", 57), ("Russian", 38.7), ("English", 10_508)]),
            ("Emotion", [("Kazakh", 74.85), ("Russian", 350), ("English", 421)]),
            ("Keyword spotting", [("Kazakh", 1), ("Russian", 137), ("English", 1_986.4)]),
            ("Speaker verification*", [("Kazakh", 600), ("Russian", 22_052), ("English", 18_826.86)]),
        ],
        "hours",
    )


def gen_spoken_qa_comparison():
    vertical_bars(
        "spoken_qa_samples_comparison.svg",
        "Hours are not published consistently, so this panel compares documented question/example counts.",
        [("Spoken QA", [("Kazakh", 3_156), ("Russian", 900), ("English", 900)])],
        "samples",
    )


def main():
    OUT.mkdir(exist_ok=True)
    datasets = load_datasets()

    gen_overview_dashboard(datasets)
    gen_dataset_growth(datasets)

    gen_section_overview(datasets, SECTIONS[0], "nlp_overview.svg")
    gen_section_overview(datasets, SECTIONS[1], "speech_overview.svg")
    gen_section_overview(datasets, SECTIONS[2], "vision_overview.svg")

    gen_release_calendar(datasets, SECTIONS[0], "nlp_release_calendar.svg", "blue")
    gen_release_calendar(datasets, SECTIONS[1], "speech_release_calendar.svg", "orange")
    gen_release_calendar(datasets, SECTIONS[2], "cv_release_calendar.svg", "aqua")

    gen_speech_task_hours_comparison()
    gen_spoken_qa_comparison()

    print(f"Wrote visualizations (light + dark) to {OUT}")


if __name__ == "__main__":
    main()
