# Disponível a partir do Python 3.10
def main():
    numero = int(input("Digite um numero: "))

    # Match-case é o equivalente mais direto ao switch do C
    match numero:
        case 1:
            print("numero 1")
        case 2:
            print("numero 2")
        case _:  # case padrão (equivalente ao default)
            print("caso nao for nem 1 e nem 2")

    input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()