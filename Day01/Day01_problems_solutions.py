print("qs.1")
def question1(n:int):
    result = 0
    for i in range(0, n+1):
        result = result + i
    return result

print(question1(10))

print("qs.2")
def question2(n:str) -> int :
    rev = int(str(n)[::-1]) 
    return rev

print(question2("110998"))

print("qs.3")
def question3(n:int):
    return len(str(abs(n)))

print(question3(1000))

print("qs.4")
def question4(n):
    sorted_n = sorted(n)
    min = sorted_n[0]
    max = sorted_n[-1]
    return max, min

print(question4([3, 7, 1, 9, 4]))
print(question4([-2, -8, -1, -5]))

print("qs.5")
def question5(a,b):
    c = a
    a = b
    b = c
    return a, b
def question_5(a,b):
    a, b = b, a
    return a, b

print(question5(4,5))
print(question_5(3,5))

print("qs.6")
def question6(a:int):
    calculation = a % 2
    if calculation == 0:
        return "Even"
    else:
        return "Odd"

print(question6(4))

print("qs.7")
def question7(a: int):
    sum_result = 0
    for i in a:
        sum_result += i
    return sum_result
def sum_of_digits(n: int) -> int:
    n = abs(n)
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

print(question7(145))
print(sum_of_digits(145))

print("qs.8")
def question8(a):
    even, odd = 0, 0
    for i in a:
        res = question6(i)
        if res == "Even":
            even += 1
        elif res == "Odd":
            odd += 1
    return (even, odd)

print(question8([1, 2, 3, 4, 5]))


print("qs.9")
def question9(a):
    res = 0
    for i in range(10):
        res = a * i
    return f"The factorial of {a} is {res}"

print(question9(5))

print("qs.10")
def question10(a):
    res = a % 2 == 0
    if res:
        print("Yes")
    else:
        print("No")

print(question10(5))

