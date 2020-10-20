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
    result = 1 # Intial modular exponentiation result
    base %= modulus_to # Performing modulus on the base and assigning it back to the base.

    while (power > 0): # Looping over untill the value of power is more than 0.

        # To perform operation accordingly for odd and even powers.
        if ((power & 1) == 1): # To extract the lowest bit.
            result = (result * base) % modulus_to # For even power values we perform this.

        power = power//2 # For odd value of power.
        base = (base ** 2) % modulus_to # Repeatitive squaring of the base and performing modulus operation

    return result


if __name__ == "__main__":
    base = int(input("Enter the base number: "))
    power = int(input("Enter the power number: "))
    modulus_to = int(
        input("Enter the number which is used to perform modulus operation: "))
    print(f"The result is {modular_exponentiation(base, power, modulus_to)}")
