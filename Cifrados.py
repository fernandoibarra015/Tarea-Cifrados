# Cifrado César
def cifrado_cesar(texto, clave):
    resultado = ''
    for char in texto:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - offset + clave) % 26 + offset)
        else:
            resultado += char
    return resultado

def descifrado_cesar(texto, clave):
    return cifrado_cesar(texto, -clave)

# Cifrado Espartano
def cifrado_espartano(texto, clave):
    resultado = ''
    for char in texto:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - offset + clave * 3) % 26 + offset)
        else:
            resultado += char
    return resultado

def descifrado_espartano(texto, clave):
    return cifrado_espartano(texto, -clave)

# Cifrado Vigenère
def cifrado_vigenere(texto, clave):
    resultado = ''
    clave_index = 0
    for char in texto:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            shift = ord(clave[clave_index % len(clave)]) - ord('a')
            resultado += chr((ord(char) - offset + shift) % 26 + offset)
            clave_index += 1
        else:
            resultado += char
    return resultado

def descifrado_vigenere(texto, clave):
    resultado = ''
    clave_index = 0
    for char in texto:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            shift = ord(clave[clave_index % len(clave)]) - ord('a')
            resultado += chr((ord(char) - offset - shift) % 26 + offset)
            clave_index += 1
        else:
            resultado += char
    return resultado

# Main
def main():
    texto = input("Ingresa el texto a cifrar: ")
    clave = int(input("Ingresa la clave para el cifrado César y Espartano: "))
    clave_vigenere = input("Ingresa la clave para el cifrado Vigenère: ")

    texto_cifrado_cesar = cifrado_cesar(texto, clave)
    texto_descifrado_cesar = descifrado_cesar(texto_cifrado_cesar, clave)

    texto_cifrado_espartano = cifrado_espartano(texto, clave)
    texto_descifrado_espartano = descifrado_espartano(texto_cifrado_espartano, clave)

    texto_cifrado_vigenere = cifrado_vigenere(texto, clave_vigenere)
    texto_descifrado_vigenere = descifrado_vigenere(texto_cifrado_vigenere, clave_vigenere)

    print("\nCifrado César:")
    print("Texto cifrado:", texto_cifrado_cesar)
    print("Texto descifrado:", texto_descifrado_cesar)

    print("\nCifrado Espartano:")
    print("Texto cifrado:", texto_cifrado_espartano)
    print("Texto descifrado:", texto_descifrado_espartano)

    print("\nCifrado Vigenère:")
    print("Texto cifrado:", texto_cifrado_vigenere)
    print("Texto descifrado:", texto_descifrado_vigenere)

if __name__ == "__main__":
    main()
