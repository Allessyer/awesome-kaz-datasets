# Changelog

Notable changes to this project, newest first. Entries before the 2026-08-19
catalog overhaul predate `data/datasets.yaml` and the generator pipeline;
they're reconstructed from the git history for context, not from a
contemporaneous changelog.

## 2026-08-27 — Central Asian Food Dataset (CAFD)

### Added

- Added **Central Asian Food Dataset (CAFD)** to Vision, OCR, and multimodal section (#13): 16,499 images across 42 food classes for food image recognition and dietary assessment, published in *Nutrients* (2023) by ISSAI researchers.

## 2026-08-24 — KazCulture paper reference

### Added

- Added IEEE Access 2026 publication reference (`Introducing Cultural Knowledge in Language Models: KazCulture Dataset for Kazakh Culture`) and individual author attribution for **KazCulture** (#12).

## 2026-08-24 — Contributors LinkedIn cards

### Changed

- Replaced the dynamic contrib.rocks widget with static contributor cards linking
  directly to contributors' LinkedIn profiles.

## 2026-08-21 — Storage/license re-verification pass

### Corrected

Every entry still missing `storage.value` or `license` was re-checked against
its live primary source (Hugging Face datasets-server API, GitHub license
detection, Mendeley/Dataverse metadata, arXiv paper text) rather than left as
an assumed gap:

- Filled in real storage figures for **FineWeb2 Kazakh** (6.86 GB),
  **WikiANN Kazakh** (0.21 MB), **HPLT 3.0 Kazakh** (8.76 GB), **CulturaX
  Kazakh** (~9.07 GB, summed from its four `kk` parquet shards), **CC-100
  Kazakh** (889 MB), **KSC** (19 GB), and **QazLip** (4.41 GB).
- Filled in real licenses, sourced from arXiv paper text or the dataset's
  GitHub/HF license tag where the HF card itself carried none: **KazParC**,
  **KazEmoTTS**, **KazakhTTS**, **KazakhTTS2** (all CC-BY-4.0), **Kazakh
  Speech MFA Punctuation** (MIT), **QazLip** (CC0-1.0).
- **KSC**'s `links.dataset` repointed from the ISSAI project page (which now
  renders KSC2 content, not this original 332h/153,000-utterance corpus) to
  its OpenSLR mirror.
- Everything else that was still null/"Not reported" was confirmed genuinely
  unpublished at the source (e.g. WikiANN and CC-100's HF cards explicitly
  declare `license: unknown`; several Mendeley DOIs carry no file-size
  metadata at all) rather than an uncollected fact — left as-is with a note
  recording what was checked.

## 2026-08-20 — README redesign, Watchlist audit

### Changed — README presentation redesign

Full rebuild of the README/visualization presentation, aimed at fast scanning
over narrative:

- Header made compact: the Kazakhstan flag sits either side of the `<h1>`
  title instead of a full-width banner image above it; the long Background
  narrative was cut down to a short About section.
- The separate "Dataset landscape" heading was dropped — its growth chart now
  sits directly in About, with a one-line caption instead of a heading and a
  wall-of-text "Datasets per task" chip list.
- Badges trimmed to Stars / Datasets / Open access / Last verified (dropped
  the License badge from the top; License stays as its own section at the
  bottom) and reordered so Last verified is last.
- The dense, name-in-cell release calendars were replaced with compact year x
  month release **heatmaps** — color intensity only, no dataset names crammed
  into cells. Went through several rounds of sizing (native pixel size read as
  too small; widened into a landscape strip with rectangular, not square,
  cells; settled on stretching to the full README column width off a larger
  baseline size so sparse sections don't get blown up into oversized cells)
  and color tuning. Dark theme's ramp direction is reversed from light
  theme on purpose: going *darker* for "more releases" made the busiest
  cells nearly invisible against the near-black surface, so dark theme goes
  brighter instead.

  The legend went through three designs before landing: numbers printed on
  top of each swatch with per-swatch adaptive text color (correct by
  contrast math, but a mixed dark/light row at 16px didn't read as legible
  as it measured); a single fixed text color per theme (simpler, but broke
  on whichever step of the ramp was closest to that theme's surface color);
  a palette capped to a narrow luminance-safe subrange so a fixed color
  always worked (fixed the text, but compressed the 5 steps enough that they
  got hard to tell apart). It settled on the simplest fix: count labels sit
  *below* each swatch, in the theme's normal text color on the plain
  surface, never printed on top of a fill — no text-contrast constraint on
  the palette at all, so the ramps went back to their more distinct,
  wider-range colors.
- `overview_dashboard.svg` and the three per-section `*_overview.svg`
  stat-tile images removed — they duplicated the badges and the tables.
- Dataset tables restructured to `ID | Released | Dataset | Task |
  Description | Storage | Samples`: a stable per-section row number added;
  author moved under the dataset name (organization/affiliation dropped from
  display); task tags and storage/sample scale broken out of the old combined
  "Properties" cell into their own columns; license dropped from the visible
  table (it stays recorded in `data/datasets.yaml`, just not surfaced as a
  table cell).
- The three per-section abbreviation glossaries consolidated into one
  Abbreviations section near the bottom.
- Removed the "Inclusion and maintenance" section — its exclusion criteria
  were a shorter preview of the same rules already spelled out in
  [CONTRIBUTING.md](CONTRIBUTING.md), which the About section already links to.
- Added a Contributors section (contrib.rocks avatar grid) above License.
- All of the above (plus the dataset moves below) was squashed into one
  commit on top of the 2026-08-19 catalog overhaul for a clean history.

### Added

- **Multimedia Corpus of Modern Spoken Kazakh Language (Module 1)** — moved from
  the Watchlist to the main catalog (Speech and audio) after finding the actual
  downloadable Module 1 artifact on GitHub (`gtroiani/MultCorSKL`): ≈12 h of
  naturally occurring spoken Kazakh across 33 speech events, with WAV audio and
  EAF/TSV/linear transcriptions, licensed CC-BY-NC-SA-4.0 per its `LICENSE.md`.
- **Til-Web-Raw-KK-v1** — moved from the Watchlist (previously listed as the
  unverifiable "Til-Web-KK") to the main catalog (Text, NLP, and LLM) after
  finding it listed in TilQazyna's public
  [`til-web-crawls-and-archive`](https://huggingface.co/collections/TilQazyna/til-web-crawls-and-archive)
  collection: a gated, 19.50 GB raw HTML mirror of two Kazakh educational/QA
  sites (≈222,890 pages), createdAt 2026-06-22 per the HF API.

### Removed

- **Zerde-QA-Wiki-20K** watchlist entry — no dataset card, repository, or source
  of any kind could be independently verified for this name, so there was
  nothing left to responsibly list even as a Watchlist pointer.

## 2026-08-20 — Coverage gap audit

### Added

17 new verified datasets closing the gaps the previous overhaul's closing note
had flagged as unverified (HPLT, CulturaX, CC-100, OSCAR-family, SIB-200, and a
broader sweep of Kazakhstani institutional repositories):

- **HPLT 3.0 Kazakh** (`kaz_Cyrl` config) — ≈5.12M documents, ≈100.6M segments,
  ≈7.34B tokens; CC0-1.0, open.
- **CulturaX Kazakh** (`kk` config) — 2,733,982 documents, 2,802,485,195 tokens;
  gated, license not reported (points to source mC4/OSCAR terms).
- **CC-100 Kazakh** (`kk` config) — included with scale/storage left as "not
  reported": it uses a loading script rather than a Parquet conversion, so an
  exact Kazakh-only row count could not be confirmed via the Datasets Server API,
  and the card lists its license as unknown.
- **mOSCAR Kazakh** (`kaz_Cyrl` config) — 248,403 documents, ~548.6 MB; the
  canonical OSCAR-family entry for this catalog (the global, all-language OSCAR
  release is not separately catalogued).
- **SIB-200 Kazakh** (`kaz_Cyrl` config) — 1,004 examples; catalogued as
  `derivative_of: flores200-kazakh` rather than a new FLORES entry.
- **KazBench-KK** — moved from the Watchlist to the main catalog after
  independently verifying the public Hugging Face artifact
  (`kz-transformers/kk-socio-cultural-bench-mc`).
- Nine **TilQazyna** datasets: **Til-Corpus**, **Til-Instruct**, **Til-Books**,
  **Til-Parallel**, **Til-Morphology**, **Til-Classification**,
  **Til-Terminology** (Text, NLP, and LLM), plus **Til-Audio** (Speech and
  audio) — replacing the previous generic "TilQazyna collections" Watchlist
  entry with eight named, individually verified datasets.
- Three **Al-Farabi Kazakh National University / farabi-lab** datasets:
  **Kazakh Analytical RAG (Single-Document)**, **Content Moderation and Safety —
  Kazakh**, and **Multi-Step Reasoning for Kazakh Context**.
- New canonical task **Morphological analysis** (`MORPH`), used by
  Til-Morphology.

### Corrected during verification

An earlier automated draft of this pass had assembled candidate entries via a
base64/gzip-encoded payload that was corrupted in transit (see Infrastructure
below); every figure in it was re-verified from scratch against the Hugging Face
API rather than trusted as-is, and several did not match:

- **Content Moderation and Safety — Kazakh** — example count corrected to
  **17,827** (the corrupted draft read 7,827); access corrected to **gated**.
- **Multi-Step Reasoning for Kazakh Context** — storage corrected to **39.0 MB**
  (the corrupted draft read 407.8 MB, off by roughly 10x).
- **Kazakh Analytical RAG (Single-Document)** — storage corrected to **33.4 MB**
  (the corrupted draft read 0.35 MB); access corrected to **gated**.
- **SIB-200 Kazakh** and **mOSCAR Kazakh** — row counts and storage that the
  draft had left as "not reported" were filled in from the Hugging Face
  Datasets Server size API.

### Watchlist

- **KazBench-KK** removed (moved to the main catalog).
- Generic **TilQazyna collections** entry removed (superseded by the eight named
  TilQazyna datasets added above).
- **National Corpus of the Kazakh Language (QazCorpus)** added — verified to
  exist, with a Main Corpus reporting 31,105,900 word usages and rich
  morphological/semantic/lexical/phonetic annotation, but no independently
  verifiable bulk-download artifact or reusable dataset license.
- **Til-Web-KK** added — referenced in TilQazyna's own materials as a cleaned
  Kazakh web-crawl release, but the repository returns HTTP 401 for anonymous
  access and does not appear in the organization's public repository listing;
  it could not be independently verified this pass, so — unlike the other eight
  TilQazyna datasets — it was **not** added to the main catalog.
- **Aqbileq** removed — no dataset card, repository, or paper could be
  independently located under this name.
- **Zerde-QA-Wiki-20K** and the announced 10B-token/10,000-speech-hour suite
  retained unchanged.

### Excluded / deduplicated (considered, not added)

- `farabi-lab/kazakh-stt` — mirror of the existing KSD/SLR140 entry.
- `Til-GEC` / `Til-GEC-v2` — deprecated.
- `Til-Corpus-Additions-v2` — aggregate duplicate of Til-Corpus.
- `Til-Web-Raw-KK-v1` — raw duplicate of the (unverified, watchlisted)
  Til-Web-KK.
- Til-Books source-specific shards, `datalake`, and other TilQazyna
  experimental/task-specific repositories (e.g. `til-kk-title-v1`).
- Smaller Farabi Lab instruction/safety variants
  (`Content_Moderation_and_Safety_Kazakh_Context`) that duplicate the three
  farabi-lab datasets added above.

### Infrastructure and cleanup

- Removed `.github/workflows/_finalize_catalog_once.yml`,
  `scripts/_finalize_catalog_once.py`, and `scripts/_trigger_finalize.txt`. An
  earlier session had committed a workflow that decoded a base64/gzip-encoded
  Python payload on every push to `main` and used it to auto-commit and push
  catalog changes under the `github-actions[bot]` identity, bypassing PR review.
  This pass does the catalog work directly in a reviewable commit instead.
- `scripts/validate_catalog.py` now hard-fails a main-catalog entry with
  `access: unavailable` (belongs in the Watchlist) or `kind: mirror` (excluded
  entirely), instead of only accepting them as valid-but-discouraged enum
  values.
- `.github/workflows/validate.yml` push trigger now also watches `README.md`
  and `assets/**`, matching the existing `pull_request` trigger.
- Fixed the per-section abbreviation glossary: cells wrapped their text in
  `<sub>`, which visually shrank it and pulled it toward the bottom of the
  cell; switched to plain `<strong>` text so `align="center" valign="middle"`
  centers it correctly.
- Contributing section: replaced "Hugging Face row/download counts drift" with
  "Hugging Face row counts and reported storage sizes may change over time" —
  the catalog does not report download counts.
- Removed the previous entry's closing note flagging HPLT, CulturaX, CC-100,
  OSCAR, SIB-200, and a broader institutional sweep as unverified — those gaps
  are closed by this pass (CC-100 remains partially unverifiable at the field
  level: exact Kazakh row count and license, not existence).

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

## 2026-08-14 — TurkicOCR-Cyrillic, calendar fixes

### Added

- **TurkicOCR-Cyrillic** — synthetic Turkic-Cyrillic OCR dataset spanning
  Kazakh, Kyrgyz, Kazakh-Russian, and Kyrgyz-Russian text/layouts.

### Fixed

- Author attribution and the vision release-calendar rendering following the
  TurkicOCR addition (`scripts/generate_timeline_plots.py` at the time).

## 2026-08-12 – 2026-08-13 — Visualization suite, expanded coverage

The visualization approach went through several iterations in a short span
before settling: per-section dataset-size timeline plots
(`scripts/generate_timeline_plots.py`) → reworked to separate storage from
scale and add calendar-style plots → compacted to show only months with an
actual release → rebuilt again as the release-calendar charts
(`nlp_release_calendar.svg`, `speech_release_calendar.svg`,
`cv_release_calendar.svg`) that later eras built on.

### Added

- **YO-CPT-kk** — YouTube-oriented Kazakh continual-pretraining corpus
  (ASR/TTS/speaker-verification).
- A general coverage-expansion pass ("Expand verified Kazakh dataset
  coverage").
- Cross-language (Kazakh/Russian/English) comparison plots
  (`scripts/generate_language_comparisons.py`), an audited speech-task-hours
  comparison chart, and a `speech_language_comparison.md` write-up of the
  sourcing/deduplication methodology behind it.
- PNG mirrors alongside every SVG chart, and a Kazakhstan flag in the README
  header.

Note: the timeline/comparison-plot scripts and `speech_language_comparison.md`
from this era were superseded by the unified `scripts/generate_visualizations.py`
during the 2026-08-19 catalog overhaul above — the release-calendar *concept*
survived (as `data/datasets.yaml`-generated charts), the standalone scripts and
markdown write-up didn't.

## 2025-01-29 – 2025-02-26 — Initial catalog creation

The repository began as a two-line README ("Datasets in kazakh language for
different tasks") and grew, commit by commit, into a hand-maintained Markdown
table — Date / Dataset / Title / Link / Task columns, no generator, no CI, no
`data/datasets.yaml` — covering Text/NLP and Speech datasets as they were
found (KazNERD, KazParC, KazQAD, MDBKD, KazEmoTTS, ISSAI SKIMMED,
Belebele-FLEURS, and others; roughly 17 entries by the end of this period).
Individual additions aren't itemized here — at this stage they were small,
frequent, hand-edited README diffs rather than discrete, independently
verifiable changes. The generator pipeline, validation, and generated visuals
all arrived later, starting 2026-08-13.

