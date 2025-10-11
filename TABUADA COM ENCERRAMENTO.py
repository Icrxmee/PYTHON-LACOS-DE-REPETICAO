while True: #Começa o While infinito.
    n = int ( input("Deseja ver a tabuada de qual número:")) #Usuário escolhe o número que deseja a tabuada.

    if n <= -1: #Define se por acaso, o número for negativo, o código encerra.
        break

    for i in range(1, 11): #O For vai de 1 a 10
      print (f"{n} x {i} = {n*i}") #Múltiplica o número escolhido, pelo index de cada volta do laço.

print("TABUADA ENCERRADA")

