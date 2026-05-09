#!/usr/bin/env python3
"""
sync-posts.py — Pull LinkedIn post history from a Google Sheet into the repo.

Google Sheet format (one row per post):
  Column A: Date         (YYYY-MM-DD or MM/DD/YYYY)
  Column B: Post text    (full content)
  Column C: Funnel stage (top / mid / bottom) — optional
  Column D: Notes        — optional (e.g. "high engagement", "viral")

One-time setup:
  1. pip install gspread google-auth
  2. Google Cloud → enable Sheets API → create Service Account → download credentials.json
  3. Put credentials.json in scripts/credentials.json
  4. Share your Google Sheet with the service account email (view-only is fine)

Usage:
  python3 scripts/sync-posts.py --client acme-corp --sheet-id YOUR_SHEET_ID

The sheet ID is in the URL:
  https://docs.google.com/spreadsheets/d/THIS_IS_THE_ID/edit
"""

import argparse
import os
import re
import sys


def slugify(text, max_len=50):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:max_len].rstrip("-")


def first_line(post_text):
    for line in post_text.strip().split("\n"):
        line = line.strip()
        if line:
            return line
    return "post"


def normalize_date(raw):
    raw = raw.strip().replace("/", "-")
    if len(raw) == 8 and "-" not in raw:
        return f"{raw[:4]}-{raw[4:6]}-{raw[6:]}"
    return raw


def sync(client, sheet_id, credentials_file):
    try:
        import gspread
        from google.oauth2.service_account import Credentials
    except ImportError:
        sys.exit("Missing deps. Run: pip install gspread google-auth")

    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    creds = Credentials.from_service_account_file(credentials_file, scopes=scopes)
    gc = gspread.authorize(creds)

    rows = gc.open_by_key(sheet_id).sheet1.get_all_values()
    if not rows:
        sys.exit("Sheet is empty.")

    # Skip header if present
    start = 1 if rows[0][0].lower() in ("date", "published", "post date") else 0

    out_dir = os.path.join("clients", client, "posts", "published")
    os.makedirs(out_dir, exist_ok=True)
    existing = set(os.listdir(out_dir))

    added = skipped = 0
    for row in rows[start:]:
        if len(row) < 2:
            continue
        date = normalize_date(row[0])
        text = row[1].strip()
        funnel = row[2].strip() if len(row) > 2 else ""
        notes = row[3].strip() if len(row) > 3 else ""

        if not date or not text:
            continue

        filename = f"{date}-{slugify(first_line(text))}.md"
        if filename in existing:
            skipped += 1
            continue

        fm = f"---\nclient: {client}\ndate: {date}\n"
        if funnel:
            fm += f"funnel: {funnel}\n"
        if notes:
            fm += f"notes: {notes}\n"
        fm += "status: published\n---\n\n"

        with open(os.path.join(out_dir, filename), "w") as f:
            f.write(fm + text)

        print(f"  + {filename}")
        added += 1

    print(f"\nDone. {added} added, {skipped} already existed.")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--client", required=True)
    p.add_argument("--sheet-id", required=True)
    p.add_argument("--credentials", default="scripts/credentials.json")
    args = p.parse_args()
    print(f"Syncing: {args.client}")
    sync(args.client, args.sheet_id, args.credentials)
