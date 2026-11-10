#!/usr/bin/env python3
"""Compare a source and a target CSV dataset by key.

Reports: row counts, keys missing on either side, and per-column mismatches.
Exit code 0 = datasets match, 1 = differences found.

Usage:
    python validate_data.py sample_data/source.csv sample_data/target.csv --key id
"""
import argparse
import csv
import sys


def load(path, key):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if rows and key not in rows[0]:
        sys.exit(f"Key column '{key}' not found in {path}")
    return {r[key]: r for r in rows}, len(rows)


def compare(source, target, ignore=()):
    missing_in_target = sorted(set(source) - set(target))
    missing_in_source = sorted(set(target) - set(source))
    mismatches = []
    for k in sorted(set(source) & set(target)):
        for col, sval in source[k].items():
            if col in ignore:
                continue
            tval = target[k].get(col)
            if (sval or "").strip() != (tval or "").strip():
                mismatches.append((k, col, sval, tval))
    return missing_in_target, missing_in_source, mismatches


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    p.add_argument("source")
    p.add_argument("target")
    p.add_argument("--key", default="id", help="unique key column (default: id)")
    p.add_argument("--ignore", nargs="*", default=[], help="columns to ignore")
    a = p.parse_args()

    src, n_src = load(a.source, a.key)
    tgt, n_tgt = load(a.target, a.key)
    miss_t, miss_s, mism = compare(src, tgt, set(a.ignore))

    print(f"Rows  source={n_src}  target={n_tgt}")
    print(f"Keys missing in target: {len(miss_t)} {miss_t[:10]}")
    print(f"Keys missing in source: {len(miss_s)} {miss_s[:10]}")
    print(f"Field mismatches: {len(mism)}")
    for k, col, s, t in mism[:20]:
        print(f"  key={k} column={col} source={s!r} target={t!r}")

    ok = not (miss_t or miss_s or mism) and n_src == n_tgt
    print("RESULT:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
