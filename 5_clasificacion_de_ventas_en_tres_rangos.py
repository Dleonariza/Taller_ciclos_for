"""
Clasificación de ventas en tres rangos
Caso. Un vendedor tiene N ventas, con 0 ≤ N ≤ 1000, y se recibe el importe no negativo de cada
una. Informe cuántas fueron de 200 o menos, cuántas superaron 200 sin llegar a 400 y cuántas
fueron de 400 o más. Una venta pertenece a un solo grupo.


"""

n = int(input("Ingrese la cantidad de ventas: "))
g1 = 0
g2 = 0
g3 = 0

if 0 <= n <= 1000:
    for i in range(n):
        ingreso = int(input("Ingrese el importe de la venta: "))
        if ingreso <= 200:
            g1 += 1
        elif ingreso < 400:
            g2 += 1
        else:
            g3 += 1

print("Ventas de 200 o menos:", g1)
print("Ventas superiores a 200 y menores a 400:", g2)
print("Ventas de 400 o más:", g3)