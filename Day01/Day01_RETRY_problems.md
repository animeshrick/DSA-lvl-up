# Day 1 — RETRY Set (score 39/100, remediation)

Same difficulty, fresh problems, aimed straight at what you failed:
digit extraction, element-vs-index looping + counter init, and range() bounds.
**Rule:** dry-run one example on paper BEFORE coding. No solutions until you ask.

---

## R1. Last Digit of a Number  (digit extraction)
Given an integer `N`, output its last digit.
| Input | Output |
|-------|--------|
| `1234` | `4` |
| `9` | `9` |
| `0` | `0` |
**Concept drilled:** `N % 10`. Trivial on purpose — proves you own the modulo idea.

## R2. Sum of Digits  (REDO of the one you crashed)
Given a non-negative integer `N`, return the sum of its digits. **Input is an int, not a string.**
| Input | Output |
|-------|--------|
| `145` | `10` |
| `99` | `18` |
| `0` | `0` |
**Concept drilled:** `while n > 0: s += n % 10; n //= 10`. No `sum("145")`.

## R3. Product of Digits  (digit extraction, variation)
Given a non-negative integer `N`, return the product of its digits.
| Input | Output | Why |
|-------|--------|-----|
| `123` | `6` | 1*2*3 |
| `405` | `0` | 4*0*5 |
| `9` | `9` | — |
**Concept drilled:** same loop, start your accumulator at `1`, not `0`. Think about why.

## R4. Count Even & Odd in a List  (REDO of the one that crashed)
Given a list of integers, return `(even_count, odd_count)` — **evens first**.
| Input | Output |
|-------|--------|
| `[1, 2, 3, 4, 5]` | `(2, 3)` |
| `[2, 4, 6, 8]` | `(4, 0)` |
**Concept drilled:** initialize both counters to 0; loop over the **elements** (`for x in arr`), not the indices.

## R5. Multiplication Table  (REDO of the one that returned 0)
Given `N`, print 10 lines: `N x 1 = ...` through `N x 10 = ...`.
| Input | Output (first 2 lines) |
|-------|------------------------|
| `5` | `5 x 1 = 5`<br>`5 x 2 = 10` |
**Concept drilled:** `for i in range(1, 11)`. Don't multiply `N` into itself.

## R6. Count Digits Equal to a Given Digit  (combine both skills) ⭐
Given an integer `N` and a digit `d` (0–9), count how many times `d` appears in `N`.
| Input (N, d) | Output |
|--------------|--------|
| `122232, 2` | `4` |
| `5005, 0` | `2` |
| `9, 3` | `0` |
**Concept drilled:** digit-extraction loop + a counter you initialize and increment conditionally.

---

### Checklist
- [ ] R1  - [ ] R2  - [ ] R3  - [ ] R4  - [ ] R5  - [ ] R6 (⭐)
- [ ] Dry-ran each on paper first
- [ ] Logged in tracker

**Pass = 50+ to unlock Day 2.** Paste your code when ready for the review.
