"""
Day 1 - Reference Solutions (Python)
Complexity + I/O warm-up.

These are clean reference versions. Try your own first (Day01_problems.py),
then compare. Run this file to confirm all tests pass:  python3 Day01_solutions.py
"""


# Q1. Sum of first N natural numbers -- two ways.
def sum_n_loop(n: int) -> int:        # O(n)
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_n_formula(n: int) -> int:     # O(1)
    return n * (n + 1) // 2


# Q2. Reverse a number (stays a number, drops leading zeros).
def reverse_number(n: int) -> int:    # O(d) where d = number of digits
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return sign * rev


# Q3. Count digits.
def count_digits(n: int) -> int:
    return len(str(abs(n))) if n != 0 else 1


# Q4. Max & min in one pass -- O(n).
def max_min(arr):
    mx = mn = arr[0]
    for x in arr[1:]:
        if x > mx:
            mx = x
        if x < mn:
            mn = x
    return mx, mn


# Q5. Swap two numbers.
def swap(a, b):
    a, b = b, a
    return a, b


# Q6. Even or odd.
def even_odd(n: int) -> str:
    return "Even" if n % 2 == 0 else "Odd"


# Q7. Sum of digits.
def sum_of_digits(n: int) -> int:
    n = abs(n)
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


# Q8. Count evens and odds in a list.
def count_even_odd(arr):
    even = sum(1 for x in arr if x % 2 == 0)
    return even, len(arr) - even


# Q9. Multiplication table (returns list of lines so it's testable).
def mult_table(n: int):
    return [f"{n} x {i} = {n * i}" for i in range(1, 11)]


# Q10. Power of two.
def is_power_of_two(n: int) -> str:
    if n < 1:
        return "No"
    while n % 2 == 0:
        n //= 2
    return "Yes" if n == 1 else "No"


# ----------------------- tests -----------------------
def _run_tests():
    assert sum_n_loop(5) == 15 and sum_n_formula(5) == 15
    assert sum_n_loop(10) == 55 and sum_n_formula(10) == 55
    assert sum_n_loop(1) == 1

    assert reverse_number(1234) == 4321
    assert reverse_number(100) == 1          # leading zeros dropped
    assert reverse_number(7) == 7
    assert reverse_number(-120) == -21       # sign preserved

    assert count_digits(1234) == 4
    assert count_digits(0) == 1
    assert count_digits(-55) == 2            # minus not counted

    assert max_min([3, 7, 1, 9, 4]) == (9, 1)
    assert max_min([-2, -8, -1, -5]) == (-1, -8)
    assert max_min([42]) == (42, 42)

    assert swap(3, 7) == (7, 3)

    assert even_odd(4) == "Even" and even_odd(7) == "Odd" and even_odd(0) == "Even"

    assert sum_of_digits(1234) == 10
    assert sum_of_digits(99) == 18
    assert sum_of_digits(0) == 0

    assert count_even_odd([1, 2, 3, 4, 5]) == (2, 3)
    assert count_even_odd([2, 4, 6, 8]) == (4, 0)

    assert mult_table(5)[0] == "5 x 1 = 5"
    assert mult_table(5)[9] == "5 x 10 = 50"

    assert is_power_of_two(16) == "Yes"
    assert is_power_of_two(12) == "No"
    assert is_power_of_two(1) == "Yes"

    print("All Day-1 tests passed.")


if __name__ == "__main__":
    _run_tests()
