"""
Una inversión ficticia inicia con capital C no negativo y mantiene una tasa anual
porcentual I con 0 < I < 100. Se recibe también un entero M entre 0 y 50. El interés de cada año

es el saldo al comienzo de ese año multiplicado por I y dividido entre 100; se suma al saldo al
final del año. Determine el saldo después de M años; con M = 0 conserva el capital inicial.
Fórmula o relación: Saldo nuevo = saldo anterior × (1 + I/100).
"""

c = int(input("Digite el capital inicial: "))
i = int(input("Digitr la tasa anual porcentual: "))
m = int(input("Digite la cantidad de años: "))

saldo_nuevo = c

if m == 0:
    saldo_nuevo = 0
elif 0 < i < 100:
    for k in range(m):
        saldo_nuevo = saldo_nuevo * (1 + i/100)
print(saldo_nuevo)
