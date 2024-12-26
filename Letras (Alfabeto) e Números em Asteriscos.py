def print_letter(letter):
    alphabet = {
        'A': [
            "   *   ",
            "  * *  ",
            " ***** ",
            " *   * ",
            " *   * "
        ],
        'B': [
            " ****  ",
            " *   * ",
            " ****  ",
            " *   * ",
            " ****  "
        ],
        'C': [
            "  **** ",
            " *     ",
            " *     ",
            " *     ",
            "  **** "
        ],
        # Adicione as outras letras do alfabeto aqui
        'D': [
            " ****  ",
            " *   * ",
            " *   * ",
            " *   * ",
            " ****  "
        ],
        'E': [
            " ***** ",
            " *     ",
            " ***** ",
            " *     ",
            " ***** "
        ],
        'F': [
            " ***** ",
            " *     ",
            " ***** ",
            " *     ",
            " *     "
        ],
        'G': [
            "  **** ",
            " *     ",
            " *  ** ",
            " *   * ",
            "  **** "
        ],
        'H': [
            " *   * ",
            " *   * ",
            " ***** ",
            " *   * ",
            " *   * "
        ],
        'I': [
            "  ***  ",
            "   *   ",
            "   *   ",
            "   *   ",
            "  ***  "
        ],
        'J': [
            "   *** ",
            "    *  ",
            "    *  ",
            " *  *  ",
            "  **   "
        ],
        'K': [
            " *   * ",
            " *  *  ",
            " ***   ",
            " *  *  ",
            " *   * "
        ],
        'L': [
            " *     ",
            " *     ",
            " *     ",
            " *     ",
            " ***** "
        ],
        'M': [
            " *   * ",
            " ** ** ",
            " * * * ",
            " *   * ",
            " *   * "
        ],
        'N': [
            " *   * ",
            " **  * ",
            " * * * ",
            " *  ** ",
            " *   * "
        ],
        'O': [
            "  ***  ",
            " *   * ",
            " *   * ",
            " *   * ",
            "  ***  "
        ],
        'P': [
            " ****  ",
            " *   * ",
            " ****  ",
            " *     ",
            " *     "
        ],
        'Q': [
            "  ***  ",
            " *   * ",
            " *   * ",
            " *  ** ",
            "  **** "
        ],
        'R': [
            " ****  ",
            " *   * ",
            " ****  ",
            " *  *  ",
            " *   * "
        ],
        'S': [
            "  **** ",
            " *     ",
            "  ***  ",
            "     * ",
            " ****  "
        ],
        'T': [
            " ***** ",
            "   *   ",
            "   *   ",
            "   *   ",
            "   *   "
        ],
        'U': [
            " *   * ",
            " *   * ",
            " *   * ",
            " *   * ",
            "  ***  "
        ],
        'V': [
            " *   * ",
            " *   * ",
            " *   * ",
            "  * *  ",
            "   *   "
        ],
        'W': [
            " *   * ",
            " *   * ",
            " * * * ",
            " ** ** ",
            " *   * "
        ],
        'X': [
            " *   * ",
            "  * *  ",
            "   *   ",
            "  * *  ",
            " *   * "
        ],
        'Y': [
            " *   * ",
            "  * *  ",
            "   *   ",
            "   *   ",
            "   *   "
        ],
        'Z': [
            " ***** ",
            "    *  ",
            "   *   ",
            "  *    ",
            " ***** "
        ],
    }

    for line in alphabet.get(letter.upper(), []):
        print(line)

def exibir_numeros():
    numeros = {
        "0": [
            " *** ",
            "*   *",
            "*   *",
            "*   *",
            " *** "
        ],
        "1": [
            "  *  ",
            " **  ",
            "  *  ",
            "  *  ",
            " *** "
        ],
        "2": [
            " *** ",
            "*   *",
            "   * ",
            "  *  ",
            "*****"
        ],
        "3": [
            " *** ",
            "*   *",
            "   **",
            "*   *",
            " *** "
        ],
        "4": [
            "   * ",
            "  ** ",
            " * * ",
            "*****",
            "   * "
        ],
        "5": [
            "*****",
            "*    ",
            "**** ",
            "    *",
            "**** "
        ],
        "6": [
            " *** ",
            "*    ",
            "**** ",
            "*   *",
            " *** "
        ],
        "7": [
            "*****",
            "    *",
            "   * ",
            "  *  ",
            " *   "
        ],
        "8": [
            " *** ",
            "*   *",
            " *** ",
            "*   *",
            " *** "
        ],
        "9": [
            " *** ",
            "*   *",
            " ****",
            "    *",
            " *** "
        ]
    }
    
    for numero in range(10):
        print(f"Número {numero}:")
        for linha in numeros[str(numero)]:
            print(linha)
        print("\n")


def print_alphabet():
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print_letter(letter)
        print()


# Exibe o alfabeto completo
print_alphabet()


# Chama a função para exibir os números de 0 a 9
exibir_numeros()

input()