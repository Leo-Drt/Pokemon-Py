import pickle
from pokemon import*
from pessoas import*

def escolher_pokemon_inicial(player):
    print("Olá {}, agora você irá escolher um pokemon para lhe acompanhar em sua jornada!!".format(player))

    pikachu= PokemonEletrico("Pikachu", level=1)
    charmander= PokemonFogo("Charmander", level=1)
    squirtle= PokemonAgua("Squirtle", level=1)

    print("Faça sua escolha!!")
    print("1", pikachu)
    print("2", charmander)
    print("3", squirtle)

    while True:
        escolha= input("Esolha seu pokemon!!")

        if escolha== "1":
            player.capturar(pikachu)
            break
        elif escolha== "2":
            player.capturar(charmander)
            break
        elif escolha== "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida!!")

def salvar_jogo(player):
    try:
        with open("database.db","wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso!")
    except Exception as error:
        print("Erro ao salvar o jogo!")
        print(error)

def carregar_jogo():
    try:
        with open("database.db","rb") as arquivo:
            player= pickle.load(arquivo)
            print("Jogo carregado com sucesso!")
            return player
    except Exception as error:
        print("Erro ao carregar o jogo! Jogo não econtrado!!")
        print(error)

if __name__== "__main__":

    print("Bem-vindo a aventura pokemon python!!")
    player= carregar_jogo()

    if not player:
        nome= input("Olá, qual é seu nome aventureiro!?")
        player= Player(nome)
        print("Olá {}, esse é um mundo habitados por pokemons, seu objetivo é ser o mestre pokemon !!".format(player))
        print("Vamos começar a nossa aventura mestre pokemon!?")
        print("Seu dinheiro inicial.")
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que tem alguns pokimons!!")
            player.mostrar_pokemons()
        else:
            print("Você não possuí um pokemon para batalhar, portanto precisa escolher um pokemon.")
            escolher_pokemon_inicial(player)

        print("Agora que tem seu primeiro pokemon, hora de batalhar com seu arco inimigo. Vamos nessa!!")
        gary= Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)
        salvar_jogo(player)


    while True:
        print("----------------------------------------")
        print("O que pretende fazer?")
        print("1 -> Explorar o mundo pokemon?")
        print("2 -> Batalhar!!")
        print("3 -> Mostrar pokemons.")
        print("4 -> Mostrar pokemoedas.")
        print("0 -> Sair do game.")
        print("")
        escolha= input("Vamos lá, faça sua escolha!")
        print("----------------------------------------")

        if escolha== "0":
            print("Fechando o jogo!")
            break
        elif escolha== "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha== "2":
            player.batalhar(Inimigo())
            salvar_jogo(player)
        elif escolha== "3":
            player.mostrar_pokemons()
        elif escolha== "4":
            player.mostrar_dinheiro()
        else:
            print("Escolha inválida!")
