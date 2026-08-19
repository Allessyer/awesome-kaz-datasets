<p align="center">
  <img src="https://emojiassets.saruwakakun.design/a/lg/1f1f0_1f1ff_1o53s.webp"
       width="120"
       alt="Kazakhstan 🇰🇿">
</p>

<h1 align="center">Awesome Kazakh Datasets</h1>

<p align="center">
  A curated, research-grade catalog of public datasets for Kazakh-language NLP, LLM,
  speech, computer vision, OCR, and multimodal research.
</p>

<!-- BADGES:START -->
<p align="center">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Allessyer/awesome-kaz-datasets?style=flat&color=eda100">
  <img alt="Datasets" src="https://img.shields.io/badge/Datasets-67-2a78d6">
  <img alt="Last verified" src="https://img.shields.io/badge/Last_verified-2026--08--19-1baf7a">
  <img alt="Open access" src="https://img.shields.io/badge/Open_access-78%25-2ea44f">
</p>
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
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/overview_dashboard-dark.svg">
  <img src="assets/overview_dashboard.svg" alt="Catalog overview: dataset count, open-access rate, paper coverage, task count, and per-section breakdown" width="100%">
</picture>
<!-- DASHBOARD:END -->

## Dataset landscape

<!-- LANDSCAPE:START -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/dataset_growth-dark.svg">
  <img src="assets/dataset_growth.svg" alt="Cumulative Kazakh dataset releases over time, by section" width="100%">
</picture>

<sub>**Datasets per task** — Automatic speech recognition (ASR) (10) · Multiple-choice QA (6) · Question answering (6) · Text-to-speech (TTS) (6) · Machine translation (5) · Language modelling / pretraining (5) · Retrieval / RAG (4) · OCR (4) · Instruction tuning (3) · Legal QA (2) · Named entity recognition (2) · Text classification (2) · Sentiment classification (2) · Emotion / paralinguistic classification (2) · Visual QA (2) · Visual math reasoning (2) · Handwriting recognition (2) · Safety evaluation (1) · Cultural QA (1) · Instruction following (1) · Math reasoning (1) · Dependency parsing / POS tagging (1) · Text deduplication / similarity (1) · Target-speaker ASR / speech separation (1) · Speaker verification (1) · Speech translation (1) · Spoken QA (1) · Keyword spotting (1) · Audio question answering (1) · Cultural vision benchmark (text-to-image) (1) · Audio-visual QA (1) · Layout analysis / document understanding (1) · Diagram QA (1) · Visual speech recognition (lip reading) (1)</sub>
<!-- LANDSCAPE:END -->

## Text, NLP, and LLM

<!-- NLP_SECTION:START -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/nlp_overview-dark.svg">
  <img src="assets/nlp_overview.svg" alt="Text, NLP, and LLM dataset overview" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/nlp_release_calendar_1-dark.svg">
  <img src="assets/nlp_release_calendar_1.svg" alt="Calendar map of Text, NLP, and LLM dataset releases, 2015-2022, with year on the x-axis and month on the y-axis" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/nlp_release_calendar_2-dark.svg">
  <img src="assets/nlp_release_calendar_2.svg" alt="Calendar map of Text, NLP, and LLM dataset releases, 2023-2026, with year on the x-axis and month on the y-axis" width="100%">
</picture>

**Abbreviations:**

<table>
<tr><td><sub><strong>CQA</strong> — Cultural QA</sub></td><td><sub><strong>IF</strong> — Instruction following</sub></td><td><sub><strong>IFT</strong> — Instruction tuning</sub></td><td><sub><strong>LM</strong> — Language modelling / pretraining</sub></td></tr>
<tr><td><sub><strong>LQA</strong> — Legal QA</sub></td><td><sub><strong>MCQA</strong> — Multiple-choice QA</sub></td><td><sub><strong>MR</strong> — Math reasoning</sub></td><td><sub><strong>MT</strong> — Machine translation</sub></td></tr>
<tr><td><sub><strong>NER</strong> — Named entity recognition</sub></td><td><sub><strong>POS</strong> — Dependency parsing / POS tagging</sub></td><td><sub><strong>QA</strong> — Question answering</sub></td><td><sub><strong>RAG</strong> — Retrieval / RAG</sub></td></tr>
<tr><td><sub><strong>Safety</strong> — Safety evaluation</sub></td><td><sub><strong>SC</strong> — Sentiment classification</sub></td><td><sub><strong>STS</strong> — Text deduplication / similarity</sub></td><td><sub><strong>TC</strong> — Text classification</sub></td></tr>
</table>

| Released | Dataset | Description | Author | Properties |
|---|---|---|---|---|
| 2026-06 | **[FreshQA Kazakh](https://huggingface.co/datasets/issai/freshqa_kazakh)**<br><sub>QA</sub><br><sub>Open · Not reported</sub> | Bilingual (English/Kazakh) benchmark of factual questions with false premises, for testing how models handle incorrect assumptions. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 0.4 MB<br>– 600 |
| 2026-06 | **[DeFAn Kazakh](https://huggingface.co/datasets/issai/defan_kazakh)**<br><sub>QA</sub><br><sub>Open · MIT</sub> | Machine-translated Kazakh/English version of the DefAn hallucination benchmark for definitive question answering. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 0.2 MB<br>– 3,178 questions |
| 2026-06 | **[Kazakh Open Retrieval Benchmark](https://huggingface.co/datasets/Tim2190/kaz-rag-search-benchmark)**<br><sub>RAG · QA</sub><br><sub>Open · CC-BY-SA-4.0</sub> | Evidence-based Kazakh information-retrieval benchmark built from Kazakh Wikipedia, showing morphological stemming outperforms multilingual embeddings. | **[Timur Seidalin](https://doi.org/10.5281/zenodo.20605663)** | – 14.6 MB<br>– 300 queries; 8,370 passages |
| 2026-05 | **[KazLawBench](https://huggingface.co/datasets/raiym76/kazlawbench)**<br><sub>LQA</sub><br><sub>Gated · CC-BY-NC-SA-4.0</sub> | First bilingual (Russian + Kazakh) legal-LLM benchmark for Kazakhstan, spanning statutory codes and de-identified Supreme Court judgments across seven task types. | **Batyr Raiym** | – 9.9 MB<br>– 3,098 |
| 2026-05 | **[100k Movie Reviews from Kazakhstan](https://huggingface.co/datasets/yeshpanovrustem/100k_movie_reviews_from_kz)**<br><sub>SC</sub><br><sub>Gated · CC-BY-4.0</sub> | 100,502 kino.kz movie reviews (2001-2025) manually annotated for language ID and sentiment, capturing Russian, Kazakh, and code-switched Kazakh-Russian text. | **[Rustem Yeshpanov](https://arxiv.org/abs/2605.08600)** | – 57.7 MB<br>– 100,502 reviews |
| 2026-04 | **[Zerde-QA-50K](https://huggingface.co/datasets/kurumikz/Zerde-QA-50K)**<br><sub>IFT · QA</sub><br><sub>Open · ODC-By-1.0</sub> | Synthetic Kazakh QA collection spanning 20+ academic domains for instruction tuning and low-resource NLP research. | **kurumikz** | – 156.2 MB<br>– 51,422 pairs |
| 2026-03 | **[RAGBench Kazakh](https://huggingface.co/datasets/issai/RAGBench_Kazakh)**<br><sub>RAG</sub><br><sub>Open · CC-BY-4.0</sub> | Kazakh translation of RAGBench for evaluating retrieval-augmented-generation systems across biomedical, legal, financial, and general-knowledge domains. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 31.2 MB<br>– 11,431 |
| 2026-03 | **[IFBench Kazakh](https://huggingface.co/datasets/issai/IFBench_Kazakh)**<br><sub>IF</sub><br><sub>Open · Apache-2.0</sub> | Machine-translated Kazakh instruction-following benchmark evaluating adherence to explicit constraints. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 1.3 MB<br>– 444 |
| 2025-12 | **[MMLU-Pro Kazakh/Russian](https://huggingface.co/datasets/issai/MMLU-Pro_Kazakh_Russian)**<br><sub>MCQA</sub><br><sub>Open · MIT</sub> | Machine-translated Kazakh/Russian version of MMLU-Pro, with more answer options and more challenging reasoning tasks than MMLU. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 11.4 MB<br>– 24,064 rows; 12k per language |
| 2025-10 | **[KazCulture](https://huggingface.co/datasets/issai/KazCulture)**<br><sub>CQA</sub><br><sub>Gated · CC-BY-4.0</sub> | Human-written passage-question-answer triplets covering Kazakh traditions, music, beliefs, cuisine, games, clothing, and handicrafts. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 4.6 MB<br>– 16,137 PQA triplets |
| 2025-05 | **[Qorgau](https://github.com/mbzuai-nlp/qorgau-kaz-ru-safety)**<br><sub>Safety</sub><br><sub>Open · Not reported</sub> | Kazakh/Russian bilingual LLM-safety evaluation benchmark spanning six high-level risk areas and 17 harm types. | **[MBZUAI NLP group](https://arxiv.org/abs/2502.13640)**<br><sub>MBZUAI</sub> | – 103.9 MB<br>– 2,790 prompts |
| 2025-03 | **[KazakhTextDuplicates v2.0](https://huggingface.co/datasets/Arailym-tleubayeva/KazakhTextDuplicates)**<br><sub>STS</sub><br><sub>Open · CC-BY-4.0</sub> | Controlled multi-regime benchmark for semantic deduplication, semantic similarity, and retrieval in Kazakh, with seven deterministic duplication regimes. | **[Arailym Tleubayeva](https://www.mdpi.com/2306-5729/11/6/133)** | – 217 MB<br>– 25,922 rows |
| 2025-02 | **[Kazakh-IFT](https://huggingface.co/datasets/nurkhan5l/kazakh-ift)**<br><sub>IFT</sub><br><sub>Gated · CC-BY-NC-SA-4.0</sub> | Instruction-following dataset covering Kazakhstani governance, legal process, cultural practice, and public-service knowledge, LLM-generated with GPT-4o. | **[Laiyk et al.](https://arxiv.org/abs/2502.13647)**<br><sub>MBZUAI</sub> | – 7.85 MB<br>– ~10,600 samples |
| 2025-01 | **[KazMMLU](https://huggingface.co/datasets/MBZUAI/KazMMLU)**<br><sub>MCQA</sub><br><sub>Open · CC-BY-NC-SA-4.0</sub> | Kazakh/Russian multiple-choice benchmark covering regional knowledge of Kazakhstan across school and university subjects. | **[Togmanov et al.](https://arxiv.org/abs/2502.12829)**<br><sub>MBZUAI</sub> | – 17.4 MB<br>– 23,000 total; 10,969 Kazakh |
| 2025-01 | **[FineWeb2 Kazakh](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2/viewer/kaz_Cyrl)**<br><sub>LM</sub><br><sub>Open · ODC-By-1.0</sub> | Kazakh (kaz_Cyrl) configuration of FineWeb2, a deduplicated, quality-filtered multilingual web-crawl pretraining corpus. | **Hugging Face FineWeb team**<br><sub>Hugging Face</sub> | – 3,380,000 rows (kaz_Cyrl) |
| 2024-11 | **[Kazakh Dastur MC](https://huggingface.co/datasets/kz-transformers/kazakh-dastur-mc)**<br><sub>MCQA</sub><br><sub>Open · Apache-2.0</sub> | Multiple-choice benchmark on Kazakh traditions and customs (dastur). | **kz-transformers** | – 0.3 MB<br>– 1,005 |
| 2024-11 | **[Kazakh Constitution MC](https://huggingface.co/datasets/kz-transformers/kazakh-constitution-mc)**<br><sub>MCQA</sub><br><sub>Open · Apache-2.0</sub> | Multiple-choice benchmark on the Constitution of the Republic of Kazakhstan. | **kz-transformers** | – 0.1 MB<br>– 414 |
| 2024-11 | **[Kazakh UNT](https://huggingface.co/datasets/kz-transformers/kazakh-unified-national-testing-mc)**<br><sub>MCQA</sub><br><sub>Open · Apache-2.0</sub> | Multiple-choice benchmark built from the Kazakh Unified National Testing exam. | **kz-transformers** | – 4.4 MB<br>– 14,850 |
| 2024-11 | **[MMLU Translated KK](https://huggingface.co/datasets/kz-transformers/mmlu-translated-kk)**<br><sub>MCQA</sub><br><sub>Open · Apache-2.0</sub> | Machine-translated Kazakh version of MMLU. | **kz-transformers** | – 11.4 MB<br>– 15,854 |
| 2024-11 | **[GSM8K Translated KK](https://huggingface.co/datasets/kz-transformers/gsm8k-kk-translated)**<br><sub>MR</sub><br><sub>Open · Apache-2.0</sub> | Machine-translated Kazakh version of GSM8K grade-school math word problems. | **kz-transformers** | – 4.2 MB<br>– 8,792 |
| 2024-05 | **[Textual Foundations of Justice](https://data.mendeley.com/datasets/jdpc5658nh/3)**<br><sub>LQA · LM</sub><br><sub>Open · CC-BY-4.0</sub> | All current laws of the Republic of Kazakhstan as of 2024-04-01, in Russian and Kazakh, for legal-QA model training. | **[Akhmetov et al.](https://doi.org/10.17632/jdpc5658nh.3)**<br><sub>Kazakh-British Technical University</sub> | Not reported |
| 2024-04 | **[KazQAD](https://huggingface.co/datasets/issai/kazqad)**<br><sub>QA · RAG</sub><br><sub>Gated · CC-BY-SA-4.0</sub> | Kazakh open-domain QA dataset supporting reading comprehension, full ODQA, and information-retrieval settings, built from translated Natural Questions and the Kazakh UNT exam. | **[Yeshpanov et al.](https://arxiv.org/abs/2404.04487)**<br><sub>ISSAI, Nazarbayev University</sub> | – 281.7 MB<br>– 6,000 questions; 12,700 passages |
| 2024-03 | **[KazParC](https://huggingface.co/datasets/issai/kazparc)**<br><sub>MT</sub><br><sub>Gated · Not reported</sub> | Kazakh parallel corpus covering Kazakh, English, Russian, and Turkish across proverbs, literature, news, TED talks, legal documents, and UN publications, plus a large synthetic (SynC) extension. | **[ISSAI researchers](https://arxiv.org/abs/2403.19399)**<br><sub>ISSAI, Nazarbayev University</sub> | – 25.9 GB<br>– 372,000 sentence pairs (+ 1.8M synthetic) |
| 2024-03 | **[Kazakh–Russian KAZNU](https://huggingface.co/datasets/Dauren-Nur/kaz_rus_parallel_corpora_KAZNU)**<br><sub>MT</sub><br><sub>Open · Not reported</sub> | Parallel Kazakh-Russian corpus of governmental and official documents. | **Dauren-Nur**<br><sub>Al-Farabi Kazakh National University</sub> | – 23.4 MB<br>– 86,453 pairs |
| 2024-03 | **[KazSAnDRA](https://huggingface.co/datasets/issai/kazsandra)**<br><sub>SC</sub><br><sub>Gated · CC-BY-4.0</sub> | Kazakh Sentiment Analysis Dataset of Reviews and Attitudes, with numerically rated reviews supporting polarity and score classification. | **[ISSAI researchers](https://arxiv.org/abs/2403.19335)**<br><sub>ISSAI, Nazarbayev University</sub> | – 108 MB<br>– 180,064 reviews |
| 2024-02 | **[Kazakh–English KAZNU](https://huggingface.co/datasets/Dauren-Nur/kaz_eng_parallel)**<br><sub>MT</sub><br><sub>Open · Not reported</sub> | Parallel Kazakh-English corpus collected from law documents and news sites. | **Al-Farabi Kazakh National University researchers**<br><sub>Al-Farabi Kazakh National University</sub> | – 70.6 MB<br>– 377,044 pairs |
| 2023-11 | **[Kazakh Instruction v2](https://huggingface.co/datasets/AmanMussa/kazakh-instruction-v2)**<br><sub>IFT · QA</sub><br><sub>Open · MIT</sub> | Kazakh instruction dataset built by machine-translating Stanford Alpaca with manual correction and added Kazakhstani names, places, history, and culture instructions. | **Mussa & Mansurova**<br><sub>Al-Farabi Kazakh National University</sub> | – 35.6 MB<br>– 52,201 rows |
| 2023-04 | **[MDBKD](https://huggingface.co/datasets/kz-transformers/multidomain-kazakh-dataset)**<br><sub>LM</sub><br><sub>Open · Apache-2.0</sub> | Multi-Domain Bilingual Kazakh Dataset combining CC100, Kazakh Wikipedia, kazakhBooks, Leipzig news, OSCAR CommonCrawl, and kazakhNews sources. | **[Sagyndyk et al.](https://doi.org/10.36227/techrxiv.175942902.25827042/v1)**<br><sub>kz-transformers</sub> | – 24.7 GB<br>– 24,883,808 texts; 2.09B tokens |
| 2022-06 | **[FLORES-200 Kazakh](https://huggingface.co/datasets/facebook/flores)**<br><sub>MT</sub><br><sub>Open · CC-BY-SA-4.0</sub> | Kazakh (kaz_Cyrl) sentences within FLORES-200, a 200-language many-to-many machine-translation evaluation benchmark of professionally translated Wikipedia sentences. | **NLLB / FLORES team**<br><sub>Meta AI</sub> | – 3,001 sentences (dev + devtest) |
| 2021-11 | **[KazNERD](https://huggingface.co/datasets/issai/kaznerd)**<br><sub>NER</sub><br><sub>Gated · CC-BY-4.0</sub> | Kazakh named-entity corpus of 112,702 sentences from television news text, annotated with 25 entity classes using IOB2. | **[Yeshpanov et al.](https://aclanthology.org/2022.lrec-1.44)**<br><sub>ISSAI, Nazarbayev University</sub> | – 136.7 MB<br>– 112,702 sentences; 136,333 entity annotations |
| 2020-12 | **[KazNewsDataset](https://data.mendeley.com/datasets/hwj24p9gkh/1)**<br><sub>TC · LM</sub><br><sub>Open · CC-BY-4.0</sub> | Kazakhstani news corpus for social-significance identification with topic-modelling results, from open Kazakhstani news media and governmental development programs. | **[Yakunin et al.](https://doi.org/10.3390/data6030031)** | – 1,142,735 documents |
| 2020-12 | **[KazRusNewsDataset](https://data.mendeley.com/datasets/2vz7vtbhn2/1)**<br><sub>TC</sub><br><sub>Open · CC-BY-4.0</sub> | Kazakhstani and Russian news corpus collected via web scraping from open Kazakhstani and Russian media. | **[Yakunin et al.](https://doi.org/10.3390/data6030031)** | – 6,261,953 documents |
| 2019-06 | **[WikiANN Kazakh](https://huggingface.co/datasets/unimelb-nlp/wikiann)**<br><sub>NER</sub><br><sub>Open · Not reported</sub> | Kazakh (kk) split of WikiANN / PAN-X, a Wikipedia-derived multilingual named-entity-recognition dataset with LOC/PER/ORG IOB2 tags. | **Rahimi et al.** | – Not reported (kk split) |
| 2015-06 | **[UD Kazakh KTB](https://universaldependencies.org/treebanks/kk_ktb/)**<br><sub>POS</sub><br><sub>Open · CC-BY-SA-4.0</sub> | Kazakh Universal Dependencies treebank drawn from Wikipedia, folk tales, the UDHR, news, and phrasebook sentences. | **Makazhanov et al.**<br><sub>Universal Dependencies</sub> | – 0.4 MB<br>– 1,078 sentences; 10,536 tokens |
| Not reported | **[kaz-text-for-lm-normalized](https://huggingface.co/datasets/farabi-lab/kaz-text-for-lm-normalized)**<br><sub>LM</sub><br><sub>Gated · Not reported</sub> | Normalized Kazakh language-modelling corpus combining news, literature, academic/dissertation text, and an August-2024 Kazakh Wikipedia snapshot. | **Al-Farabi Kazakh National University** | – 5.99 GB |
| Not reported | **[Uzbek-Kazakh Parallel Corpora](https://huggingface.co/datasets/Sanatbek/uzbek-kazakh-parallel-corpora)**<br><sub>MT</sub><br><sub>Open · Not reported</sub> | Expert-translated Uzbek-Kazakh parallel sentence corpus covering literature and web news. | **[Sanatbek](https://doi.org/10.57967/hf/1748)** | – 34.2 MB<br>– 133,877 pairs |
<!-- NLP_SECTION:END -->

## Speech and audio

<!-- SPEECH_SECTION:START -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/speech_overview-dark.svg">
  <img src="assets/speech_overview.svg" alt="Speech and audio dataset overview" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/speech_release_calendar_1-dark.svg">
  <img src="assets/speech_release_calendar_1.svg" alt="Calendar map of Speech and audio dataset releases, 2020-2023, with year on the x-axis and month on the y-axis" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/speech_release_calendar_2-dark.svg">
  <img src="assets/speech_release_calendar_2.svg" alt="Calendar map of Speech and audio dataset releases, 2024-2026, with year on the x-axis and month on the y-axis" width="100%">
</picture>

**Abbreviations:**

<table>
<tr><td><sub><strong>AQA</strong> — Audio question answering</sub></td><td><sub><strong>ASR</strong> — Automatic speech recognition (ASR)</sub></td><td><sub><strong>EPC</strong> — Emotion / paralinguistic classification</sub></td><td><sub><strong>KWS</strong> — Keyword spotting</sub></td></tr>
<tr><td><sub><strong>RAG</strong> — Retrieval / RAG</sub></td><td><sub><strong>SQA</strong> — Spoken QA</sub></td><td><sub><strong>ST</strong> — Speech translation</sub></td><td><sub><strong>SV</strong> — Speaker verification</sub></td></tr>
<tr><td><sub><strong>TS-ASR</strong> — Target-speaker ASR / speech separation</sub></td><td><sub><strong>TTS</strong> — Text-to-speech (TTS)</sub></td><td></td><td></td></tr>
</table>

| Released | Dataset | Description | Author | Properties |
|---|---|---|---|---|
| 2026-08 | **[YO-CPT-kk](https://huggingface.co/datasets/NCSpeech/YO-CPT-kk)**<br><sub>ASR · TTS · SV</sub><br><sub>Open · custom (yo-cpt-kk)</sub> | YouTube-oriented Kazakh continual-pretraining corpus spanning TTS-grade, ASR, and speaker-verification use cases. | **NCSpeech** | – 100.0 GB<br>– 600 h; 156,903 utterances |
| 2026-07 | **[KazMix-3](https://huggingface.co/datasets/issai/KazMix-3)**<br><sub>TS-ASR</sub><br><sub>Open · CC-BY-4.0</sub> | Kazakh three-speaker overlapping-speech dataset for target-speaker ASR, released with the Persona-ASR project; mixtures derived from KSD/SLR140 with enrollment utterances. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 256.3 MB<br>– 89,775 rows (62.8k/13.5k/13.5k splits) |
| 2026-05 | **[KazEGA](https://huggingface.co/datasets/kazega0/KazEGA)**<br><sub>EPC</sub><br><sub>Gated · CC-BY-NC-4.0</sub> | Kazakh speech corpus for paralinguistic classification, annotated for emotion (7 classes), gender, and age group; source audio extracted from YouTube. | **kazega0** | – 38.1 GB<br>– 96,582 utterances |
| 2026-03 | **[WavCapsQA Kazakh-Russian](https://huggingface.co/datasets/issai/WavCapsQA_Kazakh_Russian)**<br><sub>AQA</sub><br><sub>Open · Not reported</sub> | Machine-translated Kazakh/Russian adaptation of the WavCaps-QA test set for audio question answering over environmental sounds, music, and ambient scenes. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 189 MB<br>– 608 rows (304 Kazakh, 304 Russian) |
| 2026-02 | **[Kazakh Songs ASR](https://huggingface.co/datasets/yeshpanovrustem/kazakh_songs_asr)**<br><sub>ASR</sub><br><sub>Gated · custom (non-commercial)</sub> | Manually aligned Kazakh vocal-audio segments from commercially released songs, for studying whether sung speech improves low-resource ASR. | **[Rustem Yeshpanov](https://arxiv.org/abs/2603.00961)** | – 2.9 GB<br>– ≈4.5 h; 3,013 audio-text pairs (195 songs, 36 artists) |
| 2026-02 | **[Kazakh Speech MFA Punctuation](https://huggingface.co/datasets/govnejri/kazakh_speech_mfa_punctuation)**<br><sub>ASR</sub><br><sub>Open · Not reported</sub> | Punctuation-restored, word-level-timestamped derivative of ISSAI KSC2, force-aligned with the Montreal Forced Aligner. | **Bekzat Uteulin**<br><sub>Jeti Labs</sub> | – 56.8 GB<br>– 408,010 utterances; ≈1,110 h |
| 2026-01 | **[Kazakh Speech Dataset (optimized KSC2)](https://huggingface.co/datasets/Flamme-VRM/kazakh-speech-dataset)**<br><sub>ASR · TTS</sub><br><sub>Open · CC-BY-4.0</sub> | VAD-sliced and Whisper-Turbo re-transcribed derivative of KSC2 with quality filtering. | **Flamme-VRM** | – 54.5 GB<br>– ≈726 h; 230,793 clips |
| 2025-12 | **[Mozilla Common Voice Kazakh](https://datacollective.mozillafoundation.org/datasets/cmj8u3pbb00dhnxxbsqe4vbpc)**<br><sub>ASR</sub><br><sub>Open · CC0-1.0</sub> | Crowdsourced Kazakh voice recordings from the Common Voice Scripted Speech project. | **Mozilla Foundation**<br><sub>Mozilla Foundation</sub> | – 2,750 clips; 3.76 h recorded (2.39 h validated); 193 speakers |
| 2025-04 | **[MATERIAL Kazakh–English Language Pack](https://catalog.ldc.upenn.edu/LDC2025S03)**<br><sub>ST · RAG</sub><br><sub>Paid · LDC membership / subscription tiers</sub> | Kazakh conversational telephone speech with English translations, transcripts, and query-relevance annotations, from Northern and Southern Kazakh dialect regions. | **Appen (for IARPA MATERIAL)**<br><sub>IARPA MATERIAL program</sub> | – ≈57 h |
| 2024-11 | **[Belebele-FLEURS](https://huggingface.co/datasets/WueNLP/belebele-fleurs)**<br><sub>SQA · ASR</sub><br><sub>Open · CC-BY-SA-4.0</sub> | Spoken reading-comprehension benchmark combining Belebele and FLEURS audio/text across 99 languages. | **WüNLP** | – 3.4 GB<br>– 870 Kazakh test examples |
| 2024-04 | **[KazEmoTTS](https://huggingface.co/datasets/issai/KazEmoTTS)**<br><sub>TTS · EPC</sub><br><sub>Application · Not reported</sub> | Kazakh emotional TTS corpus with six emotion classes (neutral, angry, happy, sad, scared, surprised) across male and female narrators. | **[Abilbekov et al.](https://arxiv.org/abs/2404.01033)**<br><sub>ISSAI, Nazarbayev University</sub> | – 10.5 GB<br>– 74.85 h; 54,760 clips |
| 2024-01 | **[ISSAI SKIMMED](https://huggingface.co/datasets/Dauren-Nur/ISSAI_SKIMMED)**<br><sub>ASR · TTS</sub><br><sub>Open · Not reported</sub> | Multimodal Kazakh audio-transcription dataset with train/test/dev splits. | **Dauren-Nur** | – 5.4 GB<br>– 21,617 clips |
| 2023-07 | **[Kazakh Speech Dataset (KSD / SLR140)](https://openslr.org/140/)**<br><sub>ASR</sub><br><sub>Open · CC-BY-SA-3.0</sub> | Open-source Kazakh speech corpus recorded on mobile devices across diverse regions, ages, and genders, verified by native speakers. | **[Mansurova & Kadyrbek](https://doi.org/10.3390/bdcc7030132)**<br><sub>Dept. of AI and Big Data, Al-Farabi Kazakh National University</sub> | – 56 GB<br>– 554 h; 204,250 utterances |
| 2023-04 | **[Kazakh Speech Commands](https://huggingface.co/datasets/issai/kazakh-speech-commands)**<br><sub>KWS</sub><br><sub>Open · Apache-2.0</sub> | Kazakh speech-command recognition dataset built via synthetic TTS generation and speech-corpus scraping, with data augmentation. | **[Kuzdeuov et al.](https://ieeexplore.ieee.org/document/10601292)**<br><sub>IS2AI</sub> | – 267.3 MB<br>– ≈1 h; 3,623 utterances |
| 2022-09 | **[Kazakh Speech Corpus 2 (KSC2)](https://huggingface.co/datasets/issai/Kazakh_Speech_Corpus_2)**<br><sub>ASR</sub><br><sub>Open · MIT</sub> | Industrial-scale open-source Kazakh speech corpus subsuming KSC and KazakhTTS2, with additional TV, radio, senate, and podcast data, including Kazakh-Russian code-switching. | **[Mussakhojayeva et al.](https://www.isca-archive.org/interspeech_2022/mussakhojayeva22_interspeech.html)**<br><sub>ISSAI, Nazarbayev University</sub> | – 80.8 GB<br>– ≈1,200 h; 600,000+ utterances |
| 2022-01 | **[KazakhTTS2](https://issai.nu.edu.kz/tts2-eng/)**<br><sub>TTS</sub><br><sub>Open · Not reported</sub> | Expanded five-speaker Kazakh TTS corpus, extending the original KazakhTTS with more data, speakers, and topics. | **[ISSAI researchers](https://arxiv.org/abs/2201.05771)**<br><sub>ISSAI, Nazarbayev University</sub> | – 35.7 GB<br>– 271 h; 5 speakers |
| 2021-04 | **[KazakhTTS](https://huggingface.co/datasets/issai/KazakhTTS)**<br><sub>TTS</sub><br><sub>Open · Not reported</sub> | Open-source Kazakh text-to-speech corpus, later expanded by KazakhTTS2. | **[Mussakhojayeva et al.](https://aclanthology.org/2022.lrec-1.578.pdf)**<br><sub>ISSAI, Nazarbayev University</sub> | – 11.9 GB<br>– ≈93 h; 42,000 utterances |
| 2020-09 | **[Kazakh Speech Corpus (KSC)](https://issai.nu.edu.kz/kz-speech-corpus/)**<br><sub>ASR</sub><br><sub>Open · CC-BY-4.0</sub> | Crowdsourced Kazakh speech corpus with an initial ASR baseline. | **[ISSAI researchers](https://arxiv.org/abs/2009.10334)**<br><sub>ISSAI, Nazarbayev University</sub> | – ≈332 h; 153,000 utterances |
<!-- SPEECH_SECTION:END -->

### English-Russian-Kazakh comparison by speech task

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/speech_task_hours_comparison-dark.svg">
  <img src="assets/speech_task_hours_comparison.svg" alt="Grouped vertical bars comparing public speech-data hours for Kazakh, Russian, and English across ASR, TTS, speech translation, emotion, keyword spotting, and speaker verification" width="100%">
</picture>

The bars are conservative lower bounds, not estimates of every dataset in existence.
Subsets, mirrors, and known derivatives are excluded. For speaker verification (`*`),
a broader speaker-presence rule counts complete multilingual corpora when they
explicitly contain speakers of the language; these are **corpus-hours containing the
language**, not language-only hours, and possible cross-corpus overlap remains.

## Vision, OCR, and multimodal

<!-- VISION_SECTION:START -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/vision_overview-dark.svg">
  <img src="assets/vision_overview.svg" alt="Vision, OCR, and multimodal dataset overview" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cv_release_calendar-dark.svg">
  <img src="assets/cv_release_calendar.svg" alt="Calendar map of Vision, OCR, and multimodal dataset releases, 2020-2026, with year on the x-axis and month on the y-axis" width="100%">
</picture>

**Abbreviations:**

<table>
<tr><td><sub><strong>AVQA</strong> — Audio-visual QA</sub></td><td><sub><strong>DQA</strong> — Diagram QA</sub></td><td><sub><strong>DU</strong> — Layout analysis / document understanding</sub></td><td><sub><strong>HTR</strong> — Handwriting recognition</sub></td></tr>
<tr><td><sub><strong>OCR</strong> — OCR</sub></td><td><sub><strong>T2I</strong> — Cultural vision benchmark (text-to-image)</sub></td><td><sub><strong>VMR</strong> — Visual math reasoning</sub></td><td><sub><strong>VQA</strong> — Visual QA</sub></td></tr>
<tr><td><sub><strong>VSR</strong> — Visual speech recognition (lip reading)</sub></td><td></td><td></td><td></td></tr>
</table>

| Released | Dataset | Description | Author | Properties |
|---|---|---|---|---|
| 2026-06 | **[Darmm Kazakh Cyrillic OCR](https://huggingface.co/datasets/Darmm/darmm-ocr-kazakh-cyrillic)**<br><sub>OCR</sub><br><sub>Open · Apache-2.0</sub> | Synthetic printed-text OCR dataset for Kazakh Cyrillic, rendered from Kazakh Wikipedia text with Kazakh-specific characters (Ә, Ғ, Қ, Ң, Ө, Ұ, Ү, Һ, І). | **Rakhat Zhumabek** | – 2.3 GB<br>– 200,000 images (100k word-level + 100k line-level) |
| 2026-06 | **[TurkicOCR-Cyrillic](https://huggingface.co/datasets/alenisaw/turkicocr-cyrillic)**<br><sub>OCR · DU</sub><br><sub>Open · CC-BY-4.0</sub> | Synthetic Turkic-Cyrillic OCR dataset spanning Kazakh, Kyrgyz, Kazakh-Russian, and Kyrgyz-Russian text and layouts. | **Alen Issayev** | – 66.7 GB<br>– 100,000 unique pages; 175,000 nested-config rows |
| 2026-04 | **[BeyneleBench](https://huggingface.co/datasets/issai/BeyneleBench)**<br><sub>T2I</sub><br><sub>Open · CC-BY-4.0</sub> | Kazakh/English benchmark for cultural fidelity in text-to-image generation, pairing prompts with reference images and cultural taxonomy levels. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 2.0 GB<br>– 750 |
| 2026-04 | **[SpokenMQA Kazakh](https://huggingface.co/datasets/issai/SpokenMQA_Kazakh)**<br><sub>AVQA</sub><br><sub>Open · Not reported</sub> | Machine-translated Kazakh adaptation of SpokenMQA for evaluating spoken mathematical reasoning in speech/audio-language models. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 1.4 GB<br>– 2,256 |
| 2026-03 | **[MMBench Kazakh](https://huggingface.co/datasets/issai/MMBench_Kazakh)**<br><sub>VQA</sub><br><sub>Open · Not reported</sub> | Kazakh translation of the MMBench validation split, evaluating perception, reasoning, and logic via multiple-choice VQA. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 772.2 MB<br>– 4,329 |
| 2026-03 | **[MathVision Kazakh](https://huggingface.co/datasets/issai/MathVision_Kazakh)**<br><sub>VMR</sub><br><sub>Open · MIT</sub> | Machine-translated MathVision dataset for evaluating mathematical reasoning and visual understanding in multimodal LLMs. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 248.7 MB<br>– 3,040 |
| 2025-12 | **[KazakhOCR](https://huggingface.co/datasets/henrygagnier/kazakh-ocr)**<br><sub>OCR</sub><br><sub>Open · MIT</sub> | Synthetic benchmark for evaluating multimodal models on Arabic-, Cyrillic-, and Latin-script Kazakh OCR. | **[Gagnier et al.](https://aclanthology.org/2026.abjadnlp-1.8/)** | – 15.3 GB<br>– 600 images |
| 2025-12 | **[AI2D Kazakh](https://huggingface.co/datasets/issai/AI2D_Kazakh)**<br><sub>DQA</sub><br><sub>Open · Not reported</sub> | Kazakh translation of AI2D diagram-question-answering data. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 465.0 MB<br>– 3,088 |
| 2025-12 | **[MathVista Kazakh](https://huggingface.co/datasets/issai/MathVista_Kazakh)**<br><sub>VMR</sub><br><sub>Open · CC-BY-SA-4.0</sub> | Kazakh translation of MathVista for visual math reasoning. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 52.6 MB<br>– 1,000 |
| 2025-12 | **[OCRBench Kazakh](https://huggingface.co/datasets/issai/OCRBench-Kazakh)**<br><sub>OCR · VQA</sub><br><sub>Open · Apache-2.0</sub> | Kazakh OCR and visual-QA benchmark translated from OCRBench. | **ISSAI researchers**<br><sub>ISSAI, Nazarbayev University</sub> | – 28.7 MB<br>– 441 |
| 2025-12 | **[QazLip](https://doi.org/10.7910/DVN/VIP1J8)**<br><sub>VSR</sub><br><sub>Open · Not reported</sub> | Kazakh lip-movement command corpus of 102 nouns recorded from 26 participants at 1080p/60fps for visual speech recognition. | **[Zhalgas, A. et al.](https://doi.org/10.1038/s41597-025-06193-0)** | – ≈34,000 videos; 1.2M frames |
| 2021-10 | **[KOHTD](https://github.com/abdoelsayed2016/KOHTD)**<br><sub>HTR</sub><br><sub>Application · CC-BY-NC-ND-4.0</sub> | Kazakh Offline Handwritten Text Dataset of exam papers (99% Kazakh, 1% Russian). | **[Toiganbayeva et al.](https://doi.org/10.1016/j.image.2022.116827)**<br><sub>Satbayev University · Al-Farabi Kazakh National University</sub> | – 2.6 MB<br>– 3,000 exam papers; 140,335+ segmented images; ≈922,010 symbols |
| 2020-07 | **[HKR](https://github.com/abdoelsayed2016/HKR_Dataset)**<br><sub>HTR</sub><br><sub>Application · CC-BY-NC-ND-4.0</sub> | Handwritten Kazakh and Russian database (HKR), predominantly Russian (≈95%) with a Kazakh minority share (≈5%). | **[Nurseitov et al.](https://doi.org/10.1007/s11042-021-11399-6)** | – 1,400+ forms; ≈63,000 sentences; ≈715,699 symbols (≈5% Kazakh) |
<!-- VISION_SECTION:END -->

## Watchlist / announced resources

Resources below are announced, described in a paper without a public artifact,
license-conflicted, or not yet independently verifiable as usable Kazakh-language
datasets. They are intentionally **not** part of the main catalog above.

<!-- WATCHLIST:START -->
- **KazBench-KK** — A 7,111-question cultural-knowledge benchmark introduced at the Fourth Workshop on NLP Applications to Field Linguistics (August 2025). No public dataset download, GitHub repository, or Hugging Face card could be located from the paper — only the [ACL Anthology paper](https://aclanthology.org/2025.fieldmatters-1.4/) is verifiable.
- **Zerde-QA-Wiki-20K** — Referenced as a candidate Kazakh Wikipedia-QA release; no dataset card, repository, or download under this name could be independently verified.
- **TilQazyna collections** — Numerous text and speech repositories appeared on Hugging Face in June-August 2026, but several are gated and their cards do not yet provide stable totals or independent documentation.
- **Kazakh Text Corpus / Speech Corpus / AI Evaluation Benchmark Suite** — Announced in July 2026 as more than 10B text tokens and 10,000 speech hours (including 1,000 manually transcribed hours), but no public dataset download was identified.
- **Multimedia Corpus of Modern Spoken Kazakh Language** — The searchable project exists, but the first module's downloadable size and reuse terms could not be confirmed.
- **Aqbileq** — Named as a candidate Kazakh resource; no dataset card, repository, or paper could be independently located under this name.
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
