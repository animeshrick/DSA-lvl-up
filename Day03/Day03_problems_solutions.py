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
  - Hints name the technique only — no formulas, no snippets. Derive the code yourself.
  - Solutions only when you ask. Reviews are blunt.
"""

# ===== Part A — Number Theory II warm-up ==============================

# Q1 — GCD. Euclidean algorithm. Target: O(log min(a,b)) time, O(1) space.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Q2 — LCM. Derive it from the GCD (there's a product identity).
def lcm(a, b):
    return a*b // gcd(a, b)


# Q3 — First n Fibonacci numbers as a list. fib(0)->[], fib(1)->[0]. O(n)/O(1).
def fib(n):
    result = []
    prev = 0
    current = 1
    for _ in range(0, n):
        result.append(prev)
        next = prev + current
        prev = current
        current = next
    return result


# ===== Part B — Arrays ================================================

# Q4 — Reverse array IN PLACE (two pointers). No slicing/reversed(). O(n)/O(1).
def reverse_arr(a):
    if len(a) == 0:
        return []
    left = 0
    right = abs(len(a) - 1)
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    return a


# Q5 — (max, min) in ONE pass. No sorted()/max()/min(). O(n)/O(1).
def max_min(a):
    max = min = a[0]
    for i in a:
        if min > i:
            min = i
        if max < i:
            max = i
    return max, min


# Q6 — Second largest DISTINCT value, else None. One pass.
def second_largest(a):
    a = sorted(set(a))
    if len(a) < 2:
        return None
    else:
        return a[-2]


# Q7 — Move all zeros to the end IN PLACE, keep order. O(n)/O(1).
def move_zeros(a):
    pos = 0
    for i in a:
        if i!=0:
            # print("a[pos]", a[pos])
            a[pos] = i
            pos+=1
            # print("pos", pos)
    for j in range(pos, len(a)): 
        a[j] = 0.
    return a


# Q8 — Missing number from a permutation of 1..n (len(a)=n-1).
#      Think: a sum identity, or XOR. Target O(n)/O(1).
def missing_number(a):
    n = len(a) + 1
    expected_sum = n * (n + 1) // 2
    missing = expected_sum - sum(a)
    return missing


# Q9 — Rotate array RIGHT by k. Remember k can be larger than len(a).
def rotate(a, k):
    if len(a) < k:
        return a
    
    sub_arr = a[k+1:len(a)]
    for i in sub_arr:
        a.remove(i)
    a = sub_arr + a
    return a
# Note: rotate([1, 2, 3], 4) -> got [1, 2, 3], expected [3, 1, 2] --> not clear the example


# ===== Part C — Hashing / Dictionaries ================================

# Q10 — Frequency count -> dict {value: count}. O(n).
def freq_count(a):
    count_map = {}
    for num in a:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
    return count_map


# Q11 — Two Sum: return (i, j), i<j, with a[i]+a[j]==target. Hashing -> O(n).
def two_sum(a, target):
    for i in range(len(a)):
        sum = a[i] + a[i+1]
        if sum == target:
            return (i, i+1)


# Q12 — First element appearing exactly once, else None. Hashing -> O(n).
def first_unique(a):
    result = freq_count(a)
    data = None
    for key, value in result.items():
        # print("key:", key, "value:", value)
        if value == 1:
            data = key
            break
    return data

# ===== Stretch ⭐ ======================================================

# Q13 (⭐) — Valid anagram of two strings. Frequency dict / Counter. O(n).
def is_anagram(s, t):
    # your code here
    pass


# Q14 (⭐) — Majority element (> n//2 times, exists). Boyer-Moore -> O(n)/O(1).
def majority(a):
    res = freq_count(a)
    max_key = max(res, key=res.get)
    return max_key


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
