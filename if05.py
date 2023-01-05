def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    if a > 0 and b > 0 and c > 0 :
        i = 0
    if (a > 0 and b > 0 and c < 0) or (a < 0 and b > 0 and c > 0) or (a > 0 and b < 0 and c > 0) :
        i = 1
    if (a > 0 and b < 0 and c < 0) or (a < 0 and b > 0 and c < 0) or (a < 0 and b < 0 and c > 0) :
        i = 2
    if a < 0 and b < 0 and c < 0 :
        i = 3
        
    return i
print(main(6,4,-5))