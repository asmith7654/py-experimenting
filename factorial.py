def whileFactorial(num: int) -> int:
    output = num
    while num>1:
       num -= 1
       output *= (num)

    return output

def forFactorial(num: int) -> int:
    if num<=1:
        return num
    
    output = num
    for newNum in range(num-1,0,-1):
        if newNum<=1:
            return output
        else:
            output *= newNum


print(whileFactorial(1))
print(whileFactorial(2))
print(whileFactorial(3))
print(whileFactorial(4))
print(whileFactorial(5))

print(forFactorial(1))
print(forFactorial(2))
print(forFactorial(3))
print(forFactorial(4))
print(forFactorial(5))
