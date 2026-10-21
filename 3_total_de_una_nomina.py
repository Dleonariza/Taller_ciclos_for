"""
Una empresa tiene N empleados, con 0 ≤ N ≤ 1000. Se recibe el sueldo no negativo de
cada empleado y se desea el total de la nómina. Para una empresa sin empleados, el total es
cero.
Fórmula o relación: Nómina = sueldo1 + sueldo2 + ... + sueldon.
"""

n = int(input("Digite la cantidad de empleados: "))
nomina = 0

if n == 0:
    nomina = 0
elif 0 <= n <= 1000:
    for i in range(n):
        print("Digite el sueldo del empleado #", i + 1)
        sueldo = int(input("Digite el sueldo: "))
        nomina += sueldo
print("Nomina:", nomina)