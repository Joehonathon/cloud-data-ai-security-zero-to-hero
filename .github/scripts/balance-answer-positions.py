#!/usr/bin/env python3
"""Balance answer positions in resources/practice-questions/*.md.

Why: 2026-10-14 found most banks had the correct answer at B (some 40 of 40). A learner
who notices the pattern passes without knowing the material. New banks should vary the
correct letter; run --check before committing a bank, and run --write to rebalance one.

Per question: shuffle the 4 options so the correct letter follows a balanced,
seeded target sequence; remap letter references in the explanation and in any
Answer Key table. Questions it cannot remap safely are left untouched and listed.

usage: balance-answer-positions.py [--write | --check] [--threshold 0.4] files...
  --check  exit 1 if any file has one letter correct in more than the threshold share of questions
"""
import hashlib, random, re, sys
from collections import Counter

LET = "ABCD"
Q_SPLIT = re.compile(r"(?=^#{2,4} Question \d+)", re.M)
OPT_BLOCK = re.compile(r"((?:^[A-D]\. .*\n){4})", re.M)
CORRECT = re.compile(r"\*\*Correct: ([A-D])\*\*")
DETAILS_END = "</details>"

# a bare letter that is clearly an option reference
REF_AFTER = re.compile(
    r"\s*(?:\)|,|:|;|\.(?:\s|$)|is\b|are\b|would\b|can\b|cannot\b|could\b|does\b|doesn't\b|do\b|don't\b|has\b|have\b|"
    r"will\b|was\b|were\b|fails\b|only\b|alone\b|and\s+[A-D]\b|or\s+[A-D]\b|but\b|also\b|looks\b|sounds\b|"
    r"may\b|might\b|should\b|shouldn't\b|requires\b|uses\b|adds\b|gives\b|provides\b|describes\b|states\b|is$)")
BARE = re.compile(r"(?<![\w'’/.\-\*#])([A-D])(?![\w'’\-])")
PAREN = re.compile(r"\(([A-D])\)")
OPTWORD = re.compile(r"\b((?:[Oo]ptions?|[Aa]nswers?|[Cc]hoices?|[Dd]istractors?)\s+)([A-D])\b")


def refs_ok(text, mapping):
    """Return (new_text, ambiguous?)"""
    ambiguous = False

    # single pass only: every option reference is remapped exactly once below

    out, last = [], 0
    for m in BARE.finditer(text):
        letter = m.group(1)
        after = text[m.end():m.end() + 30]
        before = text[max(0, m.start() - 12):m.start()]
        is_ref = bool(REF_AFTER.match(after)) or re.search(r"(?:[Oo]ptions?|[Aa]nswers?|[Cc]hoices?)\s+$", before) \
            or re.search(r"\b[A-D]\s*(?:,|and|or)\s*$", before) and REF_AFTER.match(after)
        if letter == "A" and not is_ref:
            continue                       # the article
        if letter in "BCD" and not is_ref:
            # single capital B/C/D followed by a word: could be "B vs C"; treat as ambiguous
            if re.match(r"\s+(?:vs\.?|versus|to|over)\s", after) or re.match(r"\s*[-/]", after):
                ambiguous = True
            else:
                ambiguous = True
            continue
        out.append((m.start(), m.end(), mapping[letter]))
    res, pos = [], 0
    for s, e, new in out:
        res.append(text[pos:s]); res.append(new); pos = e
    res.append(text[pos:])
    return "".join(res), ambiguous


OPTION_REF_IN_OPTS = re.compile(r"\b(?:above|below|all of|none of|both|neither|either of|option [A-D]|\b[A-D] and [A-D]\b)", re.I)


def process(path, write, threshold, report):
    t = open(path, encoding="utf-8").read()
    parts = Q_SPLIT.split(t)
    head, qs = parts[0], parts[1:]
    letters = []
    for q in qs:
        m = CORRECT.search(q)
        if m:
            letters.append(m.group(1))
    if len(qs) < 4 or len(letters) < len(qs) - 1:
        report.append((path, "SKIP: unparseable", len(qs), len(letters)))
        return
    cnt = Counter(letters)
    share = cnt.most_common(1)[0][1] / len(letters)
    if share <= threshold:
        report.append((path, "ok (share %.2f)" % share, len(qs), 0))
        return
    seed = int(hashlib.sha256(path.encode()).hexdigest()[:8], 16)
    rng = random.Random(seed)
    # balanced target sequence
    base = [LET[i % 4] for i in range(len(qs))]
    rng.shuffle(base)
    new_qs, qmap, skipped = [], {}, []
    for idx, q in enumerate(qs):
        num = int(re.search(r"Question (\d+)", q).group(1))
        mo = OPT_BLOCK.search(q)
        mc = CORRECT.search(q)
        if not mo or not mc:
            skipped.append((num, "format")); new_qs.append(q); qmap[num] = mc.group(1) if mc else None; continue
        opts = [l[3:] for l in mo.group(1).rstrip("\n").split("\n")]
        old_c = LET.index(mc.group(1))
        if any(OPTION_REF_IN_OPTS.search(o) for o in opts):
            skipped.append((num, "options reference options")); new_qs.append(q); qmap[num] = mc.group(1); continue
        tgt = LET.index(base[idx])
        others = [i for i in range(4) if i != old_c]
        rng.shuffle(others)
        perm = [None] * 4                     # perm[new_pos] = old_pos
        perm[tgt] = old_c
        it = iter(others)
        for k in range(4):
            if perm[k] is None:
                perm[k] = next(it)
        mapping = {LET[old]: LET[new] for new, old in enumerate(perm)}
        # explanation = text after the Correct marker up to </details>
        c_end = mc.end()
        d_end = q.find(DETAILS_END, c_end)
        if d_end < 0:
            d_end = len(q)
        expl, amb = refs_ok(q[c_end:d_end], mapping)
        if amb:
            skipped.append((num, "ambiguous letters in explanation")); new_qs.append(q); qmap[num] = mc.group(1); continue
        new_opts = "".join(f"{LET[k]}. {opts[perm[k]]}\n" for k in range(4))
        nq = q[:mo.start()] + new_opts + q[mo.end():c_end - len(mc.group(0))]
        nq = nq[:mo.start()] + new_opts + q[mo.end():mc.start()] + f"**Correct: {LET[tgt]}**" + expl + q[d_end:]
        # safety: the correct option text must be unchanged
        assert opts[old_c] == new_opts.split("\n")[tgt][3:], (path, num)
        new_qs.append(nq); qmap[num] = LET[tgt]
    result = head + "".join(new_qs)
    # answer key tables
    def key_row(m):
        n = int(m.group(1))
        return f"| {n} | {qmap.get(n, m.group(2))} |" if n in qmap and qmap[n] else m.group(0)
    result = re.sub(r"^\| (\d+) \| ([A-D]) \|", key_row, result, flags=re.M)
    after = Counter(re.findall(r"\*\*Correct: ([A-D])\*\*", result))
    report.append((path, "shuffled %s -> %s" % (dict(sorted(cnt.items())), dict(sorted(after.items()))), len(qs), skipped))
    if write:
        open(path, "w", encoding="utf-8").write(result)


if __name__ == "__main__":
    args = sys.argv[1:]
    write = "--write" in args
    check = "--check" in args
    thr = 0.4
    if "--threshold" in args:
        thr = float(args[args.index("--threshold") + 1])
    files = [a for a in args if a.endswith(".md")]
    rep = []
    for f in files:
        process(f, write, thr, rep)
    if check:
        bad = [r[0] for r in rep if str(r[1]).startswith("shuffled")]
        for b in bad:
            print("SKEWED:", b)
        sys.exit(1 if bad else 0)
    tot_sk = 0
    for r in rep:
        sk = r[3] if isinstance(r[3], list) else []
        tot_sk += len(sk)
        print(r[0].split("/")[-1], "|", r[1], "|", r[2], "q", ("| skipped %s" % sk) if sk else "")
    print("files", len(rep), "skipped questions", tot_sk)
