# Day 3 — Arrays + Hashing (Dictionaries), with a Number-Theory II warm-up

**Date (plan):** 2026-06-24 · **Language:** Python · **Time:** ~2–3 hrs
**Difficulty:** LEVEL UP — you scored ~91/100 on Day 2, so this jumps ahead of the original roadmap. We pull **arrays and dictionaries forward** (you asked) and keep the high-yield Number-Theory II quick wins.
**12 core questions (Q1–Q12) + 3 stretch (⭐).**

> Rules: hints only, no solutions until you ask. Reviews are blunt.
> New non-negotiable at this level: **state the time AND space complexity of every function as a comment above it** (you have the complexity doc — use it). I grade complexity hard now.

---

## Concept primer (read before coding)

### Why arrays + hashing now
These two topics are ~60% of service-company coding rounds. Arrays teach traversal, two-pointers, and in-place tricks. Dictionaries/sets give O(1) lookups, which is how you turn an O(n²) brute force into O(n). This is the single most important upgrade in your prep.

### Python lists (your "array")
```python
a = [3, 1, 4, 1, 5]
a[0]            # index access      -> O(1)
a[-1]           # last element      -> O(1)
a.append(9)     # add to end        -> O(1)
a.pop()         # remove from end   -> O(1)
a.insert(0, x)  # insert at front   -> O(n)  (shifts everything)
x in a          # membership search -> O(n)  (scans the list)
len(a)          # length            -> O(1)
a[i], a[j] = a[j], a[i]   # swap in place, no temp
```
**Two-pointer pattern** (one index from each end) and **in-place** edits (O(1) extra space) are what interviewers look for.

### Python dict & set (your "hash table")
```python
d = {}
d[k] = d.get(k, 0) + 1   # frequency-count idiom -> O(1) per op
k in d                   # key lookup            -> O(1) average
s = set(a)               # unique elements       -> O(n) build, O(1) lookup
from collections import Counter, defaultdict     # know these exist
```
Mental model: **a dict trades O(n) memory for O(1) lookups.** When a problem says "find a pair / duplicate / count / first unique", reach for a dict or set first.

---

## Part A — Number Theory II warm-up (quick, high-yield)

### Q1 ✅ — GCD (Euclidean)  →  `gcd(a, b) -> int`
GCD using `a, b = b, a % b` until b is 0.
- Required: **O(log(min(a,b)))** — Euclidean loop, not trial division.
- `gcd(12,18)→6`, `gcd(17,5)→1`, `gcd(0,9)→9`, `gcd(100,10)→10`.

### Q2 ✅ — LCM  →  `lcm(a, b) -> int`
Use `a*b // gcd(a,b)` (reuse Q1).
- `lcm(4,6)→12`, `lcm(3,5)→15`, `lcm(12,18)→36`.

### Q3 ✅ — Fibonacci, first N terms  →  `fib(n) -> list[int]`
Iterative. `fib(0)→[]`, `fib(1)→[0]`, `fib(7)→[0,1,1,2,3,5,8]`.
- Required: **O(n) time, O(1) extra** (besides the output list).

---

## Part B — Arrays

### Q4 ✅ — Reverse an array IN PLACE  →  `reverse_arr(a) -> list`
Two pointers, swap ends inward. No `a[::-1]`, no `reversed()`.
- Required: **O(n) time, O(1) space.** `reverse_arr([1,2,3,4])→[4,3,2,1]`, `reverse_arr([])→[]`.

### Q5 ✅ — Max & min in ONE pass  →  `max_min(a) -> tuple`
Return `(max, min)`. **This is your Day-1 Q4 done right.** No `sorted()`, no `max()/min()`.
- Required: **O(n) time, O(1) space.** `max_min([3,7,1,9,4])→(9,1)`, `max_min([-2,-8,-1,-5])→(-1,-8)`, `max_min([5])→(5,5)`.

### Q6 ✅ — Second largest DISTINCT element  →  `second_largest(a) -> int | None`
One pass, track largest and second. If no distinct second, return None.
- `second_largest([3,7,1,9,4])→7`, `second_largest([5,5,5])→None`, `second_largest([2,2,3])→2`.

### Q7 ✅ — Move all zeros to the end  →  `move_zeros(a) -> list`
Keep non-zero order; push zeros to the back, **in place**.
- Required: **O(n) time, O(1) space.** `move_zeros([0,1,0,3,12])→[1,3,12,0,0]`, `move_zeros([0,0])→[0,0]`.

### Q8 ✅ — Missing number  →  `missing_number(a) -> int`
`a` is a permutation of 1..n with exactly one value missing (so `len(a) = n-1`). Return the missing one.
- Use `n*(n+1)//2 - sum(a)` where `n = len(a)+1`, or XOR. O(1) space, no nested search.
- `missing_number([1,2,4,5])→3`, `missing_number([2,3,1,5])→4`, `missing_number([2])→1`.

### Q9 ✅ — Rotate array right by k  →  `rotate(a, k) -> list`
Rotate right by k. Handle `k > len(a)` with `k %= len(a)`.
- `rotate([1,2,3,4,5],2)→[4,5,1,2,3]`, `rotate([1,2,3],4)→[3,1,2]`, `rotate([1],3)→[1]`.

---

## Part C — Hashing / Dictionaries

### Q10 ✅ — Frequency count  →  `freq_count(a) -> dict`
Dict mapping each element to its count. Required: **O(n).**
- `freq_count([1,2,2,3,3,3])→{1:1, 2:2, 3:3}`, `freq_count([])→{}`.

### Q11 ✅ — Two Sum (indices)  →  `two_sum(a, target) -> tuple`
Indices `(i, j)`, `i < j`, of the two numbers summing to target. **O(n) with a dict**, not the O(n²) double loop.
- `two_sum([2,7,11,15],9)→(0,1)`, `two_sum([3,2,4],6)→(1,2)`.

### Q12 ✅ — First non-repeating element  →  `first_unique(a) -> int | None`
First element that appears exactly once; None if there is none.
- Frequency dict, then a second pass in order. `first_unique([4,5,4,6,5,7])→6`, `first_unique([1,1,2,2])→None`.

---

## Stretch ⭐

### Q13 ⭐ — Valid anagram  →  `is_anagram(s, t) -> bool`
Same letters, any order. Frequency dict / Counter, O(n).
- `is_anagram("listen","silent")→True`, `is_anagram("rat","car")→False`, `is_anagram("a","ab")→False`.

### Q14 ⭐ — Majority element  →  `majority(a) -> int`
Appears more than n//2 times (assume it exists). Dict works; **Boyer–Moore voting** does O(n) time, O(1) space — aim for that.
- `majority([3,3,4,2,3,3,3])→3`, `majority([1,1,1,2])→1`.

### Q15 ⭐⭐ — Longest substring without repeating characters  →  `longest_unique(s) -> int`
Length of the longest substring with all-distinct characters. **Sliding window + set/dict, O(n)** — not O(n²). (This was on your Day-3 radar already; it's the hardest thing here.)
- `longest_unique("abcabcbb")→3`, `longest_unique("bbbbb")→1`, `longest_unique("pwwkew")→3`, `longest_unique("")→0`.

---

## How to use the playground
Open **`Day03_problems_solutions.py`**, fill each stub, then run:

```
python Day03_problems_solutions.py
```

It prints PASS/FAIL per question with expected vs your output and a running score. All green before you ask for review. Reference solutions stay locked until you've cleared the harness yourself.

## Submission checklist
- [ ] Complexity comment (time + space) above every function.
- [ ] In-place where required (Q4, Q5, Q7) — O(1) extra space.
- [ ] Dict/set used to hit O(n) on Q10–Q13 (no nested loops).
- [ ] Edge cases: empty list/string, single element, all-equal, k > len, no valid answer (None).
- [ ] Harness all PASS.
- [ ] Logged time + confidence in the tracker.
