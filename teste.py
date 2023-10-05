import tkinter as tk

# Função para calcular o resultado
def calcular_resultado():
    try:
        trabalho = float(valor_trabalho.get())
        calor = float(valor_calor.get())
        resultado = calor - calor
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Valores inválidos. Insira números válidos.")

# Criar a janela principal
janela = tk.Tk()
janela.geometry("560x180")
janela.title("Calculadora de Trabalho e Calor")

# Criar rótulo e entrada para o valor do trabalho
valor_trabalho_label = tk.Label(janela, text="Valor do Trabalho:")
valor_trabalho_label.pack()
valor_trabalho = tk.Entry(janela)
valor_trabalho.pack()

# Criar rótulo e entrada para o valor do calor
valor_calor_label = tk.Label(janela, text="Valor do Calor:")
valor_calor_label.pack()
valor_calor = tk.Entry(janela)
valor_calor.pack()

# Botão para calcular o resultado
calcular_botao = tk.Button(janela, text="Calcular", command=calcular_resultado)
calcular_botao.pack()

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Iniciar a interface gráfica
janela.mainloop()
