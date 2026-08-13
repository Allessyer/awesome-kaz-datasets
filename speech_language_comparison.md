# English–Russian–Kazakh speech-data audit

This audit supports the comparison plot in the README. Values are conservative, deduplicated **lower bounds** for identifiable public or research-accessible releases, checked in August 2026. They are not a claim about every corpus in existence.

## Rules

- Count a release only when a publisher states a duration for the relevant language and task.
- Do not add a subset, mirror, optimized copy, or earlier release when its parent/superseding corpus is counted.
- A corpus may appear in two task totals only when its documentation explicitly supports both tasks; task totals must never be added together.
- Automatically transcribed and licensed/gated corpora are allowed but identified by the source notes.
- For speaker verification only, follow the broader **speaker-presence** rule: count the full duration of a corpus when the publisher confirms that it contains speakers of the language. Because multilingual hours are not partitioned by language, these are corpus-hours containing the language, not monolingual speech hours. The same multilingual corpus can therefore contribute to more than one language bar.

## Deduplicated totals

| Task | English | Russian | Kazakh | Interpretation |
|---|---:|---:|---:|---|
| ASR | ≥60,670 h | ≥21,530.23 h | ≥2,358.5 h | Transcribed speech suitable for ASR |
| TTS / TTS-grade | ≥36,700 h | ≥6,083 h | ≥945.85 h | Publisher-designated TTS or TTS-grade speech |
| Speech translation | ≥10,508 h | ≥38.7 h | ≥57 h | Source speech paired with translated text or speech |
| Speech emotion | ≥421 h | ≥350 h | ≥74.85 h | Audio carrying emotion annotations |
| Keyword spotting | ≥1,986.4 h | ≥137 h | ≥1 h | Isolated words or command utterances |
| Speaker verification | ≥18,826.86 corpus-h | ≥22,052 corpus-h | ≥600 h | Corpora with confirmed speakers of the language; multilingual totals can repeat across languages |
| Spoken QA | 900 samples | 900 samples | 3,156 samples | Kept separate because published hours are unavailable |

## Included releases

| Task | Language | Dataset | Counted | Why included | Source |
|---|---|---|---:|---|---|
| ASR | English | The People's Speech | 51,890 h | Final paper reports the English portion | [Paper](https://arxiv.org/abs/2111.09344) |
| ASR | English | SPGISpeech 1.0 + 2.0 | 8,780 h | 5,000 h plus 3,780 additional financial speech | [1.0](https://research.nvidia.com/publication/2021-04_spgispeech-5000-hours-transcribed-financial-audio-fully-formatted-end-end) · [2.0](https://arxiv.org/abs/2508.05554) |
| ASR | Russian | Open STT | 20,000 h | Publisher total; mixed annotation quality | [Microsoft documentation](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-open-speech-text) |
| ASR | Russian | Golos | 1,240 h | Independently collected Russian ASR corpus | [OpenSLR](https://openslr.org/114/) |
| ASR | Russian | Common Voice 24 | 290.23 h | Recorded duration, not only validated duration | [Datasheet](https://dev.mozilladatacollective.com/datasets/cmj8l8ct700o5nlovbdnv58yr) |
| ASR | Kazakh | KSC2 | 1,200 h | Supersedes/incorporates KSC and KazakhTTS2 for this total | [Dataset](https://huggingface.co/datasets/issai/Kazakh_Speech_Corpus_2) |
| ASR | Kazakh | KSD / SLR140 | 554 h | Separate Farabi/OpenSLR corpus | [OpenSLR](https://openslr.org/140/) |
| ASR | Kazakh | YO-CPT-kk | 600 h | Ensemble-verified transcripts; publisher explicitly supports ASR | [Dataset](https://huggingface.co/datasets/NCSpeech/YO-CPT-kk) |
| ASR | Kazakh | Kazakh Songs ASR | 4.5 h | Separate singing-speech corpus | [Paper](https://arxiv.org/abs/2603.00961) |
| TTS | English | HiFiTTS-2 | 36,700 h | 22.05-kHz TTS training release | [Paper](https://arxiv.org/abs/2506.04152) |
| TTS | Russian | YO-CPT-ru | 6,052 h | TTS-grade, force-aligned release | [Dataset](https://huggingface.co/datasets/NCSpeech/YO-CPT-ru) |
| TTS | Russian | RUSLAN | 31 h | Independent single-speaker TTS corpus | [Project](https://ruslan-corpus.github.io/) |
| TTS | Kazakh | YO-CPT-kk | 600 h | TTS-grade continual-pretraining corpus | [Dataset](https://huggingface.co/datasets/NCSpeech/YO-CPT-kk) |
| TTS | Kazakh | KazakhTTS2 | 271 h | Supersedes KazakhTTS in the TTS total | [Paper](https://arxiv.org/abs/2201.05771) |
| TTS | Kazakh | KazEmoTTS | 74.85 h | Separate emotional TTS material | [Paper](https://arxiv.org/abs/2404.01033) |
| Speech translation | English | GigaST | 10,000 h | Pseudo translations aligned to GigaSpeech audio | [Paper](https://arxiv.org/abs/2204.03939) |
| Speech translation | English | PhoST | 508 h | English speech with Vietnamese translations | [Dataset](https://huggingface.co/datasets/vinai/PhoST) |
| Speech translation | Russian | CoVoST 2 / CVSS source split | 38.7 h | Published Russian source-speech duration | [Google table](https://research.google/blog/introducing-cvss-a-massively-multilingual-speech-to-speech-translation-corpus/) |
| Speech translation | Kazakh | MATERIAL Kazakh–English | 57 h | Publisher-documented language pack | [LDC](https://catalog.ldc.upenn.edu/LDC2025S03) |
| Emotion | English | MSP-Podcast 2.0 | 400 h | Current emotion-annotated corpus total | [Paper](https://arxiv.org/abs/2509.09791) |
| Emotion | English | IEMOCAP | 12 h | Independent acted/dyadic corpus | [Review table](https://www.mdpi.com/2076-3417/15/10/5731) |
| Emotion | English | MSP-IMPROV | 9 h | Independent improvised corpus | [Review table](https://www.mdpi.com/2076-3417/15/10/5731) |
| Emotion | Russian | Dusha | 350 h | Russian emotion corpus | [Paper](https://arxiv.org/abs/2212.12266) |
| Emotion | Kazakh | KazEmoTTS | 74.85 h | Emotional labels and TTS recordings | [Paper](https://arxiv.org/abs/2404.01033) |
| Keyword spotting | English | MLCommons Spoken Words | 1,957 h | Published English language split | [Dataset card](https://huggingface.co/datasets/MLCommons/ml_spoken_words) |
| Keyword spotting | English | Speech Commands v2 | 29.4 h | 105,829 one-second files | [Dataset card](https://huggingface.co/datasets/google/speech_commands) |
| Keyword spotting | Russian | MLCommons Spoken Words | 137 h | Published Russian language split | [Dataset card](https://huggingface.co/datasets/MLCommons/ml_spoken_words) |
| Keyword spotting | Kazakh | Kazakh Speech Commands | ≈1 h | Publisher-reported duration | [Dataset](https://huggingface.co/datasets/issai/kazakh-speech-commands) |
| Speaker verification | Russian | YO-CPT-ru | 6,052 h | Cross-video and within-video speaker identities | [Dataset](https://huggingface.co/datasets/NCSpeech/YO-CPT-ru) |
| Speaker verification | Russian | VoxBlink2 | 16,000 corpus-h | Multilingual speaker-recognition corpus identifies 3,961 Russian-tagged speakers; total hours are not language-partitioned | [Project](https://voxblink2.github.io/) |
| Speaker verification | Kazakh | YO-CPT-kk | 600 h | Publisher explicitly lists speaker verification | [Dataset](https://huggingface.co/datasets/NCSpeech/YO-CPT-kk) |
| Speaker verification | English | VoxBlink2 | 16,000 corpus-h | Multilingual speaker-recognition corpus identifies 40,000+ English-tagged speakers; total hours are not language-partitioned | [Project](https://voxblink2.github.io/) |
| Speaker verification | English | VoxCeleb1 + VoxCeleb2 | 2,794 h | Mostly-English speaker-recognition corpora: 352 h + 2,442 h | [Corpus paper](https://www.robots.ox.ac.uk/~vgg/publications/2019/Nagrani19/nagrani19.pdf) |
| Speaker verification | English | VoxPrivacy | 32.86 corpus-h | Bilingual English/Chinese release with 200 English speakers; only combined duration is published | [Project](https://interactionalprivacy.github.io/) |
| Spoken QA | English | Belebele-FLEURS | 900 samples | Language split; duration not published | [Dataset](https://huggingface.co/datasets/WueNLP/belebele-fleurs) |
| Spoken QA | Russian | Belebele-FLEURS | 900 samples | Language split; duration not published | [Dataset](https://huggingface.co/datasets/WueNLP/belebele-fleurs) |
| Spoken QA | Kazakh | Belebele-FLEURS + SpokenMQA | 3,156 samples | 900 + 2,256; distinct benchmark releases | [Belebele-FLEURS](https://huggingface.co/datasets/WueNLP/belebele-fleurs) · [SpokenMQA](https://huggingface.co/datasets/issai/SpokenMQA_Kazakh) |

## Material exclusions and uncertainty

| Dataset | Decision | Reason |
|---|---|---|
| GigaSpeech, LibriSpeech, MLS English | Excluded from English ASR sum | Likely source overlap with the broad People's Speech aggregation cannot be resolved at recording level |
| YO-CPT-ru from Russian ASR | Excluded | Explicitly ASR-capable, but its YouTube provenance may overlap Open STT; retained under TTS and speaker verification |
| Kazakh Speech Corpus and KazakhTTS2 from Kazakh ASR | Excluded | KSC2 incorporates these sources |
| Optimized KSC2 | Excluded everywhere | Derivative of KSC2 |
| KazakhTTS | Excluded from TTS | KazakhTTS2 is its expanded successor |
| HiFiTTS, LibriTTS and other LibriVox TTS corpora | Excluded from English TTS sum | HiFiTTS-2 is much larger and audiobook-level overlap cannot be ruled out |
| SOVA 28,853 h | Excluded | Publisher gives only a combined Russian-and-English total, not language-specific hours |
| LEMAS 150,000 h | Excluded | No defensible English/Russian per-language hours in the release summary |
| VoxBlink 1 | Excluded | Earlier/smaller release in the VoxBlink family; VoxBlink2 is counted |
| SITW | Excluded | The VoxCeleb paper documents possible overlap with VoxCeleb1; duration would risk double counting |
| KazEGA, ISSAI SKIMMED, Common Voice Kazakh v25 | Excluded from hour totals | Cards provide counts/storage but no verified duration used in this audit |
| MSP-Conversation | Excluded | Explicitly overlaps MSP-Podcast |
| CREMA-D and other emotion datasets | Excluded | Public source gives clip counts but no sufficiently precise duration for this hours-only comparison |

The largest uncertainty is not arithmetic but coverage: “public” varies from unrestricted download to gated research access, and detecting overlap between web-mined corpora requires file- or source-ID-level comparison that publishers generally do not expose. In particular, VoxBlink2 and VoxCeleb are independently released YouTube-derived collections but may share identities or source videos; their union cannot be perfectly deduplicated from public metadata. Speaker-verification bars therefore use the requested broad coverage rule and should not be compared as monolingual-hour estimates.
