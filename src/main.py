from prime_utils import read_distinct_primes

from rsa_utils import (
    calculate_n_verbose,
    calculate_phi_verbose,
    generate_valid_exponents_verbose,
    read_public_exponent,
    calculate_private_exponent_verbose,
    show_keys_verbose,
    encrypt_with_public_key_verbose,
    decrypt_with_private_key_verbose,
    encrypt_with_private_key_verbose,
    decrypt_with_public_key_verbose,
)

from message_utils import (
    read_message,
    prepare_message_verbose,
    text_to_ascii_verbose,
    validate_ascii_values_verbose,
    ascii_to_text_verbose,
)

def main():
    print("\n" + "=" * 60)
    print("              SISTEMA RSA SIMPLIFICADO")
    print("=" * 60)

    # PASO 1 - Leer y validar los números primos
    p, q = read_distinct_primes()

    print("\n" + "=" * 60)
    print("NÚMEROS PRIMOS VALIDADOS")
    print("=" * 60)

    print(f"\np = {p}")
    print(f"q = {q}")

    print("\n✓ Validación inicial completada correctamente.")

    # PASO 2 - Calcular n
    n = calculate_n_verbose(p, q)

    # PASO 3 - Calcular φ(n)
    phi = calculate_phi_verbose(p, q)

    # PASO 4 - Generar posibles valores para e
    valid_exponents = generate_valid_exponents_verbose(phi)

    # PASO 5 - Permitir al usuario seleccionar e
    e = read_public_exponent(valid_exponents, phi)

    # PASO 6 - Calcular k y el exponente privado d
    k, d = calculate_private_exponent_verbose(e, phi)
    
    # PASO 7 - Mostrar las llaves RSA
    show_keys_verbose(n, e, d)

    # PASO 8 - Leer el mensaje en texto plano
    message = read_message()

    # PASO 9 - Agregar + al inicio y - al final
    prepared_message = prepare_message_verbose(message)

    # PASO 10 - Convertir el mensaje a ASCII
    ascii_values = text_to_ascii_verbose(prepared_message)

    # PASO 11 - Validar que los valores puedan procesarse con RSA
    ascii_valid = validate_ascii_values_verbose(
        prepared_message,
        ascii_values,
        n,
    )

    if not ascii_valid:
        print("\nNo es posible continuar con el cifrado RSA.")
        return

    # PASO 12 - Cifrar el mensaje con la llave pública
    encrypted_values = encrypt_with_public_key_verbose(
        ascii_values,
        n,
        e,
    )

    # PASO 13 - Descifrar el mensaje con la llave privada
    decrypted_values = decrypt_with_private_key_verbose(
        encrypted_values,
        n,
        d,
    )

    # PASO 14 - Reconstruir el mensaje original
    recovered_message = ascii_to_text_verbose(
        decrypted_values
    )

    # PASO 15 - Verificar que el mensaje recuperado sea correcto
    print("\n" + "=" * 60)
    print("VERIFICACIÓN DEL MENSAJE RECUPERADO")
    print("=" * 60)

    print(f"\nMensaje procesado originalmente: {prepared_message}")
    print(f"Mensaje recuperado:             {recovered_message}")

    if recovered_message == prepared_message:
        print("\n✓ El mensaje fue recuperado correctamente.")
    else:
        print("\n✗ El mensaje recuperado no coincide con el original.")

    # PASO 16 - Procesar el mensaje con la llave privada
    signed_values = encrypt_with_private_key_verbose(
        ascii_values,
        n,
        d,
    )
    
    # PASO 17 - Recuperar el mensaje con la llave pública
    verified_values = decrypt_with_public_key_verbose(
        signed_values,
        n,
        e,
    )
    
    # PASO 18 - Reconstruir el mensaje verificado
    verified_message = ascii_to_text_verbose(
        verified_values
    )
    
    # PASO 19 - Verificar la firma digital simplificada
    print("\n" + "=" * 60)
    print("VERIFICACIÓN FINAL DE FIRMA DIGITAL")
    print("=" * 60)
    
    print(f"\nMensaje procesado originalmente: {prepared_message}")
    print(f"Mensaje recuperado:             {verified_message}")
    
    if verified_message == prepared_message:
        print("\n✓ La firma digital simplificada fue verificada correctamente.")
    else:
        print("\n✗ La verificación de la firma digital falló.")

    print("\n" + "=" * 60)
    print("RESUMEN DE PARÁMETROS RSA")
    print("=" * 60)

    print(f"\np     = {p}")
    print(f"q     = {q}")
    print(f"n     = {n}")
    print(f"φ(n)  = {phi}")
    print(f"e     = {e}")
    print(f"k     = {k}")
    print(f"d     = {d}")

if __name__ == "__main__":
    main()