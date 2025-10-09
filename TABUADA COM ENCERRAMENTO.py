while True:
    n = int ( input("Deseja ver a tabuada de qual número:"))

    if n <= -1:
        break

    for i in range(1, 11):
      print (f"{n} x {i} = {n*i}")

print("TABUADA ENCERRADA")
