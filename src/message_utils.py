def read_message() -> str:
    print("\n" + "=" * 60)
    print("INGRESO DEL MENSAJE")
    print("=" * 60)

    while True:
        message = input("\nIngrese el mensaje en texto plano: ")

        if message:
            print(f"\n✓ Mensaje recibido: {message}")
            return message

        print("\n✗ El mensaje no puede estar vacío.")


def prepare_message_verbose(message: str) -> str:
    print("\n" + "=" * 60)
    print("PREPARACIÓN DEL MENSAJE")
    print("=" * 60)

    print("\nEl enunciado solicita agregar:")
    print("- El símbolo + al principio.")
    print("- El símbolo - al final.")

    print(f"\nMensaje original:")
    print(message)

    prepared_message = "+" + message + "-"

    print("\nAplicando los símbolos:")
    print(f'"+" + "{message}" + "-"')

    print("\nMensaje preparado:")
    print(prepared_message)

    print(f"\n✓ Mensaje final a procesar: {prepared_message}")

    return prepared_message


def text_to_ascii_verbose(message: str) -> list[int]:
    print("\n" + "=" * 60)
    print("CONVERSIÓN DEL MENSAJE A ASCII")
    print("=" * 60)

    print("\nCada carácter será convertido a su código numérico ASCII.")
    print("\nMapeo carácter → código:\n")

    ascii_values = []

    for character in message:
        ascii_code = ord(character)

        ascii_values.append(ascii_code)

        print(f"'{character}' → {ascii_code}")

    print("\nRepresentación numérica completa:")
    print(ascii_values)

    print("\n✓ Conversión a ASCII completada correctamente.")

    return ascii_values


def validate_ascii_values_verbose(
    message: str,
    ascii_values: list[int],
    n: int
) -> bool:
    print("\n" + "=" * 60)
    print("VALIDACIÓN DE LOS VALORES ASCII PARA RSA")
    print("=" * 60)

    print("\nPara procesar cada carácter individualmente con RSA")
    print("debe cumplirse que cada valor numérico sea menor que n.")

    print("\nCondición:")
    print("\nm < n")

    print(f"\nValor actual de n = {n}\n")

    all_valid = True

    for character, ascii_code in zip(message, ascii_values):
        if ascii_code < n:
            print(
                f"'{character}' → {ascii_code}: "
                f"{ascii_code} < {n}  ✓ Válido"
            )
        else:
            print(
                f"'{character}' → {ascii_code}: "
                f"{ascii_code} >= {n}  ✗ No válido"
            )
            all_valid = False

    if all_valid:
        print("\n✓ Todos los valores ASCII pueden procesarse con RSA.")
    else:
        print("\n✗ Existen valores ASCII mayores o iguales que n.")
        print(
            "Debe utilizar números primos que produzcan "
            "un valor de n suficientemente grande."
        )

    return all_valid

def ascii_to_text_verbose(ascii_values: list[int]) -> str:
    print("\n" + "=" * 60)
    print("RECONSTRUCCIÓN DEL MENSAJE")
    print("=" * 60)

    print("\nConvirtiendo cada código numérico nuevamente a carácter:\n")

    characters = []

    for ascii_code in ascii_values:
        character = chr(ascii_code)

        print(f"{ascii_code} → '{character}'")

        characters.append(character)

    recovered_message = "".join(characters)

    print("\nMensaje reconstruido:")
    print(recovered_message)

    print("\n✓ Conversión de ASCII a texto completada.")

    return recovered_message