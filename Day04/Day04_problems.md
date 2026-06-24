# Day 4 — Strings + Search & Two Pointers

**Date (plan):** 2026-06-25 · **Language:** Python · **Time:** ~2–3 hrs
**Difficulty:** ADVANCE — assuming Day 3 scored ~50, so this nudges up one notch (not a big jump).
We add **strings** (the next big service-company topic) and two new techniques: **binary search**
and the **two-pointer** pattern.
**10 core questions (Q1–Q10) + 2 stretch (⭐).**

> Rules: hints name the technique only — no code handed over. Reviews are honest but kind, and
> on any failure you get a small nudge toward the fix. Solutions only when you ask.
> Keep stating time + space complexity above each function — good habit, keep it going.

---

## Concept primer (quick read)

### Strings in Python
A string is like a read-only list of characters.
- `s[i]` reads a character; `s[::-1]` reverses (but some problems ask you to do it manually).
- Strings are **immutable** — you can't change `s[i]`; you build a new string or work with a list of chars.
- `s.split()` breaks a sentence into words; `s.lower()`, `s.upper()`, `.isalpha()`, `.isvowel`(no — check membership in `"aeiou"`).

### Binary search (the new technique)
Only works on a **sorted** list. You repeatedly look at the middle element and throw away half:
if the middle is too small, the answer must be in the right half; too big, the left half.
This is why it's **O(log n)** instead of O(n). The whole game is keeping two bounds (`low`, `high`)
and moving them toward each other.

### Two pointers (the other new technique)
Keep two indices and move them based on a condition — often one at each end moving inward
(great on sorted arrays), or both moving forward at different speeds. Turns many O(n²) brute
forces into O(n).

---

## Part A — Strings

### Q1 ✅ — Reverse a string  →  `reverse_string(s) -> str`
Return the reversed string. Try it with the **two-pointer idea** (swap ends inward on a list of
chars), not just `s[::-1]`.
- `reverse_string("hello")→"olleh"`, `reverse_string("")→""`, `reverse_string("a")→"a"`.

### Q2 ✅ — Palindrome string  →  `is_palindrome_str(s) -> bool`
True if the string reads the same forwards and backwards. Two pointers from both ends.
- `is_palindrome_str("racecar")→True`, `is_palindrome_str("hello")→False`, `is_palindrome_str("a")→True`, `is_palindrome_str("")→True`.

### Q3 ✅ — Count vowels and consonants  →  `count_vowels_consonants(s) -> tuple`
Return `(vowels, consonants)`. Count only alphabetic characters; treat `y` as a consonant.
- `count_vowels_consonants("hello")→(2, 3)`, `count_vowels_consonants("xyz")→(0, 3)`, `count_vowels_consonants("aei")→(3, 0)`.

### Q4 ✅ — Count words in a sentence  →  `count_words(s) -> int`
Number of words. Mind extra/leading/trailing spaces.
- `count_words("hello world")→2`, `count_words("  one  two  three ")→3`, `count_words("")→0`.

### Q5 ✅ — Toggle case  →  `toggle_case(s) -> str`
Swap upper↔lower for each letter; leave non-letters alone.
- `toggle_case("Hello World")→"hELLO wORLD"`, `toggle_case("abc123")→"ABC123"`.

### Q6 ✅ — Remove duplicate characters (keep order)  →  `remove_dups(s) -> str`
Keep only the first occurrence of each character, in order.
- `remove_dups("aabbcc")→"abc"`, `remove_dups("abcabc")→"abc"`, `remove_dups("")→""`.

### Q7 ✅ — First non-repeating character  →  `first_non_repeat(s) -> str | None`
First character that appears exactly once; None if there isn't one. (A frequency dict helps.)
- `first_non_repeat("aabbc")→"c"`, `first_non_repeat("aabb")→None`, `first_non_repeat("abc")→"a"`.

---

## Part B — Search & Two Pointers

### Q8 ✅ — Linear search  →  `linear_search(a, target) -> int`
Return the index of target, or -1 if absent. O(n).
- `linear_search([4,2,7,1], 7)→2`, `linear_search([1,2,3], 5)→-1`.

### Q9 ✅ — Binary search (iterative)  →  `binary_search(a, target) -> int`
`a` is **sorted ascending**. Return the index of target, or -1. **Required: O(log n)** — keep
`low`/`high` bounds, check the middle, discard half each step.
- `binary_search([1,3,5,7,9], 7)→3`, `binary_search([1,3,5], 4)→-1`, `binary_search([], 1)→-1`.

### Q10 ✅ — Pair with given sum (sorted)  →  `pair_sum(a, target) -> tuple | None`
`a` is sorted ascending. Return indices `(i, j)`, `i < j`, of two values that add to target;
None if no such pair. **Use two pointers** (one at each end), O(n) — not a double loop.
- `pair_sum([1,2,4,7,11], 6)→(1, 2)`, `pair_sum([1,2,3], 100)→None`, `pair_sum([1,2], 3)→(0, 1)`.

---

## Stretch ⭐

### Q11 ⭐ — Remove duplicates from sorted array (in place)  →  `remove_duplicates_sorted(a) -> int`
`a` is sorted. Move unique values to the front in order and return the count of uniques.
Two pointers (a slow "write" index, a fast "read" index). O(n)/O(1).
- `remove_duplicates_sorted([1,1,2,3,3])→3`, `remove_duplicates_sorted([])→0`, `remove_duplicates_sorted([1,2,3])→3`.

### Q12 ⭐ — Reverse words in a sentence  →  `reverse_words(s) -> str`
Reverse the order of words (not the letters). Collapse to single spaces.
- `reverse_words("hello world")→"world hello"`, `reverse_words("the sky is blue")→"blue is sky the"`, `reverse_words("single")→"single"`.

---

## How to use the playground
Open **`Day04_problems_solutions.py`**, fill the stubs, run:

```
python Day04_problems_solutions.py
```

PASS/FAIL per question + a score. Get the core green before asking for review.

## Submission checklist
- [ ] Complexity (time + space) noted above each function.
- [ ] Binary search is O(log n) (bounds + middle), not a linear scan.
- [ ] Two pointers used on Q10/Q11 — no nested loops.
- [ ] Edge cases: empty string/list, single element, no match (-1 / None), extra spaces.
- [ ] Harness core all PASS.
- [ ] Logged time + confidence in the tracker.
