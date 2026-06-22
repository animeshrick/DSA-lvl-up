# Day 2 — Number Theory I (modulo & divisibility)

**Date (plan):** 2026-06-23 · **Language:** Python · **Time:** ~2–3 hrs
**Difficulty:** nudged up one notch (Day 1 = 71/100 → ADVANCE).
**10 core questions (Q1–Q10) + 2 stretch (Q11–Q12 ⭐).**

> Rules: hints only, no solutions until you explicitly ask. Reviews are blunt.
> Before writing any function: **write the expected output for the sample beside it, and dry-run one example on paper.** This is the habit that keeps failing you.

---

## Today's engine: `%` and `//`

- `%` → remainder. `n % d == 0` means d divides n.
- `//` → floor quotient.
- The digit loop you must own by tonight:

```python
while n > 0:
    digit = n % 10     # last digit
    n = n // 10        # drop it
```

For each problem the **required complexity is part of the spec** — correct output with the wrong complexity is still wrong.

---

## Core problems

### Q1 ✅ — Check prime  →  `is_prime(n) -> bool`
True if n is prime, else False.
- Edge: n < 2 → False (0, 1, negatives are not prime). 2 → True.
- **Required: O(√n).** Loop with `i*i <= n`. Looping to n is marked wrong.
- `is_prime(1)→False`, `is_prime(2)→True`, `is_prime(17)→True`, `is_prime(18)→False`, `is_prime(97)→True`.

### Q2 ✅ — Primes up to N  →  `primes_upto(n) -> list[int]`
List of all primes from 2 to n inclusive.
- Simple: reuse Q1 in a loop. `primes_upto(20)→[2,3,5,7,11,13,17,19]`, `primes_upto(1)→[]`.

### Q3 ✅ — Factorial, iterative  →  `fact_iter(n) -> int`
n! using a loop.
- Edge: `fact_iter(0)→1`, `fact_iter(1)→1`. `fact_iter(5)→120`.

### Q4 ✅ — Factorial, recursive  →  `fact_rec(n) -> int`
Same result, but recursive. Identify your base case before you write it.
- `fact_rec(0)→1`, `fact_rec(5)→120`.

### Q5 ✅ — Count digits WITHOUT string  →  `count_digits(n) -> int`
Number of digits, using only `% / //`. No `str()`, no `len()`.
- Edge: `count_digits(0)→1` (your loop will miss this — handle it). Use `abs` for negatives.
- `count_digits(7)→1`, `count_digits(1000)→4`, `count_digits(-345)→3`.

### Q6 ✅ — Sum of digits  →  `sum_digits(n) -> int`
Sum of the digits, digit loop, works on an **int** (not a string).
- `sum_digits(145)→10`, `sum_digits(0)→0`, `sum_digits(-99)→18`.

### Q7 ✅ — Reverse a number (math)  →  `reverse_num(n) -> int`
Reverse using `rev = rev*10 + n%10`. No `str[::-1]`.
- Edge: trailing zeros drop (`reverse_num(1200)→21`). Negatives keep the sign (`reverse_num(-123)→-321`).
- `reverse_num(1234)→4321`.

### Q8 ✅ — Armstrong number  →  `is_armstrong(n) -> bool`
d-digit number where sum of each digit^d equals the number. `153 = 1³+5³+3³`.
- **Use the digit loop**, not string indexing — that's the skill being graded.
- `is_armstrong(153)→True`, `is_armstrong(154)→False`, `is_armstrong(9474)→True`, `is_armstrong(9)→True`.

### Q9 ✅ — Palindrome number  →  `is_palindrome(n) -> bool`
True if the number reads the same reversed. Reverse with **math** (reuse Q7's idea).
- Edge: single digit → True. Negatives → False (the `-` breaks symmetry).
- `is_palindrome(121)→True`, `is_palindrome(123)→False`, `is_palindrome(7)→True`, `is_palindrome(-121)→False`.

### Q10 ✅ — Power of two  →  `is_power_of_two(n) -> bool`
**This is your Day-1 Q10 done right.** Not an even check.
- One-liner: `n > 0 and (n & (n-1)) == 0`. Understand WHY before you copy it.
- `is_power_of_two(1)→True`, `is_power_of_two(8)→True`, `is_power_of_two(6)→False`, `is_power_of_two(0)→False`.

---

## Stretch ⭐ (do these if you cleared the core comfortably)

### Q11 ⭐ — Sieve of Eratosthenes  →  `sieve(n) -> list[int]`
Same output as Q2 but in **O(n log log n)**. Cross out multiples instead of testing each number.
- `sieve(30)→[2,3,5,7,11,13,17,19,23,29]`.

### Q12 ⭐ — Count set bits  →  `count_set_bits(n) -> int`
Number of 1s in n's binary form. Loop with `n & 1` and `n >>= 1` (Brian Kernighan's `n &= n-1` for the faster version).
- `count_set_bits(13)→3` (1101), `count_set_bits(0)→0`, `count_set_bits(255)→8`.

---

## How to use the playground
Open **`Day02_problems_solutions.py`**. Each function has a stub — fill in your code. Then just run the file:

```
python Day02_problems_solutions.py
```

It auto-runs a built-in test harness and prints PASS/FAIL per question with the expected vs your output. Green all the way down before you ask me for the blunt review. Don't peek at the locked reference file until you've cleared the harness yourself.

## Submission checklist
- [ ] Wrote expected sample output beside each function first.
- [ ] Met required complexity (Q1 O(√n)).
- [ ] Digit-loop where required (Q5–Q9), no string tricks.
- [ ] Edge cases: 0, 1, single digit, negatives, trailing zeros.
- [ ] Harness all PASS.
- [ ] Logged time + confidence in the tracker.
