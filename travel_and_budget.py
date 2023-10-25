import random

paises = ["Czech", "Austia", "Germany", "Italy", "Spain", "France", "Belgium", "Romania"]
precios = [1500, 3200, 3500, 2000, 2500, 3000, 2900, 1000]

while True:
    try: 
         budget = int(input("ingrese su budget: "))
         break
    except ValueError:
        print("debe ingresar un presupuesto")
        
country = list(zip(paises,precios))
viaje = list(filter(lambda x: x[1] <= budget,country))

if viaje:
    choice = random.choice(viaje)
    print(f'con un presupuesto $ {budget: }, puede viajar a {choice[0]}')
else:
    print(f'con presupuesto de $ {budget: }, no hay destinos')
        