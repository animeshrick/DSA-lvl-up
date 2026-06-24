"""
Day 3 — Arrays + Hashing (Dictionaries)  ::  PLAYGROUND
=======================================================
Fill in each function, then run:

    python Day03_problems_solutions.py

The harness auto-checks your answers (PASS / FAIL / ERROR) and prints a score.
Goal: all green before you ask for the review.

LEVEL-UP RULES:
  - State TIME and SPACE complexity in a comment above EVERY function.
  - In-place where required (Q4, Q5, Q7) -> O(1) extra space.
  - Use a dict/set to reach O(n) on Q10-Q13. No nested loops there.
  - hints only, no solutions from me until you ask. Reviews are blunt.

Idioms you should use today:
    a[i], a[j] = a[j], a[i]      # in-place swap, two pointers
    d[k] = d.get(k, 0) + 1       # frequency count
    seen = set()                 # O(1) membership
"""

# ===== Part A — Number Theory II warm-up ==============================

# Q1 — GCD (Euclidean). a,b = b, a%b until b==0.  O(log min(a,b)) time, O(1) space.
def gcd(a, b):
    # your code here
    pass


# Q2 — LCM via a*b // gcd(a,b).  Reuse gcd.
def lcm(a, b):
    # your code here
    pass


# Q3 — First n Fibonacci numbers as a list. fib(0)->[], fib(1)->[0].
def fib(n):
    # your code here
    pass


# ===== Part B — Arrays ================================================

# Q4 — Reverse array IN PLACE (two pointers). No slicing/reversed(). O(n)/O(1).
def reverse_arr(a):
    # your code here
    pass


# Q5 — (max, min) in ONE pass. No sorted()/max()/min(). O(n)/O(1).
def max_min(a):
    # your code here
    pass


# Q6 — Second largest DISTINCT value, else None. One pass.
def second_largest(a):
    # your code here
    pass


# Q7 — Move all zeros to the end IN PLACE, keep order. O(n)/O(1).
def move_zeros(a):
    # your code here
    pass


# Q8 — Missing number from a permutation of 1..n (len(a)=n-1).
#      Use n*(n+1)//2 - sum(a)  or XOR. O(n)/O(1).
def missing_number(a):
    # your code here
    pass


# Q9 — Rotate array RIGHT by k. Handle k > len(a) with k %= len(a).
def rotate(a, k):
    # your code here
    pass


# ===== Part C — Hashing / Dictionaries ================================

# Q10 — Frequency count -> dict {value: count}. O(n).
def freq_count(a):
    # your code here
    pass


# Q11 — Two Sum: return (i, j), i<j, with a[i]+a[j]==target. O(n) using a dict.
def two_sum(a, target):
    # your code here
    pass


# Q12 — First element appearing exactly once, else None. dict + 2nd pass.
def first_unique(a):
    # your code here
    pass


# ===== Stretch ⭐ ======================================================

# Q13 (⭐) — Valid anagram of two strings. Frequency dict / Counter. O(n).
def is_anagram(s, t):
    # your code here
    pass


# Q14 (⭐) — Majority element (> n//2 times, exists). Boyer-Moore -> O(n)/O(1).
def majority(a):
    # your code here
    pass


# Q15 (⭐⭐) — Longest substring without repeating chars. Sliding window. O(n).
def longest_unique(s):
    # your code here
    pass


# ======================================================================
# TEST HARNESS — do not edit below. Just run the file.
# ======================================================================
def _run_tests():
    suites = [
        ("Q1  gcd", gcd, [
            ((12, 18), 6), ((17, 5), 1), ((0, 9), 9), ((100, 10), 10)]),
        ("Q2  lcm", lcm, [
            ((4, 6), 12), ((3, 5), 15), ((12, 18), 36)]),
        ("Q3  fib", fib, [
            ((0,), []), ((1,), [0]), ((7,), [0, 1, 1, 2, 3, 5, 8])]),
        ("Q4  reverse_arr", reverse_arr, [
            (([1, 2, 3, 4],), [4, 3, 2, 1]), (([],), []), (([9],), [9])]),
        ("Q5  max_min", max_min, [
            (([3, 7, 1, 9, 4],), (9, 1)), (([-2, -8, -1, -5],), (-1, -8)), (([5],), (5, 5))]),
        ("Q6  second_largest", second_largest, [
            (([3, 7, 1, 9, 4],), 7), (([5, 5, 5],), None), (([2, 2, 3],), 2)]),
        ("Q7  move_zeros", move_zeros, [
            (([0, 1, 0, 3, 12],), [1, 3, 12, 0, 0]), (([0, 0],), [0, 0]), (([1, 2, 3],), [1, 2, 3])]),
        ("Q8  missing_number", missing_number, [
            (([1, 2, 4, 5],), 3), (([2, 3, 1, 5],), 4), (([2],), 1)]),
        ("Q9  rotate", rotate, [
            (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]), (([1, 2, 3], 4), [3, 1, 2]), (([1], 3), [1])]),
        ("Q10 freq_count", freq_count, [
            (([1, 2, 2, 3, 3, 3],), {1: 1, 2: 2, 3: 3}), (([],), {})]),
        ("Q11 two_sum", two_sum, [
            (([2, 7, 11, 15], 9), (0, 1)), (([3, 2, 4], 6), (1, 2))]),
        ("Q12 first_unique", first_unique, [
            (([4, 5, 4, 6, 5, 7],), 6), (([1, 1, 2, 2],), None)]),
        ("Q13 is_anagram (stretch)", is_anagram, [
            (("listen", "silent"), True), (("rat", "car"), False), (("a", "ab"), False)]),
        ("Q14 majority (stretch)", majority, [
            (([3, 3, 4, 2, 3, 3, 3],), 3), (([1, 1, 1, 2],), 1)]),
        ("Q15 longest_unique (stretch)", longest_unique, [
            (("abcabcbb",), 3), (("bbbbb",), 1), (("pwwkew",), 3), (("",), 0)]),
    ]

    total_q, passed_q = 0, 0
    print("=" * 62)
    print("  DAY 3 PLAYGROUND — SELF CHECK")
    print("=" * 62)
    for name, fn, cases in suites:
        total_q += 1
        results, all_ok = [], True
        for args, expected in cases:
            # copy list args so in-place funcs don't corrupt later checks
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
