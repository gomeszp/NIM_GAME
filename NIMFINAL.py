def computador_escolhe_jogada(n,m):
    computadorRemove = 1

    while computadorRemove!= m:
        if (n-computadorRemove) % (m+1) == 0:
            return computadorRemove
        else:
            computadorRemove = computadorRemove + 1
    return computadorRemove

def usuario_escolhe_jogada(n,m):
    jogadaValida= False
    while not jogadaValida:
        jogadorRemove = int(input("Quantas peças você vai tirar ?"))
        if jogadorRemove > m or jogadorRemove < 1:
            print()
            print("Ooops, jogada invalida!")
            print()
            jogadaValida=False
        else :
            jogadaValida= True
    return jogadorRemove

    
def partida():
    print(" ")

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

   
    is_computer_turn = True

   
    if n % (m + 1) == 0: 
        print("Voce começa!")
        is_computer_turn = False
   
    while n > 0:

        if is_computer_turn:
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("Computador retirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("Você retirou {} peças.".format(jogada))

        
        n = n - jogada

        
        print("Restam apenas {} peças em jogo.\n".format(n))

    
    if is_computer_turn:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0


       
def campeonato():
    usuario = 0
    computador = 0

    
    for _ in range(3):

        
        vencedor = partida()

        
        if vencedor == 1:
            
            usuario = usuario + 1
        else:
            
            computador = computador + 1
        print()
        print("Placar: Você {} X {} Computador".format(usuario, computador))


tipodepartida= 0
while tipodepartida == 0:
    print("Bem vindo ao jogo do NIM! Escolha:")
    print()
    print ("1 - para jogar uma partida isolada") 
    tipodepartida=int(input("2 - para jogar um campeonato"))
    if tipodepartida == 2:
        print() 
        print("Você escolheu um campeonato")
        print()                                   
        campeonato()
        break
    if tipodepartida==1:
        print()
        print("Você escolhe uma partida isolada")
        print()
        partida()
        break
    
    else:
        print()
        print("Comando inválido!")
        tipodepartida=0            



				

                        	
                        
