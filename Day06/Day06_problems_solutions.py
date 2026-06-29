"""
Day 6 — Recursion  ::  PLAYGROUND
=================================
Fill each stub, then run:

    python Day06_problems_solutions.py

The harness checks your answers (PASS / FAIL / ERROR) and prints a score.

RULES:
  - State TIME and SPACE complexity above EVERY function (recursion: stack depth counts!).
  - These are recursion practice — no loops in Q1-Q10.
  - Hints name the technique only. Solutions only when you ask.
  - Reviews are honest but kind, with a nudge on any failure.

Every recursive function needs:
  1) a BASE CASE (smallest input, returns directly, stops the recursion)
  2) a RECURSIVE CASE (shrink the input, call yourself, combine)
"""

# ===== Part A — Number recursion ======================================

# Q1 — Sum 1..n recursively. Base case: sum_to_n(0) = ? . O(n) time, O(n) stack.
def sum_to_n(n):
    # your code here
    pass


# Q2 — Nth Fibonacci (fib(0)=0, fib(1)=1). Needs TWO base cases.
def fib(n):
    # your code here
    pass


# Q3 — Sum of digits recursively (n >= 0). Last digit n%10, rest n//10.
def sum_digits(n):
    # your code here
    pass


# Q4 — x^n recursively (n >= 0). No ** , no loop. Base case: power(x, 0) = ?
def power(x, n):
    # your code here
    pass


# Q5 — [1, 2, ..., n] built recursively.
def naturals(n):
    # your code here
    pass


# ===== Part B — String & array recursion ==============================

# Q6 — Reverse a string recursively (no slicing/loop).
def reverse_string(s):
    # your code here
    pass


# Q7 — GCD recursively (Euclid). Base case: b == 0.
def gcd(a, b):
    # your code here
    pass


# Q8 — Sum of a list recursively (no sum()/loop). first + rest.
def array_sum(a):
    # your code here
    pass


# Q9 — Palindrome check recursively (compare ends, recurse on middle).
def is_palindrome(s):
    # your code here
    pass


# Q10 — Binary search recursively on a SORTED list -> index or -1.
#       Track low/high with a helper or default params.
def binary_search(a, target):
    # your code here
    pass


# ===== Stretch ⭐ ======================================================

# Q11 (⭐) — Fast power in O(log n): even -> (x^(n/2))**2 ; odd -> x * x^(n-1).
def fast_power(x, n):
    # your code here
    pass


# Q12 (⭐) — Tower of Hanoi: return list of (from, to) moves.
#           move n-1 to aux, move big disk to target, move n-1 to target.
def hanoi(n, source, target, aux):
    # your code here
    pass


# ======================================================================
# TEST HARNESS — do not edit below. Just run the file.
# ======================================================================
def _run_tests():
    suites = [
        ("Q1  sum_to_n", sum_to_n, [
            ((5,), 15), ((1,), 1), ((0,), 0), ((10,), 55)]),
        ("Q2  fib", fib, [
            ((0,), 0), ((1,), 1), ((6,), 8), ((10,), 55)]),
        ("Q3  sum_digits", sum_digits, [
            ((145,), 10), ((0,), 0), ((7,), 7), ((10000,), 1)]),
        ("Q4  power", power, [
            ((2, 10), 1024), ((5, 0), 1), ((3, 3), 27)]),
        ("Q5  naturals", naturals, [
            ((5,), [1, 2, 3, 4, 5]), ((1,), [1]), ((0,), [])]),
        ("Q6  reverse_string", reverse_string, [
            (("hello",), "olleh"), (("",), ""), (("a",), "a")]),
        ("Q7  gcd", gcd, [
            ((12, 18), 6), ((17, 5), 1), ((9, 0), 9)]),
        ("Q8  array_sum", array_sum, [
            (([1, 2, 3, 4],), 10), (([],), 0), (([5],), 5)]),
        ("Q9  is_palindrome", is_palindrome, [
            (("racecar",), True), (("hello",), False), (("a",), True), (("",), True)]),
        ("Q10 binary_search", binary_search, [
            (([1, 3, 5, 7, 9], 7), 3), (([1, 3, 5], 4), -1), (([], 1), -1)]),
        ("Q11 fast_power (stretch)", fast_power, [
            ((2, 10), 1024), ((3, 0), 1), ((2, 13), 8192)]),
        ("Q12 hanoi (stretch)", hanoi, [
            ((1, "A", "C", "B"), [("A", "C")]),
            ((2, "A", "C", "B"), [("A", "B"), ("A", "C"), ("B", "C")])]),
    ]

    total_q, passed_q = 0, 0
    print("=" * 62)
    print("  DAY 6 PLAYGROUND — SELF CHECK")
    print("=" * 62)
    for name, fn, cases in suites:
        total_q += 1
        results, all_ok = [], True
        for args, expected in cases:
            call_args = tuple(x[:] if isinstance(x, list) else x for x in args)
            try:
                got = fn(*call_args)
                ok = got == expected
            except Exception as e:
                got, ok = f"ERROR({type(e).__name__})", False
            results.append((args, expected, got, ok))
            all_ok = all_ok and ok
        passed_q += all_ok
        print(f"\n[{'PASS' if all_ok else 'FAIL'}] {name}")
        if not all_ok:
            for args, expected, got, ok in results:
                if not ok:
                    a = ", ".join(map(repr, args))
                    print(f"        {name.split()[1]}({a}) -> got {got!r}, expected {expected!r}")
    print("\n" + "=" * 62)
    print(f"  SCORE: {passed_q}/{total_q} questions fully passing")
    print("=" * 62)
    print("  All green -> ask for the review." if passed_q == total_q
          else "  Keep going. Fix the FAILs, re-run, repeat.")


if __name__ == "__main__":
    _run_tests()
