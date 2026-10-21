"""
Una pantalla debe presentar todos los enteros comprendidos entre dos límites A y B,
ambos incluidos, empezando por A y terminando en B. Los límites son enteros entre -100 y
100. Si coinciden, presente ese único valor.
Fórmula o relación: El paso entre términos es 1 si A ≤ B y -1 si A > B.

"""

limit_a = int(input("Escriba el límite A:"))
limit_b = int(input("Escriba el límite B:"))

if limit_a < -100 and limit_b < 100 or limit_a > -100 and limit_b > 100:
    print("limites no validos")
elif limit_a <= limit_b:
    print(list(range(limit_a, limit_b + 1, 1)))
elif limit_a > limit_b:
    print(list(range(limit_a, limit_b - 1, -1)))
