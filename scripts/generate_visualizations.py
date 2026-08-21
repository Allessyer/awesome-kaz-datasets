#!/usr/bin/env python3
"""Generate all SVG visualizations for the README from data/datasets.yaml.

Deterministic: same input always produces byte-identical output. No network access.

Every chart is rendered twice — a light variant (`name.svg`) and a dark variant
(`name-dark.svg`) — using the same validated categorical palette. README.md embeds
both via `<picture>`/`prefers-color-scheme` so the chart matches the reader's
browser theme.
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
        "na_stroke": "#e1e0d9",
        # A darker/more saturated 5-step blue ramp (ColorBrewer Blues,
        # palest step dropped) for good step-to-step distinction. The legend
        # no longer prints numbers on top of these fills (see the heatmap
        # legend below), so there's no text-contrast constraint on the
        # palette itself anymore.
        "seq": ["#c6dbef", "#9ecae1", "#6baed6", "#3182bd", "#08519c"],
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
        "na_stroke": "#383835",
        # Brightest step = most releases — the opposite direction from the
        # light ramp on purpose: on a near-black surface, going *darker*
        # for "more" makes the busiest cells fade into the background
        # instead of standing out (checked — with an earlier "more =
        # darker" version, the busiest cells were nearly invisible next to
        # empty ones). No text-contrast constraint on this palette either
        # (see the light theme's note above).
        "seq": ["#2c5580", "#2f6bab", "#2f83d6", "#3f9df0", "#6dc3ff"],
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
        f'.axis{{font-size:12px;fill:{t["ink_muted"]}}}'
        f'.grid{{stroke:{t["grid"]};stroke-width:1}}'
        f'.legend{{font-size:12px;fill:{t["ink_secondary"]}}}'
        f'{extra_style}</style>',
    ]


# ---------------------------------------------------------------------------
# Release heatmap (per section) — year x month grid, cell shade = release
# count that month. No dataset names on the image; exact counts are printed
# in each non-empty cell instead.
# ---------------------------------------------------------------------------

def gen_release_heatmap(datasets, section, filename):
    section_datasets = [d for d in datasets if d["section"] == section]
    counts = Counter()
    for d in section_datasets:
        y, m = year_of(d["released"]), month_of(d["released"])
        if y and m:
            counts[(y, m)] += 1
    if not counts:
        return

    years = list(range(min(y for y, _ in counts), max(y for y, _ in counts) + 1))
    max_n = max(counts.values())

    def render(t):
        # Cells are wider than tall (not square) so the grid reads as a wide
        # landscape strip — matching the wide README column — rather than a
        # small near-square block. Sized close to a typical rendered README
        # column width (~860-900px) so the width:100% stretch in the README
        # scales it up only slightly instead of blowing sparse sections
        # (fewer years = fewer rows, same fixed width) up into oversized cells.
        cell_w, cell_h, gap = 60, 26, 6
        step_x, step_y = cell_w + gap, cell_h + gap
        left, top, right = 56, 30, 20
        legend_h = 50
        bottom = 20 + legend_h
        width = left + 12 * step_x + right
        height = top + len(years) * step_y + bottom

        parts = svg_header(
            width, height, t,
            ".count{font-size:10px;font-weight:700}"
            f'.axis-strong{{font-size:12px;font-weight:700;fill:{t["ink_secondary"]}}}',
        )

        for col, month in enumerate(range(1, 13)):
            x = left + col * step_x
            parts.append(f'<text x="{x + cell_w/2}" y="{top - 10}" text-anchor="middle" class="axis-strong">{MONTHS[month-1]}</text>')

        for row, year in enumerate(years):
            y = top + row * step_y
            parts.append(f'<text x="{left - 10}" y="{y + cell_h/2 + 4}" text-anchor="end" class="axis-strong">{year}</text>')
            for col, month in enumerate(range(1, 13)):
                x = left + col * step_x
                n = counts.get((year, month), 0)
                if n == 0:
                    parts.append(f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" rx="5" fill="{t["na_fill"]}" stroke="{t["na_stroke"]}" stroke-width="1"/>')
                    continue
                idx = min(n - 1, len(t["seq"]) - 1)
                parts.append(f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" rx="5" fill="{t["seq"][idx]}"/>')

        # Count labels sit below each swatch, in the theme's normal text
        # color on the plain surface — not printed on top of the fill —
        # so there's no per-swatch text-contrast problem to solve at all.
        legend_y = top + len(years) * step_y + 20
        legend_label = "Releases/month:"
        parts.append(f'<text x="{left}" y="{legend_y + 9}" class="legend">{legend_label}</text>')
        lx = left + 11 * 7 + 14
        for i in range(min(max_n, len(t["seq"]))):
            fill = t["seq"][i]
            label = str(i + 1) if i < len(t["seq"]) - 1 or max_n <= len(t["seq"]) else f"{i+1}+"
            parts.append(f'<rect x="{lx}" y="{legend_y - 2}" width="16" height="16" rx="4" fill="{fill}"/>')
            parts.append(f'<text x="{lx+8}" y="{legend_y+30}" text-anchor="middle" class="legend">{label}</text>')
            lx += 24

        parts.append("</svg>")
        return parts

    write_both(filename, render)


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
        plot_w, plot_h = max(560, 70 * len(year_range)), 260
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
        group_w, plot_h = 190, 340
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


def main():
    OUT.mkdir(exist_ok=True)
    datasets = load_datasets()

    gen_dataset_growth(datasets)

    gen_release_heatmap(datasets, SECTIONS[0], "nlp_release_heatmap.svg")
    gen_release_heatmap(datasets, SECTIONS[1], "speech_release_heatmap.svg")
    gen_release_heatmap(datasets, SECTIONS[2], "cv_release_heatmap.svg")

    gen_speech_task_hours_comparison()

    print(f"Wrote visualizations (light + dark) to {OUT}")


if __name__ == "__main__":
    main()
