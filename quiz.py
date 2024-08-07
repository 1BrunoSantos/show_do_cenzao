import customtkinter as ctk
import random

# Função para verificar a resposta
def verificar_resposta(botao, resposta):
    if resposta == respostas_corretas[pergunta_atual]:
        # Se a resposta estiver correta, muda a cor do botão para verde e atualiza a pergunta
        janela.after(500, lambda: botao.configure(fg_color="green"))
        janela.after(3000, atualizar_pergunta)
    else:
        # Se a resposta estiver errada, muda a cor do botão para vermelho e mostra o frame de erro
        janela.after(500, lambda: botao.configure(fg_color="red"))
        janela.after(3000, mostrar_frame_erro)  # Exibe o frame de erro após um pequeno atraso

# Função para atualizar a pergunta
def atualizar_pergunta():
    global pergunta_atual
    pergunta_atual += 1

    if pergunta_atual < len(perguntas):
        # Atualiza o texto da pergunta e as opções de resposta
        pergunta, opcoes = perguntas[pergunta_atual]
        textbox_pergunta.delete("0.0", "end")
        textbox_pergunta.insert("0.0", pergunta)

        botao_resposta_a.configure(text=opcoes[0], fg_color="maroon", state="normal")
        botao_resposta_b.configure(text=opcoes[1], fg_color="maroon", state="normal")
        botao_resposta_c.configure(text=opcoes[2], fg_color="maroon", state="normal")
        botao_resposta_d.configure(text=opcoes[3], fg_color="maroon", state="normal")
    else:
        # Se não houver mais perguntas, exibe "Fim do jogo!" e desativa os botões de resposta
        textbox_pergunta.delete("0.0", "end")
        textbox_pergunta.insert("0.0", "Fim do jogo!")
        botao_resposta_a.configure(state="disabled")
        botao_resposta_b.configure(state="disabled")
        botao_resposta_c.configure(state="disabled")
        botao_resposta_d.configure(state="disabled")
        mostrar_botao_reiniciar()  # Mostra o botão "REINICIAR" ao final do jogo

# Função para pular a pergunta atual
def pular_pergunta():
    atualizar_pergunta()
    botao_pular.configure(state="disabled")  # Desativa o botão "Pular"

# Função para usar a ajuda (eliminar duas opções erradas)
def usar_ajuda():
    opcoes_erradas = [opcao for opcao in perguntas[pergunta_atual][1] if opcao != respostas_corretas[pergunta_atual]]
    opcoes_para_excluir = random.sample(opcoes_erradas, 2)
    
    for botao in [botao_resposta_a, botao_resposta_b, botao_resposta_c, botao_resposta_d]:
        if botao.cget("text") in opcoes_para_excluir:
            botao.configure(state="disabled")
    
    botao_ajuda.configure(state="disabled")  # Desativa o botão "Ajuda"

# Função para parar o jogo
def parar_jogo():
    valor_premio = perguntas[pergunta_atual - 1][0].split("valendo")[1].split("reais")[0].strip()  # Obtém o valor da pergunta anterior
    if not frame_parar.winfo_ismapped():
        label_parar.configure(text=f"Você parou! Seu prêmio é: R${valor_premio}")
        frame_parar.place(relx=0.5, rely=0.5, anchor="center")
        mostrar_botao_reiniciar()  # Mostra o botão "REINICIAR" ao parar o jogo
    
    botao_pular.configure(state="disabled")  # Desativa o botão "Pular"
    botao_ajuda.configure(state="disabled")  # Desativa o botão "Ajuda"
    botao_parar.configure(state="disabled")  # Desativa o botão "Parar"

# Função para mostrar o frame de erro
def mostrar_frame_erro():
    valor_premio = perguntas[pergunta_atual - 1][0].split("valendo")[1].split("reais")[0].strip()  # Obtém o valor da pergunta anterior
    label_erro.configure(text=f"Você errou! Seu prêmio : R${valor_premio}")
    frame_erro.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o frame de erro na janela
    mostrar_botao_reiniciar()  # Mostra o botão "REINICIAR" ao errar a pergunta
    
    botao_pular.configure(state="disabled")  # Desativa o botão "Pular"
    botao_ajuda.configure(state="disabled")  # Desativa o botão "Ajuda"
    botao_parar.configure(state="disabled")  # Desativa o botão "Parar"

# Função para reiniciar o jogo
def reiniciar_jogo():
    global pergunta_atual
    pergunta_atual = 0

    # Atualiza a pergunta e as opções
    pergunta, opcoes = perguntas[pergunta_atual]
    textbox_pergunta.delete("0.0", "end")
    textbox_pergunta.insert("0.0", pergunta)

    botao_resposta_a.configure(text=opcoes[0], fg_color="maroon", state="normal")
    botao_resposta_b.configure(text=opcoes[1], fg_color="maroon", state="normal")
    botao_resposta_c.configure(text=opcoes[2], fg_color="maroon", state="normal")
    botao_resposta_d.configure(text=opcoes[3], fg_color="maroon", state="normal")

    # Reativa os botões "Pular", "Ajuda" e "Parar"
    botao_pular.configure(state="normal")
    botao_ajuda.configure(state="normal")
    botao_parar.configure(state="normal")

    # Esconde os frames de erro e parar
    frame_parar.place_forget()
    frame_erro.place_forget()
    esconder_botao_reiniciar()  # Esconde o botão "REINICIAR"

# Função para mostrar o botão "REINICIAR"
def mostrar_botao_reiniciar():
    botao_reiniciar.place(x=330, y=400)  # Ajusta a posição do botão "REINICIAR"

# Função para esconder o botão "REINICIAR"
def esconder_botao_reiniciar():
    botao_reiniciar.place_forget()  # Esconde o botão "REINICIAR"

# Cria a janela principal do aplicativo
janela = ctk.CTk()
janela.title("SHOW DO CENZÃO")
janela.geometry("800x500")
janela.resizable(width=False, height=False)
janela.configure(fg_color="blue")

# Configurações de fonte para as perguntas e respostas
pergunta_font = ctk.CTkFont(family="Helvetica", size=30, weight="bold")
resposta_font = ctk.CTkFont(family="Helvetica", size=25, weight="bold")

# Lista de perguntas e opções de resposta
perguntas = [
    ("Pergunta valendo 1 real! \nO que matou os dinossauros?", ["A - Covid", "B - Guerra", "C - Meteoro", "D - Dengue"]),
    ("Pergunta valendo 2 reais! \nOnde passou a série La Casa de Papel?", ["A - Netflix", "B - Globo", "C - SBT", "D - Band"]),
    ("Pergunta valendo 3 reais! \nQual a fórmula química da água?", ["A - C&A", "B - H2O", "C - HBO", "D - MP3"]),
    ("Pergunta valendo 4 reais! \nQual o menor país do mundo?", ["A - Americanópolis", "B - Capão Redondo", "C - Lua", "D - Vaticano"]),
    ("Pergunta valendo 5 reais! \nQuem pintou a Mona Lisa?", ["A - Suvinil", "B - Maxton", "C - Leonardo da Vinci", "D - Color Gin"]),
    ("Pergunta valendo 10 reais! \nOnde está localizada a Pirâmide do Sol?", ["A - Egito", "B - México", "C - Peru", "D - Índia"]),
    ("Pergunta valendo 12 reais! \nQue tipo de animal é a baleia?", ["A - Peixe", "B - Réptil", "C - Anfíbio", "D - Mamífero"]),
    ("Pergunta valendo 15 reais! \nQual o monumento mais visitado do mundo?", ["A - Coliseu de Roma", "B - Estátua da Liberdade", "C - Torre Eiffel", "D - Cristo Redentor"]),
    ("Pergunta valendo 18 reais! \nQuantos planetas tem no sistema solar atualmente?", ["A - 9", "B - 8", "C - 6", "D - 12"]),
    ("Pergunta valendo 20 reais! \nQual a capital da Austrália?", ["A - Camberra", "B - Sydney", "C - Tasmânia", "D - Melbourne"]),
    ("Pergunta valendo 23 reais! \nQual o valor de π (pi)?", ["A - 2,14", "B - 3,15", "C - 2,16", "D - 3,14"]),
    ("Pergunta valendo 25 reais! \nQual é o elemento químico com o símbolo Au", ["A - Alumínio", "B - Ouro", "C - Prata", "D - Laurêncio"]),
    ("Pergunta valendo 30 reais! \nQuantos filmes oficiais do 007 foram produzidos?", ["A - 27", "B - 22", "C - 25", "D - 20"]),
    ("Pergunta valendo 50 reais! \nQual o nome real do cantor Freddie Mercury?", ["A - Farrokh Bulsara", "B - Fredrick Mursary", "C - Frederick Mercury", "D - Fred Bulsara"]),
    ("Pergunta valendo 100 reais! \nQual desses filósofos morreu envenenado?", ["A - Aristóteles", "B - Sócrates", "C - Platão", "D - Epicuro"]),
    ("Pergunta valendo 0 reais! \nQuem foi o inventor da vacina?", ["A - Edward Jenner", "B - Loius Pasteur", "C - Albert Sabin", "D - Oswaldo Cruz"])
]

# Lista de respostas corretas correspondentes às perguntas
respostas_corretas = ["C - Meteoro", "A - Netflix", "B - H2O", "D - Vaticano", "C - Leonardo da Vinci", "B - México", "D - Mamífero", "C - Torre Eiffel", "B - 8", "A - Camberra", "D - 3,14", "B - Ouro", "C - 25", "A - Farrokh Bulsara", "B - Sócrates", "A - Edward Jenner"]

# Variável para controlar a pergunta atual
pergunta_atual = 0

# Caixa de texto para exibir a pergunta
textbox_pergunta = ctk.CTkTextbox(janela, width=780, height=100, fg_color="maroon", font=pergunta_font)
textbox_pergunta.place(x=10, y=20)
textbox_pergunta.insert("0.0", perguntas[pergunta_atual][0])

# Botões de resposta
botao_resposta_a = ctk.CTkButton(janela, width=400, height=50, fg_color="maroon", font=resposta_font, text=perguntas[pergunta_atual][1][0], command=lambda: verificar_resposta(botao_resposta_a, botao_resposta_a.cget("text")))
botao_resposta_a.place(x=200, y=140)

botao_resposta_b = ctk.CTkButton(janela, width=400, height=50, fg_color="maroon", font=resposta_font, text=perguntas[pergunta_atual][1][1], command=lambda: verificar_resposta(botao_resposta_b, botao_resposta_b.cget("text")))
botao_resposta_b.place(x=200, y=210)

botao_resposta_c = ctk.CTkButton(janela, width=400, height=50, fg_color="maroon", font=resposta_font, text=perguntas[pergunta_atual][1][2], command=lambda: verificar_resposta(botao_resposta_c, botao_resposta_c.cget("text")))
botao_resposta_c.place(x=200, y=275)

botao_resposta_d = ctk.CTkButton(janela, width=400, height=50, fg_color="maroon", font=resposta_font, text=perguntas[pergunta_atual][1][3], command=lambda: verificar_resposta(botao_resposta_d, botao_resposta_d.cget("text")))
botao_resposta_d.place(x=200, y=340)

# Botões de ação (Pular, Ajuda, Parar)
botao_pular = ctk.CTkButton(janela, width=140, height=80, fg_color="red", font=resposta_font, text="PULAR", command=pular_pergunta)
botao_pular.place(x=150, y=400)

botao_ajuda = ctk.CTkButton(janela, width=140, height=80, fg_color="orange", font=resposta_font, text="AJUDA", command=usar_ajuda)
botao_ajuda.place(x=330, y=400)

botao_parar = ctk.CTkButton(janela, width=140, height=80, fg_color="green", font=resposta_font, text="PARAR", command=parar_jogo)
botao_parar.place(x=500, y=400)

# Botão para reiniciar o jogo, inicialmente escondido
botao_reiniciar = ctk.CTkButton(janela, width=140, height=80, fg_color="blue", font=resposta_font, text="REINICIAR", command=reiniciar_jogo)
botao_reiniciar.place_forget()

# Frame para a janela de "Parar"
frame_parar = ctk.CTkFrame(janela, width=400, height=200, fg_color="red")
label_parar = ctk.CTkLabel(frame_parar, text="", font=resposta_font)
label_parar.pack(pady=20)
frame_parar.place_forget()  # Inicialmente escondido

# Frame para a janela de erro
frame_erro = ctk.CTkFrame(janela, width=400, height=200, fg_color="red")
label_erro = ctk.CTkLabel(frame_erro, text="", font=resposta_font)
label_erro.pack(pady=20)
frame_erro.place_forget()  # Inicialmente escondido

# Inicia a execução da janela principal
janela.mainloop()
