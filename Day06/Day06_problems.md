# Day 6 — Recursion

**Date (plan):** 2026-07-02 · **Language:** Python · **Time:** ~2–3 hrs
**Difficulty:** ADVANCE — modest step up from Day 3 (~74). Recursion is the foundation for trees,
backtracking, and divide-and-conquer, so we slow down and build it properly.
**10 core questions (Q1–Q10) + 2 stretch (⭐).**

> Rules: hints name the technique only — no code handed over. Reviews are honest but kind, with a
> small nudge on any failure. Solutions only when you ask.
> Keep stating time + space complexity above each function — and for recursion, remember the call
> stack counts as space.

---

## Concept primer (read this — recursion trips everyone up at first)

A recursive function calls **itself** on a smaller version of the problem. Every recursive
function needs exactly two things:

1. **Base case** — the smallest input where you return an answer directly, WITHOUT recursing.
   This is what stops the recursion. Forget it and you get infinite recursion (`RecursionError`).
2. **Recursive case** — solve a smaller piece, call yourself on the rest, and combine.

The mental model: *"assume the function already works for a smaller input — what do I do with that
result?"* For factorial: assume `fact(n-1)` is correct; then `fact(n) = n * fact(n-1)`. Base case
`fact(0) = 1`.

**Space note:** each pending call sits on the *call stack* until it returns. Recursion that goes n
deep uses O(n) stack space even if it allocates nothing else. That's the hidden cost vs a loop.

**Two questions to ask every time:**
- What's the smallest input, and what do I return for it? (base case)
- How do I shrink the input on each call so I *reach* the base case? (progress)

---

## Part A — Number recursion

### Q1 ✅ — Sum 1..n  →  `sum_to_n(n) -> int`
Return 1 + 2 + ... + n, recursively (no loop, no formula).
- Base case: what is `sum_to_n(0)`? `sum_to_n(5)→15`, `sum_to_n(1)→1`, `sum_to_n(0)→0`.

### Q2 ✅ — Nth Fibonacci  →  `fib(n) -> int`
Return the n-th Fibonacci number (0-indexed: fib(0)=0, fib(1)=1), recursively.
- `fib(0)→0`, `fib(1)→1`, `fib(6)→8`, `fib(10)→55`. (You'll need TWO base cases here.)

### Q3 ✅ — Sum of digits (recursive)  →  `sum_digits(n) -> int`
Sum the digits using recursion (no loop). Assume n ≥ 0.
- Hint: the last digit is `n % 10`, the rest is `n // 10`. `sum_digits(145)→10`, `sum_digits(0)→0`, `sum_digits(7)→7`.

### Q4 ✅ — Power x^n  →  `power(x, n) -> int`
Compute x raised to n, recursively (assume n ≥ 0). No `**`, no loop.
- Base case: what is `power(x, 0)`? `power(2, 10)→1024`, `power(5, 0)→1`, `power(3, 3)→27`.

### Q5 ✅ — Natural numbers list  →  `naturals(n) -> list`
Return `[1, 2, ..., n]` built recursively.
- `naturals(5)→[1,2,3,4,5]`, `naturals(1)→[1]`, `naturals(0)→[]`.

---

## Part B — String & array recursion

### Q6 ✅ — Reverse a string (recursive)  →  `reverse_string(s) -> str`
Reverse `s` using recursion, not slicing or a loop.
- Hint: first char goes to the end; recurse on the rest. `reverse_string("hello")→"olleh"`, `reverse_string("")→""`, `reverse_string("a")→"a"`.

### Q7 ✅ — GCD (recursive)  →  `gcd(a, b) -> int`
Euclidean algorithm, but recursive this time. Base case: when `b == 0`.
- `gcd(12,18)→6`, `gcd(17,5)→1`, `gcd(9,0)→9`.

### Q8 ✅ — Sum of array elements (recursive)  →  `array_sum(a) -> int`
Sum a list recursively (no `sum()`, no loop).
- Hint: first element + sum of the rest. `array_sum([1,2,3,4])→10`, `array_sum([])→0`, `array_sum([5])→5`.

### Q9 ✅ — Palindrome check (recursive)  →  `is_palindrome(s) -> bool`
True if `s` is a palindrome, checked recursively (compare ends, recurse on the middle).
- `is_palindrome("racecar")→True`, `is_palindrome("hello")→False`, `is_palindrome("a")→True`, `is_palindrome("")→True`.

### Q10 ✅ — Binary search (recursive)  →  `binary_search(a, target) -> int`
`a` is sorted ascending. Return the index of target, or -1, using recursion (not a while loop).
- Hint: you'll need to track `low`/`high` bounds — use a helper or default parameters.
- `binary_search([1,3,5,7,9], 7)→3`, `binary_search([1,3,5], 4)→-1`, `binary_search([], 1)→-1`.

---

## Stretch ⭐

### Q11 ⭐ — Fast power  →  `fast_power(x, n) -> int`
Same as Q4 but in **O(log n)**: if n is even, `x^n = (x^(n/2))²`; if odd, `x * x^(n-1)`.
- `fast_power(2, 10)→1024`, `fast_power(3, 0)→1`, `fast_power(2, 13)→8192`.

### Q12 ⭐ — Tower of Hanoi  →  `hanoi(n, source, target, aux) -> list`
Return the list of moves (as `(from, to)` tuples) to move n disks from `source` to `target`
using `aux`. The classic 3-line recursion: move n-1 to aux, move the big disk, move n-1 to target.
- `hanoi(1, "A", "C", "B")→[("A","C")]`
- `hanoi(2, "A", "C", "B")→[("A","B"), ("A","C"), ("B","C")]`

---

## How to use the playground
Open **`Day06_problems_solutions.py`**, fill the stubs, run:

```
python Day06_problems_solutions.py
```

PASS/FAIL per question + a score. Core all green before you ask for review.

## Submission checklist
- [ ] Every function has a clear **base case** (no infinite recursion).
- [ ] Each recursive call shrinks the input toward the base case.
- [ ] No loops where the problem says "recursive" (Q1–Q10 are recursion practice).
- [ ] Edge cases: 0, empty string/list, single element.
- [ ] Noted time + space (incl. call-stack depth) above each function.
- [ ] Harness core all PASS.
- [ ] Logged time + confidence in the tracker.
