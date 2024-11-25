def gcd(a , b):
    while b != 0:
        r = a % b
        a = b
        b = r

    if b == 0:
        return a



print("The GCD is: ", gcd(48, 18) )

