#!/usr/bin/env python3
"""Validate the public, link-only Buffett Brain research atlas."""
import json
from pathlib import Path
from urllib.parse import urlsplit

FILE=Path(__file__).resolve().parents[1]/"knowledge"/"atlas.json"
ALLOWED={
    "www.berkshirehathaway.com","berkshirehathaway.com",
    "www.sec.gov","buffett.cnbc.com","jasonzweig.com","press.stripe.com",
    "www.penguinrandomhouse.com","scholarship.law.gwu.edu"
}
KINDS={"decision","mistake","principle","book","interview"}
REQUIRED={"id","kind","year","title","summary","evidence","interpretation","limitations",
          "sourceIds","topics","companies","locator","verification","rights"}
def check(atlas):
    errors=[]
    if atlas.get("schemaVersion")!="buffett-brain-atlas-v1":errors.append("invalid schemaVersion")
    source_ids=set()
    for source in atlas.get("sources",[]):
        sid=source.get("id")
        if not sid or sid in source_ids:errors.append(f"duplicate/missing source id {sid}")
        source_ids.add(sid)
        url=source.get("url","")
        parsed=urlsplit(url)
        if parsed.scheme!="https" or parsed.hostname not in ALLOWED:errors.append(f"unapproved source URL: {sid}")
        if source.get("rights")!="external_link_only":errors.append(f"rights boundary: {sid}")
    entry_ids=set()
    for entry in atlas.get("entries",[]):
        eid=entry.get("id")
        if not eid or eid in entry_ids:errors.append(f"duplicate/missing entry id {eid}")
        entry_ids.add(eid)
        missing=REQUIRED-set(entry)
        if missing:errors.append(f"{eid}: missing {sorted(missing)}")
        if entry.get("kind") not in KINDS:errors.append(f"{eid}: unknown kind")
        if entry.get("rights")!="original_paraphrase":errors.append(f"{eid}: rights mismatch")
        if not isinstance(entry.get("year"),int) or not 1900<=entry["year"]<=2026:errors.append(f"{eid}: invalid year")
        for field in ("summary","evidence","interpretation","limitations"):
            value=entry.get(field,"")
            if not isinstance(value,str) or len(value)<35 or len(value)>1800:errors.append(f"{eid}: malformed {field}")
        if not isinstance(entry.get("sourceIds"),list) or not entry["sourceIds"]:errors.append(f"{eid}: missing source")
        for sid in entry.get("sourceIds",[]):
            if sid not in source_ids:errors.append(f"{eid}: unknown source {sid}")
        if entry.get("verification")!="primary_source_reviewed":errors.append(f"{eid}: verification label")
    expected_letters={f"letter-{y}" for y in range(1977,2025)}
    if not expected_letters.issubset(source_ids):errors.append("Berkshire 1977–2024 index incomplete")
    return errors

if __name__=="__main__":
    with FILE.open(encoding="utf-8") as f:atlas=json.load(f)
    issues=check(atlas)
    if issues: print("\n".join("ERROR "+v for v in issues));raise SystemExit(1)
    print(f"PASS: {len(atlas['sources'])} linked references; {len(atlas['entries'])} sourced research entries. No licensed document mirroring.")
