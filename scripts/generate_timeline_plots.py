#!/usr/bin/env python3
"""Generate dependency-free SVG timeline/size plots for the README."""

from __future__ import annotations

import datetime as dt
import html
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"

NLP = [
    ("2015-06", "UD Kazakh KTB", 1078, "1,078 sentences"),
    ("2020-12", "KazNewsDataset", 4365, "4,365 articles"),
    ("2020-12", "KazRusNewsDataset", 20409, "20,409 articles"),
    ("2021-11", "KazNERD", 112702, "112,702 sentences"),
    ("2023-04", "MDBKD", 24883808, "24.9M texts"),
    ("2024-02", "Kazakh–English KAZNU", 377044, "377,044 pairs"),
    ("2024-03", "Kazakh–Russian KAZNU", 86453, "86,453 pairs"),
    ("2024-03", "KazParC", 372000, "372,000 pairs"),
    ("2024-04", "KazQAD", 6000, "6,000 questions"),
    ("2024-11", "MMLU Translated KK", 15854, "15,854 questions"),
    ("2024-11", "GSM8K Translated KK", 8792, "8,792 questions"),
    ("2024-11", "Kazakh Dastur MC", 1005, "1,005 questions"),
    ("2024-11", "Kazakh Constitution MC", 414, "414 questions"),
    ("2024-11", "Kazakh UNT", 14850, "14,850 questions"),
    ("2025-01", "KazMMLU", 23000, "23,000 questions"),
    ("2025-02", "Qorgau", 2790, "2,790 prompts"),
    ("2025-10", "KazCulture", 16137, "16,137 triplets"),
    ("2026-04", "Zerde-QA-50K", 51422, "51,422 pairs"),
    ("2026-05", "KazLawBench", 3098, "3,098 questions"),
    ("2026-06", "Kazakh Open Retrieval", 300, "300 queries"),
    ("2026-06", "FreshQA Kazakh", 600, "600 questions"),
    ("2026-06", "DeFAn Kazakh", 3178, "3,178 questions"),
    ("2026-07", "KazMix-3", 89775, "89,775 examples"),
    ("2026-03", "RAGBench Kazakh", 11431, "11,431 examples"),
    ("2026-03", "IFBench Kazakh", 444, "444 examples"),
]

SPEECH_HOURS = [
    ("2020-09", "Kazakh Speech Corpus", 332, "332 h"),
    ("2021-04", "KazakhTTS", 93, "93 h"),
    ("2022-01", "KazakhTTS2", 271, "271 h"),
    ("2022-05", "Kazakh Speech Commands", 1, "≈1 h"),
    ("2022-09", "KSC2", 1200, "≈1,200 h"),
    ("2023-07", "KSD / SLR140", 554, "554 h"),
    ("2024-04", "KazEmoTTS", 74.85, "74.85 h"),
    ("2025-04", "MATERIAL Kazakh–English", 57, "≈57 h"),
    ("2026-01", "Optimized KSC2", 726, "≈726 h"),
    ("2026-02", "Kazakh Songs ASR", 4.5, "≈4.5 h"),
    ("2026-08", "YO-CPT-kk", 600, "600 h"),
]

SPEECH_COUNTS = [
    ("2024-01", "ISSAI SKIMMED", 21617, "21,617 clips"),
    ("2024-11", "Belebele-FLEURS", 900, "900 questions"),
    ("2026-05", "KazEGA", 96582, "96,582 utterances"),
    ("2026-03", "Common Voice v25", 76.67, "76.67 MB; living dataset"),
]

CV = [
    ("2020-07", "HKR", 1400, "1,400+ forms"),
    ("2021-10", "KOHTD", 140335, "140,335+ images"),
    ("2025-12", "QazLip", 34000, "≈34,000 videos"),
    ("2025-12", "AI2D Kazakh", 3088, "3,088 examples"),
    ("2025-12", "MathVista Kazakh", 1000, "1,000 examples"),
    ("2025-12", "OCRBench Kazakh", 441, "441 examples"),
    ("2025-12", "KazakhOCR", 600, "600 images"),
    ("2026-03", "MMBench Kazakh", 4329, "4,329 examples"),
    ("2026-03", "MathVision Kazakh", 3040, "3,040 examples"),
    ("2026-04", "BeyneleBench", 750, "750 examples"),
    ("2026-04", "SpokenMQA Kazakh", 2256, "2,256 examples"),
    ("2026-06", "Darmm Kazakh OCR", 200000, "200,000 images"),
]


def month_value(value: str) -> float:
    year, month = map(int, value.split("-"))
    return year + (month - 1) / 12


def plot(filename: str, title: str, subtitle: str, rows, y_label: str, start_year: int):
    width, height = 1500, 820
    left, right, top, bottom = 115, 385, 100, 90
    x0, x1 = left, width - right
    y0, y1 = top, height - bottom
    end = 2026 + 8 / 12
    logs = [math.log10(r[2]) for r in rows]
    lo, hi = math.floor(min(logs)), math.ceil(max(logs))
    if lo == hi:
        hi += 1

    def xp(date):
        return x0 + (month_value(date) - start_year) / (end - start_year) * (x1 - x0)

    def yp(size):
        return y1 - (math.log10(size) - lo) / (hi - lo) * (y1 - y0)

    colors = ["#2563eb", "#059669", "#d97706", "#7c3aed", "#dc2626"]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<style>text{font-family:Inter,Segoe UI,Arial,sans-serif;fill:#172033}.title{font-size:30px;font-weight:700}.sub{font-size:15px;fill:#5b6472}.axis{font-size:13px;fill:#5b6472}.label{font-size:12px;font-weight:600}.small{font-size:11px;fill:#5b6472}.grid{stroke:#dfe3e8;stroke-width:1}.axisline{stroke:#7b8492;stroke-width:1.3}</style>',
        f'<text x="{left}" y="42" class="title">{html.escape(title)}</text>',
        f'<text x="{left}" y="68" class="sub">{html.escape(subtitle)}</text>',
    ]
    for power in range(lo, hi + 1):
        y = yp(10**power)
        parts += [f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" class="grid"/>',
                  f'<text x="{x0-12}" y="{y+4:.1f}" text-anchor="end" class="axis">10^{power}</text>']
    for year in range(start_year, 2027):
        x = xp(f"{year}-01")
        parts += [f'<line x1="{x:.1f}" y1="{y0}" x2="{x:.1f}" y2="{y1}" class="grid"/>',
                  f'<text x="{x:.1f}" y="{y1+28}" text-anchor="middle" class="axis">{year}</text>']
    parts += [f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" class="axisline"/>',
              f'<text transform="translate(28 {(y0+y1)/2}) rotate(-90)" text-anchor="middle" class="axis">{html.escape(y_label)} (log scale)</text>']

    ordered = sorted(enumerate(rows), key=lambda t: (month_value(t[1][0]), -t[1][2]))
    label_y = 105
    for rank, (idx, (date, name, size, display)) in enumerate(ordered):
        x, y = xp(date), yp(size)
        color = colors[idx % len(colors)]
        radius = 5 + 4 * (math.log10(size) - lo) / max(1, hi - lo)
        label_x = x1 + 22
        ly = label_y + rank * ((height - 150) / max(1, len(rows) - 1))
        parts += [
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius:.1f}" fill="{color}" fill-opacity="0.78" stroke="#fff" stroke-width="1.5"><title>{html.escape(name)} — {date} — {html.escape(display)}</title></circle>',
            f'<path d="M{x+radius:.1f},{y:.1f} C{x+35:.1f},{y:.1f} {label_x-20:.1f},{ly:.1f} {label_x-6:.1f},{ly:.1f}" fill="none" stroke="{color}" stroke-opacity="0.36"/>',
            f'<text x="{label_x}" y="{ly-2:.1f}" class="label">{html.escape(name)}</text>',
            f'<text x="{label_x}" y="{ly+12:.1f}" class="small">{date} · {html.escape(display)}</text>',
        ]
    parts.append('</svg>')
    (OUT / filename).write_text("\n".join(parts) + "\n")


def main():
    OUT.mkdir(exist_ok=True)
    plot("nlp_timeline.svg", "Kazakh NLP datasets: release date and size", "All catalogued NLP/LLM datasets; size uses each dataset’s primary example unit.", NLP, "Primary examples", 2015)
    plot("speech_timeline_hours.svg", "Kazakh speech datasets with published duration", "Duration is shown in hours; hover a point for exact release month and size.", SPEECH_HOURS, "Audio duration (hours)", 2020)
    plot("speech_timeline_counts.svg", "Speech datasets without published duration", "Count-only resources are separate; Common Voice uses release size in MB.", SPEECH_COUNTS, "Published count / release MB", 2024)
    plot("cv_timeline.svg", "Kazakh CV datasets: release date and size", "Primary published media/example unit; labels retain the exact unit.", CV, "Primary media/examples", 2020)


if __name__ == "__main__":
    main()
