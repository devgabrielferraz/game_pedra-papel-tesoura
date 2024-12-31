from random import choice

jogador_vitorias = 0
maquina_vitorias = 0


def Opcao_jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("Opção inválida. Tente novamente!")
        Opcao_jogador()


def Opcao_Maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina


while True:
    print("-"*30)
    esc_jogador = Opcao_jogador()
    esc_maquina = Opcao_Maquina()
    print("-"*30)

    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
        # Jogador ganha
        print(f"Jogador escolheu: {esc_jogador} e a Máquina escolheu: {esc_maquina}."
              " Resultado: Você ganhou!")
        jogador_vitorias += 1
    elif esc_jogador == esc_maquina:
        #Empate
        print(f"Jogador escolheu: {esc_jogador} e a Máquina escolheu: {esc_maquina}."
              " Resultado: Empate")
    else:
        #Maquina ganha
        print(f"Jogador escolheu: {esc_jogador} e a Máquina escolheu: {esc_maquina}."
              " Resultado: Você perdeu!")
        maquina_vitorias += 1

    print("-"*30)
    print(f"Vitórias do Jogador: {jogador_vitorias}")
    print(f"Vitórias da Máquina: {maquina_vitorias}")
    print("-"*30)

    esc_jogador = input("Você quer jogar novamente? ")
    if esc_jogador in ["SIM", "sim", "Sim", "S", "s"]:
        pass
    elif esc_jogador in ["NAO", "nao", "Nao", "NÃO", "não", "Não", "N", "n"]:
        break
    else:
        break
