# Contributing

Thanks for helping grow this catalog. This document is the policy the generator
and reviewers hold every submission to. Read it before opening a PR that adds or
edits `data/datasets.yaml` — most review feedback traces back to one of the rules
below.

## How the repository works

`data/datasets.yaml` is the single source of truth. `README.md`'s tables, stats,
and images are generated from it — never hand-edit a table row or a stat line
inside the `<!-- NAME:START -->` / `<!-- NAME:END -->` markers; your edit will be
silently overwritten the next time someone runs the generator. Edit the YAML,
then run:

```bash
python scripts/validate_catalog.py
python scripts/generate_visualizations.py
python scripts/generate_readme.py
```

CI (`.github/workflows/validate.yml`) reruns all three in check mode and fails the
PR if the committed README/assets don't match what the YAML generates.

## Adding a dataset

1. Verify the dataset from a **primary source** in this order of preference:
   1. official dataset repository/card (Hugging Face, GitHub, OpenSLR, ...)
   2. official project repository
   3. the associated peer-reviewed paper
   4. official institutional page (e.g. an ISSAI or Farabi Lab project page)
   5. a trusted research archive (Zenodo, Mendeley Data, Harvard Dataverse, ...)
   6. a secondary source, only when a primary one is genuinely unavailable
2. Confirm there is an **actual, currently obtainable data artifact** — not just a
   paper or an announcement. If you can't download or request it today, it belongs
   in the Watchlist, not the main tables.
3. Confirm the **Kazakh scope** is real and identifiable: either the dataset is
   Kazakh-specific, or — for a multilingual resource — it exposes a directly
   loadable, identifiable Kazakh config/split (e.g. `kaz_Cyrl`, `kk`). A multilingual
   corpus with no separable Kazakh subset does not qualify.
4. Fill in `data/datasets.yaml` using the schema below. **Never guess a missing
   fact.** Use `null` or the literal string `"Not reported"` instead of inventing a
   date, author, license, or number.
5. Run the three commands above and commit the regenerated `README.md` and
   `assets/*.svg` alongside your YAML change.

### What does NOT belong in the main catalog

- Model repositories (checkpoints, adapters, tokenizers) — not datasets.
- Duplicate mirrors of a dataset already listed (same content, different host).
- Tokenizer-specific packs, packed token blocks, alternate serializations, or
  shard reorganizations of a dataset already listed.
- Tiny personal test/demo files with no independent research utility.
- Unreleased or announced-only resources — these go in the Watchlist section.
- A dataset whose only "openness" is that the paper describing it is open access;
  the *data* itself must be obtainable.

### Derivatives and mirrors

A **derivative** (reprocessed, deduplicated, resegmented, or otherwise
substantially reworked version of an existing catalog entry) may be added when it
has independent research utility — e.g. a cleaned/deduplicated pretraining corpus,
a VAD-resliced speech corpus, a synthetic GEC corpus built on top of a parent text
corpus. Set `kind: derivative` and `derivative_of: <parent-id>`, where the parent
id must already exist in `datasets.yaml`. A dataset that is purely a mirror, a
reformatted copy, or a tokenizer-specific pack of an existing entry is **not** a
new dataset and should not be added.

### Multilingual resources

Multilingual datasets with a genuine Kazakh subset are added to the relevant
existing section (never to a separate "multilingual" section) with `kind:
multilingual`. Be conservative: verify the Kazakh config/split is directly
loadable and reasonably sized before adding it, not merely "listed as one of N
supported languages" in marketing copy.

### The SozKZ ecosystem (and similar prolific uploaders)

Some organizations publish many related Hugging Face repositories from one
underlying data collection effort. Only add entries that represent **meaningfully
different data or research use** (e.g. a raw multi-source corpus vs. its
deduplicated pretraining-ready version vs. a distinct synthetic GEC corpus built
from it). Reject or skip entries that are tokenizer-specific, packed, differently
serialized, or otherwise a reorganization of a corpus already listed. Record the
lineage via `derivative_of`.

## The `released` field

`released` is the date the dataset **(that specific artifact/version) became
publicly available** — a real person could have downloaded or requested it on
that date. It is explicitly **not**:

- a Hugging Face "last modified" timestamp (repos get re-uploaded/mirrored years
  after the true release — verify against `createdAt` via the HF API, and cross-check
  against the paper/original host if `createdAt` looks implausibly late),
- the date a paper was submitted or accepted,
- the date of the latest commit to a companion GitHub repo,
- the date the dataset was added to *this* catalog (that's `added_to_catalog`).

Use `YYYY-MM` when the month is known, `YYYY` when only the year is known. Never
upgrade a year-only date to a specific month by guessing.

## Access classification

| Value | Meaning |
|---|---|
| `open` | Directly downloadable, or requires only normal service authentication (a free account) with no special approval step. |
| `gated` | Free, but requires accepting terms, requesting access, or Hugging Face-style gating. |
| `application` | An explicit request/application to an institution or the authors is required. |
| `paid` | Commercial or licensed purchase (e.g. an LDC membership tier). |
| `restricted` | Special institutional or usage restrictions beyond a simple application. |
| `unavailable` | Described/announced but no usable artifact can currently be verified — belongs in the Watchlist, not the main table. |

Never mark a dataset `open` merely because its paper is open access — check the
data repository's own access terms.

## `kind` and `origin`

`kind` (pick one): `original`, `benchmark`, `translation`, `derivative`,
`multilingual`, `mirror`.

`origin` (pick one or more): `native`, `human-annotated`, `human-translated`,
`machine-translated`, `synthetic`, `web-crawl`, `mixed`.

Don't collapse provenance into a vague description — if a dataset is a
machine-translated benchmark, it is `kind: translation`, `origin:
[machine-translated]`, not `kind: original`.

## Canonical task labels

Use an existing task label from `data/datasets.yaml` whenever your dataset's task
matches one already in use (check the README's Abbreviations section, or search
`data/datasets.yaml` for the label) instead of inventing a near-synonym (e.g. reuse
`Question answering`, don't add "QA" or "Open-domain QA" as a separate label
unless the distinction is genuinely load-bearing). If you must introduce a new
label, keep it short and sentence-case.

## Required / optional metadata

Required: `id`, `name`, `released`, `section`, `description`, `tasks`, `access`,
`license`, `kind`, `origin`, `links.dataset`, `scale`, `storage`.

Strongly encouraged when available: `authors`, `organization`, `links.paper`,
`links.code`, `links.doi`, `paper.venue`/`paper.year`.

`id` must be a stable, kebab-case slug (`kazakh-instruction-v2`, not
`Kazakh_Instruction_V2`) — it is used as the join key for `derivative_of` and must
never be reused for a different dataset.

## Updating an existing entry

If you're correcting metadata rather than adding a dataset, edit the relevant
entry in place, update `last_verified` to today's date, and add a one-line `notes`
field explaining what changed and why (this feeds the Recent Additions / Changelog
process). Don't silently replace a value you're unsure about — if you can't verify
a correction, open an issue describing the discrepancy instead.

## Watchlist entries

A resource goes in the README's Watchlist (not `datasets.yaml`) when it's
announced but unreleased, described in a paper with no downloadable artifact,
license-conflicted, of unclear provenance, temporarily inaccessible, or its
Kazakh presence isn't yet sufficiently verified. Watchlist entries are
hand-maintained tuples in `scripts/generate_readme.py` (`WATCHLIST` list):
`(name, reason, url)`. Add a short, factual reason, not a guess about when it
might become available, and a source `url` when one exists (the project page,
announcement, or paper you found it through) so a reader can look into it
themselves — use `None` only when no such source could be found.

## PR format

- One dataset addition/correction per PR where practical (easier to review).
- Include the primary source URL(s) you verified against in the PR description.
- Run the three generator commands and commit the resulting diff to
  `README.md`/`assets/` — don't leave the repo in a state where
  `generate_readme.py --check` would fail.
- If you're unsure about a field, use `"Not reported"`/`null` and say so in the PR
  description rather than guessing.

## Repository license

The repository's own top-level license (as opposed to each dataset's license,
recorded per-entry in `datasets.yaml`) is an open decision reserved for the repo
owner. Don't add a `LICENSE` file in a PR unless the owner has explicitly asked
for one.
