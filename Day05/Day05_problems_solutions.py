"""
Day 5 — Sorting (Basics + Applications)  ::  PLAYGROUND
======================================================
Fill each stub, then run:

    python Day05_problems_solutions.py

The harness checks your answers (PASS / FAIL / ERROR) and prints a score.

RULES:
  - State TIME and SPACE complexity in a comment above EVERY function.
  - Implement Q1-Q3 by hand (no sorted()). Applications (Q5+) may use sorted().
  - Hints name the technique only. Solutions only when you ask.
  - Reviews are honest but kind, with a nudge on any failure.

Reminders:
  - Bubble: swap adjacent out-of-order pairs, biggest bubbles to the end.
  - Selection: each pass pick the smallest remaining and place it.
  - Insertion: grow a sorted front, insert each new item into place.
  - In-place swap: a[i], a[j] = a[j], a[i]
"""

# ===== Part A — Basic sorts (return a NEW ascending list) =============

# Q1 — Bubble sort. O(n^2) time, O(1) extra space.
def bubble_sort(a):
    # your code here
    pass


# Q2 — Selection sort. O(n^2) time, O(1) extra space.
def selection_sort(a):
    # your code here
    pass


# Q3 — Insertion sort. O(n^2) time, O(1) extra space.
def insertion_sort(a):
    # your code here
    pass


# Q4 — Is the array non-decreasing (ascending, ties ok)? One pass.
def is_sorted(a):
    # your code here
    pass


# ===== Part B — Sorting applications ==================================

# Q5 — Sort a list of only 0s,1s,2s. Counting (tally + rebuild) is the simple O(n) way.
def sort_012(a):
    # your code here
    pass


# Q6 — Merge two SORTED lists into one sorted list. Two pointers, O(n+m).
def merge_sorted(a, b):
    # your code here
    pass


# Q7 — Kth smallest (k is 1-indexed). Sorting first is allowed.
def kth_smallest(a, k):
    # your code here
    pass


# Q8 — Kth largest (k is 1-indexed).
def kth_largest(a, k):
    # your code here
    pass


# Q9 — Sorted list of values that appear more than once. (dict/Counter + sort)
def find_duplicates(a):
    # your code here
    pass


# Q10 — Sort by count DESC, ties by value ASC. Each value repeats by its count.
def sort_by_frequency(a):
    # your code here
    pass


# ===== Stretch ⭐ ======================================================

# Q11 (⭐) — Merge sort (recursive). Split, sort halves, merge. O(n log n).
def merge_sort(a):
    # your code here
    pass


# Q12 (⭐) — Quick sort (recursive). Pivot, partition, recurse. O(n log n) avg.
def quick_sort(a):
    # your code here
    pass


# ======================================================================
# TEST HARNESS — do not edit below. Just run the file.
# ======================================================================
def _run_tests():
    basic = [(([5, 1, 4, 2, 8],), [1, 2, 4, 5, 8]), (([],), []), (([3, 3, 1],), [1, 3, 3])]
    suites = [
        ("Q1  bubble_sort", bubble_sort, basic),
        ("Q2  selection_sort", selection_sort, basic),
        ("Q3  insertion_sort", insertion_sort, basic),
        ("Q4  is_sorted", is_sorted, [
            (([1, 2, 2, 3],), True), (([1, 3, 2],), False), (([],), True), (([5],), True)]),
        ("Q5  sort_012", sort_012, [
            (([2, 0, 2, 1, 1, 0],), [0, 0, 1, 1, 2, 2]), (([0],), [0]), (([2, 1, 0],), [0, 1, 2])]),
        ("Q6  merge_sorted", merge_sorted, [
            (([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]),
            (([], [1, 2]), [1, 2]), (([1, 2, 3], []), [1, 2, 3])]),
        ("Q7  kth_smallest", kth_smallest, [
            (([7, 10, 4, 3, 20, 15], 3), 7), (([1, 2, 3], 1), 1)]),
        ("Q8  kth_largest", kth_largest, [
            (([7, 10, 4, 3, 20, 15], 3), 10), (([1, 2, 3], 1), 3)]),
        ("Q9  find_duplicates", find_duplicates, [
            (([1, 2, 2, 3, 3, 3, 4],), [2, 3]), (([1, 2, 3],), []), (([5, 5, 5],), [5])]),
        ("Q10 sort_by_frequency", sort_by_frequency, [
            (([1, 1, 2, 2, 2, 3],), [2, 2, 2, 1, 1, 3]),
            (([4, 5, 6, 5, 4, 3],), [4, 4, 5, 5, 3, 6])]),
        ("Q11 merge_sort (stretch)", merge_sort, [
            (([5, 1, 4, 2, 8],), [1, 2, 4, 5, 8]), (([],), [])]),
        ("Q12 quick_sort (stretch)", quick_sort, [
            (([5, 1, 4, 2, 8],), [1, 2, 4, 5, 8]), (([3, 3, 1],), [1, 3, 3])]),
    ]

    total_q, passed_q = 0, 0
    print("=" * 62)
    print("  DAY 5 PLAYGROUND — SELF CHECK")
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
