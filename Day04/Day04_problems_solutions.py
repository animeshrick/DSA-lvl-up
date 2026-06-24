"""
Day 4 — Strings + Search & Two Pointers  ::  PLAYGROUND
======================================================
Fill each stub, then run:

    python Day04_problems_solutions.py

The harness checks your answers (PASS / FAIL / ERROR) and prints a score.

RULES:
  - State TIME and SPACE complexity in a comment above EVERY function.
  - Hints name the technique only — derive the code yourself.
  - Solutions only when you ask. Reviews are honest but kind, with a nudge on any failure.

New techniques today:
  - Binary search: works on a SORTED list, keep low/high bounds, check the middle,
    throw away half each step -> O(log n).
  - Two pointers: two indices that move based on a condition (often one from each end).
"""

# ===== Part A — Strings ===============================================

# Q1 — Reverse a string. Two-pointer swap on a list of chars (not just s[::-1]).
def reverse_string(s):
    # your code here
    pass


# Q2 — Palindrome string. Two pointers from both ends.
def is_palindrome_str(s):
    # your code here
    pass


# Q3 — (vowels, consonants). Count only letters; y counts as a consonant.
def count_vowels_consonants(s):
    # your code here
    pass


# Q4 — Count words in a sentence. Watch extra/leading/trailing spaces.
def count_words(s):
    # your code here
    pass


# Q5 — Toggle case: swap upper<->lower per letter, leave others alone.
def toggle_case(s):
    # your code here
    pass


# Q6 — Remove duplicate characters, keep first occurrence order.
def remove_dups(s):
    # your code here
    pass


# Q7 — First character appearing exactly once, else None. Frequency dict helps.
def first_non_repeat(s):
    # your code here
    pass


# ===== Part B — Search & Two Pointers =================================

# Q8 — Linear search: index of target, else -1. O(n).
def linear_search(a, target):
    # your code here
    pass


# Q9 — Binary search on a SORTED list: index of target, else -1. Required O(log n).
def binary_search(a, target):
    # your code here
    pass


# Q10 — Pair with given sum in a SORTED list: (i, j) with i<j, else None.
#       Two pointers from both ends. O(n).
def pair_sum(a, target):
    # your code here
    pass


# ===== Stretch ⭐ ======================================================

# Q11 (⭐) — Remove duplicates from a SORTED array in place; return count of uniques.
#           Two pointers (slow write index, fast read index). O(n)/O(1).
def remove_duplicates_sorted(a):
    # your code here
    pass


# Q12 (⭐) — Reverse the ORDER of words in a sentence (collapse to single spaces).
def reverse_words(s):
    # your code here
    pass


# ======================================================================
# TEST HARNESS — do not edit below. Just run the file.
# ======================================================================
def _run_tests():
    suites = [
        ("Q1  reverse_string", reverse_string, [
            (("hello",), "olleh"), (("",), ""), (("a",), "a")]),
        ("Q2  is_palindrome_str", is_palindrome_str, [
            (("racecar",), True), (("hello",), False), (("a",), True), (("",), True)]),
        ("Q3  count_vowels_consonants", count_vowels_consonants, [
            (("hello",), (2, 3)), (("xyz",), (0, 3)), (("aei",), (3, 0))]),
        ("Q4  count_words", count_words, [
            (("hello world",), 2), (("  one  two  three ",), 3), (("",), 0)]),
        ("Q5  toggle_case", toggle_case, [
            (("Hello World",), "hELLO wORLD"), (("abc123",), "ABC123")]),
        ("Q6  remove_dups", remove_dups, [
            (("aabbcc",), "abc"), (("abcabc",), "abc"), (("",), "")]),
        ("Q7  first_non_repeat", first_non_repeat, [
            (("aabbc",), "c"), (("aabb",), None), (("abc",), "a")]),
        ("Q8  linear_search", linear_search, [
            (([4, 2, 7, 1], 7), 2), (([1, 2, 3], 5), -1)]),
        ("Q9  binary_search", binary_search, [
            (([1, 3, 5, 7, 9], 7), 3), (([1, 3, 5], 4), -1), (([], 1), -1)]),
        ("Q10 pair_sum", pair_sum, [
            (([1, 2, 4, 7, 11], 6), (1, 2)), (([1, 2, 3], 100), None), (([1, 2], 3), (0, 1))]),
        ("Q11 remove_duplicates_sorted (stretch)", remove_duplicates_sorted, [
            (([1, 1, 2, 3, 3],), 3), (([],), 0), (([1, 2, 3],), 3)]),
        ("Q12 reverse_words (stretch)", reverse_words, [
            (("hello world",), "world hello"),
            (("the sky is blue",), "blue is sky the"),
            (("single",), "single")]),
    ]

    total_q, passed_q = 0, 0
    print("=" * 62)
    print("  DAY 4 PLAYGROUND — SELF CHECK")
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
