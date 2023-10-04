# ∆U = Q - T
from tkinter import *

deltaU = 0

Q = float(input("Informe o valor do calor: "))
T = float(input("Informe valor do trabalho: "))

deltaU = Q - T

print("A variação da enegia interna do gás é ", deltaU)

janela = TK()


janela.mainloop()
