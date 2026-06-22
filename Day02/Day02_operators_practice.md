# Operator Drills — `%`, `//`, `**` and the special operators

Short, sharp problems to make Python's arithmetic & bitwise operators muscle memory.
These are the operators that quietly decide whether your number-theory code is correct.

> Same rules: hints only, no solutions until you ask. Predict every output **on paper first**, then run to check.

---

## Part A — Predict the output (no coding, just reasoning)
Write down what each line prints, THEN run them. Every wrong guess is a gap to close.

```python
print(17 % 5)        # 1
print(17 // 5)       # 2
print(-17 % 5)       # 3  <- this surprises people in Python
print(-17 // 5)      # 4  <- and this
print(17 % -5)       # 5
print(2 ** 10)       # 6
print(10 ** -1)      # 7  <- type?
print(7 / 2)         # 8  <- type?
print(7 // 2)        # 9  <- type?
print(divmod(17, 5)) # 10
print(0 % 7)         # 11
print(7 % 1)         # 12
```

Key things this teaches: Python's `%` follows the **sign of the divisor** (not the dividend like C/Java), `/` always gives a float, `//` floors toward negative infinity, and `divmod(a, b)` gives `(a // b, a % b)` in one shot.

---

## Part B — Modulo / floor-division problems

### P1 — Last digit & first digit
Given `n`, return its last digit and its first digit.
- Last digit is trivial (`% 10`). First digit needs a loop (`// 10` until single digit) — or math with `len`.
- Example: `n = 4729 → (9, 4)`.

### P2 — Is n divisible by both 3 and 5?
Return True only if divisible by 15. Then return the FizzBuzz word for n ("Fizz"/"Buzz"/"FizzBuzz"/str(n)).
- This is literally a coding-round classic. Build it from `%`.

### P3 — Clock arithmetic
It's `h` o'clock (0–23). What hour is it after `k` hours? Use `%` so it wraps correctly.
- Example: `h = 22, k = 5 → 3`. Make sure 24 maps to 0.

### P4 — Split rupees into notes
Given an amount, return how many ₹500, ₹100, ₹10, ₹1 notes/coins, greedily.
- Pure `//` and `%` cascade. `amount = 1267 → 2×500, 2×100, 6×10, 7×1`.

### P5 — Reverse a number (math only)
Reverse `n` using `rev = rev*10 + n%10` and `n //= 10`. No strings.
- Handle trailing zeros: `1200 → 21`. Handle negatives if you want the stretch.

### P6 — Sum and count of digits in one pass
Return `(digit_count, digit_sum)` using a single `while` loop.
- Edge: `n = 0` → `(1, 0)`.

---

## Part C — Power & roots

### P7 — Fast-ish power
Compute `x ** n` yourself with a loop (don't call `**`). Then look up **fast exponentiation** (squaring) for O(log n) — that's the stretch.

### P8 — Perfect square check
Is `n` a perfect square? Try it WITHOUT `math.sqrt` (use `i*i <= n` loop or integer sqrt).
- Example: `16 → True`, `17 → False`.

---

## Part D — Bitwise & special operators (worth knowing for the stretch problems)

These show up in "power of two", "count set bits", swapping, and parity tricks.

```python
a & b    # AND
a | b    # OR
a ^ b    # XOR  (a^a == 0, a^0 == a — the swap & "find single" trick)
~a       # NOT
a << k   # left shift  == a * 2**k
a >> k   # right shift == a // 2**k
```

### P9 — Power of two (bit trick) — this is your Day-1 Q10 done right
`n > 0 and (n & (n - 1)) == 0`. Explain to yourself WHY clearing the lowest set bit gives 0 only for powers of two.
- `8 → True`, `6 → False`, `1 → True`, `0 → False`.

### P10 — Even/odd via bitmask
`n & 1` is 1 for odd, 0 for even. Reimplement even/odd with this instead of `% 2`.

### P11 — Count set bits (Hamming weight)
How many 1s in the binary form of `n`? Loop with `n & 1` and `n >>= 1`. Stretch: Brian Kernighan's `n &= (n-1)` trick.
- Example: `13 (1101) → 3`.

### P12 — Swap two numbers with XOR
`a ^= b; b ^= a; a ^= b`. No temp, no arithmetic. Trace it on paper to believe it.

---

## Other handy built-ins to know (not operators, but show up constantly)
- `abs(n)` — magnitude. Useful before a digit loop on possibly-negative input.
- `round(x, k)`, `pow(x, n, mod)` — `pow` with 3 args does modular exponentiation in one call.
- `bin(n)`, `oct(n)`, `hex(n)` — string forms; `int("1011", 2)` parses back.
- `max()`, `min()`, `sum()` — fine for real problems, but if a question says "implement it / O(n) one pass", do it by hand.

Predict, run, compare. Flag anything that surprised you in the tracker.
