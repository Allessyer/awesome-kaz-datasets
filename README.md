# Awesome Kazakh Datasets

A curated list of public datasets that contain substantial Kazakh-language data. Links in **Description** lead to a paper, project page, or dataset card; links in **Download** lead directly to the data repository or archive.

Counts are the number of rows/examples unless another unit is shown. For multilingual datasets, a count marked **total** includes non-Kazakh examples. Counts may change when a living dataset is updated; **≈** denotes a figure reported or estimated by its publisher.

## Text, NLP, and LLM

| Released | Dataset | Description | Download | Size | Task |
|---|---|---|---|---:|---|
| 2026 | KazMix-3 | [Kazakh instruction mixture (dataset card)](https://huggingface.co/datasets/issai/KazMix-3) | [Files](https://huggingface.co/datasets/issai/KazMix-3/tree/main) | 89,775 | Instruction tuning |
| 2026 | RAGBench Kazakh | [Kazakh translation of RAGBench (dataset card)](https://huggingface.co/datasets/issai/RAGBench_Kazakh) | [Files](https://huggingface.co/datasets/issai/RAGBench_Kazakh/tree/main) | 11,431 | RAG evaluation |
| 2026 | IFBench Kazakh | [Kazakh instruction-following benchmark (dataset card)](https://huggingface.co/datasets/issai/IFBench_Kazakh) | [Files](https://huggingface.co/datasets/issai/IFBench_Kazakh/tree/main) | 444 | Instruction following |
| 2026 | FreshQA Kazakh | [Kazakh FreshQA adaptation (dataset card)](https://huggingface.co/datasets/issai/freshqa_kazakh) | [Files](https://huggingface.co/datasets/issai/freshqa_kazakh/tree/main) | 600 | Current-knowledge QA |
| 2026 | DeFAn Kazakh | [Kazakh/English decomposition data (dataset card)](https://huggingface.co/datasets/issai/defan_kazakh) | [Files](https://huggingface.co/datasets/issai/defan_kazakh/tree/main) | 3,178 total | QA / decomposition |
| 2025 | KazCulture | [Human-written Kazakh cultural PQA dataset (dataset card)](https://huggingface.co/datasets/issai/KazCulture) | [Files](https://huggingface.co/datasets/issai/KazCulture/tree/main) | 16,137 PQA triplets | Cultural QA |
| 2025 | KazMMLU | [Kazakh/Russian regional-knowledge benchmark (paper)](https://arxiv.org/abs/2502.12829) | [Hugging Face](https://huggingface.co/datasets/MBZUAI/KazMMLU) | 23,000 total; 10,969 Kazakh | Multiple-choice QA |
| 2025 | Qorgau | [Kazakh/Russian LLM-safety benchmark (paper)](https://arxiv.org/abs/2502.13640) | [GitHub](https://github.com/mbzuai-nlp/qorgau-kaz-ru-safety) | 2,790 prompts | Safety evaluation |
| 2025 | Zerde-QA-50K | [Synthetic Kazakh QA collection (dataset card)](https://huggingface.co/datasets/kurumikz/Zerde-QA-50K) | [Files](https://huggingface.co/datasets/kurumikz/Zerde-QA-50K/tree/main) | 51,422 pairs | QA / instruction tuning |
| 2024 | Kazakh Dastur MC | [Dataset card](https://huggingface.co/datasets/kz-transformers/kazakh-dastur-mc) | [Files](https://huggingface.co/datasets/kz-transformers/kazakh-dastur-mc/tree/main) | 1,005 | Multiple-choice QA |
| 2024 | Kazakh Constitution MC | [Dataset card](https://huggingface.co/datasets/kz-transformers/kazakh-constitution-mc) | [Files](https://huggingface.co/datasets/kz-transformers/kazakh-constitution-mc/tree/main) | 414 | Multiple-choice QA |
| 2024 | Kazakh UNT | [Dataset card](https://huggingface.co/datasets/kz-transformers/kazakh-unified-national-testing-mc) | [Files](https://huggingface.co/datasets/kz-transformers/kazakh-unified-national-testing-mc/tree/main) | 14,850 | Multiple-choice QA |
| 2024 | MMLU Translated KK | [Dataset card](https://huggingface.co/datasets/kz-transformers/mmlu-translated-kk) | [Files](https://huggingface.co/datasets/kz-transformers/mmlu-translated-kk/tree/main) | 15,854 | Multiple-choice QA |
| 2024 | GSM8K Translated KK | [Dataset card](https://huggingface.co/datasets/kz-transformers/gsm8k-kk-translated) | [Files](https://huggingface.co/datasets/kz-transformers/gsm8k-kk-translated/tree/main) | 8,792 | Math reasoning |
| 2024 | KazQAD | [Open-domain Kazakh QA (paper)](https://arxiv.org/abs/2404.04487) | [Hugging Face](https://huggingface.co/datasets/issai/kazqad) | 6,000 questions; 12,700 passages | Open-domain QA |
| 2024 | KazParC | [Kazakh parallel corpus (paper)](https://arxiv.org/abs/2403.19399) | [Hugging Face](https://huggingface.co/datasets/issai/kazparc) · [GitHub](https://github.com/IS2AI/KazParC) | 372,000 sentence pairs | Machine translation |
| 2024 | Kazakh–Russian KAZNU | [Dataset card](https://huggingface.co/datasets/Dauren-Nur/kaz_rus_parallel_corpora_KAZNU) | [Files](https://huggingface.co/datasets/Dauren-Nur/kaz_rus_parallel_corpora_KAZNU/tree/main) | 86,453 pairs | Machine translation |
| 2024 | Kazakh–English KAZNU | [Dataset card](https://huggingface.co/datasets/Dauren-Nur/kaz_eng_parallel) | [Files](https://huggingface.co/datasets/Dauren-Nur/kaz_eng_parallel/tree/main) | 377,044 pairs | Machine translation |
| 2023 | MDBKD | [Multi-domain bilingual Kazakh dataset (dataset card)](https://huggingface.co/datasets/kz-transformers/multidomain-kazakh-dataset) | [Files](https://huggingface.co/datasets/kz-transformers/multidomain-kazakh-dataset/tree/main) | 24,883,808 texts | Language modelling |
| 2021 | KazNERD | [Kazakh named-entity corpus (paper)](https://arxiv.org/abs/2111.13419) | [Hugging Face](https://huggingface.co/datasets/issai/kaznerd) · [GitHub](https://github.com/IS2AI/KazNERD) | 112,702 sentences; 136,333 entity annotations | NER |
| 2021 | KazNewsDataset | [Kazakh news corpus (paper)](https://doi.org/10.3390/data6030031) | [Mendeley Data](https://data.mendeley.com/datasets/hwj24p9gkh/1) | 4,365 articles | Topic modelling |
| 2021 | KazRusNewsDataset | [Kazakh/Russian news corpus (paper)](https://doi.org/10.3390/data6030031) | [Mendeley Data](https://data.mendeley.com/datasets/2vz7vtbhn2/1) | 20,409 articles | Text classification |

## Speech and audio

| Released | Dataset | Description | Download | Size | Task |
|---|---|---|---|---:|---|
| 2026 | Kazakh Speech Dataset (optimized KSC2) | [VAD-sliced and re-transcribed KSC2 derivative (dataset card)](https://huggingface.co/datasets/Flamme-VRM/kazakh-speech-dataset) | [Files](https://huggingface.co/datasets/Flamme-VRM/kazakh-speech-dataset/tree/main) | ≈726 h; 230,793 clips | ASR / TTS |
| 2025 | Kazakh Speech Corpus 2 (KSC2) | [Large transcribed Kazakh corpus (dataset card)](https://huggingface.co/datasets/issai/Kazakh_Speech_Corpus_2) | [Files](https://huggingface.co/datasets/issai/Kazakh_Speech_Corpus_2/tree/main) | ≈1,200 h; 600,000+ utterances | ASR |
| 2024 | Belebele-FLEURS | [Spoken reading-comprehension benchmark (paper)](https://arxiv.org/abs/2412.08274) | [Hugging Face](https://huggingface.co/datasets/WueNLP/belebele-fleurs) | 900 Kazakh audio questions | Spoken QA / ASR |
| 2024 | KazEmoTTS | [Kazakh emotional TTS corpus (paper)](https://arxiv.org/abs/2404.01033) | [Hugging Face](https://huggingface.co/datasets/issai/KazEmoTTS) · [GitHub](https://github.com/IS2AI/KazEmoTTS) | 74.85 h; 54,760 clips | Emotional TTS |
| 2024 | ISSAI SKIMMED | [Dataset card](https://huggingface.co/datasets/Dauren-Nur/ISSAI_SKIMMED) | [Files](https://huggingface.co/datasets/Dauren-Nur/ISSAI_SKIMMED/tree/main) | 21,617 clips | ASR / TTS |
| 2023 | Kazakh Speech Dataset (KSD / SLR140) | [Corpus and paper citation (OpenSLR)](https://openslr.org/140/) | [OpenSLR files](https://openslr.org/140/) · [Hugging Face](https://huggingface.co/datasets/farabi-lab/kazakh-stt) | 554 h; 204,250 utterances | ASR |
| 2022 | Kazakh Speech Commands | [Project and paper links (GitHub)](https://github.com/IS2AI/Kazakh-Speech-Commands-Dataset) | [Hugging Face](https://huggingface.co/datasets/issai/kazakh-speech-commands) | ≈1 h; 3,623 utterances | Keyword spotting |
| 2021 | KazakhTTS | [Kazakh text-to-speech corpus (paper)](https://arxiv.org/abs/2104.08459) | [Hugging Face](https://huggingface.co/datasets/issai/KazakhTTS) | ≈93 h; 42,000 utterances | TTS |
| 2020 | Kazakh Speech Corpus (KSC) | [Crowdsourced Kazakh speech corpus (paper)](https://arxiv.org/abs/2009.10334) | [ISSAI download page](https://issai.nu.edu.kz/kz-speech-corpus/) | ≈332 h; 153,000 utterances | ASR |

## Vision, OCR, and multimodal

| Released | Dataset | Description | Download | Size | Task |
|---|---|---|---|---:|---|
| 2026 | BeyneleBench | [Kazakh/English cultural vision benchmark (dataset card)](https://huggingface.co/datasets/issai/BeyneleBench) | [Files](https://huggingface.co/datasets/issai/BeyneleBench/tree/main) | 750 | Visual QA |
| 2026 | SpokenMQA Kazakh | [Spoken multimodal QA (dataset card)](https://huggingface.co/datasets/issai/SpokenMQA_Kazakh) | [Files](https://huggingface.co/datasets/issai/SpokenMQA_Kazakh/tree/main) | 2,256 | Audio-visual QA |
| 2026 | MMBench Kazakh | [Kazakh MMBench translation (dataset card)](https://huggingface.co/datasets/issai/MMBench_Kazakh) | [Files](https://huggingface.co/datasets/issai/MMBench_Kazakh/tree/main) | 4,329 | Visual QA |
| 2026 | MathVision Kazakh | [Kazakh MathVision translation (dataset card)](https://huggingface.co/datasets/issai/MathVision_Kazakh) | [Files](https://huggingface.co/datasets/issai/MathVision_Kazakh/tree/main) | 3,040 | Visual math reasoning |
| 2025 | AI2D Kazakh | [Kazakh diagram-QA translation (dataset card)](https://huggingface.co/datasets/issai/AI2D_Kazakh) | [Files](https://huggingface.co/datasets/issai/AI2D_Kazakh/tree/main) | 3,088 | Diagram QA |
| 2025 | MathVista Kazakh | [Kazakh MathVista translation (dataset card)](https://huggingface.co/datasets/issai/MathVista_Kazakh) | [Files](https://huggingface.co/datasets/issai/MathVista_Kazakh/tree/main) | 1,000 | Visual math reasoning |
| 2025 | OCRBench Kazakh | [Kazakh OCR benchmark (dataset card)](https://huggingface.co/datasets/issai/OCRBench-Kazakh) | [Files](https://huggingface.co/datasets/issai/OCRBench-Kazakh/tree/main) | 441 | OCR / visual QA |

## Inclusion and maintenance

This list favors documented, reusable releases with accessible data and a stated size. It excludes model repositories, duplicate mirrors, private/gated uploads whose contents cannot be checked, and tiny personal test files. Multilingual resources are included when they expose an identifiable Kazakh split or are explicitly designed for Kazakh evaluation.

To suggest a dataset, open an issue or pull request with: (1) a description source, (2) a direct download link, (3) a sample count or speech duration, (4) release year, task, and license. Please report changing Hugging Face row counts from the dataset viewer or the [Dataset Server API](https://huggingface.co/docs/dataset-viewer/en/size).

### Abbreviations

- ASR — automatic speech recognition
- IFT — instruction fine-tuning
- NER — named-entity recognition
- PQA — passage–question–answer
- QA — question answering
- RAG — retrieval-augmented generation
- TTS — text to speech
