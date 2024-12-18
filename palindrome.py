def palindromeCheck(input: str) -> bool:
    decrementer = -1
    middleOfWord = round(len(input)/2)
    #loop through middle of word because decrementer is looping backwards at same rate as x
    for x in range(0,middleOfWord):
        if(input[x] == input[decrementer]):
            decrementer -= 1
        else:
            return False
        
    return True

print(palindromeCheck("racecar"))
print(palindromeCheck("hello"))
print(palindromeCheck(""))
print(palindromeCheck("o1o1o"))