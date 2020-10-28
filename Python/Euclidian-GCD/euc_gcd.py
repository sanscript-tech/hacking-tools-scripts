import sys

if len(sys.argv) < 3:
    print("Missing required number of commandline arguments.")
    sys.exit()


def euclidean_gcd(a, b):

    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = euclidean_gcd(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y

a = int(sys.argv[1])
b = int(sys.argv[2])

gcd, x, y = euclidean_gcd(a, b)

print(f"GCD of {a} and {b} is: {gcd}")
print(f"{a}*{x} + {b}*{y} = {gcd} [i.e gcd({a}, {b})]")
