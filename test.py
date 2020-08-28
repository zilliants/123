def high_and_low(numbers):
    numbers = [int(i) for i in numbers.split()]
    a = max(numbers)
    b = min(numbers)
    numbers = str(a)+' '+str(b)
    return numbers


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))