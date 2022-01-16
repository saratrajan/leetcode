def febDynamic(num, memoize):
    if(memoize[num] is not None):
        return memoize[num]
    elif(num <3):
        return 1
    else:
        result = febDynamic(num - 1, memoize) + febDynamic(num - 2, memoize)
    
    memoize[num] = result
    return result

def febMemo(num):
    memoize = [None] * (num + 1)
    return febDynamic(num, memoize)

print(febMemo(50))