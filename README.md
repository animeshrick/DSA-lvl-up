# DSA Level-1 — Interview Preparation (2026)

A structured, self-paced program to get coding-round ready for **service / IT companies**
(TCS, Infosys, Wipro, Accenture, Cognizant and similar). Language: **Python**.
Pace: ~2–3 hrs/day. Target horizon: 3 months, starting with a 4-week Level-1 foundation.

This repository is both the **curriculum** and the **proof of work** — every day has a problem
set, my own solutions, and a graded, evidence-based review.

---

## What this program is

It is run like a real interview-prep partnership with a strict feedback loop:

1. **Learn the concept** for the day, then dry-run one example on paper.
2. **Solve the problems myself** in Python (no copy-paste) inside a runnable "playground."
3. **Self-verify** against a built-in test harness (PASS/FAIL per question).
4. **Get a blunt, interviewer-style review** scored out of 100.
5. **Adaptive gating** decides whether I advance, level up, or repeat the day.

The goal is not to "finish" days — it is to actually be able to solve these cold, under time pressure.

---

## How progress is scored

Every day's submission is graded out of 100 against a fixed rubric:

| Category | Weight | What it measures |
|---|---:|---|
| Correctness | 60 | Passes all examples **and** edge cases (zero, negatives, single element, etc.) |
| Complexity / approach | 20 | Meets the required Big-O and the intended approach (e.g. one-pass O(n), no-temp swap) |
| Code quality | 10 | Naming, no dead code, no shadowed built-ins, readability |
| Completeness | 10 | All problems attempted, including stretch (⭐) |

**Adaptive difficulty gate** based on the score:

| Score | Outcome |
|---|---|
| **< 50** | **Remediate** — repeat the level with fresh problems + a targeted study list |
| **50–74** | **Advance** — move to the next day, nudge difficulty up one notch |
| **75–100** | **Level up** — advance and bump difficulty aggressively (harder variants, tighter limits) |

A review cap of **5 reviews per file** keeps the loop honest — after that, fixing it is on me.

---

## Progress so far

| Day | Topic | Status | Score | Result |
|---:|---|---|---:|---|
| 1 | Time/Space Complexity + I/O warm-up | Advanced | 71 / 100 | Climbed 39 → 46 → 71 over three reviews |
| 2 | Number Theory I (prime, factorial, Armstrong, palindrome) | ✅ Done | 91 / 100 | **Level up** — 10/10 core passing with edge cases |
| 3 | Arrays + Hashing / Dictionaries (+ GCD/LCM/Fibonacci) | 🔄 In progress | — | 15 questions (12 core + 3 stretch) |

**Trajectory:** the scores show the system working as intended — Day 1 started weak
(repeated remediation on digit-handling and "solving a different problem than written"),
those exact gaps were drilled, and Day 2 jumped to a level-up. Day 3 was pulled forward to
arrays and dictionaries — the highest-yield topics for service-company rounds.

Day-1 → Day-2 improvement, concretely: digit-by-digit math loops, `O(√n)` primality,
and the power-of-two **bit trick** all went from failing to clean.

> The authoritative, live record is **`DSA_Level1_Tracker.xlsx`** (status dropdowns,
> confidence ratings, per-day review notes, and an auto-calculating Summary tab).

---

## Repository structure

```
DSA lvl-1/
├── README.md                       <- you are here
├── 00_START_HERE_3month_roadmap.md <- the full 3-month plan
├── 01_DSA_Level1_syllabus.md       <- week-by-week Level-1 syllabus
├── DSA_Level1_Tracker.xlsx         <- live progress tracker (primary)
├── DSA_Level1_Tracker.csv          <- plain-text backup of the tracker
├── CLAUDE.md                       <- the working rules / scoring rubric
│
├── Day01/   Complexity + I/O warm-up
│   ├── Day01_problems.md           <- the day's questions
│   ├── Day01_problems_solutions.py <- my solutions
│   ├── Day01_RETRY_problems.md     <- remediation set
│   └── Day01_solutions.py          <- locked reference solutions
│
├── Day02/   Number Theory I
│   ├── Day02_problems.md
│   ├── Day02_operators_practice.md <- drills on % // ** and bitwise operators
│   ├── Day02_problems_solutions.py <- my solutions + self-check harness
│   └── Time_and_Space_Complexity_Guide.docx  <- how to calculate Big-O (reference)
│
└── Day03/   Arrays + Hashing / Dictionaries
    ├── Day03_problems.md
    └── Day03_problems_solutions.py <- playground (stubs + self-check harness)
```

---

## The tracker, explained

`DSA_Level1_Tracker.xlsx` has two tabs:

**`DSA Level-1 Tracker`** — one row per day (28 days total), with columns:

| Column | Meaning |
|---|---|
| Day / Date (plan) / Week | Schedule position |
| Topic | What that day covers |
| Problems Planned / Solved | Scope vs. actual |
| Time Spent (min) | Effort logged per day |
| Status | Not started / In progress / Done (dropdown) |
| Confidence (1–5) | Self-rated mastery (dropdown) |
| Revise? (Y/N) | Flagged for a later revision pass |
| Notes | The graded review summary + score for that day |

**`Summary`** — auto-calculated totals: days done, days in progress, total problems
solved, total time, and topics flagged to revise. These update automatically from the
tracker rows, so the dashboard is always current.

---

## How the daily "playground" works

Each day's `*_problems_solutions.py` is a runnable file: function stubs to fill in, plus a
built-in **test harness**. After writing the solutions, a single command self-checks them:

```bash
python Day03/Day03_problems_solutions.py
```

Sample output:

```
============================================================
  DAY 3 PLAYGROUND — SELF CHECK
============================================================
[PASS] Q1  gcd
[PASS] Q5  max_min
[FAIL] Q11 two_sum
        two_sum([2, 7, 11, 15], 9) -> got None, expected (0, 1)
...
  SCORE: 12/15 questions fully passing
```

The rule is simple: **all green before requesting the blunt review.** This makes correctness
non-negotiable and keeps the human review focused on approach, complexity, and quality.

---

## Curriculum at a glance (Level-1, 4 weeks)

- **Week 1 — Basics, Math & Patterns:** complexity & I/O, number theory, pattern printing, arrays.
- **Week 2 — Strings, Searching & Sorting:** string algorithms, binary search, sorting basics + applications.
- **Week 3 — Hashing, Two Pointers & Recursion:** dictionaries/sets, two-pointer patterns, recursion, intro backtracking.
- **Week 4 — Linked Lists, Stacks/Queues & Trees:** core data structures + a full revision and timed final test.

Full details in `01_DSA_Level1_syllabus.md`. After Level-1: Level-2 (trees/BST, sliding window,
intro DP, basic graphs), an aptitude module, and a core-CS module (DBMS, OOP, OS, CN).

---

## Practice platforms used
GeeksforGeeks (service-company "must-do" lists), HackerRank (Problem Solving track), and
LeetCode (Easy set, filtered by topic).

---

*Last updated: 2026-06-24 · Maintained as a daily, evidence-backed prep log.*
