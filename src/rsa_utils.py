import math


def calculate_n_verbose(p: int, q: int) -> int:
    print("\n" + "=" * 60)
    print("CÁLCULO DEL MÓDULO n")
    print("=" * 60)

    print("\nLa fórmula para calcular n es:")
    print("\nn = p × q")

    print("\nSustituyendo los valores:")
    print(f"\nn = {p} × {q}")

    n = p * q

    print(f"\nn = {n}")
    print(f"\n✓ El valor del módulo RSA es n = {n}")

    return n


def calculate_phi_verbose(p: int, q: int) -> int:
    print("\n" + "=" * 60)
    print("CÁLCULO DE LA INDICATRIZ DE EULER φ(n)")
    print("=" * 60)

    print("\nLa fórmula para calcular φ(n) es:")
    print("\nφ(n) = (p - 1) × (q - 1)")

    print("\nSustituyendo los valores:")
    print(f"\nφ(n) = ({p} - 1) × ({q} - 1)")

    p_minus_one = p - 1
    q_minus_one = q - 1

    print("\nResolviendo las restas:")
    print(f"\np - 1 = {p} - 1 = {p_minus_one}")
    print(f"q - 1 = {q} - 1 = {q_minus_one}")

    print("\nAhora multiplicamos:")
    print(f"\nφ(n) = {p_minus_one} × {q_minus_one}")

    phi = p_minus_one * q_minus_one

    print(f"\nφ(n) = {phi}")
    print(f"\n✓ La indicatriz de Euler es φ(n) = {phi}")

    return phi


def generate_valid_exponents_verbose(phi: int) -> list[int]:
    print("\n" + "=" * 60)
    print("GENERACIÓN DE POSIBLES VALORES PARA e")
    print("=" * 60)

    print("\nEl exponente público e debe cumplir:")
    print("\n1 < e < φ(n)")
    print("MCD(e, φ(n)) = 1")

    print("\nEn este caso:")
    print(f"φ(n) = {phi}")

    print("\nBuscando valores válidos para e...")

    valid_exponents = []

    # Se evalúan todos los valores posibles internamente
    for e in range(2, phi):
        gcd = math.gcd(e, phi)

        if gcd == 1:
            valid_exponents.append(e)

    # Mostrar únicamente algunos ejemplos del proceso
    print("\n" + "-" * 60)
    print("EJEMPLOS DE VALIDACIÓN")
    print("-" * 60)

    examples_to_show = min(10, phi - 2)

    for e in range(2, 2 + examples_to_show):
        gcd = math.gcd(e, phi)

        if gcd == 1:
            status = "✓ Válido"
        else:
            status = "✗ No válido"

        print(f"MCD({e}, {phi}) = {gcd}  {status}")

    if phi - 2 > examples_to_show:
        print("\n...")
        print(
            f"El programa continúa evaluando internamente "
            f"todos los valores hasta {phi - 1}."
        )

    print("\n" + "-" * 60)
    print("VALORES VÁLIDOS PARA e")
    print("-" * 60)

    # Mostrar la lista de exponentes en grupos para mejorar la lectura
    values_per_line = 12

    for i in range(0, len(valid_exponents), values_per_line):
        group = valid_exponents[i:i + values_per_line]
        print("  " + ", ".join(str(value) for value in group))

    print(
        f"\nSe evaluaron todos los valores desde 2 hasta {phi - 1}."
    )

    print(
        f"Se encontraron {len(valid_exponents)} valores "
        f"que cumplen MCD(e, φ(n)) = 1."
    )

    return valid_exponents


def read_public_exponent(
    valid_exponents: list[int],
    phi: int
) -> int:
    print("\n" + "=" * 60)
    print("SELECCIÓN DEL EXPONENTE PÚBLICO e")
    print("=" * 60)

    print("\nSeleccione uno de los valores válidos generados:")
    print(f"\n{valid_exponents}")

    while True:
        try:
            e = int(input("\nIngrese el valor de e: "))

            print("\nValidando el valor seleccionado...")
            print(f"\ne = {e}")

            gcd = math.gcd(e, phi)

            print(f"MCD({e}, {phi}) = {gcd}")

            if e not in valid_exponents:
                print(
                    "\n✗ El valor seleccionado no pertenece "
                    "a la lista de exponentes válidos."
                )
                print("Seleccione nuevamente un valor de e.")
                continue

            if gcd != 1:
                print(
                    f"\n✗ MCD({e}, {phi}) debe ser igual a 1."
                )
                continue

            print(
                f"\n✓ e = {e} es un exponente público válido."
            )

            return e

        except ValueError:
            print(
                "\n✗ Entrada inválida. Debe ingresar un número entero."
            )

def calculate_private_exponent_verbose(e: int, phi: int) -> tuple[int, int]:
    print("\n" + "=" * 60)
    print("CÁLCULO DEL EXPONENTE PRIVADO d")
    print("=" * 60)

    print("\nPara calcular d utilizamos la relación:")
    print("\nd = (1 + k × φ(n)) / e")

    print("\nDebemos encontrar un valor de k que haga que:")
    print("\n1 + k × φ(n)")
    print("\nsea divisible exactamente entre e.")

    print(f"\nValores conocidos:")
    print(f"e = {e}")
    print(f"φ(n) = {phi}")

    k = 1

    print("\n" + "-" * 60)
    print("BÚSQUEDA DEL VALOR DE k")
    print("-" * 60)

    while True:
        numerator = 1 + (k * phi)
        remainder = numerator % e

        print(f"\nk = {k}")
        print(f"1 + ({k} × {phi}) = {numerator}")
        print(f"{numerator} mod {e} = {remainder}")

        if remainder == 0:
            d = numerator // e

            print("\n✓ La división es exacta.")
            print(f"{numerator} / {e} = {d}")

            break

        print("✗ La división no es exacta. Probamos otro valor de k.")

        k += 1

    print("\n" + "-" * 60)
    print("CÁLCULO FINAL DE d")
    print("-" * 60)

    print("\nAplicando la fórmula:")
    print("\nd = (1 + k × φ(n)) / e")

    print("\nSustituyendo:")
    print(f"\nd = (1 + ({k} × {phi})) / {e}")

    numerator = 1 + (k * phi)

    print(f"\nd = {numerator} / {e}")
    print(f"\nd = {d}")

    print(f"\n✓ El valor encontrado es k = {k}")
    print(f"✓ El exponente privado es d = {d}")

    print("\n" + "-" * 60)
    print("VERIFICACIÓN DEL INVERSO MODULAR")
    print("-" * 60)

    multiplication = e * d
    verification = multiplication % phi

    print("\nDebe cumplirse:")
    print("\ne × d mod φ(n) = 1")

    print("\nSustituyendo:")
    print(f"\n{e} × {d} mod {phi}")

    print(f"\n{e} × {d} = {multiplication}")
    print(f"{multiplication} mod {phi} = {verification}")

    if verification == 1:
        print("\n✓ Verificación correcta.")
        print("✓ d es el inverso modular de e respecto a φ(n).")
    else:
        print("\n✗ Error en la verificación del exponente privado.")

    return k, d


def show_keys_verbose(n: int, e: int, d: int) -> None:
    print("\n" + "=" * 60)
    print("GENERACIÓN DE LLAVES RSA")
    print("=" * 60)

    print("\nLa llave pública está formada por:")
    print("\n[n, e]")

    print("\nSustituyendo:")
    print(f"\n[{n}, {e}]")

    print("\n✓ Llave pública:")
    print(f"[{n}, {e}]")

    print("\nLa llave privada está formada por:")
    print("\n[n, d]")

    print("\nSustituyendo:")
    print(f"\n[{n}, {d}]")

    print("\n✓ Llave privada:")
    print(f"[{n}, {d}]")

def encrypt_with_public_key_verbose(
    ascii_values: list[int],
    n: int,
    e: int
) -> list[int]:
    print("\n" + "=" * 60)
    print("CIFRADO RSA CON LA LLAVE PÚBLICA")
    print("=" * 60)

    print("\nUtilizaremos la llave pública:")
    print(f"\n[n, e] = [{n}, {e}]")

    print("\nPara cifrar cada valor utilizamos la fórmula:")
    print("\nC = M^e mod n")

    encrypted_values = []

    for index, value in enumerate(ascii_values, start=1):
        print("\n" + "-" * 60)
        print(f"VALOR {index}")
        print("-" * 60)

        print(f"\nMensaje numérico M = {value}")

        print("\nAplicando la fórmula:")
        print(f"\nC = {value}^{e} mod {n}")

        encrypted_value = pow(value, e, n)

        print(f"\nC = {encrypted_value}")

        print(
            f"\n✓ {value} cifrado con la llave pública "
            f"produce {encrypted_value}"
        )

        encrypted_values.append(encrypted_value)

    print("\n" + "=" * 60)
    print("RESULTADO DEL CIFRADO")
    print("=" * 60)

    print("\nValores originales:")
    print(ascii_values)

    print("\nValores cifrados:")
    print(encrypted_values)

    return encrypted_values


def decrypt_with_private_key_verbose(
    encrypted_values: list[int],
    n: int,
    d: int
) -> list[int]:
    print("\n" + "=" * 60)
    print("DESCIFRADO RSA CON LA LLAVE PRIVADA")
    print("=" * 60)

    print("\nUtilizaremos la llave privada:")
    print(f"\n[n, d] = [{n}, {d}]")

    print("\nPara descifrar cada valor utilizamos la fórmula:")
    print("\nM = C^d mod n")

    decrypted_values = []

    for index, encrypted_value in enumerate(
        encrypted_values,
        start=1
    ):
        print("\n" + "-" * 60)
        print(f"VALOR {index}")
        print("-" * 60)

        print(f"\nValor cifrado C = {encrypted_value}")

        print("\nAplicando la fórmula:")
        print(
            f"\nM = {encrypted_value}^{d} mod {n}"
        )

        decrypted_value = pow(
            encrypted_value,
            d,
            n
        )

        print(f"\nM = {decrypted_value}")

        print(
            f"\n✓ {encrypted_value} descifrado "
            f"produce {decrypted_value}"
        )

        decrypted_values.append(decrypted_value)

    print("\n" + "=" * 60)
    print("RESULTADO DEL DESCIFRADO")
    print("=" * 60)

    print("\nValores cifrados:")
    print(encrypted_values)

    print("\nValores recuperados:")
    print(decrypted_values)

    return decrypted_values

def encrypt_with_private_key_verbose(
    ascii_values: list[int],
    n: int,
    d: int
) -> list[int]:
    print("\n" + "=" * 60)
    print("PROCESAMIENTO CON LA LLAVE PRIVADA")
    print("FIRMA DIGITAL SIMPLIFICADA")
    print("=" * 60)

    print("\nUtilizaremos la llave privada:")
    print(f"\n[n, d] = [{n}, {d}]")

    print("\nPara procesar cada valor utilizamos:")
    print("\nS = M^d mod n")

    signed_values = []

    for index, value in enumerate(ascii_values, start=1):
        print("\n" + "-" * 60)
        print(f"VALOR {index}")
        print("-" * 60)

        print(f"\nMensaje numérico M = {value}")

        print("\nAplicando la fórmula:")
        print(f"\nS = {value}^{d} mod {n}")

        signed_value = pow(value, d, n)

        print(f"\nS = {signed_value}")

        print(
            f"\n✓ {value} procesado con la llave privada "
            f"produce {signed_value}"
        )

        signed_values.append(signed_value)

    print("\n" + "=" * 60)
    print("RESULTADO DEL PROCESAMIENTO CON LLAVE PRIVADA")
    print("=" * 60)

    print("\nValores originales:")
    print(ascii_values)

    print("\nValores procesados:")
    print(signed_values)

    return signed_values


def decrypt_with_public_key_verbose(
    signed_values: list[int],
    n: int,
    e: int
) -> list[int]:
    print("\n" + "=" * 60)
    print("RECUPERACIÓN CON LA LLAVE PÚBLICA")
    print("VERIFICACIÓN DE FIRMA DIGITAL SIMPLIFICADA")
    print("=" * 60)

    print("\nUtilizaremos la llave pública:")
    print(f"\n[n, e] = [{n}, {e}]")

    print("\nPara recuperar cada valor utilizamos:")
    print("\nM = S^e mod n")

    recovered_values = []

    for index, signed_value in enumerate(
        signed_values,
        start=1
    ):
        print("\n" + "-" * 60)
        print(f"VALOR {index}")
        print("-" * 60)

        print(f"\nValor procesado S = {signed_value}")

        print("\nAplicando la fórmula:")
        print(f"\nM = {signed_value}^{e} mod {n}")

        recovered_value = pow(
            signed_value,
            e,
            n
        )

        print(f"\nM = {recovered_value}")

        print(
            f"\n✓ {signed_value} procesado con la llave pública "
            f"produce {recovered_value}"
        )

        recovered_values.append(recovered_value)

    print("\n" + "=" * 60)
    print("RESULTADO DE LA VERIFICACIÓN")
    print("=" * 60)

    print("\nValores procesados con llave privada:")
    print(signed_values)

    print("\nValores recuperados con llave pública:")
    print(recovered_values)

    return recovered_values