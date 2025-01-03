a = int(input("Ingresa a: "))
b = int(input("Ingresa b: "))
c = int(input("Ingresa c: "))

raiz1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
raiz2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(raiz1)
print(raiz2)