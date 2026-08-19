#!/usr/bin/env python3
"""Validate data/datasets.yaml structure and taxonomy. Does not check scientific accuracy."""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "datasets.yaml"

SECTIONS = {"Text, NLP, and LLM", "Speech and audio", "Vision, OCR, and multimodal"}
ACCESS_VALUES = {"open", "gated", "application", "paid", "restricted", "unavailable"}
KIND_VALUES = {"original", "benchmark", "translation", "derivative", "multilingual", "mirror"}
ORIGIN_VALUES = {
    "native", "human-annotated", "human-translated", "machine-translated",
    "synthetic", "web-crawl", "mixed",
}
REQUIRED_FIELDS = ["id", "name", "released", "section", "tasks", "access", "license", "kind", "origin", "links"]
DATE_RE = re.compile(r"^\d{4}(-\d{2})?$")
URL_RE = re.compile(r"^https?://\S+$")


def fail(errors, msg):
    errors.append(msg)


def main():
    errors = []
    if not CATALOG.exists():
        print(f"FATAL: {CATALOG} not found", file=sys.stderr)
        return 1

    doc = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    datasets = doc.get("datasets", [])
    if not datasets:
        fail(errors, "datasets.yaml has no datasets")

    ids_seen = {}
    urls_seen = {}

    for i, d in enumerate(datasets):
        where = f"[{i}] {d.get('id', '<no id>')}"

        for field in REQUIRED_FIELDS:
            if field not in d or d[field] in (None, ""):
                fail(errors, f"{where}: missing required field '{field}'")

        did = d.get("id")
        if did:
            if not re.match(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$", did):
                fail(errors, f"{where}: id '{did}' is not kebab-case")
            if did in ids_seen:
                fail(errors, f"{where}: duplicate id '{did}' (also at index {ids_seen[did]})")
            ids_seen[did] = i

        section = d.get("section")
        if section and section not in SECTIONS:
            fail(errors, f"{where}: invalid section '{section}'")

        released = d.get("released")
        if released and released != "Not reported" and not DATE_RE.match(str(released)):
            fail(errors, f"{where}: released '{released}' is not YYYY or YYYY-MM")

        access = d.get("access")
        if access and access not in ACCESS_VALUES:
            fail(errors, f"{where}: invalid access '{access}'")

        kind = d.get("kind")
        if kind and kind not in KIND_VALUES:
            fail(errors, f"{where}: invalid kind '{kind}'")

        origin = d.get("origin") or []
        for o in origin:
            if o not in ORIGIN_VALUES:
                fail(errors, f"{where}: invalid origin value '{o}'")

        if kind == "derivative" and not d.get("derivative_of"):
            fail(errors, f"{where}: kind=derivative but derivative_of is not set")

        links = d.get("links") or {}
        dataset_url = links.get("dataset")
        if not dataset_url:
            fail(errors, f"{where}: links.dataset is required")
        else:
            if not URL_RE.match(dataset_url):
                fail(errors, f"{where}: links.dataset '{dataset_url}' is not a valid URL")
            if dataset_url in urls_seen:
                fail(errors, f"{where}: duplicate links.dataset URL, also used by '{urls_seen[dataset_url]}'")
            else:
                urls_seen[dataset_url] = did
        for key, val in links.items():
            if val and not URL_RE.match(val):
                fail(errors, f"{where}: links.{key} '{val}' is not a valid URL")

        scale = d.get("scale") or {}
        if "value" not in scale:
            fail(errors, f"{where}: scale.value is missing (use null if not reported)")

        storage = d.get("storage") or {}
        if "value" not in storage:
            fail(errors, f"{where}: storage.value is missing (use null if not reported)")

    for did, idx in ids_seen.items():
        d = datasets[idx]
        dep = d.get("derivative_of")
        if dep and dep not in ids_seen:
            fail(errors, f"[{idx}] {did}: derivative_of '{dep}' does not match any known dataset id")

    if errors:
        print(f"FAILED: {len(errors)} error(s)\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {len(datasets)} datasets validated, no errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
