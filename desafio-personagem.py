xp = int(input("coloque a quantidade de experiencia que o personagem tem: "))

if xp < 100:
    print("Você é um iniciante")
elif xp  <= 500:
    print("Você esta em um nivel intermediario")
else :
    print("Você é um veterano no jogo")

atacar = "você ataca o alvo" 
defender = "Você levanta seu escudo"
fugir = "Você foge da batalha" 

print("a = Atacar \nd = Defender \nf = Fugir")
acoes= input("oque você quer fazer: ")

match acoes:
    case "a":
        print(atacar)
        print("Você acerta um critico derrotando o seu adversario")
    case "d":
        print(defender)
        print("Você se defende de um ataque fatal")
    case "f":
        print(fugir)
        print("Para se recuperar seus ferimentos")
    case _:

        print("Não há mais ações disponiveis")

