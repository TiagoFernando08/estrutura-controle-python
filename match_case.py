'''
Qual é a logica da calculadora?

Precisa de valores (números)

ETAPA 1: ENTRADA:
1) O usuario precisa digitar DOIS números ou +
2) O usuario precisa selecionar qual operação ele ira usar

ETAPA 2: PROCESSAMENTO:
Realizar operações matematicas (+, -, * e /)

ETAPA 3: SAIDA:
Exibir o resultado da opreração
'''
print("essa é a calculadora digita logo")
primeiro_numero = float(input("digite o seu número: "))
segundo_numero = float(input("digita o seu segundo número: "))
operador =  input("Escolhe +, -, * ou /: ")

match operador: 
    case "+":
        print(" resultado é esse:", primeiro_numero + segundo_numero)
    case "-":
        print(" resultado é esse:", primeiro_numero - segundo_numero)
    case "*":
        print(" resultado é esse:", primeiro_numero * segundo_numero)
    case "/":
        if segundo_numero == 0:
            print("porque você ta tenta dividir por 0: ")
        else:       
            print(" resultado é esse:", primeiro_numero / segundo_numero)
    case _:
        print("tenta denovo ai: ")