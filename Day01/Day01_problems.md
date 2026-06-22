# Day 1 — Complexity + I/O Warm-up (Structured Problems)

**Language:** Python · **Date:** 2026-06-21 (Day 1)
**How to use:** Read statement → note input/output format → dry-run the example by hand → code it → test against the examples → log in tracker.

---

## Q1. Sum of First N Natural Numbers  ✅
**Difficulty:** Easy
**Statement:** Given a positive integer `N`, compute the sum `1 + 2 + 3 + ... + N`. Solve it **two ways** — a loop (O(N)) and the formula `N*(N+1)//2` (O(1)) — and confirm both give the same answer.

**Input format:** A single integer `N`.
**Output format:** A single integer — the sum.

| Example | Input | Output | Why |
|---------|-------|--------|-----|
| 1 | `5` | `15` | 1+2+3+4+5 = 15 |
| 2 | `10` | `55` | 1+...+10 = 55 |
| 3 | `1` | `1` | only 1 |

**Constraints:** `1 ≤ N ≤ 10^6`
**Hint:** The formula avoids the loop entirely — that's the O(1) vs O(N) lesson.

---

## Q2. Reverse a Number  ✅
**Difficulty:** Easy
**Statement:** Given an integer `N`, output its digits in reverse order. Leading zeros in the result are dropped naturally (e.g., 100 → 1).

**Input format:** A single integer `N`.
**Output format:** A single integer — `N` with digits reversed.

| Example | Input | Output |
|---------|-------|--------|
| 1 | `1234` | `4321` |
| 2 | `100` | `1` |
| 3 | `7` | `7` |

**Constraints:** `0 ≤ N ≤ 10^9`
**Hint:** Use modulo and integer division: `digit = n % 10`, then `n = n // 10`. Build the result as `rev = rev*10 + digit`.

---

## Q3. Count Digits in a Number  ✅
**Difficulty:** Easy
**Statement:** Given a non-negative integer `N`, count how many digits it has.

**Input format:** A single integer `N`.
**Output format:** A single integer — the digit count.

| Example | Input | Output |
|---------|-------|--------|
| 1 | `1234` | `4` |
| 2 | `9` | `1` |
| 3 | `1000000` | `7` |

**Constraints:** `0 ≤ N ≤ 10^18`
**Edge case:** `N = 0` should output `1` (it has one digit).
**Hint:** Loop dividing by 10 and count, OR use `len(str(N))`. Try both and compare.

---

## Q4. Find Max & Min in a List
**Difficulty:** Easy
**Statement:** Given a list of `N` integers, find and print the maximum and minimum values. Do it manually with a single pass (don't just call `max()`/`min()` — though you can use them to verify).

**Input format:**
- Line 1: integer `N` (number of elements)
- Line 2: `N` space-separated integers

**Output format:** Two integers — the maximum and the minimum, space-separated.

| Example | Input | Output |
|---------|-------|--------|
| 1 | `5`<br>`3 7 1 9 4` | `9 1` |
| 2 | `4`<br>`-2 -8 -1 -5` | `-1 -8` |
| 3 | `1`<br>`42` | `42 42` |

**Constraints:** `1 ≤ N ≤ 10^5`, each element fits in a normal int.
**Hint:** Initialize `mx = mn = arr[0]`, then loop from index 1 updating both. One pass = O(N).

---

## Q5. Swap Two Numbers (without a temp variable)
**Difficulty:** Easy
**Statement:** Given two integers `a` and `b`, swap their values. Try it the Pythonic way (`a, b = b, a`) and also the arithmetic way (`a = a + b; b = a - b; a = a - b`).

**Input format:** Two space-separated integers `a b`.
**Output format:** Two integers after swap: `b a`.

| Example | Input | Output |
|---------|-------|--------|
| 1 | `3 7` | `7 3` |
| 2 | `-1 5` | `5 -1` |

**Constraints:** values fit in a normal int.
**Hint:** Interviewers like the no-temp trick; Python's tuple swap is the clean real-world way.

---

## Q6. Check Even or Odd  ✅
**Difficulty:** Easy
**Statement:** Given an integer `N`, print `Even` if it is divisible by 2, else `Odd`.

**Input format:** A single integer `N`.
**Output format:** The string `Even` or `Odd`.

| Example | Input | Output |
|---------|-------|--------|
| 1 | `4` | `Even` |
| 2 | `7` | `Odd` |
| 3 | `0` | `Even` |

**Constraints:** `-10^9 ≤ N ≤ 10^9`
**Hint:** `N % 2 == 0`. Note `0` is even, and `%` works on negatives in Python.

---

## Q7. Sum of Digits of a Number  ✅
**Difficulty:** Easy
**Statement:** Given a non-negative integer `N`, return the sum of its digits.

**Input format:** A single integer `N`.
**Output format:** A single integer — the digit sum.

| Example | Input | Output | Why |
|---------|-------|--------|-----|
| 1 | `1234` | `10` | 1+2+3+4 |
| 2 | `99` | `18` | 9+9 |
| 3 | `0` | `0` | — |

**Constraints:** `0 ≤ N ≤ 10^18`
**Hint:** Loop with `n % 10` and `n // 10`, OR `sum(int(d) for d in str(n))`. Do the math version for practice.

---

## Q8. Count Even and Odd Numbers in a List
**Difficulty:** Easy
**Statement:** Given a list of `N` integers, count how many are even and how many are odd.

**Input format:**
- Line 1: integer `N`
- Line 2: `N` space-separated integers

**Output format:** Two integers — count of evens and count of odds, space-separated.

| Example | Input | Output |
|---------|-------|--------|
| 1 | `5`<br>`1 2 3 4 5` | `2 3` |
| 2 | `4`<br>`2 4 6 8` | `4 0` |

**Constraints:** `1 ≤ N ≤ 10^5`
**Hint:** One pass, two counters. O(N).

---

## Q9. Multiplication Table of a Number
**Difficulty:** Easy
**Statement:** Given an integer `N`, print its multiplication table from 1 to 10, one per line, in the form `N x i = result`.

**Input format:** A single integer `N`.
**Output format:** 10 lines, e.g. `5 x 1 = 5` ... `5 x 10 = 50`.

| Example | Input | Output (first 3 lines) |
|---------|-------|------------------------|
| 1 | `5` | `5 x 1 = 5`<br>`5 x 2 = 10`<br>`5 x 3 = 15` |

**Constraints:** `-10^4 ≤ N ≤ 10^4`
**Hint:** A simple `for i in range(1, 11)` loop with an f-string.

---

## Q10. Check if a Number is a Power of Two  ⭐ (stretch)
**Difficulty:** Easy-Medium
**Statement:** Given a positive integer `N`, determine whether it is a power of two (1, 2, 4, 8, 16, ...). Print `Yes` or `No`.

**Input format:** A single integer `N`.
**Output format:** `Yes` or `No`.

| Example | Input | Output |
|---------|-------|--------|
| 1 | `16` | `Yes` |
| 2 | `12` | `No` |
| 3 | `1` | `Yes` |

**Constraints:** `1 ≤ N ≤ 10^9`
**Hint:** Keep dividing by 2 while even and check you reach 1. (Bit-trick `n & (n-1) == 0` is the O(1) version — learn it later.)

---

### Reading input in Python (for online judges)
```python
n = int(input())                       # single integer
arr = list(map(int, input().split()))  # space-separated integers on one line
```

### Today's checklist
- [ ] Q1 (both loop + formula)
- [ ] Q2
- [ ] Q3
- [ ] Q4
- [ ] Q5
- [ ] Q6
- [ ] Q7
- [ ] Q8
- [ ] Q9
- [ ] Q10 (stretch)
- [ ] Logged in tracker
