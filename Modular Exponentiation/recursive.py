def modular_exponentiation(base, power, modulus_to):
    """This function uses the recursive approach to
       perform modular exponentiation.

    Args:
        base (int): The number used for the base value of the expression.
        power (int): The number choosed for power value of the expression.
        modulus_to (int): The number used to take modulus of the expression.

    Returns:
        result(int): The evaluated value of modular exponentiaion.
    """

    # Base Cases for recursion
    if (base == 0): # This reduces computation if base is 0.
        return 0
    if (power == 0): # This reduces computation if power is 0.
        return 1
    if (modulus_to == 1): # This reduces computation if modulus_to is 1.
        return 0

    # Recursive cases for recursion
    result = 0
    if (power % 2 == 0): # To check if the power is even
        result = modular_exponentiation(base, power / 2, modulus_to) # Recursive call if power/2
        result = (result * result) % modulus_to # Storing the squared result value's mod back into result

    else: # For odd power values
        result = base % modulus_to # Mod of the base value
        # In the below line the function has been called recursively and successive mods have been performed
        # with reducing values of power by a factor of 1
        result = (result * modular_exponentiation(base, power - 1,
                                                  modulus_to) % modulus_to) % modulus_to 
    return ((result + modulus_to) % modulus_to)


if __name__ == "__main__":
    base = int(input("Enter the base number: "))
    power = int(input("Enter the power number: "))
    modulus_to = int(
        input("Enter the number which is used to perform modulus operation: "))
    print(f"The result is {modular_exponentiation(base, power, modulus_to)}")
