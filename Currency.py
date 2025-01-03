#Programa que pide al usuario el monto que tiene en pesos, soles y reales y calcula el total en dólares.

pesos = int(input('¿Que te queda en pesos? '))
soles = int(input('¿Que te queda en soles? '))
reais = int(input('¿Que te queda en reales? '))

total = pesos * 0.00025 + soles * 0.28 + reais * 0.21

print('USD',total)