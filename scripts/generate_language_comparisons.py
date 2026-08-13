#!/usr/bin/env python3
"""Generate dependency-free SVG comparisons of documented reference datasets."""

from html import escape
from math import log10
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
COLORS = {"English": "#2563eb", "Russian": "#dc2626", "Kazakh": "#0891b2"}
SHORT = {"English": "eng", "Russian": "ru", "Kazakh": "kz"}


def compact(value):
    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}K"
    return f"{value:g}"


def grouped_bars(filename, title, subtitle, groups, unit):
    left, top, right, bottom = 170, 112, 40, 42
    plot_w, group_h = 760, 112
    width, height = left + plot_w + right, top + len(groups) * group_h + bottom
    maximum = max(value for _, rows in groups for _, value, _ in rows)
    max_log = log10(maximum)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fff"/>',
        '<style>text{font-family:Inter,Segoe UI,Arial,sans-serif;fill:#172033}.title{font-size:27px;font-weight:700}.sub{font-size:12px;fill:#5b6472}.group{font-size:15px;font-weight:700}.label{font-size:12px}.value{font-size:11px;font-weight:700;fill:#fff}.grid{stroke:#dfe3e8;stroke-width:1}.bar{opacity:.9}</style>',
        f'<text x="24" y="38" class="title">{escape(title)}</text>',
        f'<text x="24" y="64" class="sub">{escape(subtitle)}</text>',
        '<text x="24" y="84" class="sub">Logarithmic bar length; exact values are printed on every bar.</text>',
    ]
    for exponent in range(0, int(max_log) + 1):
        x = left + (exponent / max_log) * plot_w
        parts.append(f'<line x1="{x}" y1="{top-8}" x2="{x}" y2="{height-bottom}" class="grid"/>')
        parts.append(f'<text x="{x}" y="{top-15}" text-anchor="middle" class="sub">10^{exponent}</text>')
    for group_index, (group, rows) in enumerate(groups):
        base_y = top + group_index * group_h
        parts.append(f'<text x="24" y="{base_y+16}" class="group">{escape(group)}</text>')
        for row_index, (language, value, dataset) in enumerate(rows):
            y = base_y + 28 + row_index * 25
            bar_w = max(2, log10(value) / max_log * plot_w)
            parts.append(f'<text x="{left-10}" y="{y+10}" text-anchor="end" class="label">{language}</text>')
            parts.append(f'<rect x="{left}" y="{y}" width="{bar_w}" height="16" rx="3" fill="{COLORS[language]}" class="bar"/>')
            value_label = f"{compact(value)} {unit} · {dataset}"
            parts.append(f'<text x="{left+bar_w-7}" y="{y+12}" text-anchor="end" class="value">{escape(value_label)}</text>')
    parts.append('</svg>')
    (OUT / filename).write_text("\n".join(parts) + "\n")


def vertical_bars(filename, title, subtitle, groups, unit, missing=None):
    """Draw grouped vertical bars with a shared logarithmic y-axis."""
    missing = missing or set()
    left, top, right, bottom = 86, 108, 28, 96
    group_w, plot_h = 190, 430
    width = max(760, left + len(groups) * group_w + right)
    height = top + plot_h + bottom
    positive = [value for _, rows in groups for language, value in rows if value is not None]
    max_log = int(log10(max(positive))) + 1
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fff"/>',
        '<style>text{font-family:Inter,Segoe UI,Arial,sans-serif;fill:#172033}.title{font-size:25px;font-weight:700}.sub{font-size:11px;fill:#5b6472}.task{font-size:12px;font-weight:700}.lang{font-size:10px;font-weight:700}.value{font-size:10px;font-weight:700}.grid{stroke:#dfe3e8;stroke-width:1}.na{fill:#f3f4f6;stroke:#9ca3af;stroke-dasharray:4 3}</style>',
        f'<text x="24" y="36" class="title">{escape(title)}</text>',
        f'<text x="24" y="61" class="sub">{escape(subtitle)}</text>',
        f'<text x="24" y="80" class="sub">Logarithmic y-axis; totals are conservative deduplicated lower bounds ({unit}).</text>',
    ]
    baseline = top + plot_h
    for exponent in range(max_log + 1):
        y = baseline - exponent / max_log * plot_h
        parts.append(f'<line x1="{left}" y1="{y}" x2="{width-right}" y2="{y}" class="grid"/>')
        parts.append(f'<text x="{left-9}" y="{y+4}" text-anchor="end" class="sub">10^{exponent}</text>')
    bar_w, gap = 38, 8
    for group_index, (task, rows) in enumerate(groups):
        available_w = width - left - right
        center = left + (group_index + .5) * available_w / len(groups)
        start = center - (3 * bar_w + 2 * gap) / 2
        for row_index, (language, value) in enumerate(rows):
            x = start + row_index * (bar_w + gap)
            if value is None:
                parts.append(f'<rect x="{x}" y="{baseline-26}" width="{bar_w}" height="26" class="na"/>')
                parts.append(f'<text x="{x+bar_w/2}" y="{baseline-10}" text-anchor="middle" class="value">N/A</text>')
            else:
                bar_h = max(3, log10(value) / max_log * plot_h)
                y = baseline - bar_h
                parts.append(f'<rect x="{x}" y="{y}" width="{bar_w}" height="{bar_h}" rx="3" fill="{COLORS[language]}"/>')
                parts.append(f'<text x="{x+bar_w/2}" y="{max(top+10, y-6)}" text-anchor="middle" class="value">{compact(value)}</text>')
            parts.append(f'<text x="{x+bar_w/2}" y="{baseline+18}" text-anchor="middle" class="lang">{SHORT[language]}</text>')
        parts.append(f'<text x="{center}" y="{baseline+43}" text-anchor="middle" class="task">{escape(task)}</text>')
    parts.append('</svg>')
    (OUT / filename).write_text("\n".join(parts) + "\n")


def main():
    OUT.mkdir(exist_ok=True)
    grouped_bars(
        "language_comparison_nlp.svg",
        "Reference QA dataset scale by language",
        "One documented public reference dataset per language; counts are questions or QA pairs, not total language supply.",
        [("QA samples", [
            ("English", 107_785, "SQuAD 1.1"),
            ("Russian", 379_284, "Russian Jeopardy"),
            ("Kazakh", 51_422, "Zerde-QA-50K"),
        ])],
        "samples",
    )
    grouped_bars(
        "language_comparison_speech.svg",
        "Reference speech dataset scale by language",
        "Representative public corpora by intended use; hours are not summed because releases and derivatives can overlap.",
        [
            ("ASR", [
                ("English", 10_000, "GigaSpeech XL"),
                ("Russian", 20_000, "Open STT"),
                ("Kazakh", 1_200, "KSC2"),
            ]),
            ("TTS / TTS-grade", [
                ("English", 585, "LibriTTS"),
                ("Russian", 6_052, "YO-CPT-ru"),
                ("Kazakh", 600, "YO-CPT-kk"),
            ]),
        ],
        "hours",
    )
    grouped_bars(
        "language_comparison_cv.svg",
        "Reference visual-QA dataset scale by language",
        "One documented public VQA reference per language; counts are questions/examples and task scopes differ.",
        [("Visual question answering", [
            ("English", 614_163, "VQA v1 real images"),
            ("Russian", 3_025, "ruCommonVQA"),
            ("Kazakh", 4_329, "MMBench Kazakh"),
        ])],
        "questions",
    )
    vertical_bars(
        "speech_task_hours_comparison.svg",
        "Public speech-data hours by task and language",
        "kz = Kazakh · ru = Russian · eng = English · exact corpus decisions are documented in speech_language_comparison.md",
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
    vertical_bars(
        "spoken_qa_samples_comparison.svg",
        "Public spoken-QA samples by language",
        "Hours are not published consistently, so this panel compares documented question/example counts.",
        [("Spoken QA", [("Kazakh", 3_156), ("Russian", 900), ("English", 900)])],
        "samples",
    )


if __name__ == "__main__":
    main()
