# Day 5 — Sorting (Basics + Applications)

**Date (plan):** 2026-06-26 · **Language:** Python · **Time:** ~2–3 hrs
**Difficulty:** continues the climb — you've done search and two pointers, now sorting.
**10 core questions (Q1–Q10) + 2 stretch (⭐).**

> Rules: hints name the technique only — no code handed over. Reviews are honest but kind,
> with a small nudge on any failure. Solutions only when you ask.
> Keep stating time + space complexity above each function.

---

## Concept primer (quick read)

### Why learn the sorts by hand
You'll almost always use Python's built-in `sorted()` in real problems (it's O(n log n)).
But interviewers ask you to *implement* bubble/selection/insertion to check you understand
loops, swaps, and complexity. So: implement them once, understand them, then in application
problems you're free to use `sorted()`.

### The three basic sorts (all O(n²), all O(1) space)
- **Bubble sort:** repeatedly walk the list swapping adjacent out-of-order pairs; the biggest
  value "bubbles" to the end each pass.
- **Selection sort:** each pass, find the smallest of the remaining items and put it in place.
- **Insertion sort:** grow a sorted region at the front, inserting each new item into its spot
  (like sorting playing cards in your hand).

### Know the complexities (interviewers ask)
| Algorithm | Time (avg/worst) | Space | Stable? |
|---|---|---|---|
| Bubble / Selection / Insertion | O(n²) | O(1) | bubble & insertion yes, selection no |
| Merge sort | O(n log n) | O(n) | yes |
| Quick sort | O(n log n) avg, O(n²) worst | O(log n) | no |
| Python `sorted()` (Timsort) | O(n log n) | O(n) | yes |

---

## Part A — Implement the basic sorts (return a NEW sorted list, ascending)

### Q1 ✅ — Bubble sort  →  `bubble_sort(a) -> list`
- `bubble_sort([5,1,4,2,8])→[1,2,4,5,8]`, `bubble_sort([])→[]`, `bubble_sort([3,3,1])→[1,3,3]`.

### Q2 ✅ — Selection sort  →  `selection_sort(a) -> list`
- Same examples as Q1.

### Q3 ✅ — Insertion sort  →  `insertion_sort(a) -> list`
- Same examples as Q1.

### Q4 ✅ — Is the array sorted?  →  `is_sorted(a) -> bool`
True if non-decreasing (ascending, ties allowed). One pass — compare each pair of neighbours.
- `is_sorted([1,2,2,3])→True`, `is_sorted([1,3,2])→False`, `is_sorted([])→True`, `is_sorted([5])→True`.

---

## Part B — Sorting applications

### Q5 ✅ — Sort an array of 0s, 1s, 2s  →  `sort_012(a) -> list`
Sort a list containing only 0, 1, 2. **Counting** (tally each, rebuild) is the simple O(n) way;
the Dutch-national-flag two-pointer version is the slick one.
- `sort_012([2,0,2,1,1,0])→[0,0,1,1,2,2]`, `sort_012([0])→[0]`, `sort_012([2,1,0])→[0,1,2]`.

### Q6 ✅ — Merge two sorted arrays  →  `merge_sorted(a, b) -> list`
Both inputs are sorted ascending; return one merged sorted list. **Two pointers**, O(n+m) — do
NOT just concatenate and re-sort.
- `merge_sorted([1,3,5],[2,4,6])→[1,2,3,4,5,6]`, `merge_sorted([],[1,2])→[1,2]`, `merge_sorted([1,2,3],[])→[1,2,3]`.

### Q7 ✅ — Kth smallest element  →  `kth_smallest(a, k) -> int`
Return the k-th smallest (k is 1-indexed). Sorting first is allowed here.
- `kth_smallest([7,10,4,3,20,15], 3)→7`, `kth_smallest([1,2,3], 1)→1`.

### Q8 ✅ — Kth largest element  →  `kth_largest(a, k) -> int`
Return the k-th largest (1-indexed).
- `kth_largest([7,10,4,3,20,15], 3)→10`, `kth_largest([1,2,3], 1)→3`.

### Q9 ✅ — Find duplicates  →  `find_duplicates(a) -> list`
Return a **sorted** list of the values that appear more than once. (A dict/Counter from Day 3
plus a sort.)
- `find_duplicates([1,2,2,3,3,3,4])→[2,3]`, `find_duplicates([1,2,3])→[]`, `find_duplicates([5,5,5])→[5]`.

### Q10 ✅ — Sort by frequency  →  `sort_by_frequency(a) -> list`
Return the elements ordered by **count descending**; for equal counts, by **value ascending**.
Each element appears as many times as its count.
- `sort_by_frequency([1,1,2,2,2,3])→[2,2,2,1,1,3]`, `sort_by_frequency([4,5,6,5,4,3])→[4,4,5,5,3,6]`.

---

## Stretch ⭐

### Q11 ⭐ — Merge sort  →  `merge_sort(a) -> list`
Recursive: split in half, sort each half, merge them (reuse Q6's merge idea). **O(n log n)**.
- `merge_sort([5,1,4,2,8])→[1,2,4,5,8]`, `merge_sort([])→[]`.

### Q12 ⭐ — Quick sort  →  `quick_sort(a) -> list`
Recursive: pick a pivot, partition into smaller/equal/greater, recurse. Average **O(n log n)**.
- `quick_sort([5,1,4,2,8])→[1,2,4,5,8]`, `quick_sort([3,3,1])→[1,3,3]`.

---

## How to use the playground
Open **`Day05_problems_solutions.py`**, fill the stubs, run:

```
python Day05_problems_solutions.py
```

PASS/FAIL per question + a score. Core all green before you ask for review.

## Submission checklist
- [ ] Complexity (time + space) noted above each function.
- [ ] Basic sorts implemented by hand (no `sorted()` in Q1–Q3).
- [ ] Q6 merges with two pointers (no concat-then-sort).
- [ ] Edge cases: empty list, single element, all-equal, k=1, k=len.
- [ ] Harness core all PASS.
- [ ] Logged time + confidence in the tracker.
