#!/usr/bin/env python3
"""Generate dependency-free SVG comparisons of documented reference datasets."""

from html import escape
from math import log10
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
COLORS = {"English": "#2563eb", "Russian": "#dc2626", "Kazakh": "#0891b2"}


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


if __name__ == "__main__":
    main()
