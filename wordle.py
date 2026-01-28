cantidad_letras = 5

def verificador_palabra(palabra_ingresada, palabra_secreta):
    letras_verificadas = []  # se reinicia en cada intento

    for i in range(cantidad_letras):
        las_palabras_son_iguales = palabra_ingresada[i] == palabra_secreta[i]
        la_letra_existe_en_la_palabra = palabra_ingresada[i] in palabra_secreta

        if las_palabras_son_iguales:
            letras_verificadas.append(f"[{palabra_ingresada[i]}]")   # correcta y en su lugar
        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append(f"({palabra_ingresada[i]})")   # existe pero en otro lugar
        else:
            letras_verificadas.append(palabra_ingresada[i])          # no existe

    return letras_verificadas


palabra_secreta = "calor"
intentos = 0

while intentos < 6:
    print(f"\nTe quedan {6 - intentos} intentos")
    palabra_ingresada = input("Ingrese una palabra de 5 letras: ").lower()

    # Validación
    if len(palabra_ingresada) != cantidad_letras or not palabra_ingresada.isalpha():
        print("❌ Error: debe ser una palabra de 5 letras (solo letras).")
        continue  # no cuenta como intento

    intentos += 1

    resultado = verificador_palabra(palabra_ingresada, palabra_secreta)
    print("Resultado:", " ".join(resultado))

    if palabra_ingresada == palabra_secreta:
        print("✅ Ganaste!")
        break
else:
    print(f"😢 Perdiste. La palabra era: {palabra_secreta}")
