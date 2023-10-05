#### bibliotecas #####
import tkinter as tk

##### funçôes #####
def calcular_energia_interna():
    try:
        calor = float(calor_entry.get())
        trabalho = float(trabalho_entry.get())

        if cedido_ou_recebido.get() == "Cedido":
            calor = -calor  # Calor cedido é negativo

        if realizado_sobre_ou_pelo.get() == "Sobre":
            trabalho = -trabalho  # Trabalho sobre o gás é negativo

        energia_interna = calor + trabalho

        resultado_label.config(
            text=f"Energia Interna (ΔU): {energia_interna} J"
        )
    except ValueError:
        resultado_label.config(
            text="Por favor, insira valores válidos."
        )

##### Criação da janela #####
janela = tk.Tk()
janela.geometry("240x280")
janela.title("DeltaU")
janela.resizable(False, False)


#####Labels e campos de entrada#####
calor_label = tk.Label(janela, text="Calor (Q):")
calor_label.pack()


calor_entry = tk.Entry(janela)
calor_entry.pack()


trabalho_label = tk.Label(janela, text="Trabalho (W):")
trabalho_label.pack()

trabalho_entry = tk.Entry(janela)
trabalho_entry.pack()

##### Opções para calor cedido ou recebido #####
cedido_ou_recebido_label = tk.Label(janela, text="Calor cedido ou recebido:")
cedido_ou_recebido_label.pack()

cedido_ou_recebido = tk.StringVar()
cedido_ou_recebido.set("Recebido")

cedido_radio = tk.Radiobutton(janela, text="Recebido", variable=cedido_ou_recebido, value="Recebido")
cedido_radio.pack()

cedido_radio = tk.Radiobutton(janela, text="Cedido", variable=cedido_ou_recebido, value="Cedido")
cedido_radio.pack()

##### Opções para trabalho sobre ou pelo gás #####
realizado_sobre_ou_pelo_label = tk.Label(janela, text="Trabalho sobre ou pelo gás:")
realizado_sobre_ou_pelo_label.pack()

realizado_sobre_ou_pelo = tk.StringVar()
realizado_sobre_ou_pelo.set("Sobre")

sobre_radio = tk.Radiobutton(janela, text="Sobre", variable=realizado_sobre_ou_pelo, value="Sobre")
sobre_radio.pack()

pelo_radio = tk.Radiobutton(janela, text="Pelo", variable=realizado_sobre_ou_pelo, value="Pelo")
pelo_radio.pack()

##### Botão de cálcular #####
calcular_botao = tk.Button(janela, text="Calcular", command=calcular_energia_interna)
calcular_botao.pack()

##### Rótulo para exibir o resultado ####
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

##### fim ##### 
janela.mainloop()