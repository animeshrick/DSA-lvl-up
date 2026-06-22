print("qs.1")
def q1(n: int)-> int:
    return n % 10
print(f"q1 --> {q1(1234)}")

print("qs.2")
def q2(n: int)-> int:
    sum = 0
    n = 0
    while n > 0:
        sum += n%10
        n //= 10
    return sum
print(f"q2 --> {q2(1234)}")

# print("qs.3")
# def q3(n: int)-> int:
#     res = 0
#     while n > 0:
#         d = n%10
#         res = n * d
#     return res
# print(f"q3 --> {q3(1234)}")

print("qs.6")
def q6(n: int, d: int)-> int:
    # | `122232, 2` | `4` |
    count = 0
    for i in str(n):
        if d in i:
            count += 1
    return count
print(f"q6 --> {q6(122232, 2)}")