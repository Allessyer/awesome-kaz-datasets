#!/usr/bin/env python3
"""Best-effort link checker for data/datasets.yaml.

Not part of the required PR-blocking CI job (external hosts are too flaky for
that — gating, rate limiting, HEAD-request rejection, geo-blocking). Intended to
be run manually or on a nightly schedule; always exits 0 unless the catalog
itself fails to parse, so it never blocks a PR by itself.
"""

import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "datasets.yaml"

TIMEOUT = 10
UA = "Mozilla/5.0 (compatible; awesome-kaz-datasets-link-check/1.0)"

# Hosts known to reject HEAD requests or bots; fall back to GET, or skip politely.
GET_ONLY_HOSTS = ("huggingface.co", "arxiv.org", "doi.org", "aclanthology.org")


def check(url):
    req_method = "GET" if any(h in url for h in GET_ONLY_HOSTS) else "HEAD"
    req = urllib.request.Request(url, method=req_method, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, None
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:  # noqa: BLE001 - link checking must never crash the run
        return None, str(e)


def main():
    if not DATA.exists():
        print(f"FATAL: {DATA} not found", file=sys.stderr)
        return 1

    doc = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    datasets = doc.get("datasets", [])

    urls = {}
    for d in datasets:
        for key, url in (d.get("links") or {}).items():
            if url:
                urls.setdefault(url, []).append(f"{d['id']}.links.{key}")

    print(f"Checking {len(urls)} unique URLs across {len(datasets)} datasets...\n")
    ok, warn, fail = 0, 0, 0
    for url, refs in sorted(urls.items()):
        status, error = check(url)
        if error:
            print(f"  ? {url}  ({error})  [{', '.join(refs)}]")
            warn += 1
        elif status and status < 400:
            ok += 1
        elif status in (401, 403, 429):
            print(f"  ~ {url}  (HTTP {status} — likely gating/rate-limit, not necessarily broken)  [{', '.join(refs)}]")
            warn += 1
        else:
            print(f"  x {url}  (HTTP {status})  [{', '.join(refs)}]")
            fail += 1

    print(f"\n{ok} ok, {warn} inconclusive, {fail} likely broken.")
    return 0  # informational only — never fails CI


if __name__ == "__main__":
    raise SystemExit(main())
