from pyscript import document, when

# Informações do jogo
nome = "Valente"
idade = 10
personagem = "Guerreiro"
pontos = 0

# Seleciona os elementos do HTML
mensagem = document.querySelector("#mensagem")
placar = document.querySelector("#pontos")

# Mostra a mensagem inicial
mensagem.innerText = f"Olá! Eu sou {nome} e meu personagem é {personagem}."
placar.innerText = str(pontos)

# Função para responder ao clique no alvo
@when("click", "#alvo")
def clicou_no_alvo(evento):
    global pontos
    pontos += 3
    placar.innerText = str(pontos)
