import math


def is_prime_verbose(number: int, variable_name: str) -> bool:
    print("\n" + "=" * 60)
    print(f"VALIDACIÓN DEL NÚMERO PRIMO {variable_name}")
    print("=" * 60)

    print(f"\nNúmero ingresado: {number}")
    print(f"Verificando si {number} es un número primo...\n")

    if number <= 1:
        print(f"{number} no es primo porque debe ser mayor que 1.")
        return False

    if number == 2:
        print("2 es primo porque únicamente es divisible entre 1 y 2.")
        print(f"\n✓ {variable_name} = {number} es primo.")
        return True

    limit = math.isqrt(number)

    print(
        f"Para verificar si {number} es primo, "
        f"probamos divisores desde 2 hasta √{number}."
    )
    print(f"Parte entera de √{number} = {limit}\n")

    for divisor in range(2, limit + 1):
        remainder = number % divisor

        print(
            f"{number} mod {divisor} = {remainder}"
        )

        if remainder == 0:
            print(
                f"\n{number} es divisible exactamente entre {divisor}."
            )
            print(
                f"✗ {variable_name} = {number} NO es primo."
            )
            return False

    print(
        f"\nNo se encontró ningún divisor exacto "
        f"entre 2 y {limit}."
    )
    print(f"✓ {variable_name} = {number} es primo.")

    return True


def read_prime(variable_name: str) -> int:
    while True:
        try:
            value = int(
                input(
                    f"\nIngrese el número primo {variable_name}: "
                )
            )

            if is_prime_verbose(value, variable_name):
                return value

            print(
                f"\nDebe ingresar nuevamente el valor de {variable_name}."
            )

        except ValueError:
            print(
                "\n✗ Entrada inválida. Debe ingresar un número entero."
            )


def read_distinct_primes() -> tuple[int, int]:
    print("\n" + "=" * 60)
    print("INGRESO DE LOS NÚMEROS PRIMOS p Y q")
    print("=" * 60)

    p = read_prime("p")

    while True:
        q = read_prime("q")

        print("\n" + "-" * 60)
        print("VALIDACIÓN: p Y q DEBEN SER DIFERENTES")
        print("-" * 60)

        print(f"\np = {p}")
        print(f"q = {q}")

        if p != q:
            print(f"\n{p} != {q}")
            print("\n✓ Los números primos p y q son diferentes.")
            return p, q

        print(f"\n{p} = {q}")
        print("\n✗ p y q no pueden ser iguales.")
        print("Ingrese nuevamente el valor de q.")