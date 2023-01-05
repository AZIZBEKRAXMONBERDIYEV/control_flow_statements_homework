def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    if a > 0 and b > 0 and c > 0 :
        n = 3
    if (a > 0 and b > 0 and c < 0) or (a < 0 and b > 0 and c > 0) or (a > 0 and b < 0 and c > 0) :
        n = 2
    if (a > 0 and b < 0 and c < 0) or (a < 0 and b > 0 and c < 0) or (a < 0 and b < 0 and c > 0) :
        n = 1
    if a < 0 and b < 0 and c < 0 :
        n = 0
    if a > 0 and b > 0 and c > 0 :
        i = 0
    if (a > 0 and b > 0 and c < 0) or (a < 0 and b > 0 and c > 0) or (a > 0 and b < 0 and c > 0) :
        i = 1
    if (a > 0 and b < 0 and c < 0) or (a < 0 and b > 0 and c < 0) or (a < 0 and b < 0 and c > 0) :
        i = 2
    if a < 0 and b < 0 and c < 0 :
        i = 3
    return i,n
print(main(1,2,-3))