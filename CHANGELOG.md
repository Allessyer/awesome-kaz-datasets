# Changelog

This changelog starts from the 2026-08-19 catalog overhaul (migration to
`data/datasets.yaml` as the source of truth). Earlier history is in the git log.

## 2026-08-19 — Table layout and audit trim

- Dataset table columns reordered to Released / Dataset / Description / Author
  / Properties / Links: task and access/license moved under the dataset name,
  author/affiliation got its own column, and "Scale / Storage" was renamed to
  "Properties" (storage first, then scale, stacked).
- Removed the "Full source-by-source audit" collapsible block from the Speech
  and audio section (the detailed rules/included-releases/exclusions tables
  that used to live in `speech_language_comparison.md`) — it was too much
  detail for the README itself. The chart and its short caveat paragraph stay;
  the full reasoning is preserved in git history (see the 2026-08-19 catalog
  overhaul entry below) rather than reproduced inline.
- Removed the README's Contributors section.
- Task tags under the dataset name now use short abbreviations (ASR, MCQA,
  MT, ...) instead of full task names; each section's table is preceded by a
  glossary line spelling out only the abbreviations actually used in that
  section (replacing the single global "Abbreviations" list that used to sit
  at the bottom of the README).
- The Properties column (storage + scale) is dash-prefixed, one item per line.
- Removed the Links column: the dataset name now links to the dataset itself,
  and the author name links to the paper (or DOI, if there's no paper link).
  Code/project links are no longer shown in the table (still in `datasets.yaml`).
- Author cell restyled to match the Dataset cell: author name prominent, with
  affiliation in small text underneath.
- Calendar/chart accent colors (blue/orange/aqua) darkened slightly for better
  contrast against the white/near-white text drawn on top of them.
- Top nav updated to match the current section order and headings (added
  Background, dropped the stale Recent Additions link).
- Background expanded (why this catalog exists, what verification actually
  involves) and its explanatory paragraph on table columns rewritten to match
  the current layout (Dataset/Author links, Properties) instead of the old
  Links/Scale/Storage columns that no longer exist.
- Inclusion and maintenance trimmed to just the exclusion criteria (the
  verification framing now lives in Background, not duplicated here).
- Contributing restructured into three concrete actions (add a dataset, fix
  an entry, report a stale number) instead of one paragraph.
- Per-section abbreviation glossary reflowed into a 4-column grid on its own
  line below the "Abbreviations:" label, instead of one long inline sentence.
- Calendar accent colors (blue/orange/aqua) darkened further for contrast
  against the white text drawn on top of them.

## 2026-08-19 — Kazakh Speech MFA Punctuation

### Added

- **Kazakh Speech MFA Punctuation** (Jeti Labs) — a punctuation-restored,
  word-level-timestamped derivative of ISSAI KSC2, force-aligned with the
  Montreal Forced Aligner (408,010 utterances, ≈1,110 h, 56.8 GB, open access).
  `derivative_of: ksc2`.

## 2026-08-19 — Catalog overhaul

### Added

13 new verified datasets, discovered from Hugging Face, GitHub, arXiv, ACL
Anthology, Mendeley Data, and Kazakhstani institution pages:

- **KazSAnDRA** — Kazakh sentiment analysis dataset (180,064 rated reviews), ISSAI.
- **100k Movie Reviews from Kazakhstan** — kino.kz sentiment/language corpus (2001-2025).
- **Kazakh-IFT** — instruction-following dataset on Kazakhstani governance/culture, MBZUAI.
- **kaz-text-for-lm-normalized** — Farabi Lab normalized LM pretraining corpus (derivative of MDBKD).
- **Kazakh Instruction v2** — machine-translated-and-corrected Alpaca-style instruction set.
- **KazakhTextDuplicates v2.0** — controlled semantic-deduplication/STS benchmark.
- **Textual Foundations of Justice** — all current Kazakhstani laws, Russian + Kazakh.
- **MMLU-Pro Kazakh/Russian** — ISSAI machine translation of MMLU-Pro.
- **FineWeb2 Kazakh** (`kaz_Cyrl` config) — multilingual web-crawl pretraining corpus.
- **FLORES-200 Kazakh** (`kaz_Cyrl` config) — multilingual MT evaluation benchmark.
- **WikiANN Kazakh** (`kk` split) — multilingual NER benchmark.
- **Uzbek-Kazakh Parallel Corpora** — Uzbek-Kazakh MT corpus.
- **WavCapsQA Kazakh-Russian** — ISSAI audio-QA benchmark (Speech and audio section).

### Corrected

Every one of the 53 pre-existing entries was re-verified against its primary
source. Notable corrections:

- **KazMix-3** — moved from *Text, NLP, and LLM* to *Speech and audio*: it is a
  target-speaker-ASR / speech-separation corpus derived from KSD/SLR140, not an
  "instruction mixture." Description and task label corrected accordingly.
- **KazNewsDataset** — scale corrected from 4,365 to **1,142,735 documents**
  (the Mendeley record of record; ~260x understated).
- **KazRusNewsDataset** — scale corrected from 20,409 to **6,261,953 documents**
  (~307x understated).
- **Kazakh Speech Dataset (KSD / SLR140)** — storage corrected from 141.9 GB to
  **~56 GB** (independently confirmed twice from the OpenSLR archive listing).
- **Kazakh Speech Commands** — release date corrected from 2022-05 to **2023-04**
  (verified GitHub repository `created_at`).
- **Qorgau** — release date corrected from 2025-02 (paper submission) to
  **2025-05** (the GitHub repository with the actual data/code was created
  2025-05-24, three months after the paper).
- **Belebele-FLEURS** — Kazakh-subset scale corrected from 900 to **870** test
  examples; storage rescoped to the Kazakh (`kaz_Cyrl`) config (~3.4 GB) instead
  of an all-99-language total.
- **Mozilla Common Voice Kazakh** — re-sourced to the Mozilla Data Collective
  platform with a precise, current release (Common Voice Scripted Speech 24.0,
  2025-12-05: 2,750 clips, 3.76 h recorded / 2.39 h validated) in place of a vague
  "v25, storage only" entry.
- **MDBKD** — release date reconfirmed at 2023-04 (HF `createdAt`); an initial
  read had mistaken a 2025 TechRxiv preprint/`lastModified` date for the release.
- **KazNERD / KSC2 / KazakhTTS / KazEmoTTS** — release dates kept at their
  original (paper-era) dates rather than a later Hugging Face re-upload date;
  several ISSAI datasets were bulk re-uploaded to HF around January 2025, which
  would have overstated their release year by 2-4 years if taken at face value.
- **TurkicOCR-Cyrillic** — author corrected to Alen Issayev (was recorded under
  the GitHub handle `alenisaw`).
- Access classification added or corrected (previously unmarked in most rows) for
  ~15 entries, including: KazQAD, KazParC, KazNERD, KazCulture, KazEmoTTS (upgraded
  to `application` — requires a Google Form request), KazEGA, MATERIAL
  Kazakh-English (reclassified to `paid`), KOHTD and HKR (reclassified to
  `application` — require a form + author email approval).
- Paper, code, and/or DOI links added where previously missing: Kazakh Open
  Retrieval Benchmark, KazNERD, KSD/SLR140, Kazakh Speech Commands, KazakhTTS,
  KSC2, QazLip, MDBKD, KOHTD, HKR.
- Minor storage-figure corrections (card-verified) for RAGBench Kazakh, DeFAn
  Kazakh, and Kazakh-English KAZNU.

### Removed

- `assets/language_comparison_{nlp,cv,speech}.svg` (and their `.png` mirrors) —
  orphaned charts not referenced from the README; dropped to keep the
  visualization set aligned with what's actually documented and required.
- All `assets/*.png` mirrors — no SVG-to-PNG rendering toolchain was available in
  this environment; the repository is SVG-only until an owner reintroduces a
  conversion step in CI.
- `scripts/generate_language_comparisons.py` and `scripts/generate_timeline_plots.py`
  — superseded by the unified `scripts/generate_visualizations.py`.
- `speech_language_comparison.md` as a standalone file — its rules, deduplicated
  totals, included-releases, and exclusions tables now live inline in the
  README's Speech and audio section (a collapsible "Full source-by-source audit"
  block), so the analysis travels with the chart instead of living in a
  separate, easy-to-miss file.
- The Citation section (the catalog itself has no DOI to cite) and the Coverage
  matrix section (redundant with "Datasets per task").
- The Recent Additions section — the same information now lives in this
  CHANGELOG, which the README's Background section points to.
- Decorative emoji in the title and headings; the `---` rules that briefly
  separated sections; the per-image stat-line captions that just repeated the
  numbers already shown as tiles inside the image above them; the CI "Validate"
  badge and "Contributions welcome" badge (the former had nothing to link to
  before the workflow's first run; the latter added little).

### Visuals

- New: `assets/overview_dashboard.svg` and `assets/dataset_growth.svg`
  (catalog-wide), `assets/nlp_overview.svg`, `assets/speech_overview.svg`,
  `assets/vision_overview.svg` (per-section). Every chart ships light and dark
  variants (`name.svg` / `name-dark.svg`), selected automatically via
  `<picture>`/`prefers-color-scheme` to match the reader's browser theme.
- Rebuilt (same filenames, now generated from `data/datasets.yaml` instead of a
  hardcoded list): `assets/nlp_release_calendar.svg`,
  `assets/speech_release_calendar.svg`, `assets/cv_release_calendar.svg`,
  `assets/speech_task_hours_comparison.svg`, `assets/spoken_qa_samples_comparison.svg`.
- Release-calendar charts redesigned for readability: solid, section-identity
  fill (blue for Text/NLP, orange for Speech, aqua for Vision) instead of a
  five-step blue heat ramp that several readers found too monotone to scan;
  wider cells, larger bold text, and word-wrapped dataset names so long titles
  never overflow into the next year's column.
- Stat-tile charts (dashboard + per-section overviews) redesigned: no title
  baked into the image (the README supplies the caption as text), and
  center-aligned label/value pairs instead of left-aligned.
- Replaced the `task_landscape.svg` bar chart (34 rows, ~1000px tall) with an
  inline "Datasets per task" text summary in the Dataset landscape section.
- All visuals share one typography/palette system via
  `scripts/generate_visualizations.py`.

### Infrastructure

- Added `data/datasets.yaml` as the canonical, machine-readable dataset registry
  (66 entries) — the README tables, stats, and charts are now generated from it.
- Added `scripts/validate_catalog.py` — schema/taxonomy/URL/derivative-reference
  validation.
- Added `scripts/generate_readme.py` — regenerates managed README blocks
  (badges, dashboard, per-section tables sorted strictly newest-first, task
  summary, watchlist, contributors) while preserving hand-authored prose
  outside the `<!-- NAME:START/END -->` markers.
- Added `scripts/generate_visualizations.py` — single deterministic generator for
  all `assets/*.svg` charts (light + dark).
- Added `scripts/check_links.py` — best-effort, non-blocking link checker.
- Added `CONTRIBUTING.md`, this `CHANGELOG.md`, and
  `.github/ISSUE_TEMPLATE/dataset-submission.yml`.
- Added `.github/workflows/validate.yml` — CI runs the catalog validator and
  checks that committed `README.md`/`assets/*.svg` match what the generators
  produce from `data/datasets.yaml`.

### README redesign

- Hero with GitHub stars, dataset count, last-verified, and open-access badges
  (in that order); a compact nav; a Background section explaining the project's
  motivation and verification methodology; a "Catalog overview" dashboard; a
  Dataset landscape section (cumulative growth chart + task summary); the three
  dataset sections (each strictly newest-first); a Watchlist for
  unverifiable/announced resources; and a two-person Contributors section
  (Allessyer, creator/maintainer; Alen Issayev, editor).

### Notes on this pass

Dataset discovery for this overhaul was originally planned as a large parallel
multi-agent research sweep; that run hit an account-level usage limit partway
through (26 of 27 research agents failed), so discovery was completed via direct,
sequential primary-source verification instead. Coverage is solid for the
explicitly named priority candidates and several major multilingual benchmarks
(FineWeb2, FLORES-200, WikiANN), but a handful of sources named in the original
research brief — HPLT, CulturaX, CC-100, OSCAR, SIB-200 Kazakh subsets, and a
broader sweep of Kazakhstani university/government repositories — were not
individually re-verified this round and remain good candidates for a future pass.
