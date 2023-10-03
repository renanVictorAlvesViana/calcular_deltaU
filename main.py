# ∆U = Q + T

# Calor cedido : ∆U = - Q - T
# Calor recebido: ∆U = Q - T
# Trabalho sobre o gás: ∆U= Q + T
# Trabalho pelo gás: ∆U= Q - T

ifCalor = int(input("O calor é cedido(0) ou recebido(1) pelo gás? [0/1] "))
ifTrabalho = int(input("O trabalho é sobre o gaś(0) ou realizado(1) pelo gás? [0/1] "))
 

Q = float(input("Informe o valor do calor: "))
T = float(input("Informe valor do trabalho: "))


if ifCalor == 0 and ifTrabalho == 0:
    print("certo")