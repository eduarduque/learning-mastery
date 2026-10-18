"""Validate classes/*.json and bundle them into classes/data.js (works from file:// and GitHub Pages)."""
import json, glob, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ORDER = ["biology", "cpp", "discrete", "ethics"]
banks, problems = [], []
for path in sorted(glob.glob(os.path.join(HERE, "classes", "*.json"))):
    b = json.load(open(path, encoding="utf-8"))
    tids = {t["id"] for t in b["topics"]}
    seen = set()
    for q in b["questions"]:
        if q["id"] in seen: problems.append(f"{b['id']}: duplicate id {q['id']}")
        seen.add(q["id"])
        if q["topic"] not in tids: problems.append(f"{q['id']}: unknown topic {q['topic']}")
        if len(q["choices"]) != 4 or len(set(q["choices"])) != 4: problems.append(f"{q['id']}: needs 4 unique choices")
        if not 0 <= q["answer"] < len(q["choices"]): problems.append(f"{q['id']}: bad answer index")
    banks.append(b)
    print(f"{b['name']}: {len(b['topics'])} topics, {len(b['questions'])} questions")
banks.sort(key=lambda b: ORDER.index(b["id"]) if b["id"] in ORDER else 99)
if problems:
    print("\n".join(problems)); sys.exit(1)
with open(os.path.join(HERE, "classes", "data.js"), "w", encoding="utf-8") as f:
    f.write("window.CLASSES=" + json.dumps(banks, ensure_ascii=False, separators=(",", ":")) + ";\n")
print("wrote classes/data.js")
