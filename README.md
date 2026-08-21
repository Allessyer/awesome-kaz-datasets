<h1 align="center">
  <img src="https://emojiassets.saruwakakun.design/a/lg/1f1f0_1f1ff_1o53s.webp" width="34" valign="middle" alt="Kazakhstan flag">
  Awesome Kazakh Datasets
  <img src="https://emojiassets.saruwakakun.design/a/lg/1f1f0_1f1ff_1o53s.webp" width="34" valign="middle" alt="Kazakhstan flag">
</h1>

<p align="center">
  A curated, verified catalog of public datasets for Kazakh-language NLP, LLM, speech, and vision research.
</p>

<!-- BADGES:START -->
<p align="center">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Allessyer/awesome-kaz-datasets?style=flat&color=eda100">
  <img alt="Datasets" src="https://img.shields.io/badge/Datasets-86-2a78d6">
  <img alt="Open access" src="https://img.shields.io/badge/Open_access-67%25-2ea44f">
  <img alt="Last verified" src="https://img.shields.io/badge/Last_verified-2026--08--20-1baf7a">
</p>
<!-- BADGES:END -->

<p align="center">
  <a href="#about">About</a> ·
  <a href="#text-nlp-and-llm">Text &amp; NLP</a> ·
  <a href="#speech-and-audio">Speech</a> ·
  <a href="#vision-ocr-and-multimodal">Vision &amp; OCR</a> ·
  <a href="#watchlist--announced-resources">Watchlist</a> ·
  <a href="#contributing">Contributing</a> ·
  <a href="#license">License</a>
</p>

---

## About

Kazakh is spoken by roughly 13 million people, yet reusable public datasets for it
are scattered across Hugging Face, GitHub, institutional pages, and archives with
no reliable map of what's actually downloadable today.

Every entry below is checked against its primary source, with release date, access
terms, and license recorded rather than assumed. Resources that are announced but
not yet independently verifiable go in the [Watchlist](#watchlist--announced-resources)
instead of the main tables. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full
inclusion policy and [CHANGELOG.md](CHANGELOG.md) for what's new.

<!-- LANDSCAPE:START -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/dataset_growth-dark.svg">
  <img src="assets/dataset_growth.svg" alt="Cumulative Kazakh dataset releases over time, by section" width="100%">
</picture>

<sub>Cumulative Kazakh dataset releases over time, by section.</sub>
<!-- LANDSCAPE:END -->

## Text, NLP, and LLM

<!-- NLP_SECTION:START -->

| ID | Released | Dataset | Task | Description | Storage | Samples |
|---:|---|---|---|---|---|---|
| 1 | 2026-06 | **[FreshQA Kazakh](https://huggingface.co/datasets/issai/freshqa_kazakh)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | QA | Bilingual (English/Kazakh) benchmark of factual questions with false premises, for testing how models handle incorrect assumptions. | 0.4 MB | 600 |
| 2 | 2026-06 | **[DeFAn Kazakh](https://huggingface.co/datasets/issai/defan_kazakh)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | QA | Machine-translated Kazakh/English version of the DefAn hallucination benchmark for definitive question answering. | 0.2 MB | 3,178 questions |
| 3 | 2026-06 | **[Kazakh Open Retrieval Benchmark](https://huggingface.co/datasets/Tim2190/kaz-rag-search-benchmark)**<br><sub>[Timur Seidalin](https://doi.org/10.5281/zenodo.20605663)</sub><br><sub>Open</sub> | RAG · QA | Evidence-based Kazakh information-retrieval benchmark built from Kazakh Wikipedia, showing morphological stemming outperforms multilingual embeddings. | 14.6 MB | 300 queries; 8,370 passages |
| 4 | 2026-06 | **[Til-Corpus](https://huggingface.co/datasets/TilQazyna/Til-Corpus)**<br><sub>Til-Qazyna</sub><br><sub>Gated</sub> | LM | Kazakh-centered, quality-tiered text corpus for language-model pretraining, with Russian, English, and mixed-language material. | 204.2 GB | 58,850,639 documents |
| 5 | 2026-06 | **[Til-Instruct](https://huggingface.co/datasets/TilQazyna/Til-Instruct)**<br><sub>Til-Qazyna</sub><br><sub>Gated</sub> | IFT | Unified, model-judged and quality-tiered Kazakh-focused instruction-tuning collection assembled from TilQazyna SFT sources. | 8.35 GB | 2,563,966 raw; 2,114,016 clean; 1,581,787 premium (≈6.26M rows total) |
| 6 | 2026-06 | **[Til-Books](https://huggingface.co/datasets/TilQazyna/Til-Books)**<br><sub>Til-Qazyna</sub><br><sub>Gated</sub> | LM | Two-layer full-text book corpus with exact extraction/OCR and cleaned reading text for Kazakh language modelling. | 2.02 GB | 16,847 books; 13,194 Kazakh |
| 7 | 2026-06 | **[Til-Parallel](https://huggingface.co/datasets/TilQazyna/Til-Parallel)**<br><sub>Til-Qazyna</sub><br><sub>Gated</sub> | LM | Large quality-tiered multilingual corpus centered on Kazakh, with Russian and English material. | 72.16 GB | 23,294,865 rows |
| 8 | 2026-06 | **[Til-Morphology](https://huggingface.co/datasets/TilQazyna/Til-Morphology)**<br><sub>Til-Qazyna</sub><br><sub>Gated</sub> | MORPH | Kazakh morphological-analysis collection with word segmentation and morpheme-count fields, quality-tiered by model judging. | 207.8 MB | 3,767,518 analyses |
| 9 | 2026-06 | **[Til-Classification](https://huggingface.co/datasets/TilQazyna/Til-Classification)**<br><sub>Til-Qazyna</sub><br><sub>Gated</sub> | TC | Quality-tiered Kazakh-focused text-classification collection with labels, tasks, provenance, and model-judge scores. | 15.1 MB | 91,766 rows |
| 10 | 2026-06 | **[Til-Terminology](https://huggingface.co/datasets/TilQazyna/Til-Terminology)**<br><sub>Til-Qazyna</sub><br><sub>Gated</sub> | LM | Quality-tiered terminology-focused text collection for Kazakh language research and text generation/pretraining. | 5.7 MB | 317,277 rows |
| 11 | 2026-06 | **[Til-Web-Raw-KK-v1](https://huggingface.co/datasets/TilQazyna/Til-Web-Raw-KK-v1)**<br><sub>Til-Qazyna</sub><br><sub>Gated</sub> | LM | Raw HTML mirror of two Kazakh educational and Q&A websites (bilim-all.kz, surak.baribar.kz) — server-rendered pages, images, and attachments collected before text extraction/cleaning, as source material for the Til foundation-model program. | 19.5 GB | ≈222,890 pages |
| 12 | 2026-05 | **[KazLawBench](https://huggingface.co/datasets/raiym76/kazlawbench)**<br><sub>Batyr Raiym</sub><br><sub>Gated</sub> | LQA | First bilingual (Russian + Kazakh) legal-LLM benchmark for Kazakhstan, spanning statutory codes and de-identified Supreme Court judgments across seven task types. | 9.9 MB | 3,098 |
| 13 | 2026-05 | **[100k Movie Reviews from Kazakhstan](https://huggingface.co/datasets/yeshpanovrustem/100k_movie_reviews_from_kz)**<br><sub>[Rustem Yeshpanov](https://arxiv.org/abs/2605.08600)</sub><br><sub>Gated</sub> | SC | 100,502 kino.kz movie reviews (2001-2025) manually annotated for language ID and sentiment, capturing Russian, Kazakh, and code-switched Kazakh-Russian text. | 57.7 MB | 100,502 reviews |
| 14 | 2026-04 | **[Zerde-QA-50K](https://huggingface.co/datasets/kurumikz/Zerde-QA-50K)**<br><sub>kurumikz</sub><br><sub>Open</sub> | IFT · QA | Synthetic Kazakh QA collection spanning 20+ academic domains for instruction tuning and low-resource NLP research. | 156.2 MB | 51,422 pairs |
| 15 | 2026-03 | **[RAGBench Kazakh](https://huggingface.co/datasets/issai/RAGBench_Kazakh)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | RAG | Kazakh translation of RAGBench for evaluating retrieval-augmented-generation systems across biomedical, legal, financial, and general-knowledge domains. | 31.2 MB | 11,431 |
| 16 | 2026-03 | **[IFBench Kazakh](https://huggingface.co/datasets/issai/IFBench_Kazakh)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | IF | Machine-translated Kazakh instruction-following benchmark evaluating adherence to explicit constraints. | 1.3 MB | 444 |
| 17 | 2026-02 | **[Kazakh Analytical RAG (Single-Document)](https://huggingface.co/datasets/farabi-lab/KZ-RAG-single-docs-final-gold)**<br><sub>[Kadyrbek et al.](https://doi.org/10.3390/bdcc9050137)</sub><br><sub>Gated</sub> | RAG · QA | High-density Kazakh analytical question-answering collection with single-document context, for retrieval-augmented generation research. | 33.4 MB | 4,522 examples; ≈5.98M words |
| 18 | 2026-02 | **[Content Moderation and Safety — Kazakh](https://huggingface.co/datasets/farabi-lab/Content-Moderation-and-Safety)**<br><sub>[Kadyrbek et al.](https://doi.org/10.3390/bdcc9050137)</sub><br><sub>Gated</sub> | Safety · TC | Kazakh content-moderation and safety dataset with toxicity categories, severity labels, domain tags, and constructive de-escalating responses. | 9.3 MB | 17,827 examples; ≈1.67M words |
| 19 | 2026-02 | **[Multi-Step Reasoning for Kazakh Context](https://huggingface.co/datasets/farabi-lab/multi_step_reasoning_kazakh_context)**<br><sub>[Kadyrbek et al.](https://doi.org/10.3390/bdcc9050137)</sub><br><sub>Gated</sub> | QA | Kazakh question-answering and instruction collection centered on complex multi-step reasoning and culturally grounded analysis. | 39.0 MB | 10,981 examples; ≈6.65M words |
| 20 | 2025-12 | **[MMLU-Pro Kazakh/Russian](https://huggingface.co/datasets/issai/MMLU-Pro_Kazakh_Russian)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | MCQA | Machine-translated Kazakh/Russian version of MMLU-Pro, with more answer options and more challenging reasoning tasks than MMLU. | 11.4 MB | 24,064 rows; 12k per language |
| 21 | 2025-10 | **[KazCulture](https://huggingface.co/datasets/issai/KazCulture)**<br><sub>ISSAI researchers</sub><br><sub>Gated</sub> | CQA | Human-written passage-question-answer triplets covering Kazakh traditions, music, beliefs, cuisine, games, clothing, and handicrafts. | 4.6 MB | 16,137 PQA triplets |
| 22 | 2025-07 | **[HPLT 3.0 Kazakh](https://huggingface.co/datasets/HPLT/HPLT3.0)**<br><sub>HPLT project</sub><br><sub>Open</sub> | LM | Kazakh Cyrillic subset of HPLT 3.0, a large multilingual web-crawl corpus for language-model pretraining. | Not reported | ≈5.12M documents; ≈100.6M segments; ≈7.34B tokens |
| 23 | 2025-05 | **[Qorgau](https://github.com/mbzuai-nlp/qorgau-kaz-ru-safety)**<br><sub>[MBZUAI NLP group](https://arxiv.org/abs/2502.13640)</sub><br><sub>Open</sub> | Safety | Kazakh/Russian bilingual LLM-safety evaluation benchmark spanning six high-level risk areas and 17 harm types. | 103.9 MB | 2,790 prompts |
| 24 | 2025-03 | **[KazakhTextDuplicates v2.0](https://huggingface.co/datasets/Arailym-tleubayeva/KazakhTextDuplicates)**<br><sub>[Arailym Tleubayeva](https://www.mdpi.com/2306-5729/11/6/133)</sub><br><sub>Open</sub> | STS | Controlled multi-regime benchmark for semantic deduplication, semantic similarity, and retrieval in Kazakh, with seven deterministic duplication regimes. | 217 MB | 25,922 rows |
| 25 | 2025-02 | **[Kazakh-IFT](https://huggingface.co/datasets/nurkhan5l/kazakh-ift)**<br><sub>[Laiyk et al.](https://arxiv.org/abs/2502.13647)</sub><br><sub>Gated</sub> | IFT | Instruction-following dataset covering Kazakhstani governance, legal process, cultural practice, and public-service knowledge, LLM-generated with GPT-4o. | 7.85 MB | ~10,600 samples |
| 26 | 2025-01 | **[KazMMLU](https://huggingface.co/datasets/MBZUAI/KazMMLU)**<br><sub>[Togmanov et al.](https://arxiv.org/abs/2502.12829)</sub><br><sub>Open</sub> | MCQA | Kazakh/Russian multiple-choice benchmark covering regional knowledge of Kazakhstan across school and university subjects. | 17.4 MB | 23,000 total; 10,969 Kazakh |
| 27 | 2025-01 | **[FineWeb2 Kazakh](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2/viewer/kaz_Cyrl)**<br><sub>Hugging Face FineWeb team</sub><br><sub>Open</sub> | LM | Kazakh (kaz_Cyrl) configuration of FineWeb2, a deduplicated, quality-filtered multilingual web-crawl pretraining corpus. | Not reported | 3,380,000 rows (kaz_Cyrl) |
| 28 | 2025 | **[KazBench-KK](https://huggingface.co/datasets/kz-transformers/kk-socio-cultural-bench-mc)**<br><sub>[KazBench-KK authors](https://aclanthology.org/2025.fieldmatters-1.4/)</sub><br><sub>Open</sub> | CQA · MCQA | Culturally grounded Kazakh multiple-choice benchmark spanning 17 domains of traditions, society, history, and contemporary knowledge. | 2.35 MB | 7,111 questions |
| 29 | 2024-11 | **[Kazakh Dastur MC](https://huggingface.co/datasets/kz-transformers/kazakh-dastur-mc)**<br><sub>kz-transformers</sub><br><sub>Open</sub> | MCQA | Multiple-choice benchmark on Kazakh traditions and customs (dastur). | 0.3 MB | 1,005 |
| 30 | 2024-11 | **[Kazakh Constitution MC](https://huggingface.co/datasets/kz-transformers/kazakh-constitution-mc)**<br><sub>kz-transformers</sub><br><sub>Open</sub> | MCQA | Multiple-choice benchmark on the Constitution of the Republic of Kazakhstan. | 0.1 MB | 414 |
| 31 | 2024-11 | **[Kazakh UNT](https://huggingface.co/datasets/kz-transformers/kazakh-unified-national-testing-mc)**<br><sub>kz-transformers</sub><br><sub>Open</sub> | MCQA | Multiple-choice benchmark built from the Kazakh Unified National Testing exam. | 4.4 MB | 14,850 |
| 32 | 2024-11 | **[MMLU Translated KK](https://huggingface.co/datasets/kz-transformers/mmlu-translated-kk)**<br><sub>kz-transformers</sub><br><sub>Open</sub> | MCQA | Machine-translated Kazakh version of MMLU. | 11.4 MB | 15,854 |
| 33 | 2024-11 | **[GSM8K Translated KK](https://huggingface.co/datasets/kz-transformers/gsm8k-kk-translated)**<br><sub>kz-transformers</sub><br><sub>Open</sub> | MR | Machine-translated Kazakh version of GSM8K grade-school math word problems. | 4.2 MB | 8,792 |
| 34 | 2024-06 | **[mOSCAR Kazakh](https://huggingface.co/datasets/oscar-corpus/mOSCAR)**<br><sub>[OSCAR project](https://arxiv.org/abs/2406.08707)</sub><br><sub>Open</sub> | LM | Kazakh Cyrillic configuration of mOSCAR, the multimodal multilingual OSCAR web-crawl release. | 548.6 MB | 248,403 documents |
| 35 | 2024-05 | **[Textual Foundations of Justice](https://data.mendeley.com/datasets/jdpc5658nh/3)**<br><sub>[Akhmetov et al.](https://doi.org/10.17632/jdpc5658nh.3)</sub><br><sub>Open</sub> | LQA · LM | All current laws of the Republic of Kazakhstan as of 2024-04-01, in Russian and Kazakh, for legal-QA model training. | Not reported | Not reported |
| 36 | 2024-04 | **[KazQAD](https://huggingface.co/datasets/issai/kazqad)**<br><sub>[Yeshpanov et al.](https://arxiv.org/abs/2404.04487)</sub><br><sub>Gated</sub> | QA · RAG | Kazakh open-domain QA dataset supporting reading comprehension, full ODQA, and information-retrieval settings, built from translated Natural Questions and the Kazakh UNT exam. | 281.7 MB | 6,000 questions; 12,700 passages |
| 37 | 2024-03 | **[KazParC](https://huggingface.co/datasets/issai/kazparc)**<br><sub>[ISSAI researchers](https://arxiv.org/abs/2403.19399)</sub><br><sub>Gated</sub> | MT | Kazakh parallel corpus covering Kazakh, English, Russian, and Turkish across proverbs, literature, news, TED talks, legal documents, and UN publications, plus a large synthetic (SynC) extension. | 25.9 GB | 372,000 sentence pairs (+ 1.8M synthetic) |
| 38 | 2024-03 | **[Kazakh–Russian KAZNU](https://huggingface.co/datasets/Dauren-Nur/kaz_rus_parallel_corpora_KAZNU)**<br><sub>Dauren-Nur</sub><br><sub>Open</sub> | MT | Parallel Kazakh-Russian corpus of governmental and official documents. | 23.4 MB | 86,453 pairs |
| 39 | 2024-03 | **[KazSAnDRA](https://huggingface.co/datasets/issai/kazsandra)**<br><sub>[ISSAI researchers](https://arxiv.org/abs/2403.19335)</sub><br><sub>Gated</sub> | SC | Kazakh Sentiment Analysis Dataset of Reviews and Attitudes, with numerically rated reviews supporting polarity and score classification. | 108 MB | 180,064 reviews |
| 40 | 2024-02 | **[Kazakh–English KAZNU](https://huggingface.co/datasets/Dauren-Nur/kaz_eng_parallel)**<br><sub>Al-Farabi Kazakh National University researchers</sub><br><sub>Open</sub> | MT | Parallel Kazakh-English corpus collected from law documents and news sites. | 70.6 MB | 377,044 pairs |
| 41 | 2023-11 | **[Kazakh Instruction v2](https://huggingface.co/datasets/AmanMussa/kazakh-instruction-v2)**<br><sub>Mussa & Mansurova</sub><br><sub>Open</sub> | IFT · QA | Kazakh instruction dataset built by machine-translating Stanford Alpaca with manual correction and added Kazakhstani names, places, history, and culture instructions. | 35.6 MB | 52,201 rows |
| 42 | 2023-09 | **[CulturaX Kazakh](https://huggingface.co/datasets/uonlp/CulturaX)**<br><sub>[CulturaX authors](https://arxiv.org/abs/2309.09400)</sub><br><sub>Gated</sub> | LM | Kazakh subset of CulturaX, a cleaned and deduplicated multilingual web corpus for language-model pretraining. | Not reported | 2,733,982 documents; 2,802,485,195 tokens |
| 43 | 2023-09 | **[SIB-200 Kazakh](https://huggingface.co/datasets/Davlan/sib200)**<br><sub>[David Ifeoluwa Adelani](https://arxiv.org/abs/2309.07445)</sub><br><sub>Open</sub> | TC | Kazakh topic-classification configuration of SIB-200, derived from FLORES-200 and covering seven news topics. | 0.14 MB | 1,004 examples (701 train; 99 validation; 204 test) |
| 44 | 2023-04 | **[MDBKD](https://huggingface.co/datasets/kz-transformers/multidomain-kazakh-dataset)**<br><sub>[Sagyndyk et al.](https://doi.org/10.36227/techrxiv.175942902.25827042/v1)</sub><br><sub>Open</sub> | LM | Multi-Domain Bilingual Kazakh Dataset combining CC100, Kazakh Wikipedia, kazakhBooks, Leipzig news, OSCAR CommonCrawl, and kazakhNews sources. | 24.7 GB | 24,883,808 texts; 2.09B tokens |
| 45 | 2022-06 | **[FLORES-200 Kazakh](https://huggingface.co/datasets/facebook/flores)**<br><sub>NLLB / FLORES team</sub><br><sub>Open</sub> | MT | Kazakh (kaz_Cyrl) sentences within FLORES-200, a 200-language many-to-many machine-translation evaluation benchmark of professionally translated Wikipedia sentences. | Not reported | 3,001 sentences (dev + devtest) |
| 46 | 2021-11 | **[KazNERD](https://huggingface.co/datasets/issai/kaznerd)**<br><sub>[Yeshpanov et al.](https://aclanthology.org/2022.lrec-1.44)</sub><br><sub>Gated</sub> | NER | Kazakh named-entity corpus of 112,702 sentences from television news text, annotated with 25 entity classes using IOB2. | 136.7 MB | 112,702 sentences; 136,333 entity annotations |
| 47 | 2020-12 | **[KazNewsDataset](https://data.mendeley.com/datasets/hwj24p9gkh/1)**<br><sub>[Yakunin et al.](https://doi.org/10.3390/data6030031)</sub><br><sub>Open</sub> | TC · LM | Kazakhstani news corpus for social-significance identification with topic-modelling results, from open Kazakhstani news media and governmental development programs. | Not reported | 1,142,735 documents |
| 48 | 2020-12 | **[KazRusNewsDataset](https://data.mendeley.com/datasets/2vz7vtbhn2/1)**<br><sub>[Yakunin et al.](https://doi.org/10.3390/data6030031)</sub><br><sub>Open</sub> | TC | Kazakhstani and Russian news corpus collected via web scraping from open Kazakhstani and Russian media. | Not reported | 6,261,953 documents |
| 49 | 2020 | **[CC-100 Kazakh](https://huggingface.co/datasets/statmt/cc100)**<br><sub>[CC-Net / XLM-R team](https://arxiv.org/abs/1911.02116)</sub><br><sub>Open</sub> | LM | Explicit Kazakh (kk) monolingual subset of CC-100 reconstructed from Common Crawl for multilingual language modelling. | Not reported | Not reported |
| 50 | 2019-06 | **[WikiANN Kazakh](https://huggingface.co/datasets/unimelb-nlp/wikiann)**<br><sub>Rahimi et al.</sub><br><sub>Open</sub> | NER | Kazakh (kk) split of WikiANN / PAN-X, a Wikipedia-derived multilingual named-entity-recognition dataset with LOC/PER/ORG IOB2 tags. | Not reported | Not reported (kk split) |
| 51 | 2015-06 | **[UD Kazakh KTB](https://universaldependencies.org/treebanks/kk_ktb/)**<br><sub>Makazhanov et al.</sub><br><sub>Open</sub> | POS | Kazakh Universal Dependencies treebank drawn from Wikipedia, folk tales, the UDHR, news, and phrasebook sentences. | 0.4 MB | 1,078 sentences; 10,536 tokens |
| 52 | Not reported | **[kaz-text-for-lm-normalized](https://huggingface.co/datasets/farabi-lab/kaz-text-for-lm-normalized)**<br><sub>Al-Farabi Kazakh National University</sub><br><sub>Gated</sub> | LM | Normalized Kazakh language-modelling corpus combining news, literature, academic/dissertation text, and an August-2024 Kazakh Wikipedia snapshot. | 5.99 GB | Not reported |
| 53 | Not reported | **[Uzbek-Kazakh Parallel Corpora](https://huggingface.co/datasets/Sanatbek/uzbek-kazakh-parallel-corpora)**<br><sub>[Sanatbek](https://doi.org/10.57967/hf/1748)</sub><br><sub>Open</sub> | MT | Expert-translated Uzbek-Kazakh parallel sentence corpus covering literature and web news. | 34.2 MB | 133,877 pairs |
<!-- NLP_SECTION:END -->

## Speech and audio

<!-- SPEECH_SECTION:START -->

| ID | Released | Dataset | Task | Description | Storage | Samples |
|---:|---|---|---|---|---|---|
| 1 | 2026-08 | **[YO-CPT-kk](https://huggingface.co/datasets/NCSpeech/YO-CPT-kk)**<br><sub>NCSpeech</sub><br><sub>Open</sub> | ASR · TTS · SV | YouTube-oriented Kazakh continual-pretraining corpus spanning TTS-grade, ASR, and speaker-verification use cases. | 100.0 GB | 600 h; 156,903 utterances |
| 2 | 2026-07 | **[KazMix-3](https://huggingface.co/datasets/issai/KazMix-3)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | TS-ASR | Kazakh three-speaker overlapping-speech dataset for target-speaker ASR, released with the Persona-ASR project; mixtures derived from KSD/SLR140 with enrollment utterances. | 256.3 MB | 89,775 rows (62.8k/13.5k/13.5k splits) |
| 3 | 2026-06 | **[Til-Audio](https://huggingface.co/datasets/TilQazyna/Til-Audio)**<br><sub>Til-Qazyna</sub><br><sub>Gated</sub> | ASR · TTS | Kazakh audio-and-transcript collection for speech recognition, speech synthesis, and audio classification. | 249.77 GB | 380,068 audio/transcript rows |
| 4 | 2026-05 | **[KazEGA](https://huggingface.co/datasets/kazega0/KazEGA)**<br><sub>kazega0</sub><br><sub>Gated</sub> | EPC | Kazakh speech corpus for paralinguistic classification, annotated for emotion (7 classes), gender, and age group; source audio extracted from YouTube. | 38.1 GB | 96,582 utterances |
| 5 | 2026-03 | **[WavCapsQA Kazakh-Russian](https://huggingface.co/datasets/issai/WavCapsQA_Kazakh_Russian)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | AQA | Machine-translated Kazakh/Russian adaptation of the WavCaps-QA test set for audio question answering over environmental sounds, music, and ambient scenes. | 189 MB | 608 rows (304 Kazakh, 304 Russian) |
| 6 | 2026-02 | **[Multimedia Corpus of Modern Spoken Kazakh Language (Module 1)](https://github.com/gtroiani/MultCorSKL)**<br><sub>[Troiani et al.](https://doi.org/10.5334/johd.529)</sub><br><sub>Open</sub> | ASR | First module of a corpus of naturally occurring spoken Kazakh conversations (2021-2023), with WAV audio, ELAN/EAF time-aligned transcriptions, verticalized TSV and linearized text, plus participant and speech-event metadata. | Not reported | ≈12 h; 33 speech events; 78 participants |
| 7 | 2026-02 | **[Kazakh Songs ASR](https://huggingface.co/datasets/yeshpanovrustem/kazakh_songs_asr)**<br><sub>[Rustem Yeshpanov](https://arxiv.org/abs/2603.00961)</sub><br><sub>Gated</sub> | ASR | Manually aligned Kazakh vocal-audio segments from commercially released songs, for studying whether sung speech improves low-resource ASR. | 2.9 GB | ≈4.5 h; 3,013 audio-text pairs (195 songs, 36 artists) |
| 8 | 2026-02 | **[Kazakh Speech MFA Punctuation](https://huggingface.co/datasets/govnejri/kazakh_speech_mfa_punctuation)**<br><sub>Bekzat Uteulin</sub><br><sub>Open</sub> | ASR | Punctuation-restored, word-level-timestamped derivative of ISSAI KSC2, force-aligned with the Montreal Forced Aligner. | 56.8 GB | 408,010 utterances; ≈1,110 h |
| 9 | 2026-01 | **[Kazakh Speech Dataset (optimized KSC2)](https://huggingface.co/datasets/Flamme-VRM/kazakh-speech-dataset)**<br><sub>Flamme-VRM</sub><br><sub>Open</sub> | ASR · TTS | VAD-sliced and Whisper-Turbo re-transcribed derivative of KSC2 with quality filtering. | 54.5 GB | ≈726 h; 230,793 clips |
| 10 | 2025-12 | **[Mozilla Common Voice Kazakh](https://datacollective.mozillafoundation.org/datasets/cmj8u3pbb00dhnxxbsqe4vbpc)**<br><sub>Mozilla Foundation</sub><br><sub>Open</sub> | ASR | Crowdsourced Kazakh voice recordings from the Common Voice Scripted Speech project. | Not reported | 2,750 clips; 3.76 h recorded (2.39 h validated); 193 speakers |
| 11 | 2025-04 | **[MATERIAL Kazakh–English Language Pack](https://catalog.ldc.upenn.edu/LDC2025S03)**<br><sub>Appen (for IARPA MATERIAL)</sub><br><sub>Paid</sub> | ST · RAG | Kazakh conversational telephone speech with English translations, transcripts, and query-relevance annotations, from Northern and Southern Kazakh dialect regions. | Not reported | ≈57 h |
| 12 | 2024-11 | **[Belebele-FLEURS](https://huggingface.co/datasets/WueNLP/belebele-fleurs)**<br><sub>WüNLP</sub><br><sub>Open</sub> | SQA · ASR | Spoken reading-comprehension benchmark combining Belebele and FLEURS audio/text across 99 languages. | 3.4 GB | 870 Kazakh test examples |
| 13 | 2024-04 | **[KazEmoTTS](https://huggingface.co/datasets/issai/KazEmoTTS)**<br><sub>[Abilbekov et al.](https://arxiv.org/abs/2404.01033)</sub><br><sub>Application</sub> | TTS · EPC | Kazakh emotional TTS corpus with six emotion classes (neutral, angry, happy, sad, scared, surprised) across male and female narrators. | 10.5 GB | 74.85 h; 54,760 clips |
| 14 | 2024-01 | **[ISSAI SKIMMED](https://huggingface.co/datasets/Dauren-Nur/ISSAI_SKIMMED)**<br><sub>Dauren-Nur</sub><br><sub>Open</sub> | ASR · TTS | Multimodal Kazakh audio-transcription dataset with train/test/dev splits. | 5.4 GB | 21,617 clips |
| 15 | 2023-07 | **[Kazakh Speech Dataset (KSD / SLR140)](https://openslr.org/140/)**<br><sub>[Mansurova & Kadyrbek](https://doi.org/10.3390/bdcc7030132)</sub><br><sub>Open</sub> | ASR | Open-source Kazakh speech corpus recorded on mobile devices across diverse regions, ages, and genders, verified by native speakers. | 56 GB | 554 h; 204,250 utterances |
| 16 | 2023-04 | **[Kazakh Speech Commands](https://huggingface.co/datasets/issai/kazakh-speech-commands)**<br><sub>[Kuzdeuov et al.](https://ieeexplore.ieee.org/document/10601292)</sub><br><sub>Open</sub> | KWS | Kazakh speech-command recognition dataset built via synthetic TTS generation and speech-corpus scraping, with data augmentation. | 267.3 MB | ≈1 h; 3,623 utterances |
| 17 | 2022-09 | **[Kazakh Speech Corpus 2 (KSC2)](https://huggingface.co/datasets/issai/Kazakh_Speech_Corpus_2)**<br><sub>[Mussakhojayeva et al.](https://www.isca-archive.org/interspeech_2022/mussakhojayeva22_interspeech.html)</sub><br><sub>Open</sub> | ASR | Industrial-scale open-source Kazakh speech corpus subsuming KSC and KazakhTTS2, with additional TV, radio, senate, and podcast data, including Kazakh-Russian code-switching. | 80.8 GB | ≈1,200 h; 600,000+ utterances |
| 18 | 2022-01 | **[KazakhTTS2](https://issai.nu.edu.kz/tts2-eng/)**<br><sub>[ISSAI researchers](https://arxiv.org/abs/2201.05771)</sub><br><sub>Open</sub> | TTS | Expanded five-speaker Kazakh TTS corpus, extending the original KazakhTTS with more data, speakers, and topics. | 35.7 GB | 271 h; 5 speakers |
| 19 | 2021-04 | **[KazakhTTS](https://huggingface.co/datasets/issai/KazakhTTS)**<br><sub>[Mussakhojayeva et al.](https://aclanthology.org/2022.lrec-1.578.pdf)</sub><br><sub>Open</sub> | TTS | Open-source Kazakh text-to-speech corpus, later expanded by KazakhTTS2. | 11.9 GB | ≈93 h; 42,000 utterances |
| 20 | 2020-09 | **[Kazakh Speech Corpus (KSC)](https://issai.nu.edu.kz/kz-speech-corpus/)**<br><sub>[ISSAI researchers](https://arxiv.org/abs/2009.10334)</sub><br><sub>Open</sub> | ASR | Crowdsourced Kazakh speech corpus with an initial ASR baseline. | Not reported | ≈332 h; 153,000 utterances |
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

| ID | Released | Dataset | Task | Description | Storage | Samples |
|---:|---|---|---|---|---|---|
| 1 | 2026-06 | **[Darmm Kazakh Cyrillic OCR](https://huggingface.co/datasets/Darmm/darmm-ocr-kazakh-cyrillic)**<br><sub>Rakhat Zhumabek</sub><br><sub>Open</sub> | OCR | Synthetic printed-text OCR dataset for Kazakh Cyrillic, rendered from Kazakh Wikipedia text with Kazakh-specific characters (Ә, Ғ, Қ, Ң, Ө, Ұ, Ү, Һ, І). | 2.3 GB | 200,000 images (100k word-level + 100k line-level) |
| 2 | 2026-06 | **[TurkicOCR-Cyrillic](https://huggingface.co/datasets/alenisaw/turkicocr-cyrillic)**<br><sub>Alen Issayev</sub><br><sub>Open</sub> | OCR · DU | Synthetic Turkic-Cyrillic OCR dataset spanning Kazakh, Kyrgyz, Kazakh-Russian, and Kyrgyz-Russian text and layouts. | 66.7 GB | 100,000 unique pages; 175,000 nested-config rows |
| 3 | 2026-04 | **[BeyneleBench](https://huggingface.co/datasets/issai/BeyneleBench)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | T2I | Kazakh/English benchmark for cultural fidelity in text-to-image generation, pairing prompts with reference images and cultural taxonomy levels. | 2.0 GB | 750 |
| 4 | 2026-04 | **[SpokenMQA Kazakh](https://huggingface.co/datasets/issai/SpokenMQA_Kazakh)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | AVQA | Machine-translated Kazakh adaptation of SpokenMQA for evaluating spoken mathematical reasoning in speech/audio-language models. | 1.4 GB | 2,256 |
| 5 | 2026-03 | **[MMBench Kazakh](https://huggingface.co/datasets/issai/MMBench_Kazakh)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | VQA | Kazakh translation of the MMBench validation split, evaluating perception, reasoning, and logic via multiple-choice VQA. | 772.2 MB | 4,329 |
| 6 | 2026-03 | **[MathVision Kazakh](https://huggingface.co/datasets/issai/MathVision_Kazakh)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | VMR | Machine-translated MathVision dataset for evaluating mathematical reasoning and visual understanding in multimodal LLMs. | 248.7 MB | 3,040 |
| 7 | 2025-12 | **[KazakhOCR](https://huggingface.co/datasets/henrygagnier/kazakh-ocr)**<br><sub>[Gagnier et al.](https://aclanthology.org/2026.abjadnlp-1.8/)</sub><br><sub>Open</sub> | OCR | Synthetic benchmark for evaluating multimodal models on Arabic-, Cyrillic-, and Latin-script Kazakh OCR. | 15.3 GB | 600 images |
| 8 | 2025-12 | **[AI2D Kazakh](https://huggingface.co/datasets/issai/AI2D_Kazakh)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | DQA | Kazakh translation of AI2D diagram-question-answering data. | 465.0 MB | 3,088 |
| 9 | 2025-12 | **[MathVista Kazakh](https://huggingface.co/datasets/issai/MathVista_Kazakh)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | VMR | Kazakh translation of MathVista for visual math reasoning. | 52.6 MB | 1,000 |
| 10 | 2025-12 | **[OCRBench Kazakh](https://huggingface.co/datasets/issai/OCRBench-Kazakh)**<br><sub>ISSAI researchers</sub><br><sub>Open</sub> | OCR · VQA | Kazakh OCR and visual-QA benchmark translated from OCRBench. | 28.7 MB | 441 |
| 11 | 2025-12 | **[QazLip](https://doi.org/10.7910/DVN/VIP1J8)**<br><sub>[Zhalgas, A. et al.](https://doi.org/10.1038/s41597-025-06193-0)</sub><br><sub>Open</sub> | VSR | Kazakh lip-movement command corpus of 102 nouns recorded from 26 participants at 1080p/60fps for visual speech recognition. | Not reported | ≈34,000 videos; 1.2M frames |
| 12 | 2021-10 | **[KOHTD](https://github.com/abdoelsayed2016/KOHTD)**<br><sub>[Toiganbayeva et al.](https://doi.org/10.1016/j.image.2022.116827)</sub><br><sub>Application</sub> | HTR | Kazakh Offline Handwritten Text Dataset of exam papers (99% Kazakh, 1% Russian). | 2.6 MB | 3,000 exam papers; 140,335+ segmented images; ≈922,010 symbols |
| 13 | 2020-07 | **[HKR](https://github.com/abdoelsayed2016/HKR_Dataset)**<br><sub>[Nurseitov et al.](https://doi.org/10.1007/s11042-021-11399-6)</sub><br><sub>Application</sub> | HTR | Handwritten Kazakh and Russian database (HKR), predominantly Russian (≈95%) with a Kazakh minority share (≈5%). | Not reported | 1,400+ forms; ≈63,000 sentences; ≈715,699 symbols (≈5% Kazakh) |
<!-- VISION_SECTION:END -->

## Watchlist / announced resources

Resources below are announced, described in a paper without a public artifact,
license-conflicted, or not yet independently verifiable as usable Kazakh-language
datasets. They are intentionally **not** part of the main catalog above. Where a
source is known, the entry links to it.

<!-- WATCHLIST:START -->
- **[Kazakh Text Corpus / Speech Corpus / AI Evaluation Benchmark Suite](https://turkystan.kz/article/282605-10-milliard-token-10-myn-sagat-audio-qazaq-tili-qogamy-men-openai-biregei-ai-infraqurylymyn-tanystyrdy)** — Announced in 2026 as more than 10B text tokens and over 10,000 speech hours (including 1,000 manually transcribed "gold standard" hours) and a nine-dimension AI evaluation benchmark suite, from a joint initiative between the Qazaq Tili Qogamy and OpenAI, but no public dataset download was identified.
- **[National Corpus of the Kazakh Language (QazCorpus)](https://qazcorpus.kz/indexen.php)** — Official searchable Kazakh corpus ecosystem with multiple subcorpora. The Main Corpus reports 31,105,900 word usages with morphological, semantic, lexical, phonetic, and phonological annotation. No independently verified bulk-download artifact and reusable dataset license could be confirmed, so it remains outside the main catalog.
<!-- WATCHLIST:END -->

## Abbreviations

<!-- ABBREVIATIONS:START -->
<table width="100%">
<tr><td align="center" valign="middle"><strong>AQA</strong> — Audio question answering</td><td align="center" valign="middle"><strong>ASR</strong> — Automatic speech recognition (ASR)</td><td align="center" valign="middle"><strong>AVQA</strong> — Audio-visual QA</td><td align="center" valign="middle"><strong>CQA</strong> — Cultural QA</td><td align="center" valign="middle"><strong>DQA</strong> — Diagram QA</td><td align="center" valign="middle"><strong>DU</strong> — Layout analysis / document understanding</td></tr>
<tr><td align="center" valign="middle"><strong>EPC</strong> — Emotion / paralinguistic classification</td><td align="center" valign="middle"><strong>HTR</strong> — Handwriting recognition</td><td align="center" valign="middle"><strong>IF</strong> — Instruction following</td><td align="center" valign="middle"><strong>IFT</strong> — Instruction tuning</td><td align="center" valign="middle"><strong>KWS</strong> — Keyword spotting</td><td align="center" valign="middle"><strong>LM</strong> — Language modelling / pretraining</td></tr>
<tr><td align="center" valign="middle"><strong>LQA</strong> — Legal QA</td><td align="center" valign="middle"><strong>MCQA</strong> — Multiple-choice QA</td><td align="center" valign="middle"><strong>MORPH</strong> — Morphological analysis</td><td align="center" valign="middle"><strong>MR</strong> — Math reasoning</td><td align="center" valign="middle"><strong>MT</strong> — Machine translation</td><td align="center" valign="middle"><strong>NER</strong> — Named entity recognition</td></tr>
<tr><td align="center" valign="middle"><strong>OCR</strong> — OCR</td><td align="center" valign="middle"><strong>POS</strong> — Dependency parsing / POS tagging</td><td align="center" valign="middle"><strong>QA</strong> — Question answering</td><td align="center" valign="middle"><strong>RAG</strong> — Retrieval / RAG</td><td align="center" valign="middle"><strong>Safety</strong> — Safety evaluation</td><td align="center" valign="middle"><strong>SC</strong> — Sentiment classification</td></tr>
<tr><td align="center" valign="middle"><strong>SQA</strong> — Spoken QA</td><td align="center" valign="middle"><strong>ST</strong> — Speech translation</td><td align="center" valign="middle"><strong>STS</strong> — Text deduplication / similarity</td><td align="center" valign="middle"><strong>SV</strong> — Speaker verification</td><td align="center" valign="middle"><strong>T2I</strong> — Cultural vision benchmark (text-to-image)</td><td align="center" valign="middle"><strong>TC</strong> — Text classification</td></tr>
<tr><td align="center" valign="middle"><strong>TS-ASR</strong> — Target-speaker ASR / speech separation</td><td align="center" valign="middle"><strong>TTS</strong> — Text-to-speech (TTS)</td><td align="center" valign="middle"><strong>VMR</strong> — Visual math reasoning</td><td align="center" valign="middle"><strong>VQA</strong> — Visual QA</td><td align="center" valign="middle"><strong>VSR</strong> — Visual speech recognition (lip reading)</td><td align="center" valign="middle"></td></tr>
</table>
<!-- ABBREVIATIONS:END -->

## Contributing

Missing a Kazakh dataset, or spotted outdated metadata? Contributions are welcome:

- **Add a dataset** — [open a submission issue](../../issues/new?template=dataset-submission.yml)
  or send a PR directly.
- **Fix or update an entry** — edit `data/datasets.yaml` and open a PR.
- **Report a stale number** — Hugging Face row counts and reported storage
  sizes may change over time; flag it with the current value from the
  [Dataset Server API](https://huggingface.co/docs/dataset-viewer/en/size).

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full inclusion criteria, required
metadata, and PR format.

## Contributors

<p align="center">
  <a href="https://github.com/Allessyer/awesome-kaz-datasets/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=Allessyer/awesome-kaz-datasets" alt="Contributors to awesome-kaz-datasets">
  </a>
</p>

## License

This catalog's own content — the repository structure, documentation, generated
tables, and scripts — is released under the [MIT License](LICENSE). Datasets
linked from this catalog remain under their own respective licenses (recorded
per entry above); this MIT license does not extend to their contents.
