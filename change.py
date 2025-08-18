def change():
    expense = 23.75
    money = 100
    pesos = int(money - expense)
    centavos = int((money - expense - pesos) * 100)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("  ")
    print("Vuelto")
    print("  ")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
