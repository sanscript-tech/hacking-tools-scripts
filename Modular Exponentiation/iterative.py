def modular_exponentiation(base, power, modulus_to):
    """This function uses the iterative approach to
       perform modular exponentiation.

    Args:
        base (int): The number used for the base value of the expression.
        power (int): The number choosed for power value of the expression.
        modulus_to (int): The number used to take modulus of the expression.

    Returns:
        result(int): The evaluated value of modular exponentiaion.
    """
    result = 1
    base %= modulus_to

    while (power > 0):

        # To perform operation accordingly for odd and even powers
        if ((power & 1) == 1):
            result = (result * base) % modulus_to

        power = power//2
        base = (base ** 2) % modulus_to

    return result


if __name__ == "__main__":
    base = int(input("Enter the base number: "))
    power = int(input("Enter the power number: "))
    modulus_to = int(
        input("Enter the number which is used to perform modulus operation: "))
    print(f"The result is {modular_exponentiation(base, power, modulus_to)}")
