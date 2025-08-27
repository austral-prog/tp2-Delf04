def change():
    expense = 23.75
    money = 100
    pesos = int(money - expense)
    centavos = int((money - expense - pesos) * 100)
    print("Ingresar gasto:")
    print(f"{expense}")
    print("Dinero recibido:")
    print(f"{money}")
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(f"{pesos}")
    print("Centavos:")
    print(f"{centavos}")
