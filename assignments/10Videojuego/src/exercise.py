def main():
    #escribe tu código abajo de esta línea
    price = 1000
    price2 = 350
    nuevos = int(input("Dame la cantidad de juegos nuevos: "))
    usados = int(input("Dame la cantidad de juegos usados: "))
    total = ((nuevos*price)+(usados*price2))
    print ("El total de la compra es: " + str(total))
    




if __name__ == '__main__':
    main()
