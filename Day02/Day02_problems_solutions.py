"""
Day 2 — Number Theory I  ::  PLAYGROUND
=======================================
Fill in each function below. Then just run this file:

    python Day02_problems_solutions.py

The test harness at the bottom auto-checks your answers and prints
PASS / FAIL / ERROR per question, with expected vs your output.
Goal: all green before you ask for the review.

RULES: hints only, no solutions from me until you ask. Reviews are blunt.
TIP : write the expected output for the sample BESIDE the function first,
      then dry-run one example on paper. That's the habit you keep skipping.

Digit loop you must own today:
    while n > 0:
        digit = n % 10
        n = n // 10
"""

# ----------------------------------------------------------------------
# Q1 — Check prime.  Required complexity: O(sqrt(n)).
#      n < 2 -> False.  Use  i*i <= n  (don't loop to n).
def is_prime(n):
    # your code here
    pass


# ----------------------------------------------------------------------
# Q2 — All primes from 2..n (inclusive) as a list.  Reuse is_prime.
def primes_upto(n):
    # your code here
    pass


# ----------------------------------------------------------------------
# Q3 — Factorial, ITERATIVE (loop).  0! = 1, 1! = 1.
def fact_iter(n):
    # your code here
    pass


# ----------------------------------------------------------------------
# Q4 — Factorial, RECURSIVE.  Find the base case first.
def fact_rec(n):
    # your code here
    pass


# ----------------------------------------------------------------------
# Q5 — Count digits WITHOUT str()/len().  Only % and //.
#      count_digits(0) must return 1.  Use abs() for negatives.
def count_digits(n):
    # your code here
    pass


# ----------------------------------------------------------------------
# Q6 — Sum of digits of an INT (not a string).  sum_digits(-99) -> 18.
def sum_digits(n):
    # your code here
    pass


# ----------------------------------------------------------------------
# Q7 — Reverse a number with MATH (rev = rev*10 + n%10). No str[::-1].
#      reverse_num(1200) -> 21 ;  reverse_num(-123) -> -321
def reverse_num(n):
    # your code here
    pass


# ----------------------------------------------------------------------
# Q8 — Armstrong number (sum of digit**num_of_digits == n). Digit loop only.
def is_armstrong(n):
    # your code here
    pass


# ----------------------------------------------------------------------
# Q9 — Palindrome number. Reverse with math (reuse Q7 idea).
#      Negatives -> False.
def is_palindrome(n):
    # your code here
    pass


# ----------------------------------------------------------------------
# Q10 — Power of two (bit trick).  n > 0 and (n & (n-1)) == 0.
def is_power_of_two(n):
    # your code here
    pass


# ----------------------------------------------------------------------
# Q11 (STRETCH) — Sieve of Eratosthenes.  Same output as Q2, O(n log log n).
def sieve(n):
    # your code here
    pass


# ----------------------------------------------------------------------
# Q12 (STRETCH) — Count set bits (1s in binary).  count_set_bits(13) -> 3.
def count_set_bits(n):
    # your code here
    pass


# ======================================================================
# TEST HARNESS — do not edit below. Just run the file.
# ======================================================================
def _run_tests():
    # (function, [(args_tuple, expected), ...])
    suites = [
        ("Q1  is_prime", is_prime, [
            ((1,), False), ((2,), True), ((17,), True), ((18,), False),
            ((0,), False), ((-7,), False), ((97,), True)]),
        ("Q2  primes_upto", primes_upto, [
            ((20,), [2, 3, 5, 7, 11, 13, 17, 19]), ((1,), []), ((2,), [2])]),
        ("Q3  fact_iter", fact_iter, [
            ((0,), 1), ((1,), 1), ((5,), 120), ((6,), 720)]),
        ("Q4  fact_rec", fact_rec, [
            ((0,), 1), ((5,), 120), ((7,), 5040)]),
        ("Q5  count_digits", count_digits, [
            ((0,), 1), ((7,), 1), ((1000,), 4), ((-345,), 3)]),
        ("Q6  sum_digits", sum_digits, [
            ((145,), 10), ((0,), 0), ((-99,), 18), ((10000,), 1)]),
        ("Q7  reverse_num", reverse_num, [
            ((1234,), 4321), ((1200,), 21), ((-123,), -321), ((5,), 5)]),
        ("Q8  is_armstrong", is_armstrong, [
            ((153,), True), ((154,), False), ((9474,), True), ((9,), True)]),
        ("Q9  is_palindrome", is_palindrome, [
            ((121,), True), ((123,), False), ((7,), True), ((-121,), False)]),
        ("Q10 is_power_of_two", is_power_of_two, [
            ((1,), True), ((8,), True), ((6,), False), ((0,), False)]),
        ("Q11 sieve (stretch)", sieve, [
            ((30,), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]), ((1,), [])]),
        ("Q12 count_set_bits (stretch)", count_set_bits, [
            ((13,), 3), ((0,), 0), ((255,), 8)]),
    ]

    total_q, passed_q = 0, 0
    print("=" * 60)
    print("  DAY 2 PLAYGROUND — SELF CHECK")
    print("=" * 60)
    for name, fn, cases in suites:
        total_q += 1
        results = []
        all_ok = True
        for args, expected in cases:
            try:
                got = fn(*args)
                ok = got == expected
            except Exception as e:               # not implemented / crash
                got, ok = f"ERROR({type(e).__name__})", False
            results.append((args, expected, got, ok))
            all_ok = all_ok and ok
        passed_q += all_ok
        status = "PASS" if all_ok else "FAIL"
        print(f"\n[{status}] {name}")
        if not all_ok:
            for args, expected, got, ok in results:
                if not ok:
                    a = ", ".join(map(repr, args))
                    print(f"        {fn.__name__ if hasattr(fn,'__name__') else name}({a}) -> got {got!r}, expected {expected!r}")
    print("\n" + "=" * 60)
    print(f"  SCORE: {passed_q}/{total_q} questions fully passing")
    print("=" * 60)
    if passed_q == total_q:
        print("  All green. Now ask for the review.")
    else:
        print("  Keep going. Fix the FAILs, re-run, repeat.")


if __name__ == "__main__":
    _run_tests()
