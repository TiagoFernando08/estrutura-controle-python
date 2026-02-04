print("Bem vindo ao atendimento por favor escolha uma opção abaixo")

atendente = "você esta falando com o atendente"
boleto =  "essa é sua segunda via de boleto"
cancelamento = "deseja cancelar o serviço"
plano = " informações sobre o plano"
sair = "sair"
print("1 Falar com atendente \n2 Segunda via de boleto \n3 Cancelar serviço \n4 Informações sobre planos \n5  Sair")
numeros = input("Digite um dos numeros acima: ")

match numeros:
    case "1":
        print(atendente)
    case "2":
        print(boleto)
    case "3":
        print(cancelamento)
    case "4":
        print(plano)
    case "5":
        print(sair)
    case _:
        print("tenta denovo")



