def primeChecker1(num: int) -> bool:
    if num<=1 or (not isinstance(num, int)):
        return False

    divisor = 2
    while divisor < (round(num/2)):
        if num%divisor==0:
            return False
        else:
            divisor += 1

    return True

def primeChecker2(num: int) -> bool:
    if num<=1 or (not isinstance(num, int)):
        return False

    #check if even first
    if num%2==0:
        return False

    #now divide by incrementing value that skips all evens, improving efficiency to O(n/4) from 0(n/2)
    divisor = 3
    while divisor < num/2:
        if num%divisor==0:
            return False
        else:
            divisor += 2

    return True

print(primeChecker2(1000003))

