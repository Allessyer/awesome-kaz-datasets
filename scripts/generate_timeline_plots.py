#!/usr/bin/env python3
"""Generate calendar-style SVG release maps for the README."""

from collections import defaultdict
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"

NLP = [
    ("2015-06", "UD Kazakh KTB"), ("2020-12", "KazNewsDataset"),
    ("2020-12", "KazRusNewsDataset"), ("2021-11", "KazNERD"),
    ("2023-04", "MDBKD"), ("2024-02", "Kazakh–English KAZNU"),
    ("2024-03", "Kazakh–Russian KAZNU"), ("2024-03", "KazParC"),
    ("2024-04", "KazQAD"), ("2024-11", "MMLU Translated KK"),
    ("2024-11", "GSM8K Translated KK"), ("2024-11", "Kazakh Dastur MC"),
    ("2024-11", "Kazakh Constitution MC"), ("2024-11", "Kazakh UNT"),
    ("2025-01", "KazMMLU"), ("2025-02", "Qorgau"),
    ("2025-10", "KazCulture"), ("2026-03", "RAGBench Kazakh"),
    ("2026-03", "IFBench Kazakh"), ("2026-04", "Zerde-QA-50K"),
    ("2026-05", "KazLawBench"), ("2026-06", "Kazakh Open Retrieval"),
    ("2026-06", "FreshQA Kazakh"), ("2026-06", "DeFAn Kazakh"),
    ("2026-07", "KazMix-3"),
]

SPEECH = [
    ("2020-09", "Kazakh Speech Corpus"), ("2021-04", "KazakhTTS"),
    ("2022-01", "KazakhTTS2"), ("2022-05", "Speech Commands"),
    ("2022-09", "KSC2"), ("2023-07", "KSD / SLR140"),
    ("2024-01", "ISSAI SKIMMED"), ("2024-04", "KazEmoTTS"),
    ("2024-11", "Belebele-FLEURS"), ("2025-04", "MATERIAL Kazakh–English"),
    ("2026-01", "Optimized KSC2"), ("2026-02", "Kazakh Songs ASR"),
    ("2026-03", "Common Voice v25"), ("2026-05", "KazEGA"),
    ("2026-08", "YO-CPT-kk"),
]

CV = [
    ("2020-07", "HKR"), ("2021-10", "KOHTD"),
    ("2025-12", "QazLip"), ("2025-12", "AI2D Kazakh"),
    ("2025-12", "MathVista Kazakh"), ("2025-12", "OCRBench Kazakh"),
    ("2025-12", "KazakhOCR"), ("2026-03", "MMBench Kazakh"),
    ("2026-03", "MathVision Kazakh"), ("2026-04", "BeyneleBench"),
    ("2026-04", "SpokenMQA Kazakh"), ("2026-06", "Darmm Kazakh OCR"),
    ("2026-06", "TurkicOCR-Cyrillic"),
]

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def release_map(filename: str, title: str, rows):
    grouped = defaultdict(list)
    years = sorted({int(date[:4]) for date, _ in rows})
    months = sorted({int(date[5:]) for date, _ in rows})
    for date, name in rows:
        grouped[(int(date[:4]), int(date[5:]))].append(name)

    cell_w = 190
    row_heights = {
        month: max(54, 16 + max(len(grouped[(year, month)]) for year in years) * 14)
        for month in months
    }
    left, top, right, bottom = 78, 120, 24, 28
    width = left + len(years) * cell_w + right
    height = top + sum(row_heights.values()) + bottom
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fff"/>',
        '<style>text{font-family:Inter,Segoe UI,Arial,sans-serif;fill:#172033}.title{font-size:28px;font-weight:700}.year{font-size:17px;font-weight:700}.month{font-size:13px;fill:#5b6472}.name{font-size:11px;font-weight:600}.cell{stroke:#dfe3e8;stroke-width:1}.filled{fill:#eff6ff}.empty{fill:#fafbfc}</style>',
        f'<text x="{left}" y="39" class="title">{escape(title)}</text>',
        f'<text x="{left}" y="67" class="month">Year → · Month ↓ · Dataset names appear in their release cell</text>',
    ]
    for col, year in enumerate(years):
        x = left + col * cell_w
        parts.append(f'<text x="{x + cell_w/2}" y="{top-18}" text-anchor="middle" class="year">{year}</text>')
        y = top
        for month in months:
            cell_h = row_heights[month]
            names = grouped.get((year, month), [])
            klass = "filled" if names else "empty"
            parts.append(f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" class="cell {klass}"/>')
            for idx, name in enumerate(names):
                parts.append(f'<text x="{x+8}" y="{y+18+idx*14}" class="name">{escape(name)}</text>')
            y += cell_h
    y = top
    for month in months:
        cell_h = row_heights[month]
        y_label = y + cell_h / 2
        parts.append(f'<text x="{left-12}" y="{y_label+4}" text-anchor="end" class="month">{MONTHS[month-1]}</text>')
        y += cell_h
    parts.append('</svg>')
    (OUT / filename).write_text("\n".join(parts) + "\n", encoding="utf-8")


def main():
    OUT.mkdir(exist_ok=True)
    release_map("nlp_release_calendar.svg", "Kazakh NLP and LLM dataset releases", NLP)
    release_map("speech_release_calendar.svg", "Kazakh speech and audio dataset releases", SPEECH)
    release_map("cv_release_calendar.svg", "Kazakh CV and multimodal dataset releases", CV)


if __name__ == "__main__":
    main()
