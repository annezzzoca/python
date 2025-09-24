def resultadoSoma(n1,n2):
    return print(f'A soma dos números é: {n1 + n2}')

def resultadoSubtracao(n1,n2):
    return print(f'A subtração dos números é: {n1 - n2}')

def resultadoMultiplicacao(n1,n2):
    return print(f'A multiplicação dos números é: {n1 * n2}')

def resultadoDivisao(n1,n2):
    return print(f'A divisão dos números é: {n1 / n2}')

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

resultadoSoma(n1,n2)
resultadoSubtracao(n1,n2)
resultadoMultiplicacao(n1,n2)
resultadoDivisao(n1,n2)