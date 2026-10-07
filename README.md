# Sistema RSA Simplificado y Verboso

Programa desarrollado en **Python** para implementar de manera didáctica el algoritmo RSA.

El objetivo principal del proyecto es mostrar paso a paso cómo se generan las llaves RSA, cómo se cifra y descifra un mensaje y cómo se realiza una firma digital simplificada.

El programa fue diseñado de manera **verbosa**, mostrando en consola las operaciones matemáticas relevantes realizadas durante todo el proceso.

---

## Objetivo

El programa permite:

- Ingresar dos números primos `p` y `q`.
- Validar que ambos números sean primos.
- Validar que `p` y `q` sean diferentes.
- Calcular el módulo RSA `n`.
- Calcular la función indicatriz de Euler `φ(n)`.
- Generar los posibles exponentes públicos `e`.
- Permitir al usuario seleccionar un `e` válido.
- Calcular el exponente privado `d`.
- Generar la llave pública y la llave privada.
- Convertir un mensaje a su representación ASCII.
- Cifrar el mensaje con la llave pública.
- Descifrarlo con la llave privada.
- Procesar el mensaje con la llave privada.
- Verificarlo utilizando la llave pública.
- Mostrar paso a paso todas las operaciones realizadas.

---

# Funcionamiento de RSA

## 1. Selección de números primos

El usuario ingresa dos números:

```text
p
q
```

El programa verifica que:

```text
p sea primo
q sea primo
p != q
```

Ejemplo:

```text
p = 17
q = 23
```

---

## 2. Cálculo de n

Se calcula:

```text
n = p × q
```

Ejemplo:

```text
n = 17 × 23
n = 391
```

El valor `n` será utilizado tanto en la llave pública como en la llave privada.

---

## 3. Cálculo de φ(n)

Se utiliza la función indicatriz de Euler:

```text
φ(n) = (p - 1) × (q - 1)
```

Ejemplo:

```text
φ(n) = (17 - 1) × (23 - 1)

φ(n) = 16 × 22

φ(n) = 352
```

---

## 4. Selección del exponente público e

El programa genera valores que cumplan:

```text
1 < e < φ(n)
```

y además:

```text
MCD(e, φ(n)) = 1
```

Esto significa que `e` y `φ(n)` deben ser coprimos.

Ejemplo:

```text
MCD(3, 352) = 1
```

Por lo tanto:

```text
e = 3
```

es válido.

El programa genera automáticamente la lista de posibles valores y permite que el usuario seleccione uno.

---

## 5. Cálculo del exponente privado d

Para obtener `d`, el programa busca un valor `k` que permita que la siguiente expresión produzca un número entero:

```text
d = (1 + k × φ(n)) / e
```

Ejemplo:

```text
e = 3
φ(n) = 352
```

Probando:

```text
k = 1

1 + (1 × 352) = 353

353 mod 3 = 2
```

No sirve.

Luego:

```text
k = 2

1 + (2 × 352) = 705

705 mod 3 = 0
```

Por lo tanto:

```text
d = 705 / 3

d = 235
```

Se verifica además que:

```text
e × d mod φ(n) = 1
```

Ejemplo:

```text
3 × 235 mod 352 = 1
```

---

# Generación de llaves

Con los valores calculados:

```text
n = 391
e = 3
d = 235
```

se generan las llaves RSA.

## Llave pública

```text
[n, e]
```

Ejemplo:

```text
[391, 3]
```

## Llave privada

```text
[n, d]
```

Ejemplo:

```text
[391, 235]
```

---

# Procesamiento del mensaje

El usuario ingresa un mensaje en texto plano.

Ejemplo:

```text
HOLA
```

Antes de procesarlo, el programa agrega:

```text
+
```

al principio y:

```text
-
```

al final.

Por lo tanto:

```text
HOLA
```

se transforma en:

```text
+HOLA-
```

---

# Conversión a ASCII

Cada carácter se convierte a su representación numérica.

Ejemplo:

```text
'+' → 43
'H' → 72
'O' → 79
'L' → 76
'A' → 65
'-' → 45
```

Resultado:

```text
[43, 72, 79, 76, 65, 45]
```

El programa también verifica que cada valor pueda ser procesado por RSA mediante:

```text
M < n
```

---

# Cifrado RSA tradicional

Para cifrar el mensaje se utiliza la **llave pública**.

La fórmula utilizada es:

```text
C = M^e mod n
```

Donde:

- `M` es el valor ASCII original.
- `e` es el exponente público.
- `n` es el módulo RSA.
- `C` es el valor cifrado.

Ejemplo:

```text
43^3 mod 391 = 134
```

Para el mensaje:

```text
+HOLA-
```

los valores ASCII:

```text
[43, 72, 79, 76, 65, 45]
```

son transformados en:

```text
[134, 234, 379, 274, 143, 22]
```

---

# Descifrado con la llave privada

Para recuperar el mensaje se utiliza:

```text
M = C^d mod n
```

donde `d` pertenece a la llave privada.

Los valores cifrados:

```text
[134, 234, 379, 274, 143, 22]
```

vuelven a convertirse en:

```text
[43, 72, 79, 76, 65, 45]
```

Finalmente los códigos se convierten nuevamente a caracteres:

```text
+HOLA-
```

De esta manera se comprueba que:

```text
Mensaje original == Mensaje recuperado
```

---

# Firma digital simplificada

El programa también realiza el proceso contrario.

Primero se procesa el mensaje utilizando la **llave privada**:

```text
S = M^d mod n
```

Posteriormente se utiliza la **llave pública** para recuperar y verificar el mensaje:

```text
M = S^e mod n
```

El flujo es:

```text
Mensaje
   ↓
ASCII
   ↓
Llave privada
   ↓
Valores procesados
   ↓
Llave pública
   ↓
ASCII recuperado
   ↓
Mensaje original
```

Si el mensaje recuperado coincide con el original, la verificación final es correcta.

---

# Flujo general

```text
p y q
  ↓
Validación de números primos
  ↓
n = p × q
  ↓
φ(n) = (p - 1)(q - 1)
  ↓
Generación de posibles valores de e
  ↓
Selección de e
  ↓
Búsqueda de k
  ↓
Cálculo de d
  ↓
Llave pública [n, e]
Llave privada [n, d]
  ↓
Ingreso del mensaje
  ↓
+MENSAJE-
  ↓
Conversión ASCII
  ↓
Cifrado pública → privada
  ↓
Recuperación del mensaje
  ↓
Procesamiento privada → pública
  ↓
Verificación de firma digital simplificada
```

---

# Estructura del proyecto

```text
rsa-verbose/
│
├── .venv/
│
├── src/
│   ├── __init__.py
│   ├── prime_utils.py
│   ├── rsa_utils.py
│   ├── message_utils.py
│   └── main.py
│
├── README.md
└── requirements.txt
```

### `prime_utils.py`

Contiene las funciones encargadas de:

- Validar números primos.
- Solicitar `p` y `q`.
- Verificar que sean diferentes.

### `rsa_utils.py`

Contiene la lógica matemática de RSA:

- Cálculo de `n`.
- Cálculo de `φ(n)`.
- Generación de exponentes `e`.
- Cálculo de `k`.
- Cálculo de `d`.
- Generación de llaves.
- Cifrado con llave pública.
- Descifrado con llave privada.
- Procesamiento con llave privada.
- Verificación con llave pública.

### `message_utils.py`

Contiene las funciones relacionadas con el mensaje:

- Lectura del mensaje.
- Adición de `+` y `-`.
- Conversión texto → ASCII.
- Validación de valores.
- Conversión ASCII → texto.

### `main.py`

Controla el flujo completo de ejecución del programa.

---

# Requisitos

El proyecto utiliza únicamente funcionalidades incluidas en Python.

No requiere librerías criptográficas externas.

Se recomienda:

```text
Python 3.10+
```

El proyecto utiliza principalmente:

```python
math.gcd()
math.isqrt()
pow()
ord()
chr()
```

---

# Crear el entorno virtual

Desde la carpeta del proyecto:

```bash
python3 -m venv .venv
```

## Activar en macOS / Linux

```bash
source .venv/bin/activate
```

Cuando esté activo aparecerá algo similar a:

```text
(.venv) usuario@equipo rsa-verbose %
```

## Activar en Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

---

# Ejecutar el proyecto

Ubicarse en la raíz:

```text
rsa-verbose/
```

Activar el entorno virtual:

```bash
source .venv/bin/activate
```

Ejecutar:

```bash
python src/main.py
```

En algunos sistemas también puede utilizarse:

```bash
python3 src/main.py
```

---

# Ejemplo recomendado

Para probar el programa:

```text
p = 17
q = 23
e = 3
mensaje = HOLA
```

Los principales resultados esperados son:

```text
n = 391
φ(n) = 352
k = 2
d = 235
```

Llaves:

```text
Llave pública:
[391, 3]

Llave privada:
[391, 235]
```

Mensaje preparado:

```text
+HOLA-
```

ASCII:

```text
[43, 72, 79, 76, 65, 45]
```

Cifrado con la llave pública:

```text
[134, 234, 379, 274, 143, 22]
```

Después del descifrado debe recuperarse:

```text
+HOLA-
```

La firma digital simplificada también debe finalizar indicando que el mensaje fue recuperado correctamente.

---

# Importante

Este proyecto implementa una versión **simplificada y educativa de RSA**.

Su propósito es comprender las operaciones matemáticas involucradas en RSA mostrando los cálculos paso a paso.

No debe utilizarse como implementación criptográfica para aplicaciones reales o sistemas de producción.